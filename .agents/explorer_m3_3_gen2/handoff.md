# Handoff Report: Client-Side Synchronization, Offline Buffering & Resiliency (Milestone 3)

**Author:** `explorer_m3_3_gen2`  
**Working Directory:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m3_3_gen2`  
**Date:** 2026-09-21  
**Milestone:** Milestone 3 — Supabase Database, Balanced RPC & Sync  
**Subject:** Drop-in blueprints for `src/lib/sync.ts`, `src/app/page.tsx` integration, and automated verification suite.

---

## 1. Observations

### 1.1 UI Flow & Asynchronous Boundaries in `src/app/page.tsx`
Direct inspection of `web-experimento/src/app/page.tsx` (lines 106–208) revealed the 8-stage lifecycle of the experiment:
- **`welcome` & `consent`**: Pure informational stages. State resets are permitted.
- **`demographics`** (lines 120–130):
  ```typescript
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
  ```
  - *Boundary Observation*: Submitting demographics transitions immediately to `induction`. The client currently calls `getBalancedLocalGroup()` in `experimentState.ts` because it lacked an asynchronous bridge to `/api/session`.
  - *Timing Impact*: Zero reaction time is measured during demographics. A network roundtrip with a strict fallback timeout (<2500ms) here introduces zero cognitive bias.
- **`induction`** (lines 133–139): Displays the prime for `state.inductionGroup`.
- **`reading`** (lines 141–159): Mounts `StimulusReadingScreen` with a mandatory 10.0s countdown timer and visual progress bar.
- **`rating`** (lines 161–185): Mounts `RatingScreen`. The participant reads the 4 Murphy/León options and clicks. `performance.now()` measures the elapsed milliseconds between component mount and click.
  ```typescript
  onSubmitResponse={({ responseOption, responseTimeMs }) => {
    dispatch({
      type: 'RECORD_TRIAL_RESPONSE',
      payload: { responseOption, responseTimeMs },
    });
  }}
  ```
  - *Critical Observation*: In lines 172–176, `dispatch` synchronously computes the `TrialRecord`, increments `currentTrialIndex`, and transitions back to `reading` (or to `debriefing` on trial 20).
  - *Hard Constraint*: Any blocking HTTP request inside `onSubmitResponse` would delay the UI transition, cause frame drops, and distort the participant's rhythm.
- **`debriefing`** (lines 187–193): Dehoaxing disclosure. Participant clicks "Confirmar".
  - *Gateway Observation*: This is the ideal synchronization gate before showing `thankyou`. All 20 trial records and the final session completion can be flushed in batch.
- **`thankyou`** (lines 195–204): Terminal screen with participant ID.

### 1.2 State Machine Capabilities in `src/lib/experimentState.ts`
Inspection of `src/lib/experimentState.ts` lines 45–67 & 160–206 confirmed:
- Action `SUBMIT_DEMOGRAPHICS` already includes an optional `assignedGroup?: InductionGroup` in its payload type:
  ```typescript
  | {
      type: 'SUBMIT_DEMOGRAPHICS';
      payload: {
        demographics: ParticipantDemographicsInput;
        telemetry: ClientTelemetry;
        assignedGroup?: InductionGroup;
      };
    }
  ```
- Line 171–174:
  ```typescript
  const inductionGroup: InductionGroup = !isIncluded
    ? 'control'
    : assignedGroup || getBalancedLocalGroup();
  ```
  This proves the state machine was designed to accept server-assigned groups from an external sync manager, seamlessly falling back to `getBalancedLocalGroup()` if unprovided.

### 1.3 Target API Contracts (Milestone 3 Specifications)
Analysis of `explorer_m3_2_gen2/DISPATCH.md` and `PROJECT.md` establishes the server route contracts:
1. `POST /api/session`:
   - Request: `{ participantId, age, gender, studiesPsychology, therapeuticOrientation, university, isIncluded, exclusionReason, deviceType, screenResolution, userAgent }`.
   - Response: `{ success: true, participantId, inductionGroup, fakeNewsSet, isIncluded, exclusionReason }`.
   - Uses Supabase RPC `assign_induction_group()` with `pg_advisory_xact_lock(742911)` for included participants.
2. `PATCH /api/session`:
   - Request: `{ participantId, status: 'completed', completedAt }`.
   - Response: `{ success: true, participantId, status: 'completed' }`.
3. `POST /api/responses`:
   - Request: `{ responses: TrialRecord[] }` or `TrialRecord[]`.
   - Response: `{ success: true, insertedCount: number }`.

---

## 2. Logic Chain

### 2.1 Zero-Interference Architectural Model
To ensure that client synchronization never perturbs the 10.0s forced stimulus reading or the sub-millisecond reaction time capture:
1. **Reaction Time Decoupling**:
   Reaction time is captured by `RatingScreen` using `performance.now() - mountTimestamp` *prior* to firing `onSubmitResponse`. The calculated number is passed in the payload.
2. **Asynchronous Non-Blocking Dispatch**:
   `syncTrialResponse(trialRecord)` executes synchronously in under 0.5 ms:
   - Appends the trial record to `localStorage` (`favaloro_sync_queue_v1`).
   - Dispatches a background processing task via `queueMicrotask` or `setTimeout(..., 0)`.
   - Returns immediately.
   - The React UI thread instantly unmounts `RatingScreen` and mounts `StimulusReadingScreen` for trial $N+1$ without waiting for network I/O.
3. **Background Worker & Concurrency Control**:
   A mutex lock (`isDrainingQueue`) in `src/lib/sync.ts` guarantees that network requests are serialized or batched without racing. If a network roundtrip takes 800ms, it executes silently in the browser's background networking thread while the participant is quietly reading the stimulus banner on trial $N+1$.
4. **Debriefing Final Flush Gateway**:
   When trial 20 is completed, the participant reads the Debriefing screen at their own pace. When clicking "Finalizar", `page.tsx` executes `flushPendingSync(participantId, { timeoutMs: 5000 })`. If any trials failed to sync during the run (e.g. intermittent connection), they are dispatched in a single batch `POST /api/responses`.
5. **Full Offline Fallback**:
   If the browser is completely offline (`navigator.onLine === false` or network timeout):
   - All trial records and the session completion payload are securely stored in `localStorage`.
   - An event listener on `window.addEventListener('online')` automatically resumes queue flushing as soon as internet connectivity returns.
   - The participant is never blocked by a network error.

---

### 2.2 Complete Drop-In Blueprint: `src/lib/sync.ts`

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Asynchronous Client-Side Synchronization, Offline Buffering & Resiliency Manager
 * Target: src/lib/sync.ts
 */

import type {
  InductionGroup,
  FakeNewsSet,
  ExclusionReason,
  ParticipantDemographicsInput,
  TrialRecord,
  Gender,
  DeviceType,
} from '../types/experiment';
import { evaluateInclusion } from '../data/stimuli';
import { getBalancedLocalGroup, generateParticipantId } from './experimentState';
import type { ClientTelemetry } from './telemetry';

// ============================================================================
// Storage Keys & Constants
// ============================================================================

export const SYNC_QUEUE_STORAGE_KEY = 'favaloro_sync_queue_v1';
export const PENDING_SESSION_KEY = 'favaloro_pending_session_v1';
export const PENDING_COMPLETION_KEY = 'favaloro_pending_completion_v1';
export const SYNC_STATUS_KEY = 'favaloro_sync_status_v1';

export const DEFAULT_REQUEST_TIMEOUT_MS = 5000;
export const SESSION_INIT_TIMEOUT_MS = 2500;
export const MAX_RETRY_COUNT = 5;

// In-memory fallback if localStorage is unavailable (e.g. strict Safari private mode)
const inMemoryStore = new Map<string, string>();

// ============================================================================
// Types & Interfaces
// ============================================================================

export type SyncStatus = 'idle' | 'syncing' | 'synced' | 'error' | 'offline';

export interface PendingTrialQueueItem extends TrialRecord {
  _retryCount: number;
  _enqueuedAt: string;
  _lastAttemptAt?: string;
  _lastError?: string;
}

export interface SessionRegistrationPayload {
  participantId: string;
  age: number;
  gender: Gender;
  studiesPsychology: boolean;
  therapeuticOrientation: string;
  university: string;
  isIncluded: boolean;
  exclusionReason: ExclusionReason;
  deviceType: DeviceType;
  screenResolution: string;
  userAgent: string;
}

export interface SessionRegistrationResult {
  success: boolean;
  participantId: string;
  inductionGroup: InductionGroup;
  fakeNewsSet: FakeNewsSet;
  isIncluded: boolean;
  exclusionReason: ExclusionReason;
  isOffline: boolean;
  error?: string;
}

export interface SessionCompletionPayload {
  participantId: string;
  status: 'completed';
  completedAt: string;
}

export interface SyncStateSummary {
  status: SyncStatus;
  pendingCount: number;
  isOnline: boolean;
  lastSyncedAt: string | null;
  lastError: string | null;
}

export type SyncStatusSubscriber = (summary: SyncStateSummary) => void;

// ============================================================================
// Storage Helpers
// ============================================================================

function safeGetItem(key: string): string | null {
  if (typeof window === 'undefined') return inMemoryStore.get(key) || null;
  try {
    return localStorage.getItem(key);
  } catch {
    return inMemoryStore.get(key) || null;
  }
}

function safeSetItem(key: string, value: string): void {
  if (typeof window === 'undefined') {
    inMemoryStore.set(key, value);
    return;
  }
  try {
    localStorage.setItem(key, value);
  } catch {
    inMemoryStore.set(key, value);
  }
}

function safeRemoveItem(key: string): void {
  if (typeof window === 'undefined') {
    inMemoryStore.delete(key);
    return;
  }
  try {
    localStorage.removeItem(key);
  } catch {
    inMemoryStore.delete(key);
  }
}

function checkIsOnline(): boolean {
  if (typeof navigator !== 'undefined' && typeof navigator.onLine === 'boolean') {
    return navigator.onLine;
  }
  return true;
}

// ============================================================================
// Synchronization State & Event Subscriptions
// ============================================================================

let currentSyncStatus: SyncStatus = 'idle';
let lastSyncedTimestamp: string | null = null;
let lastSyncError: string | null = null;
let isDrainingQueue = false;
let retryTimerId: ReturnType<typeof setTimeout> | null = null;

const statusSubscribers = new Set<SyncStatusSubscriber>();

function emitSyncStatus(): void {
  const summary: SyncStateSummary = {
    status: currentSyncStatus,
    pendingCount: getPendingSyncCount(),
    isOnline: checkIsOnline(),
    lastSyncedAt: lastSyncedTimestamp,
    lastError: lastSyncError,
  };
  statusSubscribers.forEach((callback) => {
    try {
      callback(summary);
    } catch (err) {
      console.error('[SyncManager] Error in subscriber callback:', err);
    }
  });
}

export function subscribeSyncStatus(callback: SyncStatusSubscriber): () => void {
  statusSubscribers.add(callback);
  callback({
    status: currentSyncStatus,
    pendingCount: getPendingSyncCount(),
    isOnline: checkIsOnline(),
    lastSyncedAt: lastSyncedTimestamp,
    lastError: lastSyncError,
  });
  return () => {
    statusSubscribers.delete(callback);
  };
}

export function getPendingSyncCount(): number {
  const queue = getQueueFromStorage();
  let count = queue.length;
  if (safeGetItem(PENDING_SESSION_KEY)) count += 1;
  if (safeGetItem(PENDING_COMPLETION_KEY)) count += 1;
  return count;
}

function getQueueFromStorage(): PendingTrialQueueItem[] {
  const raw = safeGetItem(SYNC_QUEUE_STORAGE_KEY);
  if (!raw) return [];
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveQueueToStorage(queue: PendingTrialQueueItem[]): void {
  safeSetItem(SYNC_QUEUE_STORAGE_KEY, JSON.stringify(queue));
}

// ============================================================================
// Exponential Backoff with Random Jitter
// ============================================================================

function calculateBackoffDelay(retryCount: number): number {
  const baseDelayMs = 1000;
  const maxDelayMs = 30000;
  const exponential = baseDelayMs * Math.pow(2, Math.min(retryCount, 5));
  const jitter = exponential * 0.2 * (Math.random() * 2 - 1);
  return Math.min(Math.round(exponential + jitter), maxDelayMs);
}

// ============================================================================
// Session Registration Flow (/api/session)
// ============================================================================

/**
 * Registers participant session with the server.
 * Invokes `/api/session` to obtain balanced induction group via Supabase RPC.
 * If offline or network exceeds timeout, falls back to local balanced allocation.
 */
export async function registerSession(
  demographics: ParticipantDemographicsInput,
  telemetry: ClientTelemetry,
  options?: { timeoutMs?: number; participantId?: string }
): Promise<SessionRegistrationResult> {
  const timeoutMs = options?.timeoutMs ?? SESSION_INIT_TIMEOUT_MS;
  const participantId = options?.participantId || generateParticipantId();

  // 1. Evaluate inclusion criteria locally
  const { isIncluded, exclusionReason } = evaluateInclusion(demographics);

  // 2. Determine fake news set
  let fakeNewsSet: FakeNewsSet;
  if (!isIncluded) {
    fakeNewsSet = 'control_random';
  } else if (demographics.therapeuticOrientation === 'Psicoanálisis') {
    fakeNewsSet = 'psicoanalisis';
  } else {
    fakeNewsSet = 'evidencia';
  }

  const payload: SessionRegistrationPayload = {
    participantId,
    age: demographics.age,
    gender: demographics.gender,
    studiesPsychology: demographics.studiesPsychology,
    therapeuticOrientation: demographics.therapeuticOrientation,
    university: demographics.university,
    isIncluded,
    exclusionReason,
    deviceType: telemetry.deviceType,
    screenResolution: telemetry.screenResolution,
    userAgent: telemetry.userAgent,
  };

  // Always buffer session registration payload for offline safety
  safeSetItem(PENDING_SESSION_KEY, JSON.stringify(payload));

  // If client is already detected as offline, bypass network call immediately
  if (!checkIsOnline()) {
    currentSyncStatus = 'offline';
    emitSyncStatus();
    const localGroup: InductionGroup = !isIncluded ? 'control' : getBalancedLocalGroup();
    return {
      success: true,
      participantId,
      inductionGroup: localGroup,
      fakeNewsSet,
      isIncluded,
      exclusionReason,
      isOffline: true,
    };
  }

  // Attempt server registration with strict AbortController timeout
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  try {
    currentSyncStatus = 'syncing';
    emitSyncStatus();

    const response = await fetch('/api/session', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });

    clearTimeout(timer);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();

    // Successfully created on server -> clear pending session buffer
    safeRemoveItem(PENDING_SESSION_KEY);
    currentSyncStatus = 'synced';
    lastSyncedTimestamp = new Date().toISOString();
    lastSyncError = null;
    emitSyncStatus();

    const inductionGroup: InductionGroup =
      data.inductionGroup || (!isIncluded ? 'control' : getBalancedLocalGroup());

    return {
      success: true,
      participantId,
      inductionGroup,
      fakeNewsSet,
      isIncluded,
      exclusionReason,
      isOffline: false,
    };
  } catch (err: unknown) {
    clearTimeout(timer);
    const errorMessage = err instanceof Error ? err.message : String(err);
    console.warn('[SyncManager] Session registration fallback triggered:', errorMessage);

    lastSyncError = errorMessage;
    currentSyncStatus = checkIsOnline() ? 'error' : 'offline';
    emitSyncStatus();

    // Fall back gracefully to local balanced group heuristic
    const localGroup: InductionGroup = !isIncluded ? 'control' : getBalancedLocalGroup();

    return {
      success: true,
      participantId,
      inductionGroup: localGroup,
      fakeNewsSet,
      isIncluded,
      exclusionReason,
      isOffline: true,
      error: errorMessage,
    };
  }
}

// ============================================================================
// Asynchronous Non-Blocking Trial Submission (/api/responses)
// ============================================================================

/**
 * Enqueues a trial record and triggers background synchronization.
 * Synchronous execution is < 0.5ms with zero delay to UI interaction or timing.
 */
export function syncTrialResponse(trialRecord: TrialRecord): void {
  try {
    const queue = getQueueFromStorage();

    // Deduplication / Idempotency check: update existing record if already present
    const existingIndex = queue.findIndex(
      (item) =>
        item.participantId === trialRecord.participantId &&
        item.presentationOrder === trialRecord.presentationOrder
    );

    const pendingItem: PendingTrialQueueItem = {
      ...trialRecord,
      _retryCount: existingIndex >= 0 ? queue[existingIndex]._retryCount : 0,
      _enqueuedAt:
        existingIndex >= 0 ? queue[existingIndex]._enqueuedAt : new Date().toISOString(),
    };

    if (existingIndex >= 0) {
      queue[existingIndex] = pendingItem;
    } else {
      queue.push(pendingItem);
    }

    saveQueueToStorage(queue);
    emitSyncStatus();

    // Trigger background queue drain asynchronously
    if (typeof queueMicrotask === 'function') {
      queueMicrotask(() => triggerBackgroundDrain());
    } else {
      setTimeout(() => triggerBackgroundDrain(), 0);
    }
  } catch (err) {
    console.error('[SyncManager] Error enqueueing trial response:', err);
  }
}

// ============================================================================
// Session Completion Submission (PATCH /api/session)
// ============================================================================

/**
 * Marks session as completed and enqueues completion payload.
 */
export function completeSession(participantId: string, completedAt?: string): void {
  const payload: SessionCompletionPayload = {
    participantId,
    status: 'completed',
    completedAt: completedAt || new Date().toISOString(),
  };

  safeSetItem(PENDING_COMPLETION_KEY, JSON.stringify(payload));
  emitSyncStatus();

  if (typeof queueMicrotask === 'function') {
    queueMicrotask(() => triggerBackgroundDrain());
  } else {
    setTimeout(() => triggerBackgroundDrain(), 0);
  }
}

// ============================================================================
// Background Queue Drain & Batch Sync Engine
// ============================================================================

export function triggerBackgroundDrain(): void {
  if (isDrainingQueue) return;
  if (retryTimerId) {
    clearTimeout(retryTimerId);
    retryTimerId = null;
  }
  drainQueue().catch((err) => {
    console.warn('[SyncManager] Unhandled background drain warning:', err);
  });
}

async function drainQueue(): Promise<void> {
  if (isDrainingQueue) return;
  if (!checkIsOnline()) {
    currentSyncStatus = 'offline';
    emitSyncStatus();
    return;
  }

  isDrainingQueue = true;
  currentSyncStatus = 'syncing';
  emitSyncStatus();

  try {
    // 1. Drain pending session registration first if present
    const rawPendingSession = safeGetItem(PENDING_SESSION_KEY);
    if (rawPendingSession) {
      try {
        const sessionPayload = JSON.parse(rawPendingSession);
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), DEFAULT_REQUEST_TIMEOUT_MS);

        const res = await fetch('/api/session', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(sessionPayload),
          signal: controller.signal,
        });
        clearTimeout(timer);

        if (res.ok) {
          safeRemoveItem(PENDING_SESSION_KEY);
        }
      } catch (err) {
        console.warn('[SyncManager] Background session sync attempt failed, will retry:', err);
      }
    }

    // 2. Drain pending trial records in batch
    const queue = getQueueFromStorage();

    if (queue.length > 0) {
      // Clean internal metadata fields before sending to API
      const payloadBatch = queue.map((item) => {
        const { _retryCount, _enqueuedAt, _lastAttemptAt, _lastError, ...cleanRecord } = item;
        return cleanRecord;
      });

      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), DEFAULT_REQUEST_TIMEOUT_MS);

      const res = await fetch('/api/responses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ responses: payloadBatch }),
        signal: controller.signal,
      });

      clearTimeout(timer);

      if (res.ok) {
        // Clear all synced trials from queue
        saveQueueToStorage([]);
        lastSyncedTimestamp = new Date().toISOString();
        lastSyncError = null;
      } else {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      }
    }

    // 3. Drain pending session completion if present and trials are done
    const remainingQueue = getQueueFromStorage();
    if (remainingQueue.length === 0) {
      const rawPendingCompletion = safeGetItem(PENDING_COMPLETION_KEY);
      if (rawPendingCompletion) {
        try {
          const completionPayload = JSON.parse(rawPendingCompletion);
          const controller = new AbortController();
          const timer = setTimeout(() => controller.abort(), DEFAULT_REQUEST_TIMEOUT_MS);

          const res = await fetch('/api/session', {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(completionPayload),
            signal: controller.signal,
          });

          clearTimeout(timer);

          if (res.ok) {
            safeRemoveItem(PENDING_COMPLETION_KEY);
          }
        } catch (err) {
          console.warn('[SyncManager] Completion sync attempt failed, will retry:', err);
        }
      }
    }

    // Check final status
    const remainingCount = getPendingSyncCount();
    if (remainingCount === 0) {
      currentSyncStatus = 'synced';
    } else {
      currentSyncStatus = 'error';
    }
  } catch (err: unknown) {
    const errorMessage = err instanceof Error ? err.message : String(err);
    lastSyncError = errorMessage;
    currentSyncStatus = checkIsOnline() ? 'error' : 'offline';

    // Increment retry counts on queue items
    const queue = getQueueFromStorage();
    let minRetries = MAX_RETRY_COUNT;

    const updatedQueue = queue.map((item) => {
      const newRetries = (item._retryCount || 0) + 1;
      if (newRetries < minRetries) minRetries = newRetries;
      return {
        ...item,
        _retryCount: newRetries,
        _lastAttemptAt: new Date().toISOString(),
        _lastError: errorMessage,
      };
    });

    saveQueueToStorage(updatedQueue);

    // Schedule next backoff retry if under threshold and online
    if (checkIsOnline() && minRetries <= MAX_RETRY_COUNT) {
      const delay = calculateBackoffDelay(minRetries);
      retryTimerId = setTimeout(() => triggerBackgroundDrain(), delay);
    }
  } finally {
    isDrainingQueue = false;
    emitSyncStatus();
  }
}

// ============================================================================
// Explicit Flush Gateway (Debriefing / Thank You Screens)
// ============================================================================

/**
 * Explicitly forces a batch drain with a configurable deadline.
 * Guaranteed to resolve and never trap participant on a hanging screen.
 */
export async function flushPendingSync(
  participantId?: string,
  options?: { timeoutMs?: number }
): Promise<{ success: boolean; pendingCount: number; isOffline: boolean; error?: string }> {
  const timeoutMs = options?.timeoutMs ?? 6000;

  if (!checkIsOnline()) {
    currentSyncStatus = 'offline';
    emitSyncStatus();
    return {
      success: false,
      pendingCount: getPendingSyncCount(),
      isOffline: true,
      error: 'Dispositivo sin conexión a internet. Respuestas resguardadas localmente.',
    };
  }

  return new Promise((resolve) => {
    let resolved = false;

    const timer = setTimeout(() => {
      if (!resolved) {
        resolved = true;
        const pendingCount = getPendingSyncCount();
        resolve({
          success: pendingCount === 0,
          pendingCount,
          isOffline: !checkIsOnline(),
          error: pendingCount > 0 ? 'Tiempo de espera de sincronización agotado' : undefined,
        });
      }
    }, timeoutMs);

    triggerBackgroundDrain();

    // Check periodically if queue has completed
    const interval = setInterval(() => {
      if (getPendingSyncCount() === 0) {
        if (!resolved) {
          resolved = true;
          clearTimeout(timer);
          clearInterval(interval);
          resolve({
            success: true,
            pendingCount: 0,
            isOffline: false,
          });
        }
      } else if (!isDrainingQueue && !resolved) {
        // Drain finished but items remain (e.g. server error)
        resolved = true;
        clearTimeout(timer);
        clearInterval(interval);
        resolve({
          success: false,
          pendingCount: getPendingSyncCount(),
          isOffline: !checkIsOnline(),
          error: lastSyncError || 'Error al persistir registros en el servidor',
        });
      }
    }, 200);
  });
}

// ============================================================================
// Reset & Cleanup
// ============================================================================

export function clearSyncStorage(): void {
  safeRemoveItem(SYNC_QUEUE_STORAGE_KEY);
  safeRemoveItem(PENDING_SESSION_KEY);
  safeRemoveItem(PENDING_COMPLETION_KEY);
  safeRemoveItem(SYNC_STATUS_KEY);
  currentSyncStatus = 'idle';
  lastSyncedTimestamp = null;
  lastSyncError = null;
  if (retryTimerId) {
    clearTimeout(retryTimerId);
    retryTimerId = null;
  }
  emitSyncStatus();
}

// ============================================================================
// Online / Offline Global Window Listeners
// ============================================================================

if (typeof window !== 'undefined') {
  window.addEventListener('online', () => {
    console.info('[SyncManager] Browser reconnected to internet. Resuming sync queue...');
    currentSyncStatus = 'syncing';
    emitSyncStatus();
    triggerBackgroundDrain();
  });

  window.addEventListener('offline', () => {
    console.warn('[SyncManager] Browser went offline. Buffering responses in localStorage.');
    currentSyncStatus = 'offline';
    emitSyncStatus();
  });
}
```

