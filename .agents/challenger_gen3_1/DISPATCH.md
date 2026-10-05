# Task Assignment — Challenger Gen3-1 (Visual Timer Stress & Oracles)

**Role**: teamwork_preview_challenger
**Assigned Working Directory**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_gen3_1
**Authoritative Request**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md
**Project Plan**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_3\PROJECT.md
**Worker Handoff**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_gen3_1\handoff.md
**Target Codebase**: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento

## Objective
Empirically verify and stress test R1 (Visual Timer in `StimulusReadingScreen.tsx` & `src/lib/timing.ts`).

## Verification Instructions
1. Verify that `STIMULUS_EXPOSURE_DURATION_MS` is strictly 15000 ms.
2. Verify that there is NO user bypass, skip button, or key press that allows advancing before the 15 seconds expire.
3. Test adversarial scenarios: image already cached, image fails to load (fallback headline shown), fast unmounts, double-completion attempts.
4. Execute `npx tsx tests/adversarial_m2_timing_ui.test.ts`.
5. Run custom empirical scripts or assertions if needed.
6. Record your explicit verdict: `APPROVE` or `REQUEST_CHANGES` in:
   `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_gen3_1\handoff.md`.
Send a message back to parent when done.

## 2026-09-21T19:05:03Z
You are assigned as Challenger Gen3-1 (Visual Timer Stress & Oracles).
Your working directory is: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_gen3_1
Your task assignment is at: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_gen3_1\DISPATCH.md
The authoritative user request is at: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md
The project plan is at: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_3\PROJECT.md
Worker handoff: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_gen3_1\handoff.md
Target codebase: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento

Empirically verify and stress test R1 (Visual Timer in StimulusReadingScreen.tsx & src/lib/timing.ts).
1. Verify STIMULUS_EXPOSURE_DURATION_MS is strictly 15000ms.
2. Verify that there is no bypass, skip button, or key press that allows advancing early.
3. Test adversarial scenarios: preloaded/cached image, image load failure fallback, double-completion attempts.
4. Run npx tsx tests/adversarial_m2_timing_ui.test.ts and any additional empirical verifications.
Record your explicit verdict: APPROVE or REQUEST_CHANGES in:
C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_gen3_1\handoff.md
Send a message back to parent when done.
