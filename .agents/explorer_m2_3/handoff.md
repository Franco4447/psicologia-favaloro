# Handoff Report: Global Experiment State Machine, Trial Runner, Telemetry & Session Recovery

**Agent**: explorer_m2_3  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_3`  
**Target File**: `src/app/page.tsx`, `src/lib/telemetry.ts`, `src/lib/sessionRecovery.ts`  
**Milestone**: M2 (Participant Flow & Cognitive UI Engine)  
**Date**: 2026-09-20T23:55:00Z  

---

## 1. Observation

Direct observations from the codebase, test suites, and specification documents:

1. **Original Experimental Specification (`ORIGINAL_REQUEST.md`)**:
   - §5 outlines the 8 sequential stages of the experimental flow:
     - `welcome` (§5.1): Presentation of Universidad Favaloro, research aims, quiet-environment instructions.
     - `consent` (§5.2): Informed consent notice with mandatory acceptance checkbox.
     - `demographics` (§5.3): Age (>=18), sex (Femenino, Masculino, Otro), studies psychology (Sí/No), therapeutic orientation (Psicoanálisis, Basada en Evidencia Científica, Otros), university (text).
     - `inclusion screening` (§5.4): Psychology student + (Psicoanálisis or Basada en Evidencia) -> included; otherwise routed to Control prompt + random cohesive fake news set and marked excluded.
     - `induction` (§5.5): Verbatim instructions for Racional, Emocional, or Control induction.
     - `trial loop` (§5.6): 20 items (12 true news + 8 congruent fake news). For each news item: 10.0s forced reading exposure with progress indicator, followed by 4-point response scale (Murphy/León: 1=Falso Recuerdo, 2=Falsa Creencia, 3=Lo recuerdo diferente, 4=No lo recuerdo en absoluto) tracking reaction time in milliseconds.
     - `debriefing` (§5.7): Ethical disclosure of the 8 fake news and psychological purpose.
     - `thankyou` (§5.8): Final confirmation screen with anonymous participant ID.
   - §R3 specifies telemetry capture: device type (`desktop`/`mobile`/`tablet`), screen resolution, user agent.

2. **Interface Contracts & Types (`src/types/experiment.ts`)**:
   - `InductionGroup` defined as `'racional' | 'emocional' | 'control'` (lines 19-20).
   - `TherapeuticOrientation` defined as `'Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros'` (lines 25-28).
   - `FakeNewsSet` defined as `'psicoanalisis' | 'evidencia' | 'control_random'` (lines 41-42).
   - `ResponseCode` defined as `1 | 2 | 3 | 4` (line 104).
   - `ParticipantSession` (lines 138-155) and `TrialRecord` (lines 176-191) define the canonical schema for participants and responses.
   - `DeviceType` defined as `'desktop' | 'mobile' | 'tablet'` (line 60).

3. **Authoritative Stimuli & Logic Functions (`src/data/stimuli.ts`)**:
   - `evaluateInclusion(demographics)` (lines 458-498): Evaluates inclusion and returns `{ isIncluded: boolean, exclusionReason: ExclusionReason }`.
   - `getParticipantNewsDeck(therapeuticOrientation, isIncluded, randomSeed?)` (lines 560-602): Combines 12 true news + 8 congruent fake news and shuffles them with Fisher-Yates, returning exactly 20 `StimulusItem` objects.
   - `classifyResponse(isFake, responseOption)` (lines 614-627): Derives `isFalseMemory`, `isFalseBelief`, and `isTrueMemory`.
   - `getStimulusImagePath(newsIdOrItem)` (lines 637-652): Resolves public image URL, accurately handling `Noticia_26.png`.

4. **Existing E2E Test Suite (`tests/e2e/tier1_features.test.ts`)**:
   - Feature 1 to 16 assertions define exact behavior:
     - F4: Screening logic (lines 188-243).
     - F6: Excluded routing to Control and `control_random` without quota distortion (lines 303-359).
     - F7: Ideological congruence (PSA receives `[14, 16, 18, 20, 21, 23, 25, 27]`; EBP receives `[13, 15, 17, 19, 22, 24, 26, 28]`) (lines 364-398).
     - F9: Exactly 20 stimuli (12 true + 8 fake), ordered 1 to 20 without gaps or duplicates (lines 443-492).
     - F10: 10,000 ms stimulus reading exposure (lines 497-535).
     - F12: 4-point response scale mapping (lines 575-607).
     - F13: Millisecond reaction time latency tracking (lines 612-657).
     - F15: Session completion with 20 trials (lines 694-753).
     - F16: Telemetry capture (`deviceType`, `screenResolution`, `userAgent`) (lines 758-833).

5. **Current Page Implementation (`src/app/page.tsx`)**:
   - Currently a static Milestone 1 status showcase page showing stimuli counts and asset verification (94 lines).
   - Needs to be transformed into the client-side master orchestrator and state machine for Milestone 2.

6. **Peer Agent Allocations**:
   - `explorer_m2_1`: Designing `WelcomeScreen.tsx`, `ConsentScreen.tsx`, `DemographicsScreen.tsx`, `InductionScreen.tsx`, `DebriefingScreen.tsx`, and `ThankYouScreen.tsx`.
   - `explorer_m2_2`: Designing `StimulusReadingScreen.tsx` (10s forced exposure, progress bar, onLoad latch) and `RatingScreen.tsx` (4-point scale, `performance.now()` reaction time).
   - `explorer_m2_3` (Current Agent): Designing global state machine, trial runner, telemetry capture, and `sessionStorage` recovery in `src/app/page.tsx`.

---

## 2. Logic Chain

1. **State Machine Architecture Selection**:
   - The experiment flow is strictly sequential and non-branching with an inner 20-iteration loop:
     `welcome` -> `consent` -> `demographics` -> `induction` -> [loop: `reading` -> `rating` x20] -> `debriefing` -> `thankyou`.
   - Using scattered multiple `useState` hooks risks inconsistent state (e.g. `currentTrial` changing without stage changing, race conditions, or illegal stage skips).
   - A deterministic Finite State Machine (FSM) implemented via React's `useReducer` guarantees:
     - Atomicity of state transitions (e.g., advancing `currentTrialIndex` and toggling `stage: 'reading'` happen together).
     - Explicit transition validation (rejecting illegal actions like skipping reading or submitting demographics without consent).
     - Pure reducer functions that are easily unit-testable in isolation without rendering React components.

2. **Session Persistence & Recovery Strategy**:
   - Human participants may accidentally trigger a browser page refresh (F5 / Cmd+R) or navigation gesture.
   - If state lives only in React memory, a refresh destroys the session, frustrates participants, and biases research data (survival bias / attrition).
   - Solution: Synchronize the core state to `sessionStorage` (`favaloro_exp_session_v1`) after every meaningful stage transition and completed trial response.
   - `sessionStorage` is tab-scoped:
     - Closing the tab cleans the session, allowing a new participant to take the study on a shared terminal.
     - Refreshing within the tab restores the exact trial index and accumulated responses.
   - Hydration Safety: Next.js App Router renders initial markup on the server where `window.sessionStorage` does not exist. Directly reading storage in initial state causes hydration mismatch errors (`Text content did not match`).
   - Therefore, the client state machine must start in a neutral loading/initial state, run a hydration `useEffect` on mount to safely inspect `sessionStorage`, and dispatch `RESTORE_SESSION` if an active session is found.

3. **Trial Exposure & Latency Tracking**:
   - For each of the 20 trials:
     - In `reading`: Stimulus image is presented for 10.0s (10,000 ms). Progress bar advances from 0% to 100%. User cannot advance early. When 10s completes, `onExposureComplete(readingTimeMs)` triggers transition to `rating` with `readingTimeMs = 10000`.
     - In `rating`: Headline image remains visible at top for memory anchoring. 4-point response scale is rendered. `performance.now()` measures latency from screen mount to submit click.
     - On submit: `RECORD_TRIAL_RESPONSE` calculates classification flags (`isFalseMemory`, `isFalseBelief`, `isTrueMemory`), stores `TrialRecord`, and evaluates:
       - If `currentTrialIndex + 1 < 20`: `currentTrialIndex` increments by 1, stage transitions back to `reading`.
       - If `currentTrialIndex + 1 === 20`: All 20 trials complete, stage transitions to `debriefing`.

4. **Telemetry Detection**:
   - Captured silently during demographics submission:
     - `deviceType`: Detected via user agent regex and screen/viewport touch heuristics (`'desktop' | 'mobile' | 'tablet'`).
     - `screenResolution`: `${window.screen.width}x${window.screen.height}` (e.g. `'1920x1080'`).
     - `userAgent`: `navigator.userAgent`.
   - Stored in `state.telemetry` and attached to `ParticipantSession` for research quality control (distinguishing mobile vs desktop latency profiles).

5. **M3 Integration Decoupling**:
   - In M2, the state machine operates completely client-side in memory and `sessionStorage`, allowing full interactive testing and UI verification without requiring a live Supabase connection.
   - When demographics are submitted, balanced group allocation defaults to a local balanced fallback in M2.
   - In M3, this hook will asynchronously call `POST /api/session` to obtain the RPC-balanced `induction_group` from Supabase.
   - When debriefing finishes, the state machine accumulates all 20 `TrialRecord`s in `state.responses`. In M3, `syncSessionToSupabase` will POST this entire batch to `/api/responses`.
   - The data structures are 100% compliant with M3 database DDL (`supabase/schema.sql`).

---

## 3. Caveats

1. **Browser Private / Incognito Mode Restrictions**:
   - In rare high-security browser configurations or older iOS Safari private browsing modes, accessing `sessionStorage` can throw `SecurityError` or `QuotaExceededError`.
   - Mitigation: All storage operations must be wrapped in safe `try/catch` wrappers. If `sessionStorage` is blocked, the experiment still functions smoothly in memory without crashing.

2. **Interrupted Trial Exposure on Refresh**:
   - If a participant refreshes while in the middle of a 10s `reading` screen (e.g. at second 4):
     - Decision: When the session is restored, the 10-second timer for that specific news stimulus restarts from 0.0s. This ensures experimental validity (cognitive exposure proxy requires 10 seconds of processing time before rating).

3. **Image Asset Preloading**:
   - While the 10-second exposure gives adequate time for the next image to load, low-bandwidth connections might lag.
   - Mitigation: When `deck` is generated in `SUBMIT_DEMOGRAPHICS`, trigger background preloading of all 20 images using `preloadStimuliBatch` from `src/lib/assets.ts`.

---

## 4. Conclusion & Detailed Design Blueprints

### A. State Machine Definition (`src/app/page.tsx`)

#### 1. Stage Enum & Types
```typescript
export type ExperimentStage = 
  | 'welcome' 
  | 'consent' 
  | 'demographics' 
  | 'induction' 
  | 'reading' 
  | 'rating' 
  | 'debriefing' 
  | 'thankyou';

