# Handoff Report — Integration & Regression Investigation (Gen 3)

**Author**: Explorer Gen3-3 (teamwork_preview_explorer)  
**Target Codebase**: `web-experimento/`  
**Date**: 2026-09-21T18:50:00Z  
**Status**: Completed (Hard Handoff)

---

## 1. Observation

### 1.1 Existing Test Suite & Execution Performance
- **Command**: `npm test` (mapped in `package.json` line 14 to `node --experimental-strip-types tests/e2e/run_all_tests.ts`).
- **Result**: Exited with code 0 in 0.50 seconds.
- **Suites Executed**:
  - `Tier 1: Feature Coverage (95 Assertions across 19 Features)`: 95/95 passed.
  - `Tier 2: Boundary, Corner Cases & Resilience Tests`: 29/29 passed (Demographics boundaries, consent enforcement, timing/latency, offline buffer, state machine).
  - `Tier 3: Cross-Feature Combinations (Pairwise Permutations)`: 13/13 passed (Factorial conditions for included, excluded, and response classifications).
  - `Tier 4: Real-World End-to-End Simulation Scenarios`: 6/6 journeys passed (Full 20-trial flows for Psychoanalysis/Evidence/Control/Excluded, network drop, and 60-participant stress test).
  - **Total**: 143 passed, 0 failed, 0 skipped.
- **Additional Test Scripts**:
  - `npm run test:m2` (`tests/m2_components_and_state.test.ts`): 8 tests, 100% passed in 16ms.
  - `npm run test:m3` (`tests/m3_sync_and_api.test.ts`): 22 tests, 100% passed in 5.0s (includes mock network latency and offline flush simulations).
  - `tests/adversarial_m1_assets.test.ts`: 26 checks, 100% passed.
  - `tests/m2_adversarial_stress.test.ts`: 24 tests, 100% passed.
  - `tests/adversarial_m2_timing_ui.test.ts`: 10 tests, 100% passed when required/imported; had a direct tsx execution quirk where Next.js `Image` component forwarded ref symbol in Node SSR environment causes React to receive an object if run outside Next.js webpack bundler.

### 1.2 Build and Lint Health
- **Command**: `npm run lint` (`next lint`).
  - Output: `✔ No ESLint warnings or errors`. Exited with code 0.
- **Command**: `npm run build` (`next build`).
  - Output: `Next.js 14.2.35`, `Compiled successfully`, `Generating static pages (11/11)`, all routes generated (`/`, `/_not-found`, `/admin`, `/api/admin/*`, `/api/responses`, `/api/session`). Exited with code 0.
- **Configuration Analysis**:
  - In `tsconfig.json` (lines 28-30):
    ```json
    "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
    "exclude": ["node_modules", "tests"]
    ```
    Directory `tests/` is explicitly excluded from Next.js build compilation. Adding test files inside `tests/` does not pollute or fail `next build`.
  - In `.eslintrc.json`:
    ```json
    {
      "extends": ["next/core-web-vitals", "next/typescript"]
    }
    ```
    Default Next.js lint applies to application code under `src/` and does not fail on external test directories.

### 1.3 Stimulus Duration Invariants: The 10,000 ms vs 15,000 ms Divergence
A detailed cross-file audit revealed a divergence between the original Milestone 1 specifications and recent Gen 3 commits:
1. **Original Specification & Harness Assertions (10,000 ms)**:
   - `ORIGINAL_REQUEST.md` (line 52): *"Se muestra la imagen del titular con tiempo de lectura de 10 segundos (con indicador visual de progreso, avance automático)"*.
   - `tests/e2e/tier1_features.test.ts`:
     - Line 499-500 (F10.1): `const targetDurationMs = 10000; assert.equal(targetDurationMs, 10000);`
     - Line 506-508 (F10.2): `calcProgress(0, 10000) === 0`, `calcProgress(5000, 10000) === 50`, `calcProgress(10000, 10000) === 100`.
     - Line 513, 519 (F10.3, F10.4): `elapsedMs >= 10000`.
     - Line 523, 533 (F10.5): `engine.recordResponse(trials[0], 1, 10000, 1500); assert.equal(recorded.readingTimeMs, 10000);`.
   - `tests/e2e/tier2_boundaries.test.ts`:
     - Line 75-76 (B3.1, B3.2): `9,999 ms cannot advance`, `exact 10,000 ms triggers advance`.
   - `tests/e2e/harness/experimentEngine.ts` (line 159): `readingTimeMs: 10000`.
   - `tests/e2e/harness/simulatedUser.ts` (line 87): `const readingTimeMs = 10000;`.
   - `src/lib/experimentState.ts` (lines 94, 202, 260): `currentReadingTimeMs: 10000`.
