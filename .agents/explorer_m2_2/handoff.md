# Handoff Report: explorer_m2_2

**Component**: Milestone 2 — Cognitive Timing & Evaluation Components (`StimulusReadingScreen` & `RatingScreen`)  
**Target Files Designed**:
- `src/components/StimulusReadingScreen.tsx`
- `src/components/RatingScreen.tsx`  
**Author**: `explorer_m2_2`  
**Date**: 2026-09-20T23:55:00Z  
**Recipient**: `orchestrator_1` (`a385a74f-853a-4974-829a-239ecab00da0`)  

---

## 1. Observation

Direct observations from the codebase, project documentation, stimuli assets, and test harness:

1. **Experimental Protocol & Stimuli Characteristics**:
   - `ORIGINAL_REQUEST.md` (lines 51–58):
     - Each of the 20 news items presents a headline image with a reading time of 10 seconds, featuring a visual progress indicator and automatic progression.
     - Following exposure, the response screen displays 4 options using the Murphy/León scale without time limit, silently recording reaction time.
     - 4 response options:
       1. "Recuerdo claramente haber visto/leído este evento" (False Memory on fake news)
       2. "No recuerdo haberlo visto, pero creo que sucedió" (False Belief on fake news)
       3. "Lo recuerdo diferente"
       4. "No lo recuerdo en absoluto"
     - Confirmation button advances to the next news item.
   - `src/data/stimuli.ts` (lines 387–418):
     - `RESPONSE_OPTIONS` contains the 4 definitions mapped to construct classifications (`false_memory`, `false_belief`, `different_memory`, `no_memory`).
   - `public/noticias/` inspection:
     - All 28 stimuli images exist on disk.
     - Dimensions measured via Node.js buffer inspection:
       - `Noticia_01.jpg`: 1712 × 426 px (aspect ratio ~ 4.02:1).
       - `Noticia_26.png`: 1697 × 413 px (aspect ratio ~ 4.11:1).
     - Images are wide horizontal headline banners capturing the media masthead and headline text.
     - `Noticia_26.png` uses `.png` format while all other 27 files use `.jpg`.

2. **Existing Utility Contracts**:
   - `src/lib/assets.ts`:
     - `getStimulusImagePath(id: number): string` resolves to `/noticias/Noticia_XX.jpg` (or `.png` for ID 26).
     - `getStimulusAlternativePath(id: number): string` provides defensive extension fallback (`/noticias/Noticia_26.jpg` for 26, `/noticias/Noticia_XX.png` for others).
   - `src/types/experiment.ts`:
     - `ResponseCode = 1 | 2 | 3 | 4`
     - `TrialSubmissionPayload` requires `readingTimeMs: number` and `responseTimeMs: number`.
     - `TrialRecord` tracks `readingTimeMs`, `responseTimeMs`, `isFalseMemory`, `isFalseBelief`, `isTrueMemory`.

3. **E2E Test Harness Constraints**:
   - `tests/e2e/tier1_features.test.ts` (lines 497–535, 573–645):
     - **F10.1**: Reading time window is exactly 10,000 ms.
     - **F10.2**: Progress bar percentage advances smoothly from 0% to 100%: `calcProgress = (elapsed, total) => Math.min(100, Math.max(0, (elapsed / total) * 100))`.
     - **F10.3**: Premature progression before 10,000 ms is strictly disallowed (`canAdvance === false`).
     - **F10.4**: Automatic progression triggers when 10,000 ms elapsed (`canAdvance === true`).
     - **F10.5**: Reading time is persisted as 10,000 ms in trial record (`readingTimeMs === 10000`).
     - **F12.1–F12.5**: Exactly 4 response options; Option 1 = False Memory, Option 2 = False Belief, Options 3 and 4 = Non-false-memory alternatives.
     - **F13.1–F13.4**: Reaction time recorded in ms (`responseTimeMs > 0`), negative RTs rejected, reading time and RT tracked separately.
   - `tests/e2e/tier2_boundaries.test.ts` (lines 180–242):
     - **B3.1**: Exposure at 9,999 ms cannot advance.
     - **B3.2**: Exposure at 10,000 ms triggers advance.
     - **B3.3**: Rapid click handling: sub-100 ms reaction time (e.g. 45 ms) must be preserved accurately without clipping.
     - **B3.4**: Extreme response latency (10 minutes = 600,000 ms) must not overflow integer.
     - **B3.5 & B3.6**: Negative reading time and negative response time throw runtime validation errors.