export interface ExperimentState {
  isHydrated: boolean;
  stage: ExperimentStage;
  participantId: string;
  createdAt: string;
  completedAt?: string | null;
  demographics: ParticipantDemographicsInput | null;
  isIncluded: boolean;
  exclusionReason: ExclusionReason;
  inductionGroup: InductionGroup | null;
  fakeNewsSet: FakeNewsSet | null;
  deck: StimulusItem[];
  currentTrialIndex: number; // 0 to 19 (maps to presentationOrder 1 to 20)
  currentReadingTimeMs: number;
  responses: TrialRecord[];
  telemetry: ClientTelemetry;
  isSaving: boolean;
  error: string | null;
}
```

#### 2. Action Types
```typescript
export type ExperimentAction =
  | { type: 'HYDRATE_STORAGE'; payload: Partial<ExperimentState> }
  | { type: 'START_CONSENT' }
  | { type: 'ACCEPT_CONSENT' }
  | { 
      type: 'SUBMIT_DEMOGRAPHICS'; 
      payload: { 
        demographics: ParticipantDemographicsInput; 
        telemetry: ClientTelemetry;
        assignedGroup?: InductionGroup; 
      } 
    }
  | { type: 'ACKNOWLEDGE_INDUCTION' }
  | { type: 'FINISH_READING'; payload: { readingTimeMs: number } }
  | { 
      type: 'RECORD_TRIAL_RESPONSE'; 
      payload: { 
        responseOption: ResponseCode; 
        responseTimeMs: number; 
      } 
    }
  | { type: 'COMPLETE_DEBRIEFING' }
  | { type: 'RESET_EXPERIMENT' };
