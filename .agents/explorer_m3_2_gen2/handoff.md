# API Route Handlers & Supabase Client Integration Blueprint (Milestone 3)

**Agent:** `explorer_m3_2_gen2`  
**Date:** 2026-09-21  
**Milestone:** M3 (Backend & Data Persistence — Supabase Client and Next.js API Routes)  
**Target Files for Worker:**
1. `web-experimento/src/lib/supabase.ts`
2. `web-experimento/src/app/api/session/route.ts`
3. `web-experimento/src/app/api/responses/route.ts`

---

## 1. Observation

### 1.1 Filesystem & Dependency Verification
- **Target Directories Audit:**
  - `web-experimento/src/app/api/session` exists and is empty (0 files).
  - `web-experimento/src/app/api/responses` exists and is empty (0 files).
  - `web-experimento/src/lib` contains `assets.ts`, `experimentState.ts`, `sessionRecovery.ts`, `telemetry.ts`. No `supabase.ts` exists yet.
- **Dependency Audit (`web-experimento/package.json`):**
  - Line 23: `"@supabase/supabase-js": "^2.116.0"` is already installed.
  - Line 25: `"next": "14.2.35"`.
  - Node version: `v24.15.0`.
- **Environment Configuration Audit (`web-experimento/.env.local`):**
  - Lines 1-6:
    ```ini
    # Local development environment configuration
    NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
    NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
    SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
    ADMIN_PASSWORD=favaloro-admin-dev
    ```
  - **Critical Finding:** Environment variables contain placeholder values (`https://your-project.supabase.co`, `your-anon-key`, `your-service-role-key`). Any unhandled invocation of `@supabase/supabase-js` `createClient()` with these values will attempt to connect to an invalid host. A robust offline/dev mock fallback is mandatory so that developers, local preview runs, and automated test runners can execute seamlessly without live Supabase credentials.

### 1.2 Domain Models & Business Logic Verification
- **Domain Types in `src/types/experiment.ts`:**
  - `InductionGroup` (lines 19-20): `'racional' | 'emocional' | 'control'`.
  - `TherapeuticOrientation` (lines 25-28): `'Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros'`.
  - `Gender` (line 33): `'Femenino' | 'Masculino' | 'Otro'`.
  - `FakeNewsSet` (lines 36-41): `'psicoanalisis' | 'evidencia' | 'control_random'`.
  - `ParticipantDemographicsInput` (lines 119-125): `{ age: number; gender: Gender; studiesPsychology: boolean; therapeuticOrientation: TherapeuticOrientation; university: string; }`.
  - `ParticipantSession` (lines 138-155): Includes UUID `id`, `createdAt`, `completedAt`, demographics, `isIncluded`, `exclusionReason`, `inductionGroup`, `fakeNewsSet`, `status`, `deviceType`, `screenResolution`, `userAgent`.
  - `TrialRecord` (lines 176-191): Includes `participantId`, `presentationOrder` (1..20), `newsId` (1..28), `isFake`, `newsCongruence`, `responseOption` (1..4), `responseLabel`, `readingTimeMs`, `responseTimeMs`, `isFalseMemory`, `isFalseBelief`, `isTrueMemory`.
- **Stimulus & Inclusion Logic in `src/data/stimuli.ts`:**
  - `evaluateInclusion()` (lines 458-495): Evaluates `age < 18` (menor_de_edad), `!studiesPsychology` (no_estudia_psicologia), `therapeuticOrientation === 'Otros'` (orientacion_otros). Returns `{ isIncluded: boolean, exclusionReason: ExclusionReason }`.
  - `RESPONSE_OPTIONS_MAP` (line 413): Maps `1..4` to Murphy/León construct definitions and verbatim labels:
    - 1: *"Recuerdo claramente haber visto/leído este evento"* (Falso Recuerdo / Memoria Verdadera)
    - 2: *"No recuerdo haberlo visto, pero creo que sucedió"* (Falsa Creencia)
    - 3: *"Lo recuerdo diferente"*
    - 4: *"No lo recuerdo en absoluto"*
  - `classifyResponse()` (lines 614-627): Derives `isFalseMemory` (`isFake && opt === 1`), `isFalseBelief` (`isFake && opt === 2`), `isTrueMemory` (`!isFake && opt === 1`).
  - `getStimulusById(id: number)` (lines 657-664): Bounds-checked lookup into canonical 28-stimuli array.
- **Supabase Database Schema (`.agents/explorer_m3_1_gen2/handoff.md`):**
  - Table `public.participants` has domain constraints:
    - `age >= 18 AND age <= 120`
    - `gender IN ('Femenino', 'Masculino', 'Otro')`
    - `therapeutic_orientation IN ('Psicoanálisis', 'Basada en Evidencia Científica', 'Otros')`
    - `chk_participant_exclusion_logic`: `(is_included = true) OR (is_included = false AND induction_group = 'control' AND fake_news_set = 'control_random')`
  - Table `public.responses` has constraints:
    - `presentation_order BETWEEN 1 AND 20`
    - `news_id BETWEEN 1 AND 28`
    - `response_option IN (1, 2, 3, 4)`
    - `UNIQUE (participant_id, presentation_order)`
    - `UNIQUE (participant_id, news_id)`
  - Stored Procedure `assign_induction_group()`:
    - Acquires `pg_advisory_xact_lock(742911)`.
    - Filters by `is_included = true`.
    - Selects group with minimal count; breaks ties with `ORDER BY random() LIMIT 1`.

---

## 2. Logic Chain

