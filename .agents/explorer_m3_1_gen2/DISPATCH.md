# Dispatch — explorer_m3_1_gen2

## Mission
Investigate and produce a complete blueprint for the Supabase PostgreSQL Database layer (Milestone 3):
1. Complete PostgreSQL DDL (`supabase/schema.sql`) for `participants` and `responses` tables.
2. Row Level Security (RLS) policies allowing anonymous participant insertion and updates on completion while preventing public reads.
3. Stored procedure / RPC function `assign_induction_group()` utilizing `pg_advisory_xact_lock(742911)` for transactional concurrency safety, filtering strictly by `is_included = true`, computing candidate minimum count groups, and breaking ties with `ORDER BY random() LIMIT 1`.
4. Verification plan and SQL test assertions to prove balance invariant $\max(N) - \min(N) \le 1$ under serial and $\le 2$ under high concurrency.

## Mandatory Inputs & Files to Read
- ORIGINAL_REQUEST: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
- PROJECT SPEC: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
- PREVIOUS SURVEY: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_survey_3\handoff.md`
- EXISTING DOMAIN TYPES: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\types\experiment.ts`

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1_gen2`

## Output
Write a complete, self-contained handoff report to `.agents/explorer_m3_1_gen2/handoff.md` with:
- Observation: Exact schema requirements and existing types
- Logic Chain: Detailed SQL DDL, indexes, RLS, and RPC implementation
- Caveats & Risk mitigation
- Conclusion & Drop-in SQL ready for Worker implementation