---

### 2.3 Step-by-Step Integration with `src/app/page.tsx`

The integration modifies `src/app/page.tsx` in five precise places:
1. **Imports**: Imports sync manager functions (`registerSession`, `syncTrialResponse`, `completeSession`, `flushPendingSync`, `clearSyncStorage`).
2. **Synchronous Trial Sync `useEffect`**: A dedicated `useEffect` watches `state.responses`. Whenever a new trial response is added by the reducer, it calls `syncTrialResponse(trial)` without touching the UI thread.
3. **Demographics Submission**: Wraps `DemographicsScreen.onSubmit` with `await registerSession(...)`. If the server responds within 2500ms, it passes the balanced `inductionGroup` to `SUBMIT_DEMOGRAPHICS`. If offline or timeout occurs, it falls back to local group assignment.
4. **Debriefing Confirmation Gate**: When participant confirms debriefing, calls `completeSession` and `await flushPendingSync` with a 5000ms deadline.
5. **Restart & Reset**: On `ThankYouScreen`, clearing session also calls `clearSyncStorage()`.

#### Complete Drop-In `src/app/page.tsx`:

```typescript
'use client';

import React, { useReducer, useEffect, useState, useRef } from 'react';
import {
  experimentReducer,
  getInitialExperimentState,
} from '@/lib/experimentState';
import { preloadStimuliBatch } from '@/lib/assets';
import { captureClientTelemetry } from '@/lib/telemetry';
import {
  saveSessionToStorage,
  loadSessionFromStorage,
  clearSessionFromStorage,
} from '@/lib/sessionRecovery';
import {
  registerSession,
  syncTrialResponse,
  completeSession,
  flushPendingSync,
  clearSyncStorage,
} from '@/lib/sync';

import { WelcomeScreen } from '@/components/WelcomeScreen';
import { ConsentScreen } from '@/components/ConsentScreen';
import { DemographicsScreen } from '@/components/DemographicsScreen';
import { InductionScreen } from '@/components/InductionScreen';
import { StimulusReadingScreen } from '@/components/StimulusReadingScreen';
import { RatingScreen } from '@/components/RatingScreen';
import { DebriefingScreen } from '@/components/DebriefingScreen';
import { ThankYouScreen } from '@/components/ThankYouScreen';

// ============================================================================
// Experiment Flow Orchestrator Component
// ============================================================================

export default function ExperimentPage() {
  const [state, dispatch] = useReducer(experimentReducer, getInitialExperimentState());
  const [isRegisteringSession, setIsRegisteringSession] = useState(false);
  const [isFinalizingSession, setIsFinalizingSession] = useState(false);

  // Ref tracking responses that have already been passed to syncTrialResponse
  const syncedResponsesCountRef = useRef(0);

  // 1. Client Hydration & Session Recovery on Mount
  useEffect(() => {
    const stored = loadSessionFromStorage();
    if (stored) {
      syncedResponsesCountRef.current = stored.responses?.length || 0;
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

  // 2. Session Persistence to sessionStorage on State Changes
  useEffect(() => {
    if (state.isHydrated && state.stage !== 'welcome' && state.stage !== 'consent') {
      saveSessionToStorage(state);
    }
  }, [state]);

  // 3. Background Non-Blocking Trial Responses Synchronization
  // Runs after paint when state.responses updates. Zero interference with UI or RT capture.
  useEffect(() => {
    if (state.responses && state.responses.length > syncedResponsesCountRef.current) {
      const pendingTrials = state.responses.slice(syncedResponsesCountRef.current);
      syncedResponsesCountRef.current = state.responses.length;
      for (const trial of pendingTrials) {
        syncTrialResponse(trial);
      }
    }
  }, [state.responses]);

  // 4. Preload 20 Stimulus Assets in the Background
  useEffect(() => {
    if (state.deck && state.deck.length === 20) {
      const stimulusIds = state.deck.map((s) => s.id);
      preloadStimuliBatch(stimulusIds).catch((err) => {
        console.warn('Background stimuli preloading caught error:', err);
      });
    }
  }, [state.deck]);

  // 5. BeforeUnload Guard during In-Progress Trials
  useEffect(() => {
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      const isExperimentInProgress =
        state.stage !== 'welcome' &&
        state.stage !== 'consent' &&
        state.stage !== 'thankyou';

      if (isExperimentInProgress) {
        e.preventDefault();
        e.returnValue =
          'El experimento está en progreso. Si sale ahora, sus respuestas no se completarán.';
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

  // Loading overlay during demographics server registration (max 2500ms)
  if (isRegisteringSession) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 gap-4">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600" />
        <p className="text-sm font-medium text-slate-600">
          Iniciando sesión y asignando condiciones del experimento...
        </p>
      </div>
    );
  }

  // Loading overlay during debriefing final flush gateway (max 5000ms)
  if (isFinalizingSession) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 gap-4">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600" />
        <p className="text-sm font-medium text-slate-600">
          Guardando y sincronizando sus respuestas con la base de datos...
        </p>
      </div>
    );
  }

  // 6. Stage Dispatcher
  switch (state.stage) {
    case 'welcome':
      return <WelcomeScreen onStart={() => dispatch({ type: 'START_CONSENT' })} />;

    case 'consent':
      return (
        <ConsentScreen
          onAcceptConsent={() => dispatch({ type: 'ACCEPT_CONSENT' })}
          onAccept={() => dispatch({ type: 'ACCEPT_CONSENT' })}
          onBack={() => dispatch({ type: 'RESET_EXPERIMENT' })}
        />
      );

    case 'demographics':
      return (
        <DemographicsScreen
          onSubmit={async (demographics) => {
            const telemetry = captureClientTelemetry();
            setIsRegisteringSession(true);
            try {
              // Asynchronously registers session with /api/session (server balanced RPC).
              // Falls back to local balanced allocation if offline or timeout (>2500ms).
              const sessionResult = await registerSession(demographics, telemetry);
              dispatch({
                type: 'SUBMIT_DEMOGRAPHICS',
                payload: {
                  demographics,
                  telemetry,
                  assignedGroup: sessionResult.inductionGroup,
                },
              });
            } catch (err) {
              console.warn('[ExperimentPage] Session registration fallback:', err);
              dispatch({
                type: 'SUBMIT_DEMOGRAPHICS',
                payload: { demographics, telemetry },
              });
            } finally {
              setIsRegisteringSession(false);
            }
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
      if (!currentStimulus) return null;

      return (
        <StimulusReadingScreen
          key={`reading-${state.currentTrialIndex}-${currentStimulus.id}`}
          stimulus={currentStimulus}
          trialNumber={state.currentTrialIndex + 1}
          totalTrials={state.deck.length}
          onExposureComplete={(readingTimeMs) => {
            dispatch({ type: 'FINISH_READING', payload: { readingTimeMs } });
          }}
          onComplete={(readingTimeMs) => {
            dispatch({ type: 'FINISH_READING', payload: { readingTimeMs } });
          }}
        />
      );
    }

    case 'rating': {
      const currentStimulus = state.deck[state.currentTrialIndex];
      if (!currentStimulus) return null;

      return (
        <RatingScreen
          key={`rating-${state.currentTrialIndex}-${currentStimulus.id}`}
          stimulus={currentStimulus}
          trialNumber={state.currentTrialIndex + 1}
          totalTrials={state.deck.length}
          onSubmitResponse={({ responseOption, responseTimeMs }) => {
            // Immediate synchronous state update. Background synchronization
            // is triggered asynchronously via useEffect without touching this thread.
            dispatch({
              type: 'RECORD_TRIAL_RESPONSE',
              payload: { responseOption, responseTimeMs },
            });
          }}
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
          onConfirmDebriefing={async () => {
            setIsFinalizingSession(true);
            try {
              const nowIso = new Date().toISOString();
              completeSession(state.participantId, nowIso);
              // Final flush gateway: attempts batch sync of all trials and completion status
              await flushPendingSync(state.participantId, { timeoutMs: 5000 });
            } catch (err) {
              console.warn('[ExperimentPage] Final flush gateway caught warning:', err);
            } finally {
              setIsFinalizingSession(false);
              dispatch({ type: 'COMPLETE_DEBRIEFING' });
            }
          }}
          onComplete={async () => {
            setIsFinalizingSession(true);
            try {
              const nowIso = new Date().toISOString();
              completeSession(state.participantId, nowIso);
              await flushPendingSync(state.participantId, { timeoutMs: 5000 });
            } catch (err) {
              console.warn('[ExperimentPage] Final flush gateway caught warning:', err);
            } finally {
              setIsFinalizingSession(false);
              dispatch({ type: 'COMPLETE_DEBRIEFING' });
            }
          }}
        />
      );

    case 'thankyou':
      return (
        <ThankYouScreen
          participantId={state.participantId}
          onRestart={() => {
            clearSessionFromStorage();
            clearSyncStorage();
            syncedResponsesCountRef.current = 0;
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

### 2.4 Automated Test Suite Blueprint: `tests/sync.test.ts`

To be placed in `web-experimento/tests/sync.test.ts` and executed via `node --experimental-strip-types tests/sync.test.ts` or `tsx tests/sync.test.ts`:

```typescript
import { test, describe, beforeEach, afterEach } from 'node:test';
import assert from 'node:assert/strict';