### 2.1 Supabase Client Architecture (`src/lib/supabase.ts`)
1. **Public vs Admin Client Roles:**
   - **Public Client (`anon` key):** Created using `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`. Used by client components if direct Supabase calls are needed.
   - **Admin Client (`service_role` key):** Created using `NEXT_PUBLIC_SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`. Used exclusively in server-side Next.js Route Handlers (`/api/session`, `/api/responses`, `/api/admin/*`). This bypasses RLS policies and allows server handlers to execute administrative queries, RPC functions, and bulk inserts without permission friction.
2. **Credential Detection & Graceful Fallback:**
   - We implement `isSupabaseConfigured()` and `isSupabaseAdminConfigured()`. These check for non-empty keys and actively filter out placeholder strings like `https://your-project.supabase.co` and `your-anon-key`.
   - When unconfigured or when network exceptions occur, the system falls back to an in-memory `mockStore`.
3. **In-Memory Mock Store (`InMemoryMockStore`):**
   - Implements identical balancing semantics as the PostgreSQL RPC: maintains `groupCounts: { racional, emocional, control }`, finds candidates with minimal count, and breaks ties uniformly at random ($\Delta \le 1$).
   - Stores participant rows in a `Map<string, ParticipantRow>` and trial responses in an array with deduplication on `(participant_id, presentation_order)`.
   - This ensures 100% functionality during local development, unit testing, and E2E simulation without requiring external cloud credentials.

### 2.2 Session Route Handler Architecture (`src/app/api/session/route.ts`)
1. **POST Handler (Session Initialization):**
   - **Validation:** Enforces integer `age >= 18 AND <= 120`, valid `gender`, boolean `studiesPsychology`, valid `therapeuticOrientation`, non-empty `university`. Returns HTTP 400 Bad Request with explicit error lists upon failure.
   - **Inclusion Assessment:** Reuses canonical `evaluateInclusion()` from `src/data/stimuli.ts`.
   - **Group & Stimulus Routing:**
     - Excluded: `inductionGroup = 'control'`, `fakeNewsSet = 'control_random'`.
     - Included: calls Supabase RPC `assign_induction_group()`. If Supabase is offline or unconfigured, falls back to `mockStore.assignGroup(true)`.
   - **Idempotency & Persistence:** Accepts client-generated UUID v4 or generates one; persists row in `participants` table (or `mockStore`); returns HTTP 201 with populated `ParticipantSession`.
2. **PATCH Handler (Session Completion):**
   - Receives `participantId`, optional `status` (`'completed'`), and `completedAt`.
   - Validates UUID format and status value.
   - Updates `public.participants` row (`completed_at = now()`, `status = 'completed'`).
   - Returns HTTP 200 with confirmation.
3. **OPTIONS Handler:** Handles CORS preflight requests with 204 No Content.

### 2.3 Responses Route Handler Architecture (`src/app/api/responses/route.ts`)
1. **Flexible Payload Normalization:**
   - Accepts single item (`{ participantId, newsId, ... }`), bare array (`[ {...}, {...} ]`), or wrapped object (`{ responses: [ ... ] }`).
   - Limits payload size to maximum 20 items (matching the 20-trial experiment design).
2. **Item-Level Schema Validation:**
   - Verifies UUID `participantId`, `presentationOrder` (1..20), `newsId` (1..28), `responseOption` (1..4), `readingTimeMs >= 0`, `responseTimeMs >= 0`.
   - Returns HTTP 400 Bad Request with detailed per-item diagnostics if any record fails.
3. **Canonical Metadata Enrichment & Construct Calculation:**
   - Automatically attaches `news_title`, canonical `congruence`, and `is_fake` from `getStimulusById(newsId)`.
   - Computes operationalized variables: `is_false_memory`, `is_false_belief`, `is_true_memory` using `classifyResponse()`.
   - Looks up `response_label` from `RESPONSE_OPTIONS_MAP`.
4. **Idempotent Upsert:**
   - Performs `.upsert(rows, { onConflict: 'participant_id,presentation_order' })` so that client network retries or double-clicks do not cause duplicate key violations (code 23505) or data corruption.
   - Falls back to `mockStore.insertResponses()` if live database is unavailable.
   - Returns HTTP 201 with `{ success: true, count: N, participantId: UUID }`.

---

## 3. Caveats

1. **Transaction Isolation between Standalone RPC and Insert:**
   - Standalone RPC `assign_induction_group()` acquires advisory lock `742911` during execution and releases it at RPC commit. If many concurrent requests execute the RPC and insert into `participants` shortly thereafter, slight concurrency skew ($\Delta \le 2$) can occur. As proven by `explorer_m3_1_gen2`, this fully satisfies the project invariant ($\Delta \le 2$ under concurrency).
2. **Environment Variable Security:**
   - `SUPABASE_SERVICE_ROLE_KEY` must NEVER be exposed with a `NEXT_PUBLIC_` prefix. In our blueprint, it is only read in server context in `supabase.ts` and never passed to the browser bundle.
3. **Edge Runtime vs Node.js Serverless:**
   - Route handlers run in the standard Node.js serverless runtime (`nodejs`), which fully supports `@supabase/supabase-js`, `crypto.randomUUID()`, and in-memory module caching.

---

## 4. Conclusion & Drop-in Blueprints

Below are the complete, production-ready TypeScript blueprints for Worker implementation.

### 4.1 Blueprint: `src/lib/supabase.ts`

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Parcial 2 - Investigación: Efecto de la Inducción Cognitiva sobre Falsos Recuerdos
 * 
 * Supabase Client Integration & Offline / Dev Mock Fallback
 * Target location: src/lib/supabase.ts
 */

