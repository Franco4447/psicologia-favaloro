# Dispatch — auditor_m3_1_gen2

## Mission: Forensic Integrity Audit of Milestone 3 Implementation
You are `auditor_m3_1_gen2`. Perform an independent, rigorous forensic integrity audit on the Milestone 3 implementation by `worker_m3_1_gen2`.

## Audit Objectives
Inspect all files touched in Milestone 3:
- `supabase/schema.sql`
- `src/lib/supabase.ts`
- `src/lib/sync.ts`
- `src/app/api/session/route.ts`
- `src/app/api/responses/route.ts`
- `src/app/page.tsx`
- `tests/m3_sync_and_api.test.ts`
- `package.json`

## Integrity Forensics Checks
1. No hardcoded test responses, fake test passes, or mocked shortcuts designed to bypass validation.
2. Verify that `assign_induction_group()` and `create_participant_session()` implement real PostgreSQL advisory lock logic (`pg_advisory_xact_lock(742911)`), dynamic COUNT queries, and genuine tie-breaking.
3. Verify that `InMemoryMockStore` implements the identical min-fill algorithm and genuine state management for local testing without hardcoded return values.
4. Verify that psychological constructs (`is_false_memory`, `is_false_belief`) are calculated strictly and correctly according to cognitive experimental definitions.
5. Verify that `npm run build`, `npm test`, and `npm run test:m3` execute genuinely and produce real exit code 0.

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\auditor_m3_1_gen2`

## Output
Write `handoff.md` with binary verdict: `CLEAN` or `INTEGRITY VIOLATION`. Include full forensic evidence chain.
