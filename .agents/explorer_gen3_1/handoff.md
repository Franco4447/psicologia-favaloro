# Handoff Report: R1 Visual Timer Bug & Layout Investigation

**Agent ID**: `explorer_gen3_1` (Visual Timer Explorer - Generation 3)  
**Assigned Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_gen3_1`  
**Target Codebase Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  
**Authoritative Request**: `ORIGINAL_REQUEST.md` (Update 2026-09-21T18:39:02Z)  
**Date**: 2026-09-21T18:49:00Z  
**Recipient**: Parent Orchestrator (`b5cd7140-5a84-4dbb-95e1-b014abe712b3`)  

---

## Executive Summary

This investigation analyzed Requirement **R1** ("Corrección del Temporizador Visual en `StimulusReadingScreen.tsx`"). Five root causes were identified:
1. **Missing `src/lib/timing.ts` and Duration Discrepancy**: The codebase lacks a centralized `timing.ts` module. While `StimulusReadingScreen.tsx` was recently updated to `15000` ms, outdated comments and tests still reference `10000` ms.
2. **Image Cache Deadlock & Zero-Height Container**: Stimulus assets are preloaded into browser cache by `page.tsx` during experiment initialization. When an image is already cached, or rendered inside a zero-height container (`h-0 overflow-hidden`), browsers (especially Safari/WebKit) do not dispatch subsequent `onLoad` events. Because `imageLoaded` remains `false`, the exposure timer never starts and the progress bar freezes at 0%.
3. **Next.js `<Image>` Test Suite Crash**: Using Next.js `<Image>` from `next/image` in `StimulusReadingScreen.tsx` crashes unit and adversarial tests executed in Node/tsx environments with `React.createElement: type is invalid ... got: object`.
4. **Frame-Rate Thrashing vs. CSS Transition**: `requestAnimationFrame` updates state at ~60fps while the progress element possesses `transition-[width] duration-75 ease-linear`. This continuous cancellation and restarting of 75ms CSS transitions causes visible stuttering, frame drops, or apparent freezing.
5. **Vertical Clipping & Lack of Visual Feedback**: On standard laptop (1366x768 / 1280x800) and mobile viewports, the large fixed card height (380px) and lack of sticky viewport positioning push the 2.5px progress bar below the fold. In addition, no countdown label or remaining seconds text is rendered.

A drop-in implementation has been formulated to resolve all five issues.

---

## 1. Observation

### 1.1 Source Code Analysis

#### A. Missing `src/lib/timing.ts` and Constant Drift
- File search across `src/` confirms `src/lib/timing.ts` **does not exist**.
- In `src/components/StimulusReadingScreen.tsx`:
  - Line 18: `const EXPOSURE_DURATION_MS = 15000; // Exact 10.0-second exposure window`
  - The constant was updated to `15000` in commit `c08208d`, but the comment still states `10.0-second`.
- In `src/components/InductionScreen.tsx`:
  - Line 80: `<p className="text-sm font-semibold text-slate-900">Lectura del Titular (15 seg)</p>`
  - Line 82: `Cada titular se mostrará durante 15 segundos continuos con una barra de progreso visual. Léalo detenidamente.`
- In `src/types/experiment.ts`:
  - Line 169: `readingTimeMs: number; // Exposure latency on Screen 1 (~10,000 ms)`
- In `tests/adversarial_m2_timing_ui.test.ts`:
  - Line 33: `const EXPOSURE_MS = 10000;`
- In `tests/e2e/tier1_features.test.ts`:
  - Line 499: `const targetDurationMs = 10000;`

