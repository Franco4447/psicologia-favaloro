# Task Assignment: explorer_m2_3

## Objective
Design the Global Experiment State Machine & Runner for Milestone 2 (`src/app/page.tsx`):
1. State machine managing stages: `welcome` -> `consent` -> `demographics` -> `induction` -> `reading` -> `rating` (20-trial loop) -> `debriefing` -> `thankyou`.
2. Integration with `evaluateInclusion` and `getParticipantNewsDeck` to generate the 20-item randomized stimulus deck.
3. Telemetry capture: device type (`desktop`/`mobile`/`tablet`), screen resolution, user agent.
4. Robust session recovery in `sessionStorage` / `localStorage` (handling accidental F5 refresh so participant doesn't lose current trial progress).
5. State accumulation of all 20 trial responses in memory ready for Supabase synchronization in M3.

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\types\experiment.ts`

## Output Requirements
Write your detailed architecture blueprints to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3\handoff.md`
Then notify the orchestrator via `send_message`.

## 2026-09-20T23:49:25Z
You are explorer_m2_3. Your working directory is C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3.
Read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md, C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md, and C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3\DISPATCH.md.
Design the global experiment state machine in src/app/page.tsx, trial runner, telemetry capture, and sessionStorage recovery.
Write your complete report to C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3\handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.