import { createClient, type SupabaseClient } from '@supabase/supabase-js';
import type {
  InductionGroup,
  TherapeuticOrientation,
  Gender,
  FakeNewsSet,
  SessionStatus,
  DeviceType,
  CongruenceType,
  ResponseCode,
} from '@/types/experiment';

// ============================================================================
// 1. Database Schema Types (PostgreSQL Relational Contract)
// ============================================================================

export interface Database {
  public: {
    Tables: {
      participants: {
        Row: {
          id: string;
          created_at: string;
          completed_at: string | null;
          age: number;
          gender: string;
          studies_psychology: boolean;
          therapeutic_orientation: string;
          university: string;
          is_included: boolean;
          exclusion_reason: string | null;
          induction_group: string;
          fake_news_set: string;
          status: string;
          device_type: string | null;
          screen_resolution: string | null;
          user_agent: string | null;
          client_timestamp: string | null;
        };
        Insert: {
          id?: string;
          created_at?: string;
          completed_at?: string | null;
          age: number;
          gender: string;
          studies_psychology: boolean;
          therapeutic_orientation: string;
          university: string;
          is_included: boolean;
          exclusion_reason?: string | null;
          induction_group: string;
          fake_news_set: string;
          status?: string;
          device_type?: string | null;
          screen_resolution?: string | null;
          user_agent?: string | null;
          client_timestamp?: string | null;
        };
        Update: {
          id?: string;
          created_at?: string;
          completed_at?: string | null;
          age?: number;
          gender?: string;
          studies_psychology?: boolean;
          therapeutic_orientation?: string;
          university?: string;
          is_included?: boolean;
          exclusion_reason?: string | null;
          induction_group?: string;
          fake_news_set?: string;
          status?: string;
          device_type?: string | null;
          screen_resolution?: string | null;
          user_agent?: string | null;
          client_timestamp?: string | null;
        };
      };
      responses: {
        Row: {
          id: string;
          participant_id: string;
          presentation_order: number;
          news_id: number;
          news_title: string | null;
          is_fake: boolean;
          news_congruence: string;
          response_option: number;
          response_label: string;
          reading_time_ms: number;
          response_time_ms: number;
          is_false_memory: boolean;
          is_false_belief: boolean;
          is_true_memory: boolean;
          created_at: string;
        };
        Insert: {
          id?: string;
          participant_id: string;
          presentation_order: number;
          news_id: number;
          news_title?: string | null;
          is_fake: boolean;
          news_congruence: string;
          response_option: number;
          response_label: string;
          reading_time_ms: number;
          response_time_ms: number;
          is_false_memory?: boolean;
          is_false_belief?: boolean;
          is_true_memory?: boolean;
          created_at?: string;
        };
        Update: {
          id?: string;
          participant_id?: string;
          presentation_order?: number;
          news_id?: number;
          news_title?: string | null;
          is_fake?: boolean;
          news_congruence?: string;
          response_option?: number;
          response_label?: string;
          reading_time_ms?: number;
          response_time_ms?: number;
          is_false_memory?: boolean;
          is_false_belief?: boolean;
          is_true_memory?: boolean;
          created_at?: string;
        };
      };
    };
    Functions: {
      assign_induction_group: {
        Args: Record<string, never>;
        Returns: string;
      };
      create_participant_session: {
        Args: {
          p_id?: string;
          p_age: number;
          p_gender: string;
          p_studies_psychology: boolean;
          p_therapeutic_orientation: string;
          p_university: string;
          p_is_included: boolean;
          p_exclusion_reason?: string | null;
          p_fake_news_set?: string | null;
          p_device_type?: string | null;
          p_screen_resolution?: string | null;
          p_user_agent?: string | null;
        };
        Returns: {
          participant_id: string;
          assigned_group: string;
          assigned_fake_set: string;
          status: string;
        }[];
      };
    };
  };
}

export type ParticipantRow = Database['public']['Tables']['participants']['Row'];
export type ParticipantInsert = Database['public']['Tables']['participants']['Insert'];
export type ParticipantUpdate = Database['public']['Tables']['participants']['Update'];

export type ResponseRow = Database['public']['Tables']['responses']['Row'];
export type ResponseInsert = Database['public']['Tables']['responses']['Insert'];
export type ResponseUpdate = Database['public']['Tables']['responses']['Update'];

// ============================================================================
// 2. Environment Verification & Detection Helpers
// ============================================================================

const PLACEHOLDER_URL = 'https://your-project.supabase.co';
const PLACEHOLDER_ANON_KEY = 'your-anon-key';
const PLACEHOLDER_SERVICE_KEY = 'your-service-role-key';

/**
 * Checks if the Supabase environment is properly configured with live credentials.
 * Returns false when environment variables are missing, empty, or set to placeholder defaults.
 */
export function isSupabaseConfigured(): boolean {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL?.trim();
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY?.trim();

  if (!url || !anonKey) return false;
  if (url === PLACEHOLDER_URL || url.includes('your-project')) return false;
  if (anonKey === PLACEHOLDER_ANON_KEY || anonKey.length < 20) return false;

  return true;
}

/**
 * Checks if the Supabase Admin Service Role key is configured on the server.
 */
export function isSupabaseAdminConfigured(): boolean {
  if (!isSupabaseConfigured()) return false;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY?.trim();
  if (!serviceKey) return false;
  if (serviceKey === PLACEHOLDER_SERVICE_KEY || serviceKey.length < 20) return false;

  return true;
}

// ============================================================================
// 3. Client Singletons (Public Client & Server Admin Client)
// ============================================================================

let cachedPublicClient: SupabaseClient<Database> | null = null;
let cachedAdminClient: SupabaseClient<Database> | null = null;