#### B. Component Image Loading Flow (`src/components/StimulusReadingScreen.tsx`)
Lines 27–59 and 122–146 currently read:
```tsx
const [imageLoaded, setImageLoaded] = useState(false);
const [imageSrc, setImageSrc] = useState<string>(() => getStimulusImagePath(stimulus.id));
const [hasError, setHasError] = useState(false);
const [elapsedMs, setElapsedMs] = useState(0);

const handleImageLoad = useCallback(() => {
  if (imageLoaded) return;
  setImageLoaded(true);
}, [imageLoaded]);
...
{/* Stimulus Banner Card */}
<div className="w-full bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden flex flex-col items-center">
  {!imageLoaded && !hasError && (
    <div className="w-full h-[380px] bg-slate-100 flex flex-col items-center justify-center animate-pulse p-6 text-center">
      <Eye className="w-8 h-8 text-slate-400 mb-2 animate-bounce" />
      <p className="text-sm font-medium text-slate-500">Cargando estímulo visual...</p>
      <p className="text-xs text-slate-400 mt-1">El tiempo de lectura comenzará una vez visible</p>
    </div>
  )}

  {/* Headline Image Banner */}
  <div className={`w-full flex justify-center bg-slate-50 transition-opacity duration-300 ${imageLoaded ? 'opacity-100 relative h-[380px]' : 'absolute opacity-0 pointer-events-none h-0 overflow-hidden'}`}>
    <Image
      src={imageSrc}
      alt={stimulus.title}
      fill
      sizes="(max-width: 768px) 100vw, 896px"
      style={{ objectFit: 'contain' }}
      onLoad={handleImageLoad}
      onError={handleImageError}
      priority
      unoptimized={true}
    />
  </div>
```
Observations:
1. When `imageLoaded` is `false`, the outer div is styled as `absolute opacity-0 pointer-events-none h-0 overflow-hidden`.
2. The card parent container (`<div className="w-full bg-white rounded-xl ...">`) lacks `position: relative`, meaning the `absolute` positioning breaks standard document flow and anchors to ancestor boundaries.
3. In commit `cee8c8c`, the previous `img.complete` check was deleted:
   ```tsx
   // REMOVED in commit cee8c8c:
   useEffect(() => {
     const img = imgRef.current;
     if (img && img.complete && img.naturalWidth > 0 && !imageLoaded) {
       handleImageLoad();
     }
   }, [handleImageLoad, imageLoaded]);
   ```
4. Background preloading (`preloadStimuliBatch` in `src/app/page.tsx:91-98`) preloads all 20 stimulus images before the user reaches the trial stage. When the user navigates to `StimulusReadingScreen`, the asset is already in browser cache.

#### C. Animation Frame Loop & CSS Conflict
Lines 63–95 and 159–174 of `src/components/StimulusReadingScreen.tsx`:
```tsx
useEffect(() => {
  if (!imageLoaded) return;
  
  let isUnmounted = false;
  let rafId: number | null = null;
  const start = performance.now();

  const tick = () => {
    if (isUnmounted) return;
    const elapsed = performance.now() - start;

    if (elapsed >= EXPOSURE_DURATION_MS) {
      setElapsedMs(EXPOSURE_DURATION_MS);
      if (onExposureComplete) onExposureComplete(EXPOSURE_DURATION_MS);
      if (onComplete) onComplete(EXPOSURE_DURATION_MS);
    } else {
      setElapsedMs(elapsed);
      rafId = requestAnimationFrame(tick);
    }
  };

  rafId = requestAnimationFrame(tick);

  return () => {
    isUnmounted = true;
    if (rafId) cancelAnimationFrame(rafId);
  };
}, [imageLoaded]);

const progressPercent = Math.min(100, Math.max(0, (elapsedMs / EXPOSURE_DURATION_MS) * 100));
...
{/* Exposure Progress Indicator Bar */}
<div className="w-full bg-slate-100 p-4 border-t border-slate-200">
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
```
Observations:
1. `setElapsedMs(elapsed)` is invoked inside `requestAnimationFrame` on every tick (~16.6ms at 60Hz), forcing a re-render of the entire component tree 60 times per second.
2. The progress element defines `transition-[width] duration-75 ease-linear`. Every 16.6ms, the browser style engine interrupts the ongoing 75ms transition and starts a new one, causing GPU thread jank and stutter.
3. At completion (`elapsed >= EXPOSURE_DURATION_MS`), both `onExposureComplete` and `onComplete` are triggered concurrently, dispatching `FINISH_READING` twice in the same frame.
4. There is no countdown label, icon, or remaining seconds readout inside the progress container. Lines 160-161 are empty whitespace.

### 1.2 Test Execution Findings

Executing `npx tsx tests/adversarial_m2_timing_ui.test.ts` produces:
```
Warning: React.createElement: type is invalid -- expected a string (for built-in components) or a class/function (for composite components) but got: object.
    at StimulusReadingScreen (web-experimento\src\components\StimulusReadingScreen.tsx:21:3)
✖ ADV-M2.1: Reading screen contains no skip button or advance mechanism (11.2674ms)
  Error: Element type is invalid: expected a string (for built-in components) or a class/function (for composite components) but got: object.
      at renderElement (...react-dom-server-legacy.node.development.js:6058:9)
```
- **Cause**: In Node.js / `tsx` ESM execution, `import Image from 'next/image'` resolves to `{ default: [Function: Image] }` rather than a callable React component, breaking `renderToStaticMarkup`.