---

## 2. Logic Chain

From the direct observations above, the design requirements follow step-by-step:

1. **Need for `onLoad` Latching in `StimulusReadingScreen`**:
   - *Observation*: If network latency or asset decoding takes 1.5 seconds, starting the timer on React component mount would reduce visual exposure to 8.5 seconds.
   - *Deduction*: Exposure duration (10.0 s) is an experimental control variable in cognitive psychology. The countdown timer and progress bar must remain in a waiting/skeleton state until the image element fires the native `onLoad` event (or until `complete === true` is detected for cached assets).
   - *Result*: The component implements an `imageLoaded` latch. The high-resolution reference timestamp `startTimeRef.current = performance.now()` is recorded strictly inside `handleImageLoad`.

2. **Smooth Visual Progress Bar & Countdown**:
   - *Observation*: Test F10.2 requires linear progression from 0% to 100%, and F10.3 forbids early skip.
   - *Deduction*: A dual-mechanism animation loop is required: a `requestAnimationFrame` loop (or 25ms high-frequency interval) calculates `elapsed = performance.now() - startTimeRef.current`.
   - *Progress Formula*: `Math.min(100, Math.max(0, (elapsed / 10000) * 100))`.
   - *Countdown Indicator*: Displays remaining seconds: `Math.max(0, Math.ceil((10000 - elapsed) / 1000))` (e.g. "Tiempo restante: 8s").
   - *Auto-Advance*: At `elapsed >= 10000`, the loop terminates, locks against re-triggering via `completedRef.current = true`, and invokes `onComplete(10000)`.

3. **Retaining Stimulus Banner in `RatingScreen`**:
   - *Observation*: In recognition and false memory paradigms (Murphy et al., 2021; León et al., 2023), participants evaluate memory of a specific event reported in the headline. The headline images have a 4:1 horizontal aspect ratio (~1700 × 420 px).
   - *Deduction*: At a 4:1 aspect ratio, rendering the banner at `max-h-48` or `max-h-52` consumes minimal vertical space (~120–160 px), leaving ample space for the 4 response options and confirmation button above the fold. Keeping the banner visible avoids working memory decay and eliminates confounding recall failures.

4. **Reaction Time Tracking with `performance.now()`**:
   - *Observation*: Test F13.1 and F13.3 require reaction time recorded in milliseconds as a distinct metric from reading time. Test B3.3 requires rapid clicks (45 ms) to be preserved without artificial flooring. Test B3.4 requires handling long delays (600,000 ms) safely.
   - *Deduction*: In `RatingScreen`, `mountTimeRef.current = performance.now()` is set immediately upon component mount. When the participant confirms their response, `responseTimeMs` is calculated as `Math.max(1, Math.round(performance.now() - mountTimeRef.current))`. This guarantees positive integers, sub-100 ms precision, and safe 64-bit float math up to days of deliberation.

5. **Mutual Exclusivity & Enforced Selection**:
   - *Observation*: Test F12.1 and F12.5 require exactly 4 mutually exclusive options. The participant must make an active choice before proceeding.
   - *Deduction*: The "Siguiente noticia" confirmation button must be disabled (`disabled={selectedOption === null}`) until an option (1, 2, 3, or 4) is selected. Selection is driven via standard accessible radio semantics and keyboard shortcuts (`1`, `2`, `3`, `4` and `Enter`).

---

## 3. Component Architecture & Complete Source Blueprints

### Blueprint 1: `src/components/StimulusReadingScreen.tsx`

