# Task Assignment: challenger_m1_1

## Objective
Empirical Adversarial Stress Testing of Milestone 1 in `web-experimento`:
1. Write and execute an automated stress-testing script (in TypeScript / Node) that runs 1,000 randomized participant assignments across all permutations:
   - Psychoanalysis included
   - Evidence-based included
   - Psychology = No (excluded)
   - Orientation = Otros (excluded)
2. In each of the 1,000 iterations, verify:
   - Exactly 20 items returned.
   - Exactly 12 true news items (IDs 1-12).
   - Exactly 8 fake news items.
   - For Psychoanalysis: fake IDs must be {14, 16, 18, 20, 21, 23, 25, 27}.
   - For Evidence-Based: fake IDs must be {13, 15, 17, 19, 22, 24, 26, 28}.
   - Zero duplicate news IDs in the 20-item deck.
   - Shuffling distributes items uniformly across presentation orders 1 to 20.
3. Issue an explicit verdict: `APPROVE` or `REQUEST_CHANGES`.

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m1_1\handoff.md`

## Output Requirements
Write your adversarial test report and explicit verdict to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_m1_1\handoff.md`
## 2026-09-20T23:40:47Z
You are challenger_m1_1. Your working directory is C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_m1_1.
Read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md, C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md, and C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_m1_1\DISPATCH.md.
Also read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\worker_m1_1\handoff.md.
Empirically stress-test Milestone 1 set selection and randomization over 1,000 randomized iterations. Verify deck size (20), true/fake balance (12/8), exact congruence sets, zero duplicates, and uniform shuffling. Issue an explicit APPROVE or REQUEST_CHANGES verdict in your handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.