2. **Gen 3 Commit & User Request (15,000 ms)**:
   - `ORIGINAL_REQUEST.md` (lines 144-153): *"R1. Corrección del Temporizador Visual: Corregir la lógica visual o estructural en la pantalla de estímulos (StimulusReadingScreen.tsx) para asegurar que la barra de progreso inferior de 15 segundos crezca visiblemente en pantalla desde que la imagen termina de cargar... durante los 15 segundos."*
   - Git Commit `c08208d` ("Update consent screen texts and increase reading time to 15s"):
     - `src/components/InductionScreen.tsx` (lines 80, 82): Updated instruction text from 10 seg to 15 seg.
     - `src/components/StimulusReadingScreen.tsx` (line 18): Changed constant to `const EXPOSURE_DURATION_MS = 15000;`.
3. **Current Behavior**:
   - `npm test` passes today because the existing test harness in `tests/e2e/` tests the domain simulation oracle (`experimentEngine.ts`), which was created with 10s.
   - However, in the live application UI, `StimulusReadingScreen.tsx` runs for 15,000 ms.
   - In `src/lib/experimentState.ts`, default `currentReadingTimeMs` is still 10,000 ms, though when `FINISH_READING` is dispatched by `StimulusReadingScreen`, it overrides `currentReadingTimeMs` with `15000`.

### 1.4 StimulusReadingScreen.tsx Bug Analysis
In `src/components/StimulusReadingScreen.tsx`:
1. **Re-render Frequency vs CSS Transition Clash**:
   - Lines 63-91: `useEffect` executes `requestAnimationFrame(tick)` calling `setElapsedMs(elapsed)` ~60 times per second.
   - Line 165: The progress bar has `className="h-full bg-indigo-600 transition-[width] duration-75 ease-linear rounded-full"` and `style={{ width: `${progressPercent}%` }}`.
   - Calling React state updates every 16ms while CSS transition is animating over 75ms creates a continuous conflict between browser CSS transition interpolation and React DOM mutation, leading to visual freezing, stuttering, and dropped frames.
2. **Missing Image Caching Protection**:
   - Line 38: `handleImageLoad` is bound solely to `<Image onLoad={handleImageLoad} ... />`.
   - In Next.js/React, when an image is already in the browser HTTP cache or memory disk cache (e.g. during trials 2-20), `onLoad` can fire before React event attachment or fail to fire on component remount. If `onLoad` does not fire, `imageLoaded` remains `false`, and the timer NEVER starts.
3. **Double Callback Invocation**:
   - Lines 76-77:
     ```tsx
     if (onExposureComplete) onExposureComplete(EXPOSURE_DURATION_MS);
     if (onComplete) onComplete(EXPOSURE_DURATION_MS);
     ```
   - In `src/app/page.tsx` (lines 216-221), both callbacks are provided and both dispatch `FINISH_READING`.
4. **Layout & Skeleton Swapping**:
   - Line 133: `!imageLoaded` keeps the image container at `absolute opacity-0 pointer-events-none h-0 overflow-hidden`. In some rendering engines, a height-0 overflow-hidden container can delay image decode.