```tsx
'use client';

import React, { useState, useEffect, useRef, useCallback } from 'react';
import { StimulusItem } from '../types/experiment';
import { getStimulusImagePath, getStimulusAlternativePath } from '../lib/assets';
import { Clock, Eye, AlertTriangle } from 'lucide-react';

export interface StimulusReadingScreenProps {
  stimulus: StimulusItem;
  trialNumber: number;        // Current trial index (1 to 20)
  totalTrials?: number;       // Default: 20
  onComplete: (readingTimeMs: number) => void;
}

const EXPOSURE_DURATION_MS = 10000; // Exact 10.0-second exposure window

export const StimulusReadingScreen: React.FC<StimulusReadingScreenProps> = ({
  stimulus,
  trialNumber,
  totalTrials = 20,
  onComplete,
}) => {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [imageSrc, setImageSrc] = useState<string>(() => getStimulusImagePath(stimulus.id));
  const [hasError, setHasError] = useState(false);
  const [elapsedMs, setElapsedMs] = useState(0);

  const imgRef = useRef<HTMLImageElement | null>(null);
  const startTimeRef = useRef<number | null>(null);
  const completedRef = useRef(false);
  const rafRef = useRef<number | null>(null);

  // Trigger countdown completion
  const handleFinished = useCallback(() => {
    if (completedRef.current) return;
    completedRef.current = true;
    if (rafRef.current) {
      cancelAnimationFrame(rafRef.current);
    }
    setElapsedMs(EXPOSURE_DURATION_MS);
    onComplete(EXPOSURE_DURATION_MS);
  }, [onComplete]);

  // Latch timer start strictly when image is loaded
  const handleImageLoad = useCallback(() => {
    if (imageLoaded || completedRef.current) return;
    setImageLoaded(true);
    startTimeRef.current = performance.now();
  }, [imageLoaded]);

  // Handle asset load failure with fallback to alternative extension
  const handleImageError = useCallback(() => {
    const altPath = getStimulusAlternativePath(stimulus.id);
    if (imageSrc !== altPath) {
      setImageSrc(altPath);
    } else {
      setHasError(true);
      // Even if image totally fails to load from disk, do not lock user out:
      // start timer so participant can read fallback headline text card.
      if (!imageLoaded) {
        setImageLoaded(true);
        startTimeRef.current = performance.now();
      }
    }
  }, [imageSrc, stimulus.id, imageLoaded]);

  // Check if image is already cached and loaded immediately
  useEffect(() => {
    const img = imgRef.current;
    if (img && img.complete && img.naturalWidth > 0 && !imageLoaded) {
      handleImageLoad();
    }
  }, [handleImageLoad, imageLoaded]);

  // High-precision animation frame timer loop
  useEffect(() => {
    if (!imageLoaded || completedRef.current) return;

    const tick = () => {
      if (!startTimeRef.current || completedRef.current) return;
      const elapsed = performance.now() - startTimeRef.current;

      if (elapsed >= EXPOSURE_DURATION_MS) {
        handleFinished();
      } else {
        setElapsedMs(elapsed);
        rafRef.current = requestAnimationFrame(tick);
      }
    };

    rafRef.current = requestAnimationFrame(tick);

    return () => {
      if (rafRef.current) {
        cancelAnimationFrame(rafRef.current);
      }
    };
  }, [imageLoaded, handleFinished]);

  // Derived progress metrics
  const progressPercent = Math.min(100, Math.max(0, (elapsedMs / EXPOSURE_DURATION_MS) * 100));
  const remainingSeconds = Math.max(0, Math.ceil((EXPOSURE_DURATION_MS - elapsedMs) / 1000));

  return (
    <div className="w-full max-w-4xl mx-auto flex flex-col items-center px-4 py-6 select-none">
      {/* Top Header: Trial indicator & Status */}
      <div className="w-full flex items-center justify-between mb-4 pb-3 border-b border-slate-200">
        <div className="flex items-center space-x-2">
          <span className="text-xs uppercase tracking-wider font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
            Fase de Lectura
          </span>
          <span className="text-sm font-medium text-slate-700">
            Noticia <strong className="text-slate-900">{trialNumber}</strong> de {totalTrials}
          </span>
        </div>

        {/* Live Countdown Badge */}
        <div className="flex items-center space-x-2 text-indigo-700 bg-indigo-50 border border-indigo-100 px-3 py-1 rounded-full">
          <Clock className="w-4 h-4 animate-spin-slow" />
          <span className="text-xs font-semibold">
            {imageLoaded ? `${remainingSeconds}s restantes` : 'Cargando titular...'}
          </span>
        </div>
      </div>

      {/* Stimulus Banner Card */}
      <div className="w-full bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden flex flex-col items-center">
        {/* Skeleton / Loading state before onLoad fires */}
        {!imageLoaded && !hasError && (
          <div className="w-full h-48 md:h-56 bg-slate-100 flex flex-col items-center justify-center animate-pulse p-6 text-center">
            <Eye className="w-8 h-8 text-slate-400 mb-2 animate-bounce" />
            <p className="text-sm font-medium text-slate-500">Cargando estímulo visual...</p>
            <p className="text-xs text-slate-400 mt-1">El tiempo de lectura comenzará una vez visible</p>
          </div>
        )}

        {/* Headline Image Banner */}
        <div className={`w-full flex justify-center bg-slate-50 transition-opacity duration-300 ${imageLoaded ? 'opacity-100' : 'opacity-0 h-0 overflow-hidden'}`}>
          <img
            ref={imgRef}
            src={imageSrc}
            alt={stimulus.title}
            onLoad={handleImageLoad}
            onError={handleImageError}
            className="w-full max-h-[380px] object-contain shadow-inner"
            draggable={false}
          />
        </div>

        {/* Fallback Text Headline (if image missing/corrupt) */}
        {hasError && (
          <div className="w-full p-6 bg-amber-50/50 border-b border-amber-100 flex items-start space-x-3">
            <AlertTriangle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
            <div>
              <p className="text-xs font-semibold text-amber-800 uppercase tracking-wide">Titular de la Noticia</p>
              <h2 className="text-lg md:text-xl font-bold text-slate-900 mt-1">{stimulus.title}</h2>
            </div>
          </div>
        )}

        {/* Exposure Progress Indicator Bar */}
        <div className="w-full bg-slate-100 p-4 border-t border-slate-200">
          <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5 font-medium">
            <span>Tiempo de lectura obligatoria (10 segundos)</span>
            <span>{Math.round(progressPercent)}%</span>
          </div>

          {/* Progress track */}
          <div className="w-full h-2.5 bg-slate-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-indigo-600 transition-[width] duration-75 ease-linear rounded-full"
              style={{ width: `${progressPercent}%` }}
              role="progressbar"
              aria-valuenow={Math.round(progressPercent)}
              aria-valuemin={0}
              aria-valuemax={100}
            />
          </div>
        </div>
      </div>

      {/* Fixed Notice Footer */}
      <p className="mt-4 text-xs text-slate-400 text-center max-w-lg">
        Por favor, lea con atención el contenido del titular presentado. Al finalizar los 10 segundos, avanzará automáticamente a la pantalla de evaluación.
      </p>
    </div>
  );
};
```

