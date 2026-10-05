# Project: Plataforma Web de Psicología Experimental — Generation 3 Quality Validation & Bug Fix

**Institución**: Universidad Favaloro  
**Cátedra**: Psicología Experimental (2do Año) - Parcial 2 Investigación  
**Directorio Base**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  
**Orchestrator**: Generation 3 (`orchestrator_3`)  
**Timestamp**: 2026-09-21T19:17:00Z  

---

## Architecture

### System Overview
- **Framework**: Next.js 14+ (App Router), React 18, TypeScript, Tailwind CSS, Lucide React.
- **Backend / API**: Route handlers (`/api/session`, `/api/responses`, `/api/admin/login`, `/api/admin/stats`, `/api/admin/export-csv`) with built-in `mockStore` fallback in `src/lib/supabase.ts` for fast, hermetic, deterministic testing without live Supabase credentials.
- **Timing Engine**: Centralized in `src/lib/timing.ts` (`STIMULUS_EXPOSURE_DURATION_SECONDS = 15; STIMULUS_EXPOSURE_DURATION_MS = 15000;`).
- **Visual Display (`StimulusReadingScreen.tsx`)**: High-precision `requestAnimationFrame` timer with cached-image immediate detection, responsive visual frame (`h-[260px] sm:h-[320px] md:h-[380px]`), unthrottled progress bar, live countdown readout, and mobile sticky bottom bar.
- **E2E Automation Harness**: Playwright (`@playwright/test`) with automatic `webServer` (`npm run dev`), covering participant journey, exclusion criteria, state machine transitions, and admin dashboard with CSV export. Executable via `npm run test:e2e`.

---

## Feature Inventory

| # | Feature | Description | Milestone | Status | Source |
|---|---------|-------------|-----------|--------|--------|
| 1 | R1: 15s Exposure Timer Constant | Centralized single source of truth in `src/lib/timing.ts` for 15.0s reading window. | M1 | DONE | ORIGINAL_REQUEST (2026-09-21) / Survey |
| 2 | R1: Image Cache Latching & Zero-Height Fix | Detect cached preloaded images via `img.complete` on mount, eliminating timer deadlock. | M1 | DONE | Survey (Explorer 1 & 3) |
| 3 | R1: Stutter-Free Visual Progress Bar | Remove conflicting CSS transitions during 60fps RAF state updates; smooth linear growth. | M1 | DONE | Survey (Explorer 1 & 3) |
| 4 | R1: Anti-Clipping Responsive Layout | Prevent vertical clipping on 768px displays; provide mobile sticky bottom timer bar. | M1 | DONE | Survey (Explorer 1) |
| 5 | R1: Live Countdown Readout | Add dynamic remaining seconds display (`{remainingSeconds}s restantes`) alongside progress bar. | M1 | DONE | Survey (Explorer 1) |
| 6 | R2: Playwright Test Harness Setup | Install `@playwright/test`, author `playwright.config.ts` with Next.js `webServer`. | M2 | DONE | ORIGINAL_REQUEST (2026-09-21) / Survey |
| 7 | R2: Participant Flow E2E Spec | Automated test traversing Welcome -> Consent -> Demographics -> Induction -> Stimulus -> Rating -> Trial 2. | M2 | DONE | Survey (Explorer 2) |
| 8 | R2: Inclusion/Exclusion E2E Spec | Automated test verifying non-qualifying participants are routed to Control condition. | M2 | DONE | Survey (Explorer 2) |
| 9 | R2: Admin & CSV Export E2E Spec | Automated test verifying password login, stats cards, and downloadable CSV generation. | M2 | DONE | Survey (Explorer 2) |
| 10 | R2: Console Command Script | `npm run test:e2e` configured in `package.json` executing cleanly with exit code 0. | M2 | DONE | ORIGINAL_REQUEST (2026-09-21) |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| **M1** | Visual Timer Fix (`StimulusReadingScreen.tsx` & `timing.ts`) | Implement 15s timer, cache detection, smooth progress bar, anti-clipping responsive layout, countdown label. | Survey | DONE |
| **M2** | Automated E2E Test Suite (`npm run test:e2e`) | Playwright setup, `playwright.config.ts`, 3 E2E test specs, `package.json` scripts. | M1 | DONE |
| **M3** | Final Acceptance, Dual Track Verification & Victory Audit | Run `npm run test:e2e`, `npm test`, `npm run build`, `npm run lint`. Reviewer approval, Challenger verification, Forensic Audit. | M1, M2 | DONE |

---

## Final Verification Summary
- `npm run test:e2e`: 3/3 passed in 32.7s (exit code 0).
- `npm test`: 143/143 invariants passed across 4 tiers in 0.38s (exit code 0).
- `npx tsx tests/adversarial_m2_timing_ui.test.ts`: 10/10 passed in 18ms (exit code 0).
- `npx tsx tests/adversarial_gen3_r1_timing.test.ts`: 18/18 passed (exit code 0).
- `npm run lint`: 0 errors, 0 warnings (exit code 0).
- `npm run build`: 11/11 pages statically/dynamically compiled (exit code 0).
- Reviewer 1 Verdict: **APPROVE**
- Reviewer 2 Verdict: **APPROVE**
- Challenger 1 Verdict: **APPROVE**
- Challenger 2 Verdict: **APPROVE**
- Forensic Auditor Verdict: **CLEAN**
- Gate Result: **PASS**
