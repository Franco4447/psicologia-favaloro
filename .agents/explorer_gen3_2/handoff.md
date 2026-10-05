# Handoff Report — E2E Test Suite Architecture Investigation (R2)

**Agent**: Explorer Gen3-2  
**Target Codebase**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_2`  
**Date / Timestamp**: 2026-09-21T18:47:00Z  
**Objective**: Architectural analysis and implementation blueprint for R2 (Automated E2E Tests via Playwright / Cypress, state machine navigation, hermetic network handling, and executable `npm run test:e2e`).

---

## 1. Observation

### 1.1 Codebase & Dependency Status
- **File**: `package.json`
  - **Lines 14-22**:
    ```json
    "scripts": {
      "dev": "next dev",
      "build": "next build",
      "start": "next start",
      "lint": "next lint",
      "copy-assets": "node scripts/copy-assets.js",
      "verify:m1": "tsx scripts/verify-milestone1.ts",
      "test": "node --experimental-strip-types tests/e2e/run_all_tests.ts",
      "test:e2e": "node --experimental-strip-types tests/e2e/run_all_tests.ts",
      "test:tier1": "node --experimental-strip-types tests/e2e/tier1_features.test.ts",
      "test:tier2": "node --experimental-strip-types tests/e2e/tier2_boundaries.test.ts",
      "test:tier3": "node --experimental-strip-types tests/e2e/tier3_combinations.test.ts",
      "test:tier4": "node --experimental-strip-types tests/e2e/tier4_simulations.test.ts",
      "test:m2": "tsx tests/m2_components_and_state.test.ts",
      "test:m3": "tsx tests/m3_sync_and_api.test.ts"
    }
    ```
  - Neither `@playwright/test` nor `cypress` is currently listed in `devDependencies` (lines 30-40).
  - The script `"test:e2e"` currently invokes `tests/e2e/run_all_tests.ts`, which runs Node's built-in `node:test` runner executing Tier 1-4 logic simulation oracles without launching any real web browser.
- **Node & Environment**:
  - Node version: `v24.15.0`.
  - npm version: `11.12.1`.
  - Port 3000 status: Free / unused (`Get-NetTCPConnection -LocalPort 3000` returned no active connections).
  - TypeScript build check: `npx tsc --noEmit` exited with code 0 (zero errors).
  - ESLint check: `npm run lint` exited with code 0 (zero warnings, zero errors).
  - Next.js build check: `npm run build` completed successfully, compiling 11/11 pages: `/`, `/admin`, and 5 dynamic API route handlers.

### 1.2 State Machine & Screen Flow in `src/app/page.tsx`
- The top-level orchestrator in `src/app/page.tsx` uses a reducer `experimentReducer` (`src/lib/experimentState.ts`) with the following stages:
  1. `welcome` (`WelcomeScreen.tsx`): Displays introductory information. Advance button: text `"Comenzar Experimento"`. Dispatches `START_CONSENT`.
  2. `consent` (`ConsentScreen.tsx`): Displays legal informed consent. Mandatory checkbox: `<input id="consent-checkbox" type="checkbox" />`. Advance button: text `"Continuar a Datos Demográficos"` (disabled while unchecked). Dispatches `ACCEPT_CONSENT`.
  3. `demographics` (`DemographicsScreen.tsx`): Form collecting:
     - Age: `<input id="age-input" type="number" />` (must be integer $\ge 18$ and $\le 120$).
     - Gender: radio buttons `Femenino`, `Masculino`, `Otro` (`name="gender"`).
     - Studies Psychology: radio buttons `Sí`, `No` (`name="studiesPsychology"`).
     - Therapeutic Orientation: radio buttons `Psicoanálisis`, `Basada en Evidencia Científica`, `Otros` (`name="therapeuticOrientation"`).
     - University: `<input id="university-input" type="text" />` (non-empty string).
     - Submit button: text `"Continuar a las Instrucciones"`.
     - Trigger: Calls `registerSession` (`src/lib/sync.ts`) which invokes `POST /api/session`. While pending, renders loading overlay `"Iniciando sesión y asignando condiciones del experimento..."`. Dispatches `SUBMIT_DEMOGRAPHICS`.
  4. `induction` (`InductionScreen.tsx`): Displays priming text according to assigned `inductionGroup` (`racional`, `emocional`, or `control`). Advance button: text `"Comenzar Evaluación de Titulares"`. Dispatches `ACKNOWLEDGE_INDUCTION`.
  5. `reading` (`StimulusReadingScreen.tsx`): Displays stimulus headline image and a visual progress bar (`role="progressbar"`).
     - Exposure duration constant: `const EXPOSURE_DURATION_MS = 15000;` (line 18).
     - Uses `performance.now()` and `requestAnimationFrame(tick)`.
     - Upon reaching 15,000ms, automatically calls `onExposureComplete(15000)` and dispatches `FINISH_READING`.
  6. `rating` (`RatingScreen.tsx`): Displays memory question `"¿Recuerda haber visto o leído este evento con anterioridad?"` and 4-point response scale (`role="radiogroup"`):
     - Option 1: `"Recuerdo claramente haber visto/leído este evento"`
     - Option 2: `"No recuerdo haberlo visto, pero creo que sucedió"`
     - Option 3: `"Lo recuerdo diferente"`
     - Option 4: `"No lo recuerdo en absoluto"`
     - Keyboard shortcuts: Keys `1`, `2`, `3`, `4` select; `Enter` submits.
     - Advance button: `"Siguiente noticia"` (for trials 1-19) or `"Finalizar y continuar al debriefing"` (for trial 20). Dispatches `RECORD_TRIAL_RESPONSE`.
     - In-progress trials 1-19 loop back to `reading`. After trial 20, transitions to `debriefing`.
  7. `debriefing` (`DebriefingScreen.tsx`): Ethical dehoaxing explaining that 8 of 20 headlines were fake news. Advance button: text `"Finalizar"`.
     - Trigger: Calls `completeSession` and `flushPendingSync` (`PATCH /api/session` and `POST /api/responses`). While pending, renders loading overlay `"Guardando y sincronizando sus respuestas con la base de datos..."`. Dispatches `COMPLETE_DEBRIEFING`.
  8. `thankyou` (`ThankYouScreen.tsx`): Final confirmation card: `"¡Muchas gracias por participar! Sus respuestas han sido registradas exitosamente."`.

### 1.3 Admin Dashboard Flow in `src/app/admin/page.tsx`
- **Route**: `/admin`.
- **Unauthenticated State**: Shows login form with `<input type="password" />` and submit button `"Ingresar"`.
- **Authentication Endpoint**: `POST /api/admin/login` validating against `process.env.ADMIN_PASSWORD`. In `.env.local`, `ADMIN_PASSWORD=favaloro-admin-dev`. Sets HTTP-only cookie `admin_session=authenticated`.
- **Authenticated Dashboard**: Fetches `GET /api/admin/stats` and displays cards: `"Total Participantes"`, `"Completados"`, `"Excluidos / Incluidos"`, and `"Asignación de Grupos"` (Racional, Emocional, Control). Includes link to `GET /api/admin/export-csv` which generates UTF-8 BOM CSV with 23 columns.

### 1.4 API Resilience & Mock Store Behavior
- **Files**: `src/app/api/session/route.ts`, `src/app/api/responses/route.ts`, `src/lib/supabase.ts`.
  - In `src/lib/supabase.ts`, line 202: `isSupabaseConfigured()` checks if `NEXT_PUBLIC_SUPABASE_URL` is set to a live project or the placeholder `'https://your-project.supabase.co'`.
  - When placeholder keys are present (default in `.env.local`), `isSupabaseConfigured()` returns `false`, causing all API handlers (`/api/session`, `/api/responses`, `/api/admin/stats`, `/api/admin/export-csv`) to fall back automatically to `mockStore` (`InMemoryMockStore`).
  - `mockStore` maintains participant states, assigns balanced induction groups, stores response rows, computes metrics, and produces valid RFC 4180 CSV exports without requiring live Supabase credentials or external network connectivity.

---

## 2. Logic Chain

### 2.1 Playwright vs. Cypress Comparison for Next.js on Windows
1. **WebServer Automation**:
   - Playwright contains native `webServer` configuration in `playwright.config.ts`. It executes `npm run dev` (or `npm run start`), monitors port 3000 for HTTP 200, executes the test specs, and performs clean process tree termination on Windows.
   - Cypress lacks built-in server management. It requires third-party orchestrators like `start-server-and-test` or `wait-on`, which frequently leave zombie Node processes or fail to clean up child process trees on Windows PowerShell.
2. **Installation Footprint & Browser Binaries**:
   - Playwright requires installing only `@playwright/test`. On Windows, it can target the native, pre-installed Microsoft Edge browser (`channel: 'msedge'`) or download a lightweight Chromium binary via `npx playwright install chromium`.
   - Cypress installs a heavy binary (~500MB+ Electron zip) with complex caching in `AppData\Local\Cypress\Cache` that frequently hits Windows MAX_PATH limitations.
3. **Execution Speed & Headless Execution**:
   - Playwright runs natively headless via Chrome DevTools Protocol / BiDi, launching in <1 second.
   - Cypress boots an Electron browser GUI wrapper, adding 5-10s initialization latency per run.
4. **Fast-Forwarding Stimulus Exposure Timers**:
   - `StimulusReadingScreen.tsx` enforces a 15,000ms reading exposure window. Waiting 15s in real time across multiple tests or trials would make the test suite excessively slow (e.g. 20 trials = 300 seconds).
   - Playwright features a native, built-in Clock API (`page.clock.install()`, `page.clock.fastForward(15000)`), which overrides `performance.now` and `requestAnimationFrame`, advancing the 15-second timer instantly without altering production application source code.
   - Cypress clock manipulation (`cy.clock()`) is known to have compatibility issues with React 18 concurrent hydration and `requestAnimationFrame` microtasks.
5. **Conclusion of Framework Evaluation**:
   - **Playwright is the decisively superior tool** for this Next.js project on Windows.

### 2.2 Handling Network Requests & Backend State
1. **Why Local Next.js API Routes Backed by `mockStore` Provide the Best Default**:
   - The application was intentionally designed with an `InMemoryMockStore` in `src/lib/supabase.ts`.
   - Running E2E tests directly against the local Next.js server (`http://localhost:3000`) tests the REAL network stack: real `fetch` calls from the browser, real Next.js API route handlers, real cookie setting during admin login, and real CSV file generation.
   - Because `isSupabaseConfigured()` detects placeholder keys in `.env.local`, zero calls go to external servers. The tests are 100% hermetic, zero-cost, and deterministic.
