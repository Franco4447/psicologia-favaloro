# Task Assignment: worker_m2_1

## Objective: Milestone 2 Implementation
Implement Milestone 2: Participant Flow & Cognitive UI Engine in:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`

## Scope of Files Exclusively Owned by this Worker
- `src/components/WelcomeScreen.tsx`
- `src/components/ConsentScreen.tsx`
- `src/components/DemographicsScreen.tsx`
- `src/components/InductionScreen.tsx`
- `src/components/StimulusReadingScreen.tsx`
- `src/components/RatingScreen.tsx`
- `src/components/DebriefingScreen.tsx`
- `src/components/ThankYouScreen.tsx`
- `src/lib/telemetry.ts`
- `src/lib/sessionRecovery.ts`
- `src/app/page.tsx` (Experiment Flow Orchestrator)

## Blueprints to Follow Verbatim
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_1\handoff.md` (Screen components: Welcome, Consent, Demographics, Induction, Debriefing, Thank You)
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_2\handoff.md` (Timing & Evaluation components: StimulusReadingScreen with 10s auto-advance and onLoad latching, RatingScreen with 4 options and reaction time ms)
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3\handoff.md` (src/app/page.tsx state machine, telemetry, and session recovery)
4. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md` (Verbatim user specifications)
5. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`

## Verification Requirements
You MUST run:
1. `npx tsc --noEmit`
2. `npm run lint`
3. `npm run build`
4. `npm test` (all 143 E2E test assertions must pass!)
Document all verification commands and terminal outputs in your handoff report.

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. An auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Handoff Requirements
Write your detailed report to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m2_1\handoff.md`
Then notify the orchestrator via `send_message`.