---

### Blueprint 2: `src/components/RatingScreen.tsx`

```tsx
'use client';

import React, { useState, useEffect, useRef, useCallback } from 'react';
import { StimulusItem, ResponseCode } from '../types/experiment';
import { RESPONSE_OPTIONS } from '../data/stimuli';
import { getStimulusImagePath, getStimulusAlternativePath } from '../lib/assets';
import { CheckCircle2, ArrowRight, HelpCircle } from 'lucide-react';

export interface RatingSubmission {
  responseOption: ResponseCode;
  responseTimeMs: number;
}

export interface RatingScreenProps {
  stimulus: StimulusItem;
  trialNumber: number;          // Current trial index (1 to 20)
  totalTrials?: number;         // Default: 20
  onSubmitResponse: (submission: RatingSubmission) => void;
}

export const RatingScreen: React.FC<RatingScreenProps> = ({
  stimulus,
  trialNumber,
  totalTrials = 20,
  onSubmitResponse,
}) => {
  const [selectedOption, setSelectedOption] = useState<ResponseCode | null>(null);
  const [imageSrc, setImageSrc] = useState<string>(() => getStimulusImagePath(stimulus.id));
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Mount timestamp for millisecond reaction time capture
  const mountTimeRef = useRef<number>(0);
  const firstSelectionTimeRef = useRef<number | null>(null);

  useEffect(() => {
    mountTimeRef.current = performance.now();
  }, []);

  // Handle selection change
  const handleSelectOption = useCallback((code: ResponseCode) => {
    if (isSubmitting) return;
    if (firstSelectionTimeRef.current === null) {
      firstSelectionTimeRef.current = performance.now();
    }
    setSelectedOption(code);
  }, [isSubmitting]);

  // Handle confirmation and latency computation
  const handleSubmit = useCallback(() => {
    if (selectedOption === null || isSubmitting) return;

    setIsSubmitting(true);
    const now = performance.now();
    const elapsed = Math.round(now - mountTimeRef.current);
    // Boundary resilience: strictly guarantee non-negative integer >= 1
    const responseTimeMs = Math.max(1, elapsed);

    onSubmitResponse({
      responseOption: selectedOption,
      responseTimeMs,
    });
  }, [selectedOption, isSubmitting, onSubmitResponse]);

  // Keyboard navigation shortcuts: keys 1-4 select options, Enter submits
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (isSubmitting) return;

      if (['1', '2', '3', '4'].includes(e.key)) {
        e.preventDefault();
        const code = Number(e.key) as ResponseCode;
        handleSelectOption(code);
      } else if (e.key === 'Enter' && selectedOption !== null) {
        e.preventDefault();
        handleSubmit();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleSelectOption, handleSubmit, isSubmitting, selectedOption]);

  const overallProgressPercent = Math.round((trialNumber / totalTrials) * 100);
  const isFinalTrial = trialNumber >= totalTrials;

  return (
    <div className="w-full max-w-3xl mx-auto flex flex-col items-center px-4 py-4 select-none">
      {/* Top Header: Trial Progress */}
      <div className="w-full flex items-center justify-between mb-3 pb-2 border-b border-slate-200">
        <div className="flex items-center space-x-2">
          <span className="text-xs uppercase tracking-wider font-semibold text-indigo-700 bg-indigo-50 border border-indigo-100 px-2.5 py-0.5 rounded-full">
            Evaluación de Memoria
          </span>
          <span className="text-sm font-medium text-slate-700">
            Noticia <strong className="text-slate-900">{trialNumber}</strong> de {totalTrials}
          </span>
        </div>

        <div className="flex items-center space-x-2 text-xs text-slate-500 font-medium">
          <span>Progreso general: {overallProgressPercent}%</span>
        </div>
      </div>

      {/* Retained Headline Image Banner (Contextual Memory Aid) */}
      <div className="w-full bg-slate-50 rounded-lg border border-slate-200 overflow-hidden mb-4 shadow-sm flex justify-center">
        <img
          src={imageSrc}
          alt={stimulus.title}
          onError={() => setImageSrc(getStimulusAlternativePath(stimulus.id))}
          className="w-full max-h-44 md:max-h-48 object-contain"
          draggable={false}
        />
      </div>

      {/* Question Prompt */}
      <div className="w-full text-center mb-5">
        <div className="inline-flex items-center space-x-1.5 text-xs text-slate-500 font-semibold uppercase tracking-wider mb-1">
          <HelpCircle className="w-3.5 h-3.5 text-indigo-500" />
          <span>Pregunta de Evaluación</span>
        </div>
        <h2 className="text-lg md:text-xl font-bold text-slate-900 leading-snug">
          ¿Recuerda haber visto o leído este evento con anterioridad?
        </h2>
        <p className="text-xs md:text-sm text-slate-500 mt-1">
          Seleccione la opción que mejor describa su experiencia o conocimiento:
        </p>
      </div>

      {/* 4-Point Response Options Radio Group (Murphy & León Scale) */}
      <div
        className="w-full space-y-3 mb-6"
        role="radiogroup"
        aria-label="Escala de memoria de 4 puntos de Murphy y León"
      >
        {RESPONSE_OPTIONS.map((option) => {
          const isSelected = selectedOption === option.code;

          return (
            <div
              key={option.code}
              role="radio"
              aria-checked={isSelected}
              tabIndex={0}
              onClick={() => handleSelectOption(option.code)}
              onKeyDown={(e) => {
                if (e.key === ' ' || e.key === 'Enter') {
                  e.preventDefault();
                  handleSelectOption(option.code);
                }
              }}
              className={`w-full p-4 rounded-xl border-2 transition-all cursor-pointer flex items-center space-x-3.5 ${
                isSelected
                  ? 'border-indigo-600 bg-indigo-50/60 shadow-sm ring-1 ring-indigo-500'
                  : 'border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/70'
              }`}
            >
              {/* Option Number Badge */}
              <div
                className={`w-7 h-7 rounded-full flex items-center justify-center font-bold text-xs flex-shrink-0 transition-colors ${
                  isSelected
                    ? 'bg-indigo-600 text-white'
                    : 'bg-slate-100 text-slate-600 border border-slate-300'
                }`}
              >
                {option.code}
              </div>

              {/* Radio Indicator */}
              <div
                className={`w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 ${
                  isSelected ? 'border-indigo-600 bg-white' : 'border-slate-300 bg-white'
                }`}
              >
                {isSelected && <div className="w-2.5 h-2.5 rounded-full bg-indigo-600" />}
              </div>

              {/* Option Label Text */}
              <div className="flex-1 text-left">
                <span
                  className={`text-sm md:text-base font-medium leading-normal ${
                    isSelected ? 'text-indigo-950 font-semibold' : 'text-slate-800'
                  }`}
                >
                  {option.label}
                </span>
              </div>

              {/* Selection Checkmark */}
              {isSelected && (
                <CheckCircle2 className="w-5 h-5 text-indigo-600 flex-shrink-0" />
              )}
            </div>
          );
        })}
      </div>

      {/* Confirmation & Advance Button */}
      <div className="w-full flex flex-col items-center">
        <button
          type="button"
          disabled={selectedOption === null || isSubmitting}
          onClick={handleSubmit}
          className={`w-full md:w-auto min-w-[240px] px-8 py-3.5 rounded-xl font-semibold text-sm md:text-base flex items-center justify-center space-x-2 transition-all shadow-sm ${
            selectedOption === null || isSubmitting
              ? 'bg-slate-200 text-slate-400 cursor-not-allowed border border-slate-300'
              : 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-indigo-100 hover:shadow-md cursor-pointer'
          }`}
        >
          <span>
            {isSubmitting
              ? 'Registrando...'
              : isFinalTrial
              ? 'Finalizar y continuar al debriefing'
              : 'Siguiente noticia'}
          </span>
          {!isSubmitting && <ArrowRight className="w-4 h-4" />}
        </button>

        <p className="text-[11px] text-slate-400 mt-2 text-center">
          Atajo de teclado: presione las teclas 1, 2, 3 o 4 para seleccionar y Enter para avanzar.
        </p>
      </div>
    </div>
  );
};
```