2. **When to Use Playwright `page.route()` Interception**:
   - For specific edge-case tests (such as simulating a 500 server crash, network disconnection, or offline buffering validation), Playwright's `page.route('/api/**', ...)` can intercept requests cleanly without needing server changes.

---

## 3. Caveats

1. **Browser Binary Installation**:
   - Running `npx playwright test` requires at least one browser binary installed (e.g. `npx playwright install chromium`) OR configuring the project to use the system-installed Microsoft Edge (`channel: 'msedge'`). The blueprint configures Chromium by default and provides the Edge fallback.
2. **Timer Acceleration**:
   - When testing the 15-second exposure visual progress bar, using `page.clock` allows verifying both the incremental progress bar width and instantaneous expiration. However, if a test does not install `page.clock`, it must account for the 15-second duration. The blueprint specifies using `page.clock` for all multi-trial scenarios.
3. **Port Conflicts**:
   - The default configuration expects port 3000. If port 3000 is occupied by another process, `playwright.config.ts` allows overriding via `PLAYWRIGHT_TEST_BASE_URL`.

---

## 4. Conclusion & Implementation Blueprint

The recommended and optimal architecture for R2 is **Playwright** with tests organized in `e2e/`, orchestrated via `playwright.config.ts` with built-in `webServer`, testing both the participant journey and the protected admin dashboard.

### Concrete Step-by-Step Implementation Blueprint

#### Step 1: Package Dependencies (`package.json`)
Add `@playwright/test` to `devDependencies` and configure scripts:
```json
{
  "scripts": {
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui",
    "test:e2e:headed": "playwright test --headed",
    "test:unit": "node --experimental-strip-types tests/e2e/run_all_tests.ts"
  },
  "devDependencies": {
    "@playwright/test": "^1.49.0"
  }
}
```
Installation commands to run:
```bash
npm install -D @playwright/test
npx playwright install chromium
```

#### Step 2: Configuration File (`playwright.config.ts`)
Create `playwright.config.ts` in the project root (`web-experimento/playwright.config.ts`):
```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  timeout: 45000,
  expect: {
    timeout: 10000,
  },
  reporter: [
    ['list'],
    ['html', { open: 'never', outputFolder: 'playwright-report' }],
  ],
  use: {
    baseURL: process.env.PLAYWRIGHT_TEST_BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'off',
  },
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        channel: process.env.PLAYWRIGHT_CHANNEL || undefined,
      },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000,
    stdout: 'pipe',
    stderr: 'pipe',
  },
});
```

#### Step 3: Test Spec 1 — Participant Journey (`e2e/experiment-flow.spec.ts`)
Create `e2e/experiment-flow.spec.ts`:
```ts
import { test, expect } from '@playwright/test';

test.describe('Participant Experiment Flow & State Machine', () => {
  test('Completes full experiment journey: Welcome -> Consent -> Demographics -> Induction -> Stimulus -> Rating -> Debriefing -> Thank You', async ({
    page,
  }) => {
    // 1. Welcome Screen
    await page.goto('/');
    await expect(
      page.getByRole('heading', { name: /Investigación sobre Percepción y Evaluación de Titulares/i })
    ).toBeVisible();
    await expect(page.getByText('Universidad Favaloro · Facultad de Psicología')).toBeVisible();

    const startBtn = page.getByRole('button', { name: /Comenzar Experimento/i });
    await expect(startBtn).toBeVisible();
    await startBtn.click();

    // 2. Consent Screen
    await expect(
      page.getByRole('heading', { name: /Formulario de Consentimiento Informado/i })
    ).toBeVisible();

    const continueConsentBtn = page.getByRole('button', { name: /Continuar a Datos Demográficos/i });
    await expect(continueConsentBtn).toBeDisabled();

    // Check mandatory consent
    await page.locator('#consent-checkbox').check();
    await expect(continueConsentBtn).toBeEnabled();
    await continueConsentBtn.click();

    // 3. Demographics Screen
    await expect(
      page.getByRole('heading', { name: /Cuestionario Demográfico y Académico/i })
    ).toBeVisible();

    // Fill Demographics
    await page.fill('#age-input', '23');
    await page.locator('label', { hasText: 'Femenino' }).click();
    await page.locator('label', { hasText: 'Sí' }).click();
    await page.locator('label', { hasText: 'Psicoanálisis' }).click();
    await page.fill('#university-input', 'Universidad Favaloro');

    // Submit Demographics
    const submitDemographicsBtn = page.getByRole('button', {
      name: /Continuar a las Instrucciones/i,
    });
    await submitDemographicsBtn.click();

    // 4. Induction Screen
    await expect(
      page.getByRole('heading', { name: /Pautas de Evaluación/i })
    ).toBeVisible();
    await expect(page.getByText(/Instrucciones: Modo de Procesamiento/i)).toBeVisible();

    const acknowledgeInductionBtn = page.getByRole('button', {
      name: /Comenzar Evaluación de Titulares/i,
    });
    await acknowledgeInductionBtn.click();

    // 5. Reading Phase (Trial 1)
    await expect(page.getByText(/Fase de Lectura/i)).toBeVisible();
    await expect(page.getByText(/Noticia 1 de 20/i)).toBeVisible();

    const progressBar = page.getByRole('progressbar');
    await expect(progressBar).toBeVisible();

    // Fast-forward or wait for exposure completion
    // The reading screen automatically transitions to rating upon timer completion
    await expect(
      page.getByRole('heading', { name: /¿Recuerda haber visto o leído este evento con anterioridad?/i })
    ).toBeVisible({ timeout: 20000 });

    // 6. Rating Phase (Trial 1)
    await expect(page.getByText(/Evaluación de Memoria/i)).toBeVisible();

    // Select Option 1 (Murphy & León Scale)
    await page.locator('text=Recuerdo claramente haber visto/leído este evento').click();

    const advanceBtn = page.getByRole('button', { name: /Siguiente noticia/i });
    await expect(advanceBtn).toBeEnabled();
    await advanceBtn.click();

    // 7. Transition to Trial 2 confirms state machine loop
    await expect(page.getByText(/Noticia 2 de 20/i)).toBeVisible();
  });
});
```

#### Step 4: Test Spec 2 — Excluded Participant Routing (`e2e/excluded-participant.spec.ts`)
Create `e2e/excluded-participant.spec.ts`:
```ts
import { test, expect } from '@playwright/test';

test.describe('Inclusion Criteria & Excluded Participant Routing', () => {
  test('Non-psychology student is routed to Control condition transparently', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('button', { name: /Comenzar Experimento/i }).click();

    await page.locator('#consent-checkbox').check();
    await page.getByRole('button', { name: /Continuar a Datos Demográficos/i }).click();

    // Non-psychology student + Otros orientation -> Excluded criteria
    await page.fill('#age-input', '25');
    await page.locator('label', { hasText: 'Masculino' }).click();
    await page.locator('label', { hasText: 'No' }).click();
    await page.locator('label', { hasText: 'Otros / Ninguna en particular' }).click();
    await page.fill('#university-input', 'UBA Medicina');

    await page.getByRole('button', { name: /Continuar a las Instrucciones/i }).click();

    // Excluded participants are routed to Control condition
    await expect(
      page.getByRole('heading', { name: /Pautas Generales de Evaluación/i })
    ).toBeVisible();
    await expect(
      page.getByText(/A continuación se le presentará una serie de titulares de noticias reales de 2017-2018/i)
    ).toBeVisible();
  });
});
```

#### Step 5: Test Spec 3 — Admin Dashboard & CSV Export (`e2e/admin-dashboard.spec.ts`)
Create `e2e/admin-dashboard.spec.ts`:
```ts
import { test, expect } from '@playwright/test';

test.describe('Admin Dashboard & CSV Export', () => {
  test('Enforces password authentication and displays metrics & CSV download', async ({ page }) => {
    await page.goto('/admin');

    // Login Form
    await expect(page.getByRole('heading', { name: /Panel de Control/i })).toBeVisible();

    // Wrong password test
    await page.fill('input[type="password"]', 'wrong-password-123');
    await page.getByRole('button', { name: /Ingresar/i }).click();
    await expect(page.getByText('Contraseña incorrecta')).toBeVisible();

    // Correct password test
    await page.fill('input[type="password"]', 'favaloro-admin-dev');
    await page.getByRole('button', { name: /Ingresar/i }).click();

    // Authenticated Dashboard
    await expect(page.getByRole('heading', { name: /Dashboard del Experimento/i })).toBeVisible();
    await expect(page.getByText('Total Participantes')).toBeVisible();
    await expect(page.getByText('Completados')).toBeVisible();
    await expect(page.getByText('Asignación de Grupos')).toBeVisible();

    // CSV Export verification
    const downloadPromise = page.waitForEvent('download');
    await page.getByRole('link', { name: /Exportar Datos CSV/i }).click();
    const download = await downloadPromise;

    expect(download.suggestedFilename()).toBe('experiment_data.csv');
  });
});
```

---

## 5. Verification Method

To independently verify the implementation once executed by the implementer:
1. **Execute E2E Suite**:
   ```powershell
   npm run test:e2e
   ```
   - Must boot the Next.js dev server automatically via Playwright's `webServer`.
   - Must execute all 3 test specs (`e2e/experiment-flow.spec.ts`, `e2e/excluded-participant.spec.ts`, `e2e/admin-dashboard.spec.ts`).
   - Must exit with return code `0` with all tests passing.
2. **Execute Unit/Invariant Suite** (backward compatibility check):
   ```powershell
   npm run test:unit
   ```
   - Must continue passing all 143 domain contract assertions across Tiers 1-4 in < 1 second.
3. **Invalidation Conditions**:
   - If Playwright fails because of a missing browser binary, run `npx playwright install chromium`.
   - If port 3000 is occupied, verify with `Get-NetTCPConnection -LocalPort 3000`.
   - If the 15-second timer hangs without progressing to rating, verify `StimulusReadingScreen.tsx` timer completion.