```

#### 3. State Transition Matrix

| Current Stage | Dispatched Action | Next Stage | State Modifications | Guard / Condition |
| :--- | :--- | :--- | :--- | :--- |
| `welcome` | `START_CONSENT` | `consent` | none | None |
| `consent` | `ACCEPT_CONSENT` | `demographics` | none | Consent checkbox checked |
| `demographics` | `SUBMIT_DEMOGRAPHICS` | `induction` | `demographics`, `isIncluded`, `exclusionReason`, `inductionGroup`, `fakeNewsSet`, `deck` (20 items), `telemetry`, `participantId`, `currentTrialIndex: 0` | Valid demographics input |
| `induction` | `ACKNOWLEDGE_INDUCTION` | `reading` | none | Starts trial 1 |
| `reading` | `FINISH_READING` | `rating` | `currentReadingTimeMs = payload.readingTimeMs` | readingTimeMs >= 10000 |
| `rating` | `RECORD_TRIAL_RESPONSE` | `reading` | Appends `TrialRecord` to `responses`, `currentTrialIndex++` | `currentTrialIndex + 1 < 20` |
| `rating` | `RECORD_TRIAL_RESPONSE` | `debriefing` | Appends 20th `TrialRecord` to `responses` | `currentTrialIndex + 1 === 20` |
| `debriefing` | `COMPLETE_DEBRIEFING` | `thankyou` | `completedAt = ISOString`, triggers sync | All 20 trials present |
| `any` | `RESET_EXPERIMENT` | `welcome` | Clears storage, resets to initial state | User explicitly restarts |
| `any` (mount) | `HYDRATE_STORAGE` | `restored.stage` | Restores all session data | Valid payload in `sessionStorage` |

#### 4. Master Reducer Implementation
```typescript
export function experimentReducer(state: ExperimentState, action: ExperimentAction): ExperimentState {
  switch (action.type) {
    case 'HYDRATE_STORAGE': {
      return {
        ...state,
        ...action.payload,
        isHydrated: true,
      };
    }

    case 'START_CONSENT': {
      if (state.stage !== 'welcome') return state;
      return { ...state, stage: 'consent' };
    }

    case 'ACCEPT_CONSENT': {
      if (state.stage !== 'consent') return state;
      return { ...state, stage: 'demographics' };
    }

    case 'SUBMIT_DEMOGRAPHICS': {
      if (state.stage !== 'demographics') return state;
      const { demographics, telemetry, assignedGroup } = action.payload;

      // 1. Evaluate inclusion criteria
      const evaluation = evaluateInclusion(demographics);
      const isIncluded = evaluation.isIncluded;
      const exclusionReason = evaluation.exclusionReason;

      // 2. Assign Induction Group
      // If excluded: strictly 'control'
      // If included: use assignedGroup (from API in M3, or local balanced generator in M2)
      const inductionGroup: InductionGroup = !isIncluded 
        ? 'control' 
        : (assignedGroup || getFallbackLocalGroup());

      // 3. Determine Fake News Set
      let fakeNewsSet: FakeNewsSet;
      if (!isIncluded) {
        fakeNewsSet = 'control_random';
      } else if (demographics.therapeuticOrientation === 'Psicoanálisis') {
        fakeNewsSet = 'psicoanalisis';
      } else {
        fakeNewsSet = 'evidencia';
      }

      // 4. Assemble the 20-item randomized deck
      const deck = getParticipantNewsDeck(demographics.therapeuticOrientation, isIncluded);

      // 5. Generate unique participant UUID
      const participantId = state.participantId || (typeof crypto !== 'undefined' && crypto.randomUUID ? crypto.randomUUID() : `p_${Date.now()}`);

      return {
        ...state,
        stage: 'induction',
        participantId,
        demographics,
        isIncluded,
        exclusionReason,
        inductionGroup,
        fakeNewsSet,
        deck,
        currentTrialIndex: 0,
        currentReadingTimeMs: 10000,
        responses: [],
        telemetry,
      };
    }

    case 'ACKNOWLEDGE_INDUCTION': {
      if (state.stage !== 'induction') return state;
      return {
        ...state,
        stage: 'reading',
        currentTrialIndex: 0,
      };
    }

    case 'FINISH_READING': {
      if (state.stage !== 'reading') return state;
      return {
        ...state,
        stage: 'rating',
        currentReadingTimeMs: action.payload.readingTimeMs,
      };
    }

    case 'RECORD_TRIAL_RESPONSE': {
      if (state.stage !== 'rating') return state;
      const currentStimulus = state.deck[state.currentTrialIndex];
      if (!currentStimulus) return state;

      const { responseOption, responseTimeMs } = action.payload;
      const flags = classifyResponse(currentStimulus.isFake, responseOption);

      const trialRecord: TrialRecord = {
        id: typeof crypto !== 'undefined' && crypto.randomUUID ? crypto.randomUUID() : undefined,
        participantId: state.participantId,
        presentationOrder: state.currentTrialIndex + 1,
        newsId: currentStimulus.id,
        isFake: currentStimulus.isFake,
        newsCongruence: currentStimulus.congruence,
        responseOption,
        responseLabel: RESPONSE_OPTIONS_MAP[responseOption]?.label ?? '',
        readingTimeMs: state.currentReadingTimeMs,
        responseTimeMs,
        isFalseMemory: flags.isFalseMemory,
        isFalseBelief: flags.isFalseBelief,
        isTrueMemory: flags.isTrueMemory,
        createdAt: new Date().toISOString(),
      };

      const updatedResponses = [...state.responses, trialRecord];
      const nextIndex = state.currentTrialIndex + 1;
      const isComplete = nextIndex >= state.deck.length;

      return {
        ...state,
        responses: updatedResponses,
        currentTrialIndex: isComplete ? state.currentTrialIndex : nextIndex,
        stage: isComplete ? 'debriefing' : 'reading',
        currentReadingTimeMs: 10000,
      };
    }

    case 'COMPLETE_DEBRIEFING': {
      if (state.stage !== 'debriefing') return state;
      return {
        ...state,
        stage: 'thankyou',
        completedAt: new Date().toISOString(),
      };
    }

    case 'RESET_EXPERIMENT': {
      return {
        ...getInitialExperimentState(),
        isHydrated: true,
      };
    }

    default:
      return state;
  }
}
```

---

### B. Client Telemetry Detection Module (`src/lib/telemetry.ts`)

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Telemetry Capture Utility
 * Target: src/lib/telemetry.ts
 */

import { DeviceType } from '@/types/experiment';

export interface ClientTelemetry {
  deviceType: DeviceType;
  screenResolution: string;
  userAgent: string;
}

export function captureClientTelemetry(): ClientTelemetry {
  if (typeof window === 'undefined') {
    return {
      deviceType: 'desktop',
      screenResolution: '1920x1080',
      userAgent: 'Server-Side Rendering',
    };
  }

  const ua = navigator.userAgent || '';
  const screenWidth = window.screen?.width || window.innerWidth || 1920;
  const screenHeight = window.screen?.height || window.innerHeight || 1080;
  const screenResolution = `${screenWidth}x${screenHeight}`;

  // Multi-attribute device classification
  const isTabletRegex = /iPad|tablet|(android(?!.*mobile))|(windows(?!.*phone)(.*touch))|kindle|playbook|silk/i;
  const isMobileRegex = /Mobile|Android|iP(hone|od)|IEMobile|BlackBerry|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/i;

  let deviceType: DeviceType = 'desktop';

  if (isTabletRegex.test(ua)) {
    deviceType = 'tablet';
  } else if (isMobileRegex.test(ua)) {
    deviceType = 'mobile';
  } else {
    // Secondary heuristic: touchscreen and viewport aspect ratio
    const hasTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
    const minDimension = Math.min(window.innerWidth, window.innerHeight);

    if (hasTouch && minDimension < 640) {
      deviceType = 'mobile';
    } else if (hasTouch && minDimension >= 640 && minDimension <= 1024) {
      deviceType = 'tablet';
    } else {
      deviceType = 'desktop';
    }
  }

  return {
    deviceType,
    screenResolution,
    userAgent: ua,
  };
}
```