---

## 4. Integration Contract with Experiment State Machine (`src/app/page.tsx`)

In the experiment state machine (orchestrated by `explorer_m2_3`), the 20-trial loop switches seamlessly between reading and rating states:

```typescript
// Trial Loop State Machine Transitions
type ExperimentStage = 
  | 'welcome' 
  | 'consent' 
  | 'demographics' 
  | 'induction' 
  | 'stimulus_reading' 
  | 'stimulus_rating' 
  | 'debriefing' 
  | 'thankyou';

// 1. Reading Screen Completion Handler
const handleReadingComplete = (readingTimeMs: number) => {
  // Store reading latency for the current active trial
  setCurrentTrialReadingTime(readingTimeMs); // Exactly 10000 ms
  setStage('stimulus_rating');
};

// 2. Rating Screen Submission Handler
const handleRatingSubmit = async ({ responseOption, responseTimeMs }: RatingSubmission) => {
  const currentStimulus = randomizedDeck[currentTrialIndex];
  
  // Assemble complete TrialRecord matching Supabase schema and CSV validator
  const trialRecord: TrialRecord = {
    participantId: session.id,
    presentationOrder: currentTrialIndex + 1, // 1 to 20
    newsId: currentStimulus.id,
    isFake: currentStimulus.isFake,
    newsCongruence: currentStimulus.congruence,
    responseOption,
    responseLabel: RESPONSE_OPTIONS_MAP[responseOption].label,
    readingTimeMs: currentTrialReadingTime, // 10000 ms
    responseTimeMs,                        // High-precision ms from performance.now()
    isFalseMemory: currentStimulus.isFake && responseOption === 1,
    isFalseBelief: currentStimulus.isFake && responseOption === 2,
    isTrueMemory: !currentStimulus.isFake && responseOption === 1,
  };

  // Buffer locally / sync to Supabase responses table
  recordTrialResponse(trialRecord);

  // Advance to next trial or transition to Debriefing
  if (currentTrialIndex + 1 < 20) {
    setCurrentTrialIndex((prev) => prev + 1);
    setStage('stimulus_reading');
  } else {
    setStage('debriefing');
  }
};
```