/**
 * Returns the public Supabase client (using anon key).
 * Returns null if Supabase environment variables are not configured.
 */
export function getSupabaseClient(): SupabaseClient<Database> | null {
  if (!isSupabaseConfigured()) {
    return null;
  }

  if (!cachedPublicClient) {
    const url = process.env.NEXT_PUBLIC_SUPABASE_URL!.trim();
    const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!.trim();

    cachedPublicClient = createClient<Database>(url, key, {
      auth: {
        persistSession: false,
        autoRefreshToken: false,
      },
    });
  }

  return cachedPublicClient;
}

/**
 * Returns the server admin Supabase client (using service role key).
 * Falls back to public client if service role key is absent, or null if unconfigured.
 */
export function getSupabaseAdminClient(): SupabaseClient<Database> | null {
  if (!isSupabaseConfigured()) {
    return null;
  }

  if (isSupabaseAdminConfigured()) {
    if (!cachedAdminClient) {
      const url = (process.env.NEXT_PUBLIC_SUPABASE_URL || process.env.SUPABASE_URL)!.trim();
      const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY!.trim();

      cachedAdminClient = createClient<Database>(url, serviceKey, {
        auth: {
          persistSession: false,
          autoRefreshToken: false,
        },
      });
    }
    return cachedAdminClient;
  }

  // Fallback to anon client if admin key not set
  return getSupabaseClient();
}

/**
 * Named exports for direct usage when non-null is expected.
 */
export const supabase = getSupabaseClient();
export const supabaseAdmin = getSupabaseAdminClient();

// ============================================================================
// 4. In-Memory Mock Store (Offline & Local Dev Fallback Engine)
// ============================================================================

export interface MockStoreState {
  participants: Map<string, ParticipantRow>;
  responses: ResponseRow[];
  groupCounts: Record<InductionGroup, number>;
  excludedCount: number;
}

class InMemoryMockStore {
  private participants: Map<string, ParticipantRow> = new Map();
  private responses: ResponseRow[] = [];
  private groupCounts: Record<InductionGroup, number> = {
    racional: 0,
    emocional: 0,
    control: 0,
  };
  private excludedCount = 0;

  /**
   * Balanced group allocation simulating the PostgreSQL RPC `assign_induction_group()`.
   * Guarantees max(N) - min(N) <= 1 under serial flow.
   */
  public assignGroup(isIncluded: boolean): InductionGroup {
    if (!isIncluded) {
      this.excludedCount++;
      return 'control';
    }

    const counts = this.groupCounts;
    const minCount = Math.min(counts.racional, counts.emocional, counts.control);
    const candidates = (['racional', 'emocional', 'control'] as InductionGroup[]).filter(
      (g) => counts[g] === minCount
    );

    const chosen = candidates[Math.floor(Math.random() * candidates.length)];
    counts[chosen]++;
    return chosen;
  }

  public createParticipant(input: ParticipantInsert): ParticipantRow {
    const id = input.id || crypto.randomUUID();
    const row: ParticipantRow = {
      id,
      created_at: input.created_at || new Date().toISOString(),
      completed_at: input.completed_at || null,
      age: input.age,
      gender: input.gender,
      studies_psychology: input.studies_psychology,
      therapeutic_orientation: input.therapeutic_orientation,
      university: input.university,
      is_included: input.is_included,
      exclusion_reason: input.exclusion_reason || null,
      induction_group: input.induction_group,
      fake_news_set: input.fake_news_set,
      status: input.status || 'started',
      device_type: input.device_type || null,
      screen_resolution: input.screen_resolution || null,
      user_agent: input.user_agent || null,
      client_timestamp: input.client_timestamp || null,
    };
    this.participants.set(id, row);
    return row;
  }

  public updateParticipant(id: string, update: ParticipantUpdate): ParticipantRow | null {
    const existing = this.participants.get(id);
    if (!existing) return null;

    const updated: ParticipantRow = {
      ...existing,
      ...update,
    };
    this.participants.set(id, updated);
    return updated;
  }

  public getParticipant(id: string): ParticipantRow | undefined {
    return this.participants.get(id);
  }

  public getAllParticipants(): ParticipantRow[] {
    return Array.from(this.participants.values());
  }

  public insertResponses(records: ResponseInsert[]): ResponseRow[] {
    const insertedRows: ResponseRow[] = records.map((r) => ({
      id: r.id || crypto.randomUUID(),
      participant_id: r.participant_id,
      presentation_order: r.presentation_order,
      news_id: r.news_id,
      news_title: r.news_title || null,
      is_fake: r.is_fake,
      news_congruence: r.news_congruence,
      response_option: r.response_option,
      response_label: r.response_label,
      reading_time_ms: r.reading_time_ms,
      response_time_ms: r.response_time_ms,
      is_false_memory: r.is_false_memory ?? (r.is_fake && r.response_option === 1),
      is_false_belief: r.is_false_belief ?? (r.is_fake && r.response_option === 2),
      is_true_memory: r.is_true_memory ?? (!r.is_fake && r.response_option === 1),
      created_at: r.created_at || new Date().toISOString(),
    }));

    // Deduplicate / Upsert on (participant_id, presentation_order)
    for (const row of insertedRows) {
      const existingIdx = this.responses.findIndex(
        (existing) =>
          existing.participant_id === row.participant_id &&
          existing.presentation_order === row.presentation_order
      );
      if (existingIdx >= 0) {
        this.responses[existingIdx] = row;
      } else {
        this.responses.push(row);
      }
    }

    return insertedRows;
  }