---

### C. Session Storage & Resiliency Module (`src/lib/sessionRecovery.ts`)

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Session Storage & F5 Recovery Manager
 * Target: src/lib/sessionRecovery.ts
 */

import { ExperimentState } from '@/app/page';

export const SESSION_STORAGE_KEY = 'favaloro_exp_session_v1';
export const STORAGE_VERSION = 1;

export interface StoredSessionPayload {
  version: number;
  stage: ExperimentState['stage'];
  participantId: string;
  createdAt: string;
  completedAt?: string | null;
  demographics: ExperimentState['demographics'];
  isIncluded: boolean;
  exclusionReason: ExperimentState['exclusionReason'];
  inductionGroup: ExperimentState['inductionGroup'];
  fakeNewsSet: ExperimentState['fakeNewsSet'];
  deck: ExperimentState['deck'];
  currentTrialIndex: number;
  currentReadingTimeMs: number;
  responses: ExperimentState['responses'];
  telemetry: ExperimentState['telemetry'];
  savedAt: string;
}

/**
 * Safely persists current experiment state to sessionStorage.
 */
export function saveSessionToStorage(state: ExperimentState): boolean {
  if (typeof window === 'undefined') return false;
  // Do not store initial unconfigured states
  if (state.stage === 'welcome' || state.stage === 'consent') return false;

  try {
    const payload: StoredSessionPayload = {
      version: STORAGE_VERSION,
      stage: state.stage,
      participantId: state.participantId,
      createdAt: state.createdAt,
      completedAt: state.completedAt,
      demographics: state.demographics,
      isIncluded: state.isIncluded,
      exclusionReason: state.exclusionReason,
      inductionGroup: state.inductionGroup,
      fakeNewsSet: state.fakeNewsSet,
      deck: state.deck,
      currentTrialIndex: state.currentTrialIndex,
      currentReadingTimeMs: state.currentReadingTimeMs,
      responses: state.responses,
      telemetry: state.telemetry,
      savedAt: new Date().toISOString(),
    };

    sessionStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify(payload));
    return true;
  } catch (error) {
    console.warn('[SessionRecovery] Failed to save session to sessionStorage:', error);
    return false;
  }
}