Executing `npm run build` exits with code 0 (Next.js build succeeds with static generation for `/`, `/_not-found`, and `/admin`).

---

## 2. Logic Chain

```
[Observation 1.1.B: preloadStimuliBatch caches images + cee8c8c removed img.complete check + h-0 overflow-hidden container]
  │
  ├─► Browsers (WebKit/Safari and Chromium) do not fire synthetic load events for cached or zero-height elements
  │
  └─► handleImageLoad never fires ──► imageLoaded remains false ──► useEffect timer never starts ──► Progress bar freezes at 0%

[Observation 1.1.C: 60fps setElapsedMs() React state updates + transition-[width] duration-75 ease-linear]
  │
  ├─► Every ~16.6ms frame cancels previous 75ms transition
  │
  └─► Browser compositor thread throttles/clamps width animation ──► Perceived visual freezing/stuttering

[Observation 1.1.A: ORIGINAL_REQUEST update 2026-09-21 specifies 15s + InductionScreen text is 15s]
  │
  ├─► StimulusReadingScreen has EXPOSURE_DURATION_MS = 15000, but lacks src/lib/timing.ts module
  │
  └─► Tests and types contain conflicting 10000ms values due to lack of single source of truth

[Observation 1.1.B & 1.2: Image from next/image used instead of standard <img>]
  │
  ├─► Breached renderToStaticMarkup compatibility in tsx/Node runner
  │
  └─► Next.js fill layout forces absolute positioning, causing clipping and layout instability

[Observation 1.1.C: 380px fixed height + py-6 + Header + no sticky viewport bar]
  │
  ├─► Total vertical height is ~580px - 640px
  │
  └─► On laptop screens (1366x768) and mobile devices, bottom 2.5px bar is pushed below the fold (hidden/clipped)
```

---

## 3. Caveats

1. **Read-Only Scope**: In compliance with the Teamwork Explorer archetype, no source files were directly modified during this turn.
2. **ESLint Rule Compliance**: Replacing Next.js `<Image>` with HTML `<img>` triggers `@next/next/no-img-element`. However, `/* eslint-disable @next/next/no-img-element */` is already declared on line 2 of `StimulusReadingScreen.tsx` and is standard practice across the project's other screens (`RatingScreen.tsx`).
3. **E2E Test Integration (R2)**: The Worker must verify that Playwright/Cypress E2E tests target the updated 15-second exposure window and can locate the progress bar via standard accessibility roles (`role="progressbar"`, `aria-valuenow`).

---

## 4. Conclusion & Actionable Proposal

To satisfy Requirement R1 and all acceptance criteria, the Worker should execute the following concrete modifications:

### Step 1: Create Centralized Timing Configuration (`src/lib/timing.ts`)

Create `src/lib/timing.ts` to establish the single authoritative source of truth:

```ts
/**
 * Centralized Experiment Timing Configuration
 * Target: src/lib/timing.ts
 */

// Stimulus Reading Window
export const STIMULUS_EXPOSURE_DURATION_SECONDS = 15;
export const STIMULUS_EXPOSURE_DURATION_MS = STIMULUS_EXPOSURE_DURATION_SECONDS * 1000; // 15,000 ms

// Admin and Network Timeouts
export const SESSION_REGISTRATION_TIMEOUT_MS = 2500;
export const FINAL_SYNC_GATEWAY_TIMEOUT_MS = 5000;
```

---

### Step 2: Refactor `StimulusReadingScreen.tsx`

Replace the implementation of `src/components/StimulusReadingScreen.tsx` with the following production-grade version:

```tsx
'use client';
/* eslint-disable @next/next/no-img-element */

import React, { useState, useEffect, useRef, useCallback } from 'react';
import type { StimulusItem } from '@/types/experiment';
import { getStimulusImagePath, getStimulusAlternativePath } from '@/lib/assets';
import { STIMULUS_EXPOSURE_DURATION_MS, STIMULUS_EXPOSURE_DURATION_SECONDS } from '@/lib/timing';
import { Clock, Eye, AlertTriangle } from 'lucide-react';

export interface StimulusReadingScreenProps {
  stimulus: StimulusItem;
  trialNumber: number;        // Current trial index (1 to 20)
  totalTrials?: number;       // Default: 20
  onComplete?: (readingTimeMs: number) => void;
  onExposureComplete?: (readingTimeMs: number) => void;
}

export const StimulusReadingScreen: React.FC<StimulusReadingScreenProps> = ({
  stimulus,
  trialNumber,
  totalTrials = 20,
  onComplete,
  onExposureComplete,
}) => {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [imageSrc, setImageSrc] = useState<string>(() => getStimulusImagePath(stimulus.id));
  const [hasError, setHasError] = useState(false);
  const [elapsedMs, setElapsedMs] = useState(0);

  const imgRef = useRef<HTMLImageElement | null>(null);
  const completedRef = useRef(false);
  const rafRef = useRef<number | null>(null);

  // Single-dispatch completion handler
  const handleFinish = useCallback(() => {
    if (completedRef.current) return;
    completedRef.current = true;

    if (rafRef.current) {
      cancelAnimationFrame(rafRef.current);
    }
    setElapsedMs(STIMULUS_EXPOSURE_DURATION_MS);

    const notify = onExposureComplete || onComplete;
    if (notify) {
      notify(STIMULUS_EXPOSURE_DURATION_MS);
    }
  }, [onComplete, onExposureComplete]);

  // Latch timer start strictly when image is confirmed loaded
  const handleImageLoad = useCallback(() => {
    if (imageLoaded || completedRef.current) return;
    setImageLoaded(true);
  }, [imageLoaded]);

  // Handle asset load failure with fallback to alternative extension
  const handleImageError = useCallback(() => {
    const altPath = getStimulusAlternativePath(stimulus.id);
    if (imageSrc !== altPath) {
      setImageSrc(altPath);
    } else {
      setHasError(true);
      // If image fails completely, permit participant to read text card without deadlock
      if (!imageLoaded) {
        setImageLoaded(true);
      }
    }
  }, [imageSrc, stimulus.id, imageLoaded]);

  // Immediate Cache Detection on Mount: Handle preloaded/cached images instantly
  useEffect(() => {
    const img = imgRef.current;
    if (img && img.complete && img.naturalWidth > 0 && !imageLoaded) {
      handleImageLoad();
    }
  }, [handleImageLoad, imageLoaded]);

  // High-precision Monotonic Animation Frame Timer Loop
  useEffect(() => {
    if (!imageLoaded || completedRef.current) return;

    let isUnmounted = false;
    const start = performance.now();

    const tick = () => {
      if (isUnmounted || completedRef.current) return;
      const elapsed = performance.now() - start;

      if (elapsed >= STIMULUS_EXPOSURE_DURATION_MS) {
        handleFinish();
      } else {
        setElapsedMs(elapsed);
        rafRef.current = requestAnimationFrame(tick);
      }
    };

    rafRef.current = requestAnimationFrame(tick);

    return () => {
      isUnmounted = true;
      if (rafRef.current) {
        cancelAnimationFrame(rafRef.current);
      }
    };
  }, [imageLoaded, handleFinish]);

  // Derived progress metrics
  const progressPercent = Math.min(100, Math.max(0, (elapsedMs / STIMULUS_EXPOSURE_DURATION_MS) * 100));
  const remainingSeconds = Math.max(0, Math.ceil((STIMULUS_EXPOSURE_DURATION_MS - elapsedMs) / 1000));

  return (
    <div className="w-full max-w-4xl mx-auto flex flex-col items-center px-4 py-4 sm:py-6 pb-20 sm:pb-6 select-none">
      {/* Top Header: Trial indicator & Status */}
      <div className="w-full flex items-center justify-between mb-3 sm:mb-4 pb-2 sm:pb-3 border-b border-slate-200">
        <div className="flex items-center space-x-2">
          <span className="text-xs uppercase tracking-wider font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
            Fase de Lectura
          </span>
          <span className="text-sm font-medium text-slate-700">
            Noticia <strong className="text-slate-900">{trialNumber}</strong> de {totalTrials}
          </span>
        </div>

        {/* Loading Badge or Live Countdown */}
        {!imageLoaded ? (
          <div className="flex items-center space-x-2 text-indigo-700 bg-indigo-50 border border-indigo-100 px-3 py-1 rounded-full">
            <Clock className="w-4 h-4 animate-spin-slow" />
            <span className="text-xs font-semibold">
              Cargando titular...
            </span>
          </div>
        ) : (
          <div className="flex items-center space-x-1.5 text-xs font-semibold text-indigo-700 bg-indigo-50 border border-indigo-100 px-2.5 py-1 rounded-full">
            <Clock className="w-3.5 h-3.5" />
            <span>{remainingSeconds}s restantes</span>
          </div>
        )}
      </div>

      {/* Stimulus Banner Card */}
      <div className="w-full bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden flex flex-col items-center relative">
        {/* Visual Frame: Responsive height (260px on mobile, 320px on tablet, 380px on desktop) */}
        <div className="relative w-full h-[260px] sm:h-[320px] md:h-[380px] bg-slate-50 flex items-center justify-center overflow-hidden">
          {/* Skeleton placeholder shown while loading and no error */}
          {!imageLoaded && !hasError && (
            <div className="absolute inset-0 z-10 bg-slate-100 flex flex-col items-center justify-center animate-pulse p-6 text-center">
              <Eye className="w-8 h-8 text-slate-400 mb-2 animate-bounce" />
              <p className="text-sm font-medium text-slate-500">Cargando estímulo visual...</p>
              <p className="text-xs text-slate-400 mt-1">El tiempo de lectura comenzará una vez visible</p>
            </div>
          )}

          {/* Stimulus Image: Preserves aspect ratio, never zero height, decoded directly */}
          <img
            ref={imgRef}
            src={imageSrc}
            alt={stimulus.title}
            onLoad={handleImageLoad}
            onError={handleImageError}
            className={`max-h-full max-w-full object-contain transition-opacity duration-300 ${
              imageLoaded ? 'opacity-100' : 'opacity-0'
            }`}
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

        {/* In-Card Exposure Progress Indicator Bar */}
        <div className="w-full bg-slate-50 p-4 sm:p-5 border-t border-slate-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold text-slate-600 uppercase tracking-wider">
              Tiempo de lectura obligatoria ({STIMULUS_EXPOSURE_DURATION_SECONDS} segundos)
            </span>
            <span className="text-xs font-mono font-bold text-indigo-600">
              {remainingSeconds}s
            </span>
          </div>

          {/* Progress track */}
          <div className="w-full h-3 bg-slate-200 rounded-full overflow-hidden p-0.5">
            <div
              className="h-full bg-indigo-600 rounded-full"
              style={{ width: `${progressPercent}%` }}
              role="progressbar"
              aria-valuenow={Math.round(progressPercent)}
              aria-valuemin={0}
              aria-valuemax={100}
            />
          </div>
        </div>
      </div>

      {/* Fixed Bottom Screen Bar for Mobile/Narrow Viewports: Guarantees visibility without scroll */}
      <div
        className="fixed bottom-0 inset-x-0 z-40 bg-white/95 backdrop-blur border-t border-slate-200 shadow-lg px-4 py-2.5 sm:hidden"
        role="region"
        aria-label="Temporizador de lectura inferior"
      >
        <div className="max-w-4xl mx-auto flex items-center justify-between gap-3">
          <div className="flex items-center space-x-1.5 text-xs font-semibold text-slate-700 flex-shrink-0">
            <Clock className="w-3.5 h-3.5 text-indigo-600" />
            <span>Lectura: {remainingSeconds}s</span>
          </div>
          <div className="flex-1 h-2.5 bg-slate-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-indigo-600 rounded-full"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default StimulusReadingScreen;
```