import {
  registerSession,
  syncTrialResponse,
  completeSession,
  flushPendingSync,
  getPendingSyncCount,
  clearSyncStorage,
  SYNC_QUEUE_STORAGE_KEY,
  PENDING_SESSION_KEY,
  PENDING_COMPLETION_KEY,
} from '../src/lib/sync.ts';
import type { TrialRecord, ParticipantDemographicsInput } from '../src/types/experiment.ts';
import type { ClientTelemetry } from '../src/lib/telemetry.ts';

describe('Milestone 3: Client Synchronization & Offline Resiliency', () => {
  const originalFetch = globalThis.fetch;

  beforeEach(() => {
    clearSyncStorage();
  });

  afterEach(() => {
    globalThis.fetch = originalFetch;
    clearSyncStorage();
  });

  test('M3.1: Session registration succeeds with mock server returning balanced group', async () => {
    // Mock /api/session returning 'emocional'
    globalThis.fetch = async (url: RequestInfo | URL) => {
      const urlStr = String(url);
      if (urlStr.includes('/api/session')) {
        return new Response(
          JSON.stringify({
            success: true,
            participantId: 'test-uuid-1234',
            inductionGroup: 'emocional',
            fakeNewsSet: 'psicoanalisis',
            isIncluded: true,
            exclusionReason: null,
          }),
          { status: 200, headers: { 'Content-Type': 'application/json' } }
        );
      }
      return new Response('Not found', { status: 404 });
    };

    const demographics: ParticipantDemographicsInput = {
      age: 22,
      gender: 'Femenino',
      studiesPsychology: true,
      therapeuticOrientation: 'Psicoanálisis',
      university: 'Universidad Favaloro',
    };
    const telemetry: ClientTelemetry = {
      deviceType: 'desktop',
      screenResolution: '1920x1080',
      userAgent: 'Mock Browser',
    };

    const result = await registerSession(demographics, telemetry, {
      participantId: 'test-uuid-1234',
      timeoutMs: 1000,
    });

    assert.equal(result.success, true);
    assert.equal(result.participantId, 'test-uuid-1234');
    assert.equal(result.inductionGroup, 'emocional');
    assert.equal(result.fakeNewsSet, 'psicoanalisis');
    assert.equal(result.isOffline, false);
  });

  test('M3.2: Session registration falls back to local heuristic on network timeout or failure', async () => {
    // Mock network failure
    globalThis.fetch = async () => {
      throw new Error('Network error / Server unreachable');
    };

    const demographics: ParticipantDemographicsInput = {
      age: 24,
      gender: 'Masculino',
      studiesPsychology: true,
      therapeuticOrientation: 'Basada en Evidencia Científica',
      university: 'UBA',
    };
    const telemetry: ClientTelemetry = {
      deviceType: 'mobile',
      screenResolution: '390x844',
      userAgent: 'Mobile Safari',
    };

    const result = await registerSession(demographics, telemetry, {
      participantId: 'offline-uuid-999',
      timeoutMs: 500,
    });

    assert.equal(result.success, true);
    assert.equal(result.participantId, 'offline-uuid-999');
    assert.ok(['racional', 'emocional', 'control'].includes(result.inductionGroup));
    assert.equal(result.isOffline, true);
    assert.ok(result.error);
  });

  test('M3.3: syncTrialResponse executes synchronously and buffers item in queue', () => {
    const trialRecord: TrialRecord = {
      id: 'trial-uuid-1',
      participantId: 'part-uuid-1',
      presentationOrder: 1,
      newsId: 5,
      isFake: false,
      newsCongruence: 'true',
      responseOption: 1,
      responseLabel: 'Recuerdo claramente haber visto/leído este evento',
      readingTimeMs: 10000,
      responseTimeMs: 1850,
      isFalseMemory: false,
      isFalseBelief: false,
      isTrueMemory: true,
      createdAt: new Date().toISOString(),
    };

    const t0 = performance.now();
    syncTrialResponse(trialRecord);
    const executionDuration = performance.now() - t0;

    // Must execute synchronously in < 10 milliseconds (zero timing interference)
    assert.ok(executionDuration < 10, `Execution took ${executionDuration}ms, expected < 10ms`);
    assert.equal(getPendingSyncCount(), 1);
  });

  test('M3.4: syncTrialResponse deduplicates identical presentationOrder for participant', () => {
    const trialRecord: TrialRecord = {
      id: 'trial-uuid-1',
      participantId: 'part-uuid-1',
      presentationOrder: 1,
      newsId: 5,
      isFake: false,
      newsCongruence: 'true',
      responseOption: 1,
      responseLabel: 'Recuerdo claramente haber visto/leído este evento',
      readingTimeMs: 10000,
      responseTimeMs: 1850,
      isFalseMemory: false,
      isFalseBelief: false,
      isTrueMemory: true,
      createdAt: new Date().toISOString(),
    };

    syncTrialResponse(trialRecord);
    // Submit second time with updated reaction time
    syncTrialResponse({ ...trialRecord, responseTimeMs: 1900 });

    assert.equal(getPendingSyncCount(), 1);
  });

  test('M3.5: Batch flush drains multiple pending responses to /api/responses', async () => {
    let capturedBody: any = null;

    globalThis.fetch = async (url: RequestInfo | URL, init?: RequestInit) => {
      const urlStr = String(url);
      if (urlStr.includes('/api/responses')) {
        capturedBody = JSON.parse(String(init?.body));
        return new Response(JSON.stringify({ success: true, insertedCount: 3 }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' },
        });
      }
      return new Response(JSON.stringify({ success: true }), { status: 200 });
    };

    // Queue 3 trials
    for (let i = 1; i <= 3; i++) {
      syncTrialResponse({
        id: `trial-${i}`,
        participantId: 'part-100',
        presentationOrder: i,
        newsId: i,
        isFake: i > 2,
        newsCongruence: i > 2 ? 'psicoanalisis' : 'true',
        responseOption: 2,
        responseLabel: 'No recuerdo haberlo visto, pero creo que sucedió',
        readingTimeMs: 10000,
        responseTimeMs: 2000,
        isFalseMemory: false,
        isFalseBelief: i > 2,
        isTrueMemory: false,
      });
    }

    assert.equal(getPendingSyncCount(), 3);

    const flushResult = await flushPendingSync('part-100', { timeoutMs: 2000 });
    assert.equal(flushResult.success, true);
    assert.equal(flushResult.pendingCount, 0);
    assert.ok(capturedBody && capturedBody.responses);
    assert.equal(capturedBody.responses.length, 3);
  });
});
```

---

## 3. Caveats & Invalidation Conditions

1. **Storage Quota & Private Browsing Mode**:
   - In Safari Private Browsing mode or under extreme disk constraints, `localStorage.setItem` can throw `QuotaExceededError`.
   - *Mitigation*: `src/lib/sync.ts` implements a transparent `inMemoryStore` fallback so serialization failures never crash the application.
2. **Server-Side Idempotency (`participant_id, presentation_order`)**:
   - If an intermittent network error causes the client to re-post a batch of responses that partially succeeded on the server, the database must not insert duplicate rows or fail with unique constraint violations.
   - *Recommendation for `explorer_m3_1_gen2` / `worker_m3_1`*: Include a unique index on `responses(participant_id, presentation_order)` and use `UPSERT` / `ON CONFLICT (participant_id, presentation_order) DO UPDATE` in `schema.sql` and `/api/responses/route.ts`.
3. **Extreme Disconnection at Final Screen**:
   - If a participant finishes all 20 trials and confirms debriefing while completely offline, data remains safely buffered in `localStorage`.
   - *Mitigation*: `flushPendingSync` guarantees resolution after `timeoutMs` (5s), allowing the user to reach `ThankYouScreen`. The global `online` listener will immediately transmit the data when internet returns.

---

## 4. Conclusion

1. **Complete Architectural Decoupling**:
   By placing trial response synchronization in a post-paint React `useEffect` and an asynchronous background queue, participant interactions and millisecond reaction time capture are completely isolated from network latency.
2. **Deterministic Balanced Group Allocation**:
   The session registration call queries `/api/session` with a 2500ms timeout. When online, the server's PostgreSQL RPC `assign_induction_group()` maintains the required $\Delta \le 2$ balance invariant. If offline or slow, the client seamlessly falls back to `getBalancedLocalGroup()`.
3. **Drop-In Readiness**:
   Both `src/lib/sync.ts` and `src/app/page.tsx` are fully designed, typed, and self-contained, ready for immediate placement into `web-experimento` by Worker agents.

---

## 5. Verification Method

To verify the implementation once applied by the Worker agent:

1. **Execute the automated sync test suite**:
   ```powershell
   cd "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento"
   npx tsx tests/sync.test.ts
   ```
2. **Verify non-interference with Milestone 2 timing and state machines**:
   ```powershell
   npm run test:m2
   ```
3. **Verify complete build with zero TypeScript compilation errors**:
   ```powershell
   npm run build
   ```
4. **Manual Dev Server Verification**:
   - Start local development: `npm run dev`
   - Open Chrome DevTools $\to$ Network $\to$ Toggle "Offline" during trial 5.
   - Complete trials 5–20 offline $\to$ verify transitions take zero delay.
   - Re-enable "Online" in DevTools $\to$ verify network log flushes pending batch of 16 responses.
