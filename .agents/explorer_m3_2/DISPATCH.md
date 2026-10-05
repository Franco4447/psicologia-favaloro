# Task Assignment: explorer_m3_2

## Objective
Design the Backend API Route Handlers for Milestone 3:
1. `src/app/api/session/route.ts`:
   - POST handler receiving demographics input.
   - Evaluates inclusion via `evaluateInclusion()`.
   - If included: calls Supabase RPC `assign_induction_group` (or balanced server logic if fallback active).
   - If excluded: assigns `control` induction prompt and random cohesive fake news set.
   - Inserts participant row into Supabase `participants` table.
   - Returns session ID, assigned group, and fake news set.
2. `src/app/api/responses/route.ts`:
   - POST handler receiving array of 20 trial records.
   - Validates participant ID and exactly 20 items.
   - Inserts batch of 20 rows into `responses` table.
   - Updates participant status to `'completed'` and `completed_at = now()`.

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\types\experiment.ts`

## Output Requirements
Write your detailed API handler specifications to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_2\handoff.md`
Then notify the orchestrator via `send_message`.

## 2026-09-21T00:08:27Z
Design the Next.js API route handlers in src/app/api/session/route.ts and src/app/api/responses/route.ts.
Write your complete report to C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_2\handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.