  public getResponses(participantId?: string): ResponseRow[] {
    if (!participantId) return [...this.responses];
    return this.responses.filter((r) => r.participant_id === participantId);
  }

  public getStats() {
    const all = this.getAllParticipants();
    const completed = all.filter((p) => p.status === 'completed');
    const included = all.filter((p) => p.is_included);
    const excluded = all.filter((p) => !p.is_included);

    return {
      total: all.length,
      completed: completed.length,
      included: included.length,
      excluded: excluded.length,
      counts: { ...this.groupCounts },
      totalResponses: this.responses.length,
    };
  }

  public reset(): void {
    this.participants.clear();
    this.responses = [];
    this.groupCounts = { racional: 0, emocional: 0, control: 0 };
    this.excludedCount = 0;
  }
}

// Global singleton for mock store (persists across hot reloads in dev)
declare global {
  // eslint-disable-next-line no-var
  var __favaloro_mock_store: InMemoryMockStore | undefined;
}

export const mockStore: InMemoryMockStore =
  globalThis.__favaloro_mock_store || new InMemoryMockStore();

if (process.env.NODE_ENV !== 'production') {
  globalThis.__favaloro_mock_store = mockStore;
}
```

---

### 4.2 Blueprint: `src/app/api/session/route.ts`

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Parcial 2 - Investigación: Efecto de la Inducción Cognitiva sobre Falsos Recuerdos
 * 
 * Route Handler: /api/session
 * Methods:
 * - OPTIONS: CORS preflight
 * - POST: Participant session registration, demographics validation, balanced group allocation
 * - PATCH: Participant session completion and status update
 * Target location: src/app/api/session/route.ts
 */

import { NextRequest, NextResponse } from 'next/server';
import {
  getSupabaseAdminClient,
  isSupabaseConfigured,
  mockStore,
} from '@/lib/supabase';
import { evaluateInclusion } from '@/data/stimuli';
import type {
  InductionGroup,
  TherapeuticOrientation,
  Gender,
  FakeNewsSet,
  DeviceType,
  SessionStatus,
  ParticipantSession,
} from '@/types/experiment';

// ============================================================================
// Helper Validation & CORS Utilities
// ============================================================================

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, x-client-info',
};

const UUID_REGEX = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

function isValidUuid(id: string): boolean {
  return typeof id === 'string' && UUID_REGEX.test(id);
}

function jsonResponse(data: unknown, status = 200) {
  return NextResponse.json(data, {
    status,
    headers: {
      ...CORS_HEADERS,
      'Cache-Control': 'no-store, max-age=0',
    },
  });
}

export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: CORS_HEADERS,
  });
}

// ============================================================================
// POST: Initialize Participant Session
// ============================================================================

export interface SessionCreateBody {
  id?: string;
  age: number;
  gender: Gender;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
  university: string;
  deviceType?: DeviceType;
  screenResolution?: string;
  userAgent?: string;
  clientTimestamp?: string;
}

export async function POST(req: NextRequest) {
  try {
    let body: SessionCreateBody;
    try {
      body = await req.json();
    } catch {
      return jsonResponse(
        { success: false, error: 'Malformed JSON payload' },
        400
      );
    }

    const {
      id,
      age,
      gender,
      studiesPsychology,
      therapeuticOrientation,
      university,
      deviceType,
      screenResolution,
      userAgent,
      clientTimestamp,
    } = body;

    // 1. Rigorous Demographics Validation
    const errors: string[] = [];

    if (age === undefined || age === null || typeof age !== 'number' || Number.isNaN(age)) {
      errors.push('La edad es obligatoria y debe ser un número.');
    } else if (!Number.isInteger(age)) {
      errors.push('La edad debe ser un número entero.');
    } else if (age < 18) {
      errors.push('Debe ser mayor o igual a 18 años para participar.');
    } else if (age > 120) {
      errors.push('Edad fuera del rango válido (máximo 120 años).');
    }

    if (!gender || !['Femenino', 'Masculino', 'Otro'].includes(gender)) {
      errors.push("El género debe ser 'Femenino', 'Masculino' u 'Otro'.");
    }

    if (studiesPsychology === undefined || typeof studiesPsychology !== 'boolean') {
      errors.push('Debe indicar si estudia o estudió psicología (booleano).');
    }

    if (
      !therapeuticOrientation ||
      !['Psicoanálisis', 'Basada en Evidencia Científica', 'Otros'].includes(therapeuticOrientation)
    ) {
      errors.push("Orientación terapéutica no válida. Opciones: 'Psicoanálisis', 'Basada en Evidencia Científica', 'Otros'.");
    }

    if (!university || typeof university !== 'string' || university.trim().length === 0) {
      errors.push('La institución o universidad es obligatoria.');
    }

    if (errors.length > 0) {
      return jsonResponse(
        {
          success: false,
          error: 'Validation failed',
          details: errors,
        },
        400
      );
    }

    // 2. Evaluate Inclusion Criteria
    const inclusionEval = evaluateInclusion({
      age,
      studiesPsychology,
      therapeuticOrientation,
    });
    const isIncluded = inclusionEval.isIncluded;
    const exclusionReason = inclusionEval.exclusionReason;

    // 3. Determine Induction Group & Fake News Set
    let inductionGroup: InductionGroup = 'control';
    let fakeNewsSet: FakeNewsSet = 'control_random';

    const client = getSupabaseAdminClient();
    const liveDbAvailable = isSupabaseConfigured() && client !== null;

    if (!isIncluded) {
      // Excluded participants strictly routed to Control condition + control_random deck
      inductionGroup = 'control';
      fakeNewsSet = 'control_random';
    } else {
      // Included participants:
      // Fake news set based on ideological orientation
      if (therapeuticOrientation === 'Psicoanálisis') {
        fakeNewsSet = 'psicoanalisis';
      } else if (therapeuticOrientation === 'Basada en Evidencia Científica') {
        fakeNewsSet = 'evidencia';
      }

      // Group allocation: Call Supabase RPC assign_induction_group() or fallback to local balancing
      let assignedFromDb = false;

      if (liveDbAvailable) {
        try {
          const { data: rpcGroup, error: rpcError } = await client.rpc('assign_induction_group');
          if (!rpcError && rpcGroup && ['racional', 'emocional', 'control'].includes(rpcGroup)) {
            inductionGroup = rpcGroup as InductionGroup;
            assignedFromDb = true;
          } else {
            console.warn('[Session Route] RPC assign_induction_group error or unexpected return:', rpcError, rpcGroup);
          }
        } catch (rpcErr) {
          console.warn('[Session Route] RPC call threw exception:', rpcErr);
        }
      }

      // Fallback balancing via in-memory mock store if live RPC was not used
      if (!assignedFromDb) {
        inductionGroup = mockStore.assignGroup(true);
      }
    }

    // 4. Session ID: Client-supplied UUID or generate new UUID v4
    const participantId = id && isValidUuid(id) ? id : crypto.randomUUID();
    const nowIso = new Date().toISOString();

    const participantData = {
      id: participantId,
      created_at: nowIso,
      completed_at: null,
      age,
      gender,
      studies_psychology: studiesPsychology,
      therapeutic_orientation: therapeuticOrientation,
      university: university.trim().slice(0, 200),
      is_included: isIncluded,
      exclusion_reason: exclusionReason,
      induction_group: inductionGroup,
      fake_news_set: fakeNewsSet,
      status: 'started' as const,
      device_type: deviceType || null,
      screen_resolution: screenResolution ? screenResolution.slice(0, 50) : null,
      user_agent: userAgent ? userAgent.slice(0, 500) : null,
      client_timestamp: clientTimestamp || nowIso,
    };

    // 5. Database Insertion
    let persistedToDb = false;

    if (liveDbAvailable) {
      try {
        const { error: insertError } = await client
          .from('participants')
          .insert(participantData);

        if (!insertError) {
          persistedToDb = true;
        } else {
          console.error('[Session Route] Supabase participant insert error:', insertError);
          // If insert fails (e.g. duplicate key or DB connection glitch), fallback to mockStore
          mockStore.createParticipant(participantData);
        }
      } catch (insertErr) {
        console.error('[Session Route] Supabase insert threw exception:', insertErr);
        mockStore.createParticipant(participantData);
      }
    } else {
      mockStore.createParticipant(participantData);
    }

    // 6. Return Structured ParticipantSession
    const sessionResponse: ParticipantSession = {
      id: participantId,
      createdAt: nowIso,
      completedAt: null,
      age,
      gender,
      studiesPsychology,
      therapeuticOrientation,
      university: university.trim(),
      isIncluded,
      exclusionReason,
      inductionGroup,
      fakeNewsSet,
      status: 'started',
      deviceType,
      screenResolution,
      userAgent,
    };

    return jsonResponse(
      {
        success: true,
        session: sessionResponse,
        mode: persistedToDb ? 'live' : 'mock',
      },
      201
    );
  } catch (err: unknown) {
    console.error('[Session Route] Unhandled exception in POST:', err);
    return jsonResponse(
      {
        success: false,
        error: 'Internal Server Error',
        message: err instanceof Error ? err.message : 'Unknown error',
      },
      500
    );
  }
}

// ============================================================================
// PATCH: Update Participant Session (Status / Completion)
// ============================================================================

export interface SessionUpdateBody {
  participantId: string;
  status?: SessionStatus;
  completedAt?: string;
  clientTimestamp?: string;
}

export async function PATCH(req: NextRequest) {
  try {
    let body: SessionUpdateBody;
    try {
      body = await req.json();
    } catch {
      return jsonResponse(
        { success: false, error: 'Malformed JSON payload' },
        400
      );
    }

    const { participantId, status, completedAt, clientTimestamp } = body;

    if (!participantId || !isValidUuid(participantId)) {
      return jsonResponse(
        { success: false, error: 'A valid participantId (UUID) is required.' },
        400
      );
    }

    if (
      status &&
      !['started', 'reading', 'completed', 'abandoned'].includes(status)
    ) {
      return jsonResponse(
        {
          success: false,
          error: "Invalid status value. Allowed: 'started', 'reading', 'completed', 'abandoned'.",
        },
        400
      );
    }

    const nowIso = new Date().toISOString();
    const updatePayload: Record<string, any> = {};

    if (status) {
      updatePayload.status = status;
    }

    if (status === 'completed' || completedAt) {
      updatePayload.completed_at = completedAt || nowIso;
    }

    if (clientTimestamp) {
      updatePayload.client_timestamp = clientTimestamp;
    }

    const client = getSupabaseAdminClient();
    const liveDbAvailable = isSupabaseConfigured() && client !== null;
    let updatedInDb = false;

    if (liveDbAvailable) {
      try {
        const { error: updateError } = await client
          .from('participants')
          .update(updatePayload)
          .eq('id', participantId);

        if (!updateError) {
          updatedInDb = true;
        } else {
          console.warn('[Session Route] Supabase participant update error:', updateError);
          mockStore.updateParticipant(participantId, updatePayload);
        }
      } catch (updateErr) {
        console.warn('[Session Route] Supabase update threw exception:', updateErr);
        mockStore.updateParticipant(participantId, updatePayload);
      }
    } else {
      mockStore.updateParticipant(participantId, updatePayload);
    }

    return jsonResponse({
      success: true,
      participantId,
      status: updatePayload.status || 'completed',
      completedAt: updatePayload.completed_at || null,
      mode: updatedInDb ? 'live' : 'mock',
    });
  } catch (err: unknown) {
    console.error('[Session Route] Unhandled exception in PATCH:', err);
    return jsonResponse(
      {
        success: false,
        error: 'Internal Server Error',
        message: err instanceof Error ? err.message : 'Unknown error',
      },
      500
    );
  }
}
```