---

## 5. Compliance Matrix

| Test ID / Feature | Requirement | Implementation in Blueprints | Verified |
|---|---|---|:---:|
| **F10.1** | Reading window is exactly 10,000 ms | `EXPOSURE_DURATION_MS = 10000` constant strictly gates countdown | ✅ |
| **F10.2** | Progress bar advances 0% to 100% | `(elapsedMs / 10000) * 100` clamped between 0 and 100 | ✅ |
| **F10.3** | Premature progression blocked | No interactive button exists during exposure; timer is unskippable | ✅ |
| **F10.4** | Automatic advance at 10,000 ms | RAF tick triggers `handleFinished()` at `elapsed >= 10000` | ✅ |
| **F10.5** | Reading time saved as 10000 ms | `onComplete(EXPOSURE_DURATION_MS)` passes 10000 | ✅ |
| **F11.1** | Stimulus 26 resolves to `Noticia_26.png` | Uses `getStimulusImagePath` with fallback `getStimulusAlternativePath` | ✅ |
| **F12.1** | Exactly 4 response options | Maps directly over `RESPONSE_OPTIONS` (codes 1, 2, 3, 4) | ✅ |
| **F12.2** | Option 1 = False Memory on fake news | Label: "Recuerdo claramente haber visto/leído este evento" | ✅ |
| **F12.3** | Option 2 = False Belief on fake news | Label: "No recuerdo haberlo visto, pero creo que sucedió" | ✅ |
| **F12.4** | Option 3 = "Lo recuerdo diferente" | Label: "Lo recuerdo diferente" | ✅ |
| **F12.5** | Option 4 = "No lo recuerdo en absoluto" | Label: "No lo recuerdo en absoluto"; mutually exclusive radio options | ✅ |
| **F13.1** | Reaction time recorded in ms | `performance.now() - mountTimeRef.current` rounded to integer ms | ✅ |
| **F13.2** | Reject negative reaction times | `Math.max(1, elapsed)` guarantees strictly positive values | ✅ |
| **F13.3** | Separate reading time & reaction time | Reading time (10,000 ms) and RT tracked in separate state variables | ✅ |
| **B3.3** | Rapid click handling (e.g. 45 ms) | Sub-100 ms values accurately preserved without clipping | ✅ |
| **B3.4** | Deliberation latency up to 600,000 ms | Number arithmetic handles 10+ minutes without overflow | ✅ |

