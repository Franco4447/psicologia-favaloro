# BRIEFING — 2026-09-20T23:56:00Z

## Mission
Design the Global Experiment State Machine & Runner in `src/app/page.tsx`, trial runner, telemetry capture, and sessionStorage recovery for Milestone 2.

## 🔒 My Identity
- Archetype: explorer
- Roles: investigator, architect, designer
- Working directory: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3
- Original parent: a385a74f-853a-4974-829a-239ecab00da0
- Milestone: M2 (Participant Flow & Cognitive UI Engine)

## 🔒 Key Constraints
- Read-only investigation — do NOT implement production source code directly
- Produce structured handoff report in `handoff.md` with 5-component structure
- Design `src/app/page.tsx`, state machine, trial runner, telemetry capture, and sessionStorage recovery
- Coordinate with `explorer_m2_1` and `explorer_m2_2` component contracts
- Notify orchestrator (`a385a74f-853a-4974-829a-239ecab00da0`) via `send_message`

## Current Parent
- Conversation ID: a385a74f-853a-4974-829a-239ecab00da0
- Updated: 2026-09-20T23:56:00Z

## Investigation State
- **Explored paths**: `ORIGINAL_REQUEST.md`, `orchestrator_1/PROJECT.md`, `src/types/experiment.ts`, `src/data/stimuli.ts`, `src/lib/assets.ts`, `tests/e2e/tier1_features.test.ts`, `tests/e2e/harness/experimentEngine.ts`, `tests/e2e/harness/stimulusOracle.ts`, `explorer_m2_1/DISPATCH.md`, `explorer_m2_2/DISPATCH.md`.
- **Key findings**: Complete 8-stage state machine designed via React `useReducer`, 20-trial exposure runner (10s reading -> rating with RT), silent telemetry capture (`deviceType`, `screenResolution`, `userAgent`), tab-scoped `sessionStorage` recovery (`favaloro_exp_session_v1`) preventing loss of progress on accidental F5, and seamless accumulation of all 20 `TrialRecord`s ready for M3 Supabase synchronization.
- **Unexplored areas**: Backend RPC and Supabase tables (handled in M3), admin dashboard routes (handled in M4).

## Key Decisions Made
- Use deterministic FSM via React `useReducer` to enforce strict sequential progression without illegal stage skipping.
- Separate experimental state from ephemeral UI state: persist core experiment state (`participantId`, `demographics`, `isIncluded`, `inductionGroup`, `fakeNewsSet`, `deck`, `currentTrialIndex`, `stage`, `responses`, `telemetry`) into `sessionStorage` with key `favaloro_exp_session_v1`.
- Ensure SSR hydration safety using a mounted latch (`useEffect`) before rendering client-persisted state to avoid Next.js hydration mismatch.
- Integrate asset preloading via `preloadStimuliBatch` upon deck assembly for zero transition latency.
- Protect active participant sessions with `beforeunload` warning.

## Artifact Index
- `.agents/explorer_m2_3/DISPATCH.md` — Task assignment & instructions
- `.agents/explorer_m2_3/BRIEFING.md` — Persistent memory
- `.agents/explorer_m2_3/progress.md` — Liveness heartbeat
- `.agents/explorer_m2_3/handoff.md` — Complete 5-component architecture handoff report