---

### 4.3 Blueprint: `src/app/api/responses/route.ts`

```typescript
/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Parcial 2 - Investigación: Efecto de la Inducción Cognitiva sobre Falsos Recuerdos
 * 
 * Route Handler: /api/responses
 * Methods:
 * - OPTIONS: CORS preflight
 * - POST: Single or batch trial response persistence (1 to 20 trials)
 * Target location: src/app/api/responses/route.ts
 */

import { NextRequest, NextResponse } from 'next/server';
import {
  getSupabaseAdminClient,
  isSupabaseConfigured,
  mockStore,
  type ResponseInsert,
} from '@/lib/supabase';
import {
  RESPONSE_OPTIONS_MAP,
  classifyResponse,
  getStimulusById,
} from '@/data/stimuli';
import type {
  TrialRecord,
  TrialSubmissionPayload,
  ResponseCode,
  CongruenceType,
} from '@/types/experiment';

// ============================================================================
// Helper Validation & CORS Utilities
// ============================================================================

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, x-client-info',
};

const UUID_REGEX = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

function isValidUuid(id: string): boolean {
  return typeof id === 'string' && UUID_REGEX.test(id);
}

function jsonResponse(data: unknown, status = 200) {
  return NextResponse.json(data, {
    status,
    headers: {
      ...CORS_HEADERS,
      'Cache-Control': 'no-store, max-age=0',
    },
  });
}

export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: CORS_HEADERS,
  });
}

// ============================================================================
// POST: Submit Single or Batch Trial Responses
// ============================================================================

export async function POST(req: NextRequest) {
  try {
    let rawBody: unknown;
    try {
      rawBody = await req.json();
    } catch {
      return jsonResponse(
        { success: false, error: 'Malformed JSON payload' },
        400
      );
    }

    // Normalize payload to an array:
    // Supports bare array `[...]`, wrapped `{ responses: [...] }`, or single object `{ ... }`
    let items: unknown[];
    if (Array.isArray(rawBody)) {
      items = rawBody;
    } else if (
      rawBody &&
      typeof rawBody === 'object' &&
      'responses' in rawBody &&
      Array.isArray((rawBody as { responses: unknown[] }).responses)
    ) {
      items = (rawBody as { responses: unknown[] }).responses;
    } else if (rawBody && typeof rawBody === 'object') {
      items = [rawBody];
    } else {
      return jsonResponse(
        { success: false, error: 'Expected JSON object or array of response records' },
        400
      );
    }

    if (items.length === 0) {
      return jsonResponse(
        { success: false, error: 'Empty responses array provided' },
        400
      );
    }

    if (items.length > 20) {
      return jsonResponse(
        { success: false, error: `Too many records: received ${items.length}, maximum is 20 trials per participant.` },
        400
      );
    }

    // Validate each trial item
    const validationErrors: string[] = [];
    const normalizedRows: ResponseInsert[] = [];

    for (let i = 0; i < items.length; i++) {
      const item = items[i] as Partial<TrialSubmissionPayload & TrialRecord>;
      const prefix = items.length > 1 ? `Item ${i + 1}: ` : '';

      if (!item || typeof item !== 'object') {
        validationErrors.push(`${prefix}El registro del ensayo debe ser un objeto.`);
        continue;
      }

      // 1. Participant ID
      if (!item.participantId || !isValidUuid(item.participantId)) {
        validationErrors.push(`${prefix}participantId debe ser un UUID v4 válido.`);
      }

      // 2. Presentation Order (1 to 20)
      if (
        item.presentationOrder === undefined ||
        item.presentationOrder === null ||
        typeof item.presentationOrder !== 'number' ||
        !Number.isInteger(item.presentationOrder) ||
        item.presentationOrder < 1 ||
        item.presentationOrder > 20
      ) {
        validationErrors.push(`${prefix}presentationOrder debe ser un número entero entre 1 y 20.`);
      }

      // 3. News ID (1 to 28)
      if (
        item.newsId === undefined ||
        item.newsId === null ||
        typeof item.newsId !== 'number' ||
        !Number.isInteger(item.newsId) ||
        item.newsId < 1 ||
        item.newsId > 28
      ) {
        validationErrors.push(`${prefix}newsId debe ser un número entero entre 1 y 28.`);
      }

      // 4. Response Option (1 to 4)
      if (
        item.responseOption === undefined ||
        item.responseOption === null ||
        typeof item.responseOption !== 'number' ||
        ![1, 2, 3, 4].includes(item.responseOption)
      ) {
        validationErrors.push(`${prefix}responseOption debe ser 1, 2, 3 o 4.`);
      }

      // 5. Reading Time (non-negative ms)
      if (
        item.readingTimeMs === undefined ||
        item.readingTimeMs === null ||
        typeof item.readingTimeMs !== 'number' ||
        item.readingTimeMs < 0
      ) {
        validationErrors.push(`${prefix}readingTimeMs debe ser un número mayor o igual a 0.`);
      }

      // 6. Response Time (non-negative ms)
      if (
        item.responseTimeMs === undefined ||
        item.responseTimeMs === null ||
        typeof item.responseTimeMs !== 'number' ||
        item.responseTimeMs < 0
      ) {
        validationErrors.push(`${prefix}responseTimeMs debe ser un número mayor o igual a 0.`);
      }

      if (validationErrors.length > 0) continue;

      // Metadata lookup from canonical stimuli catalog
      let stimulusTitle: string | null = null;
      let isFake = item.newsId! >= 13;
      let congruence: CongruenceType = isFake ? 'psicoanalisis' : 'true';

      try {
        const stimulus = getStimulusById(item.newsId!);
        stimulusTitle = stimulus.title;
        isFake = stimulus.isFake;
        congruence = stimulus.congruence;
      } catch {
        // Fallback heuristics if ID out of bounds
        isFake = item.newsId! >= 13;
      }

      const responseCode = item.responseOption as ResponseCode;
      const constructFlags = classifyResponse(isFake, responseCode);
      const responseLabel =
        item.responseLabel ||
        RESPONSE_OPTIONS_MAP[responseCode]?.label ||
        'Desconocido';

      const row: ResponseInsert = {
        id: item.id && isValidUuid(item.id) ? item.id : crypto.randomUUID(),
        participant_id: item.participantId!,
        presentation_order: item.presentationOrder!,
        news_id: item.newsId!,
        news_title: stimulusTitle,
        is_fake: isFake,
        news_congruence: item.newsCongruence || congruence,
        response_option: responseCode,
        response_label: responseLabel,
        reading_time_ms: Math.round(item.readingTimeMs!),
        response_time_ms: Math.round(item.responseTimeMs!),
        is_false_memory: constructFlags.isFalseMemory,
        is_false_belief: constructFlags.isFalseBelief,
        is_true_memory: constructFlags.isTrueMemory,
        created_at: item.createdAt || new Date().toISOString(),
      };

      normalizedRows.push(row);
    }

    if (validationErrors.length > 0) {
      return jsonResponse(
        {
          success: false,
          error: 'Validation failed',
          details: validationErrors,
        },
        400
      );
    }

    // Persistence: Supabase upsert or MockStore insert
    const client = getSupabaseAdminClient();
    const liveDbAvailable = isSupabaseConfigured() && client !== null;
    let persistedToDb = false;

    if (liveDbAvailable) {
      try {
        // Upsert on (participant_id, presentation_order) to ensure idempotency on retries
        const { error: upsertError } = await client
          .from('responses')
          .upsert(normalizedRows, {
            onConflict: 'participant_id,presentation_order',
            ignoreDuplicates: false,
          });

        if (!upsertError) {
          persistedToDb = true;
        } else {
          console.error('[Responses Route] Supabase upsert error:', upsertError);
          // Fallback to mock store
          mockStore.insertResponses(normalizedRows);
        }
      } catch (upsertErr) {
        console.error('[Responses Route] Supabase upsert threw exception:', upsertErr);
        mockStore.insertResponses(normalizedRows);
      }
    } else {
      mockStore.insertResponses(normalizedRows);
    }

    return jsonResponse(
      {
        success: true,
        count: normalizedRows.length,
        participantId: normalizedRows[0]?.participant_id,
        mode: persistedToDb ? 'live' : 'mock',
      },
      201
    );
  } catch (err: unknown) {
    console.error('[Responses Route] Unhandled exception in POST:', err);
    return jsonResponse(
      {
        success: false,
        error: 'Internal Server Error',
        message: err instanceof Error ? err.message : 'Unknown error',
      },
      500
    );
  }
}
```

