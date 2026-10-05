# Task Assignment: explorer_m2_2

## Objective
Design the Cognitive Timing & Evaluation Components for Milestone 2:
1. Stimulus Reading Screen (`src/components/StimulusReadingScreen.tsx`):
   - Shows headline image banner.
   - Forced 10.0-second exposure with smooth CSS/JS animated progress bar and countdown indicator.
   - Timer starts ONLY after image successfully loads (`onLoad`).
   - Auto-advance to rating screen at exactly 10,000 ms.
   - User cannot skip early.
   - Captures `reading_time_ms`.
2. Rating Screen (`src/components/RatingScreen.tsx`):
   - Keeps headline image banner visible at top for contextual memory.
   - 4-point response radio group (Murphy & León scale: 1 = Falso Recuerdo, 2 = Falsa Creencia, 3 = Lo recuerdo diferente, 4 = No lo recuerdo en absoluto).
   - "Siguiente noticia" confirmation button disabled until selection.
   - Measures reaction time in milliseconds from mounting to click using `performance.now()`.
   - Trial progress indicator (e.g. "Noticia 1 de 20").

## Mandatory Inputs to Read
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md`
3. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\data\stimuli.ts`

## Output Requirements
Write your detailed component blueprints to:
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_2\handoff.md`
Then notify the orchestrator via `send_message`.

## 2026-09-20T23:49:25Z
You are explorer_m2_2. Your working directory is C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_2.
Read C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\ORIGINAL_REQUEST.md, C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\orchestrator_1\PROJECT.md, and C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_2\DISPATCH.md.
Design the StimulusReadingScreen (10s forced exposure, progress bar, onLoad latching) and RatingScreen (Murphy/León 4-point scale, performance.now() reaction time measurement).
Write your complete report to C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_2\handoff.md.
When finished, notify the orchestrator (conversation ID a385a74f-853a-4974-829a-239ecab00da0) via send_message.