/**
 * Safely retrieves and validates stored experiment state.
 */
export function loadSessionFromStorage(): StoredSessionPayload | null {
  if (typeof window === 'undefined') return null;

  try {
    const serialized = sessionStorage.getItem(SESSION_STORAGE_KEY);
    if (!serialized) return null;

    const parsed = JSON.parse(serialized) as StoredSessionPayload;

    // Integrity validations
    if (parsed.version !== STORAGE_VERSION) return null;
    if (!parsed.participantId || !parsed.deck || !Array.isArray(parsed.deck)) return null;
    if (parsed.deck.length !== 20) return null;
    if (typeof parsed.currentTrialIndex !== 'number' || parsed.currentTrialIndex < 0 || parsed.currentTrialIndex > 20) return null;
    if (!Array.isArray(parsed.responses)) return null;

    return parsed;
  } catch (error) {
    console.warn('[SessionRecovery] Failed to parse stored session:', error);
    return null;
  }
}

/**
 * Clears stored session upon test reset or experiment restart.
 */
export function clearSessionFromStorage(): void {
  if (typeof window === 'undefined') return;
  try {
    sessionStorage.removeItem(SESSION_STORAGE_KEY);
  } catch (error) {
    console.warn('[SessionRecovery] Failed to clear sessionStorage:', error);
  }
}
```

---

### D. Component Integration Blueprint (`src/app/page.tsx`)

The main page view seamlessly branches according to `state.stage` and passes strongly-typed props to the child components:

```tsx
'use client';

