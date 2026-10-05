# Task Assignment: explorer_m3_3

## Objective
Design the Supabase Client Module and Client-Side Sync Integration for Milestone 3:
1. `src/lib/supabase.ts`:
   - Configures `@supabase/supabase-js` client using `process.env.NEXT_PUBLIC_SUPABASE_URL` and `process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY`.
   - Server-side admin client using `process.env.SUPABASE_SERVICE_ROLE_KEY`.
   - Resilient development fallback: if env vars are missing or offline, provides an in-memory / mock repository that implements identical table queries and RPC calls so tests and local preview never crash.
2. Integration into `src/app/page.tsx`:
   - Submits demographics to `/api/session` upon demographic form completion.
   - Upon completing trial 20, transmits the 20 trial records to `/api/responses`.
   - Displays a clean saving spinner and handles retry if transient network error occurs before transitioning to Debriefing.

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\app\page.tsx`

## Output Requirements
Write your detailed client and sync integration specification to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3\handoff.md`
Then notify the orchestrator via `send_message`.

## 2026-09-21T00:08:27Z
You are explorer_m3_3. Your working directory is C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3.
Read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md, C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md, and C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3\DISPATCH.md.
Design the Supabase client module in src/lib/supabase.ts (with resilient offline/dev mock repository) and client sync integration in src/app/page.tsx.
Write your complete report to C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3\handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.