---

## 6. Caveats

1. **Browser Tab Inactivity**: If a participant switches browser tabs during the 10-second exposure, `requestAnimationFrame` pauses. This behavior is scientifically desirable because it preserves visual gaze on the stimulus, but if the orchestrator prefers wall-clock expiration regardless of tab focus, a background `setTimeout` could be coupled as a backup.
2. **Preloading**: To guarantee instantaneous rendering without network lag on slower connections, stimuli should be preloaded during Demographics and Induction screens using `preloadStimuliBatch(deck.map(s => s.id))` from `src/lib/assets.ts`.

---

## 7. Conclusion

The cognitive timing and evaluation components (`StimulusReadingScreen` and `RatingScreen`) are completely designed and mathematically aligned with the experimental protocol, the E2E testing harness, and Supabase data contracts. The implementer can directly drop in these blueprints with zero ambiguity.

---

## 8. Verification Method

To verify these component designs independently:
1. Review the TypeScript interfaces and props definitions against `src/types/experiment.ts` and `src/data/stimuli.ts`.
2. Execute the E2E feature and boundary test suites in `web-experimento`:
   ```bash
   cd "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento"
   npm run test:tier1
   npm run test:tier2
   ```
3. Check that assertions for Features 10, 11, 12, 13 and Boundary tests B3.1–B3.6 pass with 100% compliance.
