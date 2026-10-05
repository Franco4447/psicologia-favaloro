# Dispatch — worker_m3_1_gen2

## Mission: Implement Milestone 3 — Supabase Database, Balanced RPC & Sync
You are `worker_m3_1_gen2`. Your task is to implement the complete Milestone 3 backend and synchronization architecture for the Universidad Favaloro Experimental Psychology Web Platform.

## Mandatory Inputs & Blueprints to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md` (Authoritative user request)
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md` (Global architecture & contracts)
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1_gen2\handoff.md` (PostgreSQL DDL, RLS, RPC with `pg_advisory_xact_lock(742911)`)
4. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_2_gen2\handoff.md` (Supabase client & Next.js API route handlers)
5. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3_gen2\handoff.md` (Client synchronization manager & page.tsx integration)

## Exclusive File Ownership
You have exclusive write ownership of:
- `supabase/schema.sql`
- `src/lib/supabase.ts`
- `src/lib/sync.ts`
- `src/app/api/session/route.ts`
- `src/app/api/responses/route.ts`
- `src/app/page.tsx` (wire sync without disturbing 10s auto-advance or `performance.now()` RT capture)
- Unit tests: `tests/m3_sync_and_api.test.ts`
- `package.json` (if adding test script)

## Key Technical Requirements
1. `supabase/schema.sql`: Complete DDL for `participants` and `responses`, indexes, RLS policies, and `assign_induction_group()` stored procedure using `pg_advisory_xact_lock(742911)`.
2. `src/lib/supabase.ts`: Both public client (`anon`) and server client (`service_role`), plus in-memory fallback simulation when Supabase credentials are not yet configured in local environment so dev/tests run cleanly without throwing unhandled exceptions.
3. `src/app/api/session/route.ts`: POST to create participant, validate demographics, invoke group allocation (RPC or fallback), PATCH to update status on debriefing.
4. `src/app/api/responses/route.ts`: POST batch (or single) trial responses, compute/verify psychological flags (`is_false_memory`, `is_false_belief`).
5. `src/lib/sync.ts`: Background non-blocking sync, offline buffering in `sessionStorage`/`localStorage`, retry logic with exponential backoff, batch flush.
6. `src/app/page.tsx`: Integrate sync smoothly on session init, trial recording, and completion without introducing any delay to the 10.0s countdown or rating reaction times.
7. Verification: Run `npx tsc --noEmit`, `npm run lint`, `npm run build`, `npm test` (all 143 E2E test assertions must pass), and your M3 tests.

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m3_1_gen2`

## Output
Write your comprehensive handoff report to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m3_1_gen2\handoff.md`
Report exact files touched, build and test outputs, verification commands, and send a completion message to the parent orchestrator.