---

## 5. Verification Method

### 5.1 Unit and Adversarial Regression Verification
Run the adversarial UI and timing test suite:
```powershell
npx tsx tests/adversarial_m2_timing_ui.test.ts
```
**Expected Result**:
All 10 tests pass, including `ADV-M2.1: Reading screen contains no skip button or advance mechanism`. Zero `React.createElement: type is invalid` errors.

### 5.2 Test Tier Integrity Verification
Run the multi-tier automated test harness:
```powershell
npm test
```
**Expected Result**:
143 test invariants across Tiers 1–4 pass with exit code 0.

### 5.3 Production Build Verification
Verify type checking and production bundling:
```powershell
npm run build
```
**Expected Result**:
Exit code 0, clean build with all routes compiled.

### 5.4 Manual / Browser Inspection Criteria
1. Navigate to trial 1.
2. Confirm the stimulus image displays clearly without letterbox distortion.
3. Verify the progress bar at the bottom begins growing immediately when the image loads, advancing monotonically from 0% to 100% over exactly 15.0 seconds.
4. Verify the live badge updates from `15s restantes` down to `0s restantes`.
5. On mobile viewports (e.g. 375x667), confirm the fixed bottom bar remains visible and does not overlap card text or image elements.
6. Confirm automatic transition to the rating screen triggers immediately upon reaching 15,000 ms.
