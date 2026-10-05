# Dispatch — explorer_m3_2_gen2

## Mission
Investigate and produce a complete blueprint for the Next.js API Route Handlers and Supabase Client Integration (Milestone 3):
1. `src/lib/supabase.ts`: Supabase client initialization supporting both public client (`anon` key for client components or fallbacks) and admin client (`SUPABASE_SERVICE_ROLE_KEY` for server route handlers). Include mock/offline fallback mode when environment variables are not yet configured.
2. `src/app/api/session/route.ts`:
   - POST handler for participant session creation / initialization.
   - Demographics validation (age >= 18, valid options).
   - Calling `assign_induction_group()` RPC when participant is included; fallback to local heuristic if Supabase is offline.
   - PATCH / PUT handler for updating participant status (`completed`, `completed_at`).
3. `src/app/api/responses/route.ts`:
   - POST handler accepting single trial records or batch trial records (array of 20 items).
   - Validation against `TrialRecord` schema (UUID participantId, newsId 1-28, responseOption 1-4, readingTimeMs, responseTimeMs).
   - Batch insert into `responses` table.
4. Error handling, HTTP status codes (200, 400, 500), and CORS / Content-Type headers.

## Mandatory Inputs & Files to Read
- ORIGINAL_REQUEST: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
- PROJECT SPEC: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
- EXISTING TYPES: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\types\experiment.ts`
- EXISTING WORKER M2 CODE: Inspect `web-experimento/src` components and state machine.

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_2_gen2`

## Output
Write a complete, self-contained handoff report to `.agents/explorer_m3_2_gen2/handoff.md` with:
- Observation: Existing route structure and types
- Logic Chain: Exact TypeScript code for `src/lib/supabase.ts`, `/api/session/route.ts`, and `/api/responses/route.ts`
- Caveats & Security considerations
- Conclusion & Drop-in code ready for Worker implementation

## 2026-09-21T12:16:27Z
You are explorer_m3_2_gen2, an explorer agent investigating the API Route Handlers and Supabase Client for Milestone 3.
Produce a complete, drop-in TypeScript blueprint for:
1. `src/lib/supabase.ts` (public client + server client with graceful offline/dev fallback)
2. `src/app/api/session/route.ts` (POST session init, PATCH completion)
3. `src/app/api/responses/route.ts` (batch/single trial insertion)
Write your full handoff report to:
C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_2_gen2\handoff.md
When finished, send a brief completion message to your parent orchestrator.

