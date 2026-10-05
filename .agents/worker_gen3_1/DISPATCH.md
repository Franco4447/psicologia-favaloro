# Task Assignment — Worker Gen3-1 (Visual Timer & E2E Test Suite Implementation)

**Role**: teamwork_preview_worker
**Assigned Working Directory**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_gen3_1
**Authoritative Request**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md
**Project Plan**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_3\PROJECT.md
**Target Codebase**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Exclusively Owned Files
You own the following files in `web-experimento`:
- `src/lib/timing.ts` (create)
- `src/components/StimulusReadingScreen.tsx` (modify)
- `src/lib/experimentState.ts` (modify line 14 default)
- `package.json` (modify scripts & devDependencies)
- `playwright.config.ts` (create)
- `e2e/experiment-flow.spec.ts` (create)
- `e2e/excluded-participant.spec.ts` (create)
- `e2e/admin-dashboard.spec.ts` (create)

## Instructions & Specifications
Carefully consult the handoff reports from the Survey Explorers:
- Visual Timer blueprint: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_1\handoff.md`
- E2E Playwright architecture: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_2\handoff.md`
- Integration and regression constraints: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_3\handoff.md`

### Task 1: R1 Visual Timer Fix
1. Create `src/lib/timing.ts` exporting `STIMULUS_EXPOSURE_DURATION_SECONDS = 15; STIMULUS_EXPOSURE_DURATION_MS = 15000;`.
2. Update `src/components/StimulusReadingScreen.tsx` using the drop-in implementation in Explorer 1's handoff:
   - Use `<img>` with `imgRef` and immediate `img.complete && img.naturalWidth > 0` check on mount.
   - Remove conflicting CSS transitions during 60fps RAF state updates.
   - Responsive image frame height (`h-[260px] sm:h-[320px] md:h-[380px]`) and mobile sticky bottom bar.
   - Live countdown text (`{remainingSeconds}s restantes`).
   - Single-dispatch completion guard (`completedRef`).
3. Update `src/lib/experimentState.ts` line 14 default `currentReadingTimeMs: 15000`.

### Task 2: R2 Automated E2E Test Suite
1. Install `@playwright/test` into devDependencies in `web-experimento` (`npm install -D @playwright/test`).
2. Run `npx playwright install chromium` to ensure browser binary is ready.
3. Create `playwright.config.ts` with webServer targeting `http://localhost:3000` via `npm run dev`.
4. Create the 3 E2E test specs under `e2e/`:
   - `e2e/experiment-flow.spec.ts`
   - `e2e/excluded-participant.spec.ts`
   - `e2e/admin-dashboard.spec.ts`
5. Configure `package.json`:
   - `"test:e2e": "playwright test"`
   - `"test:unit": "node --experimental-strip-types tests/e2e/run_all_tests.ts"`
   - `"test": "node --experimental-strip-types tests/e2e/run_all_tests.ts"`

### Task 3: Verification
Execute and verify:
1. `npm run test:e2e` (must pass 100% with exit code 0)
2. `npm test` (must pass 100% of 143 test invariants)
3. `npm run lint` (0 warnings, 0 errors)
4. `npm run build` (100% clean Next.js build)
5. `npx tsx tests/adversarial_m2_timing_ui.test.ts` (pass)

Write your full report to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_gen3_1\handoff.md`.
Send a message back to parent when done.

## 2026-09-21T18:50:06Z
Received user assignment:
Implement R1 (Visual Timer Fix in StimulusReadingScreen.tsx & src/lib/timing.ts) and R2 (Playwright E2E automated test suite with npm run test:e2e).
Run builds and all tests:
- npm run test:e2e
- npm test
- npm run lint
- npm run build
- npx tsx tests/adversarial_m2_timing_ui.test.ts
Write complete handoff report to .agents/worker_gen3_1/handoff.md and notify parent.

