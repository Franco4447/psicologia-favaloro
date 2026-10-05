# Task Assignment: explorer_m3_1

## Objective
Design the complete PostgreSQL Database Schema and Balanced Randomization RPC for Milestone 3:
1. `supabase/schema.sql`:
   - `participants` table (UUID, timestamps, age, gender, studies_psychology, therapeutic_orientation, university, is_included, induction_group, fake_news_set, status, device_type, screen_resolution, user_agent).
   - `responses` table (UUID, participant_id foreign key, presentation_order 1-20, news_id 1-28, is_fake, news_congruence, response_option 1-4, response_label, reading_time_ms, response_time_ms, timestamps).
   - Performance indexes.
   - Row Level Security (RLS) policies.
   - Stored Procedure `assign_induction_group()` using `pg_advisory_xact_lock` to serialize concurrent requests and guarantee group discrepancy <= 1 (serial) and <= 2 (concurrent).

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_survey_3\handoff.md`

## Output Requirements
Write your detailed SQL DDL and RPC specification report to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1\handoff.md`
Then notify the orchestrator via `send_message`.

## 2026-09-21T00:08:24Z
You are explorer_m3_1. Your working directory is C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1.
Read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md, C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md, and C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1\DISPATCH.md.
Design the complete PostgreSQL schema in supabase/schema.sql and the stored procedure assign_induction_group() using pg_advisory_xact_lock.
Write your complete report to C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_1\handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.

