# Dispatch — explorer_m3_3_gen2

## Mission
Investigate and produce a complete blueprint for Client-Side Synchronization, Offline Buffering & Resiliency (Milestone 3):
1. `src/lib/sync.ts`: Synchronization manager coordinating:
   - Initial session registration with `/api/session`.
   - Asynchronous trial response buffering and submission: send each response asynchronously in the background so participant flow is never delayed by network roundtrips.
   - Batch sync fallback: if network is intermittent or offline, buffer responses in `sessionStorage` / `localStorage` and flush upon final session completion before the Debriefing/ThankYou screen.
   - Final completion signal (`completed_at`, `status = 'completed'`).
2. Integration with `src/app/page.tsx` and `src/lib/experimentState.ts`:
   - How `page.tsx` calls `sync.ts` across stage transitions without causing UI freezes or timing artifacts.
   - Retaining `performance.now()` precision regardless of network status.
   - Handling edge cases: network timeout, offline browser, retry mechanisms with exponential backoff.
3. Automated unit/integration test specifications for sync and fallback logic.

## Mandatory Inputs & Files to Read
- ORIGINAL_REQUEST: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
- PROJECT SPEC: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
- EXISTING M2 CODE:
  - `web-experimento/src/app/page.tsx`
  - `web-experimento/src/lib/experimentState.ts`
  - `web-experimento/src/lib/sessionRecovery.ts`

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3_gen2`

## Output
Write a complete, self-contaWrite your full handoff report to `.agents/explorer_m3_3_gen2/handoff.md` with:
- Observation: Current UI flow and async boundaries
- Logic Chain: Exact TypeScript code for `src/lib/sync.ts` and step-by-step diff/patch for `src/app/page.tsx`
- Caveats: Zero disruption to reaction timing
- Conclusion & Drop-in code ready for Worker implementation

## 2026-09-21T12:16:28Z
You are explorer_m3_3_gen2, an explorer agent investigating Client-Side Synchronization, Offline Buffering & Resiliency for Milestone 3.
Produce a complete, drop-in TypeScript blueprint for:
1. `src/lib/sync.ts` (asynchronous non-blocking network sync, offline buffer, retry queue)
2. Integration updates for `src/app/page.tsx` that ensure zero interference with 10.0s stimulus timing and millisecond reaction time capture.
Write your full handoff report to: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3_gen2\handoff.md
When finished, send a brief completion message to your parent orchestrator.