### 1.5 System Environment & Browser Availability
- Host OS: Windows.
- Microsoft Edge (`msedge.exe`) exists at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`.
- Google Chrome (`chrome.exe`) exists at `C:\Program Files\Google\Chrome\Application\chrome.exe`.
- Playwright CLI is available (`npx playwright@1.63.0`). Playwright can run headless using the pre-installed system browsers via `channel: 'chrome'` or `channel: 'msedge'` without requiring large external downloads.

---

## 2. Logic Chain

1. **Premise 1 (Test Suite Health)**: Existing tests in `tests/e2e/` (143 invariants) and unit tests (`test:m2`, `test:m3`) pass 100% under Node 24 native runner.
2. **Premise 2 (Build Health)**: `next build` and `next lint` pass 100% with zero errors and zero warnings. `tsconfig.json` excludes `tests/`.
3. **Premise 3 (Duration Coupling)**:
   - The existing test harness in `tests/e2e/tier1_features.test.ts` (F10.1-F10.5) explicitly asserts that `targetDurationMs === 10000`.
   - The UI in `StimulusReadingScreen.tsx` and `InductionScreen.tsx` was changed in commit `c08208d` to 15,000 ms.
   - *Inference*: If an implementer modifies `tests/e2e/tier1_features.test.ts` to assert 15,000 ms without updating `tests/e2e/harness/experimentEngine.ts` and `tier2_boundaries.test.ts`, the existing test suite will break. Conversely, if `StimulusReadingScreen.tsx` is kept at 15,000 ms, browser-based E2E tests (Playwright) running against the live UI will wait 15 seconds per trial.
4. **Premise 4 (E2E Test Execution Time)**:
   - 20 trials x 15 seconds = 300 seconds (5 minutes) of pure waiting per participant journey.
   - An automated E2E test suite running 3-5 scenarios would take 15-25 minutes if unaccelerated.
   - *Inference*: A live E2E test suite requires a mechanism to fast-forward or accelerate the stimulus exposure window during automated testing (e.g. Playwright `page.clock.fastForward()` or a URL parameter like `?test_speed=fast` / `NEXT_PUBLIC_TEST_MODE=true` that sets exposure to 500ms during automated tests).
5. **Premise 5 (Visual Timer Fix)**:
   - The visual freeze occurs because React state updates at 60fps clash with a CSS 75ms transition on the same property (`width`), and cached image loads do not latch `onLoad`.
   - *Inference*: The timer must decouple visual animation from state updates (using direct DOM ref manipulation or CSS keyframe animation / linear transition without state churn), and must latch image loading via an `imgRef.complete` check upon mount.

---

## 3. Caveats

1. **Dual Contract for Reading Duration**:
   - The empirical literature in `TEST_INFRA.md` and `Feedback_Diseño_Experimental.md` mentions 10 seconds, but the client request in Gen 3 (`ORIGINAL_REQUEST.md` line 144) explicitly states: *"asegurar que la barra de progreso inferior de 15 segundos crezca visiblemente"*.
   - We must not break existing test contracts: existing `npm test` invariants can either test the mathematical invariant (0% to 100% progress) and accept a parameter, or the harness can be updated cleanly in tandem with `experimentEngine.ts`.
2. **Playwright vs Headless Node Harness**:
   - Currently, `package.json` maps `"test:e2e"` to `node --experimental-strip-types tests/e2e/run_all_tests.ts`.
   - Adding Playwright as the official E2E tool requires adjusting scripts so that both the 143 invariant tests and the Playwright browser tests can run without conflict (e.g., `"test:unit": "node --experimental-strip-types tests/e2e/run_all_tests.ts"`, `"test:e2e": "playwright test"`).
3. **Browser Engine in Windows CI/Local**:
   - Both Chrome and Edge are installed locally, but in headless CI environments without Edge/Chrome, `@playwright/test` may need chromium installed or fallback to mock simulation.

---

## 4. Conclusion & Recommendations

### 4.1 System Health Assessment
- Codebase build and lint are in pristine condition (`npm run build` and `npm run lint` are 100% clean).
- The existing 143 test invariants in `tests/e2e/` pass 100% in 0.50 seconds.
- No blocking conflicts exist in Next.js configuration or scripts for introducing Playwright.

### 4.2 Actionable Recommendations for Implementation Agents

#### Recommendation 1: Fix `StimulusReadingScreen.tsx` Timer & Visual Progress Bar
1. **Eliminate React State Churn & Transition Conflict**:
   - Remove `transition-[width] duration-75 ease-linear` from the progress bar inner div.
   - Instead, either:
     - Use a direct DOM `ref` for the progress fill bar (`progressRef.current.style.width = ...%`) inside `requestAnimationFrame`, updating only the DOM style attribute directly without triggering React component re-renders every 16ms, OR
     - Use CSS keyframe animation / linear transition over the known duration (`transition: width 15000ms linear`), starting when `imageLoaded` becomes true.
2. **Image Caching & Latch Resilience**:
   - Add an `imgRef`: on mount in `useEffect`, check `if (imgRef.current?.complete) handleImageLoad();`.
   - Add a fallback safety timeout (e.g., 2,500 ms): if the image fails to report loaded, automatically set `imageLoaded(true)` so the participant is never trapped on a loading skeleton.
3. **Deduplicate Callback Dispatch**:
   - In `StimulusReadingScreen.tsx`, call only one completion handler or guard with `completedRef.current`.
4. **Visual Hierarchy & Stacking**:
   - Ensure the progress bar container has explicit `z-10 relative`, distinct background contrast (`bg-slate-200` track, `bg-indigo-600` bar), a minimum height of `h-3` (12px), and an optional countdown label (e.g., "Tiempo restante: Xs") to meet the visual criteria.

#### Recommendation 2: Harmonize Duration Constants Across Codebase
- Define a unified constant in `src/lib/experimentState.ts` and `src/components/StimulusReadingScreen.tsx`:
  `export const DEFAULT_EXPOSURE_DURATION_MS = 15000;`
- In `src/lib/experimentState.ts`, update lines 94, 202, and 260 to use `DEFAULT_EXPOSURE_DURATION_MS`.
- In `tests/e2e/harness/experimentEngine.ts` and `tier1_features.test.ts`, either:
  - Keep the test checking that whatever duration is configured, progress calculates 0% to 100% and advance triggers at `targetDurationMs`, OR
  - Update `targetDurationMs` to 15,000 ms consistently across `tier1_features.test.ts`, `tier2_boundaries.test.ts`, and `experimentEngine.ts`.

#### Recommendation 3: Automated E2E Test Suite Architecture (Playwright)
1. **Package Setup**:
   - Install `@playwright/test` as a devDependency.
2. **Playwright Config (`playwright.config.ts`)**:
   - Configure webServer:
     ```ts
     webServer: {
       command: 'npm run start',
       port: 3000,
       reuseExistingServer: !process.env.CI,
     }
     ```
   - Use pre-installed system browser to avoid multi-hundred-megabyte downloads:
     ```ts
     projects: [
       {
         name: 'Chromium',
         use: { channel: 'chrome' }, // or 'msedge'
       }
     ]
     ```
3. **Fast Timer Support for E2E**:
   - Support `?fastTimers=true` or use Playwright's `page.clock.install()` + `page.clock.fastForward(15000)` so that the 20-trial test navigates smoothly in < 10 seconds rather than waiting 300 seconds.
4. **Script Naming in `package.json`**:
   - `"test:unit": "node --experimental-strip-types tests/e2e/run_all_tests.ts"`
   - `"test:e2e": "playwright test"`
   - `"test": "npm run test:unit && npm run test:e2e"` (or keep `npm test` as unit and `npm run test:e2e` for browser tests, satisfying R2 AC).

---

## 5. Verification Method

To independently verify the findings in this report:

1. **Verify Existing Invariant Test Suite**:
   ```bash
   cd "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento"
   npm test
   ```
   *Expected*: Exits with code 0. 143 passed, 0 failed, duration < 1.0s.

2. **Verify Milestone 2 & 3 Unit Tests**:
   ```bash
   npm run test:m2
   npm run test:m3
   ```
   *Expected*: Both exit with code 0.

3. **Verify Next.js Build and Lint**:
   ```bash
   npm run lint
   npm run build
   ```
   *Expected*: `next lint` returns `✔ No ESLint warnings or errors`. `next build` completes with 11/11 pages statically/dynamically generated and code 0.

4. **Verify System Browser Availability for Playwright**:
   ```powershell
   Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe"
   Test-Path "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
   ```
   *Expected*: Both return `True`.

5. **Invalidation Conditions**:
   - If modifying `StimulusReadingScreen.tsx` causes `npm run build` or `npm run lint` to fail with TypeScript or JSX errors.
   - If changing duration constants in `src/` causes `npm test` to fail without synchronized updates in `tests/e2e/harness/`.
   - If Playwright tests cannot advance through trials due to unaccelerated 15s timers causing test timeouts (>30s).