import React, { useReducer, useEffect, useCallback } from 'react';
import { 
  experimentReducer, 
  getInitialExperimentState, 
  ExperimentState 
} from '@/lib/experimentState';
import { 
  saveSessionToStorage, 
  loadSessionFromStorage, 
  clearSessionFromStorage 
} from '@/lib/sessionRecovery';
import { captureClientTelemetry } from '@/lib/telemetry';
import { preloadStimuliBatch } from '@/lib/assets';

import WelcomeScreen from '@/components/WelcomeScreen';
import ConsentScreen from '@/components/ConsentScreen';
import DemographicsScreen from '@/components/DemographicsScreen';
import InductionScreen from '@/components/InductionScreen';
import StimulusReadingScreen from '@/components/StimulusReadingScreen';
import RatingScreen from '@/components/RatingScreen';
import DebriefingScreen from '@/components/DebriefingScreen';
import ThankYouScreen from '@/components/ThankYouScreen';

export default function ExperimentPage() {
  const [state, dispatch] = useReducer(experimentReducer, getInitialExperimentState());

  // 1. SSR Hydration & Session Recovery on Mount
  useEffect(() => {
    const stored = loadSessionFromStorage();
    if (stored) {
      dispatch({
        type: 'HYDRATE_STORAGE',
        payload: {
          stage: stored.stage,
          participantId: stored.participantId,
          createdAt: stored.createdAt,
          completedAt: stored.completedAt,
          demographics: stored.demographics,
          isIncluded: stored.isIncluded,
          exclusionReason: stored.exclusionReason,
          inductionGroup: stored.inductionGroup,
          fakeNewsSet: stored.fakeNewsSet,
          deck: stored.deck,
          currentTrialIndex: stored.currentTrialIndex,
          currentReadingTimeMs: stored.currentReadingTimeMs,
          responses: stored.responses,
          telemetry: stored.telemetry,
        },
      });
    } else {
      dispatch({ type: 'HYDRATE_STORAGE', payload: {} });
    }
  }, []);

  // 2. Continuous Session Persistence on State Transitions
  useEffect(() => {
    if (state.isHydrated && state.stage !== 'welcome' && state.stage !== 'consent') {
      saveSessionToStorage(state);
    }
  }, [state]);

  // 3. Preload Stimulus Assets upon Deck Generation
  useEffect(() => {
    if (state.deck && state.deck.length === 20) {
      const stimulusIds = state.deck.map((s) => s.id);
      preloadStimuliBatch(stimulusIds).catch(console.warn);
    }
  }, [state.deck]);

  // 4. Tab Unload Protection during In-Progress Experiment
  useEffect(() => {
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      const isExperimentInProgress = 
        state.stage !== 'welcome' && 
        state.stage !== 'consent' && 
        state.stage !== 'thankyou';

      if (isExperimentInProgress) {
        e.preventDefault();
        e.returnValue = 'El experimento está en progreso. Si sale ahora, sus respuestas no se completarán.';
        return e.returnValue;
      }
    };

    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [state.stage]);

  // Prevent flash of unstyled content during SSR hydration
  if (!state.isHydrated) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600" />
      </div>
    );
  }

  // 5. Stage Dispatcher
  switch (state.stage) {
    case 'welcome':
      return <WelcomeScreen onStart={() => dispatch({ type: 'START_CONSENT' })} />;

    case 'consent':
      return (
        <ConsentScreen 
          onAccept={() => dispatch({ type: 'ACCEPT_CONSENT' })}
          onBack={() => dispatch({ type: 'RESET_EXPERIMENT' })}
        />
      );

    case 'demographics':
      return (
        <DemographicsScreen
          onSubmit={(demographics) => {
            const telemetry = captureClientTelemetry();
            dispatch({
              type: 'SUBMIT_DEMOGRAPHICS',
              payload: { demographics, telemetry },
            });
          }}
        />
      );

    case 'induction':
      return (
        <InductionScreen
          inductionGroup={state.inductionGroup || 'control'}
          onAcknowledge={() => dispatch({ type: 'ACKNOWLEDGE_INDUCTION' })}
        />
      );

    case 'reading': {
      const currentStimulus = state.deck[state.currentTrialIndex];
      return (
        <StimulusReadingScreen
          key={`reading-${state.currentTrialIndex}-${currentStimulus.id}`}
          stimulus={currentStimulus}
          trialNumber={state.currentTrialIndex + 1}
          totalTrials={state.deck.length}
          onExposureComplete={(readingTimeMs) => {
            dispatch({ type: 'FINISH_READING', payload: { readingTimeMs } });
          }}
        />
      );
    }

    case 'rating': {
      const currentStimulus = state.deck[state.currentTrialIndex];
      return (
        <RatingScreen
          key={`rating-${state.currentTrialIndex}-${currentStimulus.id}`}
          stimulus={currentStimulus}
          trialNumber={state.currentTrialIndex + 1}
          totalTrials={state.deck.length}
          onSubmitRating={(responseOption, responseTimeMs) => {
            dispatch({
              type: 'RECORD_TRIAL_RESPONSE',
              payload: { responseOption, responseTimeMs },
            });
          }}
        />
      );
    }

    case 'debriefing':
      return (
        <DebriefingScreen
          onComplete={() => dispatch({ type: 'COMPLETE_DEBRIEFING' })}
        />
      );

    case 'thankyou':
      return (
        <ThankYouScreen
          participantId={state.participantId}
          onRestart={() => {
            clearSessionFromStorage();
            dispatch({ type: 'RESET_EXPERIMENT' });
          }}
        />
      );

    default:
      return null;
  }
}
```

---

## 5. Verification Method

To independently verify the architecture and prepare for implementation:

1. **Static Type Checking**:
   ```bash
   cd "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento"
   npx tsc --noEmit
   ```
   *Expected*: Zero type errors across `src/app/page.tsx`, `src/types/experiment.ts`, `src/lib/telemetry.ts`, and `src/lib/sessionRecovery.ts`.

2. **Run E2E Feature Oracle Test Suite**:
   ```bash
   npx tsx tests/e2e/run_all_tests.ts
   ```
   *Expected*: All 95 assertions pass across Tiers 1-4.

3. **Session Recovery Verification (F5 Test)**:
   - Launch local dev server: `npm run dev`
   - Complete Consent and Demographics.
   - Observe induction screen, enter trial loop (Trial 1).
   - Advance to Trial 3 `reading` screen. Press F5 (browser reload).
   - *Verification*: Component reloads directly at Trial 3 `reading` screen with accumulated responses for Trials 1 and 2 intact in memory.
   - Advance to Trial 5 `rating` screen. Press F5.
   - *Verification*: Component reloads directly at Trial 5 `rating` screen with the exact same stimulus image visible.

4. **Invalidation Conditions**:
   - If a participant can trigger `RECORD_TRIAL_RESPONSE` without being in the `rating` stage.
   - If `currentTrialIndex` skips from N to N+2 or terminates before 20 trials.
   - If F5 refresh clears `participantId` or `responses` array before completion.
   - If `evaluateInclusion` assigns an included participant to `'control'` or fails to balance groups.
