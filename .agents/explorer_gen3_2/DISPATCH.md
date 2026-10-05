# Task Assignment — Explorer Gen3-2 (E2E Test Architecture Investigation)

**Role**: teamwork_preview_explorer
**Assigned Working Directory**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_2
**Authoritative Request**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md
**Target Codebase**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento

## 2026-09-21T18:42:00Z

### Objective: R2 Investigation (E2E Automated Tests)
Investigate the automated testing setup to solve:
"Configurar e implementar un suite de pruebas automatizadas (recomendado: Playwright o Cypress) que simule la navegación de un participante a través de las distintas etapas del experimento, asegurando que la máquina de estados y las transiciones de páginas funcionen correctamente. Debe existir un comando ejecutable vía consola (npm run test:e2e) que levante el entorno de pruebas y pase exitosamente sin errores de ejecución."

### Specific Instructions:
1. Read ORIGINAL_REQUEST.md and examine `package.json`, existing test setups, scripts, and installed packages.
2. Evaluate Playwright vs Cypress for this Next.js project on Windows. Assess installation footprint, headless execution, webServer integration, and execution speed.
3. Trace the participant journey and state machine in `src/app/page.tsx`: Welcome -> Consent -> Demographics -> Induction -> Stimulus -> Rating -> Debriefing -> Thank You. Also examine the Admin flow (`/admin` and login).
4. Identify how network requests / API calls (Supabase / `/api/session`, etc.) should be handled during E2E testing to ensure fast, reliable, zero-flakiness execution without requiring live Supabase credentials.
5. Provide a step-by-step implementation blueprint: dependencies, configuration file (e.g. `playwright.config.ts`), test specs (`e2e/experiment-flow.spec.ts`), scripts in `package.json` (`"test:e2e"`).
6. Write your complete handoff report to `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_2\handoff.md`.
