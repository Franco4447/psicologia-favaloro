# Dispatch — reviewer_m3_1_gen2

## Mission: Independent Review of Milestone 3 Database Schema, RPC & API Route Handlers
You are `reviewer_m3_1_gen2`. Review the Milestone 3 implementation by `worker_m3_1_gen2`.

## Files to Review & Run
- `supabase/schema.sql`: Review DDL for `participants` and `responses`, indexes, RLS policies, `assign_induction_group()` with `pg_advisory_xact_lock(742911)`, and `create_participant_session()`.
- `src/lib/supabase.ts`: Supabase client configuration, environment detection, and fallback mock store.
- `src/app/api/session/route.ts`: Session creation, demographics validation, group allocation, completion update.
- `src/app/api/responses/route.ts`: Trial recording, batch handling, construct calculation, idempotent upserts.
- Worker handoff: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m3_1_gen2\handoff.md`
- Context: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`

## Required Verification
Execute and verify:
- `npx tsc --noEmit`
- `npm run lint`
- `npm run build`
- `npm test`
- `npm run test:m3`

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\reviewer_m3_1_gen2`

## Output
Write `handoff.md` to your directory with explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Include verbatim test results and command outputs.