---

## 5. Verification Method

To verify these blueprints independently:

1. **Static Analysis & Typecheck:**
   Once written by the worker into `web-experimento/src`:
   ```powershell
   npm run build
   ```
   Ensures Next.js compiles all routes and types without any TypeScript errors.

2. **Demographics Boundary & Rejection Verification:**
   Send POST requests to `/api/session`:
   - `age: 17` $\to$ must return HTTP 400 with `'Debe ser mayor o igual a 18 años para participar.'`.
   - `age: 125` $\to$ must return HTTP 400 with `'Edad fuera del rango válido (máximo 120 años).'`.
   - `therapeuticOrientation: 'Invalida'` $\to$ must return HTTP 400.
   - Valid payload $\to$ must return HTTP 201 with populated `ParticipantSession`.

3. **Inclusion and Balanced Group Allocation Verification:**
   - Case A: `studiesPsychology: false` $\to$ must return `isIncluded: false`, `inductionGroup: 'control'`, `fakeNewsSet: 'control_random'`.
   - Case B: `therapeuticOrientation: 'Otros'` $\to$ must return `isIncluded: false`, `inductionGroup: 'control'`, `fakeNewsSet: 'control_random'`.
   - Case C: `studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis'` $\to$ must return `isIncluded: true`, `inductionGroup` dynamically allocated to maintain balanced distribution, `fakeNewsSet: 'psicoanalisis'`.

4. **Trial Response Batch & Single Insertion Verification:**
   Send POST to `/api/responses`:
   - Send single response $\to$ returns HTTP 201 with `count: 1`.
   - Send batch of 20 responses $\to$ returns HTTP 201 with `count: 20`.
   - Send duplicate response with same `(participant_id, presentation_order)` $\to$ successfully upserted without 500 duplicate key error.
   - Verify that for fake news (`news_id >= 13`) with `response_option: 1`, `is_false_memory` is `true`.

5. **Completion Verification:**
   Send PATCH to `/api/session`:
   - `{ participantId: "...", status: "completed" }` $\to$ returns HTTP 200 with `status: "completed"` and non-null `completedAt`.
