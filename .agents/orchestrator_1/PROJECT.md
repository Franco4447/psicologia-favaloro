# Project: Plataforma Web de Psicología Experimental - Creación de Falsos Recuerdos y Creencias

**Institución**: Universidad Favaloro  
**Cátedra**: Psicología Experimental (2do Año) - Parcial 2 Investigación  
**Objetivo**: Plataforma web académica para evaluar el efecto de la inducción cognitiva (emocional, racional, control) sobre la creación de falsos recuerdos y falsas creencias ante fake news congruentes con creencias previas (psicoanálisis vs. basada en evidencia).  
**Directorio Base**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`

---

## Architecture

### System Overview
- **Frontend / Application Framework**: Next.js 14+ (App Router), React 18, TypeScript, Tailwind CSS, Lucide React icons.
- **Backend / API**: Next.js Server Route Handlers (`/api/session`, `/api/responses`, `/api/admin/login`, `/api/admin/stats`, `/api/admin/export-csv`).
- **Database & RPC**: Supabase PostgreSQL. Tables: `participants`, `responses`. Stored Procedure / RPC: `assign_induction_group()` using `pg_advisory_xact_lock` to strictly guarantee balanced distribution ($\Delta \le 1$ under serial flow, $\le 2$ under concurrent requests).
- **Client Timing Engine**: `performance.now()` for millisecond-precision reaction time measurement and 10,000 ms forced stimulus exposure with CSS visual countdown progress bar.
- **Admin Dashboard**: Route `/admin`, guarded with secure password authentication (HTTP-only signed cookie), participant overview, balance monitor, and UTF-8 BOM CSV export (20 rows per participant).
- **Deployment & Hosting**: Vercel (free tier HTTPS) and GitHub repository (`Franco4447/psicologia-favaloro` monorepo configuration with root directory pointing to `web-experimento`).

---

## Feature Inventory

Every feature discovered during the Phase 0 Survey is mapped to an implementation milestone below:

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Welcome & Presentation Screen | Academic landing screen presenting the Universidad Favaloro study, instructions, quiet-time notice. | M2 | Survey / ORIGINAL_REQUEST §5.1 |
| 2 | Mandatory Informed Consent | Informed consent screen with mandatory checkbox before proceeding. | M2 | Survey / ORIGINAL_REQUEST §5.2 |
| 3 | Demographics Collection Form | Form capturing age (>=18), sex, psychology student status, therapeutic orientation, university. | M2 | Survey / ORIGINAL_REQUEST §5.3 |
| 4 | Inclusion / Exclusion Logic | Screening logic: studies psychology + (Psychoanalysis or Evidence-Based) -> included; otherwise excluded. | M2 | Survey / ORIGINAL_REQUEST §5.4 |
| 5 | Balanced Group Allocation | Server-side balanced randomization ensuring difference between induction groups <= 2 at all times. | M3 | Survey / ORIGINAL_REQUEST §R2 |
| 6 | Excluded Participant Routing | Excluded participants receive Control prompt + cohesive fake news set, marked `is_included=false` without quota skew. | M2 / M3 | Survey / ORIGINAL_REQUEST §5.4 |
| 7 | Ideological Congruence Engine | Maps therapeutic orientation to 8 congruent fake news (attacking opposing current). | M1 / M2 | Survey / ORIGINAL_REQUEST §5.6 |
| 8 | Cognitive Induction Priming Screen | Displays verbatim Racional, Emocional, or Control induction prompt based on assigned group. | M2 | Survey / ORIGINAL_REQUEST §5.5 |
| 9 | 20-Trial Stimulus Randomizer | Combines 12 true news + 8 assigned fake news, randomized with Fisher-Yates per participant. | M1 / M2 | Survey / ORIGINAL_REQUEST §5.6 |
| 10 | 10s Stimulus Exposure Display | Banner headline image displayed for 10.0s with visual progress bar and automatic advance. | M2 | Survey / ORIGINAL_REQUEST §5.6 |
| 11 | Asset Extension Resolver | Robust image asset handling supporting 27 `.jpg` files and `Noticia_26.png`. | M1 | Survey / Asset Audit |
| 12 | 4-Point Response Scale (Murphy/León) | 4 mutually exclusive radio options (Falso Recuerdo, Falsa Creencia, Lo recuerdo diferente, No lo recuerdo). | M2 | Survey / ORIGINAL_REQUEST §5.6 |
| 13 | Millisecond Latency Tracking (RT) | Silent reaction time measurement in milliseconds from rating screen display to user click. | M2 | Survey / ORIGINAL_REQUEST §2.8 |
| 14 | Ethical Debriefing (Dehoaxing) | Mandatory disclosure that 8 news were false, explaining cognitive biases and study goals. | M2 | Survey / ORIGINAL_REQUEST §5.7 |
| 15 | Thank You & Confirmation Screen | Final confirmation screen verifying sync, thanking participant, academic contact info. | M2 | Survey / ORIGINAL_REQUEST §5.8 |
| 16 | Client Telemetry Capture | Silent recording of device type (mobile/desktop/tablet), screen resolution, and user agent. | M2 / M3 | Survey / ORIGINAL_REQUEST §R3 |
| 17 | Supabase Data Persistence | PostgreSQL relational schema (`participants`, `responses`), indexes, RLS, local offline buffer/retry. | M3 | Survey / ORIGINAL_REQUEST §R3 |
| 18 | Protected Admin Dashboard | `/admin` route with password protection, participant count by group, balance visual check. | M4 | Survey / ORIGINAL_REQUEST §R4 |
| 19 | CSV Export Engine | Downloadable Long Format CSV (20 rows/participant) with UTF-8 BOM, all experimental variables. | M4 | Survey / ORIGINAL_REQUEST §R4 |

*Cross-check verification*: All 19 features are assigned to milestones M1–M5. Zero unassigned features.

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| **E2E** | E2E Testing Suite & Harness | Requirements-driven opaque-box test runner covering Tiers 1–4, publishing `TEST_READY.md`. | none | DONE |
| **M1** | Project Scaffolding, Types & Stimuli Assets | Next.js 14+ setup, Tailwind, TypeScript contracts, all 28 stimuli data & images (`Noticia_26.png`). | none | DONE |
| **M2** | Participant Flow & Cognitive UI Engine | Welcome, Consent, Demographics, Induction, 10s Timer, Response Scale, Debriefing, Thank You. | M1 | DONE |
| **M3** | Supabase Database, Balanced RPC & Sync | PostgreSQL DDL, RPC `assign_induction_group`, API routes, local session buffer, offline resiliency. | M1, M2 | PLANNED |
| **M4** | Admin Dashboard & Long-Format CSV Export | Protected `/admin` route, metrics cards, balance badge, `/api/admin/export-csv` (20 rows/part). | M3 | PLANNED |
| **M5** | Git Setup, Deployment Configuration & README | Git repository setup, comprehensive README, environment templates, Vercel deploy configuration. | M1, M2, M3, M4 | PLANNED |
| **M6** | Final Acceptance & Dual Track Verification | Pass 100% of E2E test suite (Tiers 1–4) + Phase 2 Adversarial Hardening (Tier 5). | E2E, M1–M5 | PLANNED |

---

## Interface Contracts

### 1. TypeScript Domain Models (`src/types/experiment.ts`)
```typescript
export type InductionGroup = 'racional' | 'emocional' | 'control';
export type TherapeuticOrientation = 'Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros';
export type FakeNewsSet = 'psicoanalisis' | 'evidencia' | 'control_random';
export type ResponseCode = 1 | 2 | 3 | 4;

export interface StimulusItem {
  id: number; // 1 to 28
  title: string;
  isFake: boolean;
  imageFileName: string; // e.g. "Noticia_01.jpg" or "Noticia_26.png"
  congruence: 'psicoanalisis' | 'evidencia' | 'true';
}

export interface ParticipantSession {
  id: string; // UUID
  createdAt: string;
  completedAt?: string;
  age: number;
  gender: string;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
  university: string;
  isIncluded: boolean;
  inductionGroup: InductionGroup;
  fakeNewsSet: FakeNewsSet;
  deviceType: 'desktop' | 'mobile' | 'tablet';
  screenResolution: string;
  userAgent: string;
}

export interface TrialRecord {
  participantId: string;
  presentationOrder: number; // 1 to 20
  newsId: number;
  isFake: boolean;
  newsCongruence: string;
  responseOption: ResponseCode;
  responseLabel: string;
  readingTimeMs: number;
  responseTimeMs: number;
}
```

### 2. Supabase DDL Contract (`supabase/schema.sql`)
```sql
CREATE TABLE IF NOT EXISTS participants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at TIMESTAMPTZ NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    studies_psychology BOOLEAN NOT NULL,
    therapeutic_orientation VARCHAR(100) NOT NULL,
    university TEXT NOT NULL,
    is_included BOOLEAN NOT NULL,
    induction_group VARCHAR(50) NOT NULL,
    fake_news_set VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'started',
    device_type VARCHAR(50) NULL,
    screen_resolution VARCHAR(50) NULL,
    user_agent TEXT NULL
);

CREATE TABLE IF NOT EXISTS responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(id) ON DELETE CASCADE,
    presentation_order INT NOT NULL,
    news_id INT NOT NULL,
    is_fake BOOLEAN NOT NULL,
    news_congruence VARCHAR(50) NOT NULL,
    response_option INT NOT NULL,
    response_label TEXT NOT NULL,
    reading_time_ms INT NOT NULL,
    response_time_ms INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE OR REPLACE FUNCTION assign_induction_group()
RETURNS text LANGUAGE plpgsql SECURITY DEFINER AS $$
DECLARE chosen_group text;
BEGIN
    PERFORM pg_advisory_xact_lock(742911);
    WITH counts AS (
        SELECT 'racional' AS grp, COUNT(*) AS cnt FROM participants WHERE is_included = true AND induction_group = 'racional'
        UNION ALL
        SELECT 'emocional' AS grp, COUNT(*) AS cnt FROM participants WHERE is_included = true AND induction_group = 'emocional'
        UNION ALL
        SELECT 'control' AS grp, COUNT(*) AS cnt FROM participants WHERE is_included = true AND induction_group = 'control'
    ),
    min_candidates AS (
        SELECT grp FROM counts WHERE cnt = (SELECT MIN(cnt) FROM counts)
    )
    SELECT grp INTO chosen_group FROM min_candidates ORDER BY random() LIMIT 1;
    RETURN chosen_group;
END;
$$;
```

### 3. CSV Export Schema (Long Format: 20 Rows per Participant)
- Columns: `participant_id`, `created_at`, `completed_at`, `age`, `gender`, `studies_psychology`, `therapeutic_orientation`, `university`, `is_included`, `induction_group`, `fake_news_set`, `presentation_order`, `news_id`, `is_fake`, `news_congruence`, `response_option`, `response_label`, `is_false_memory`, `is_false_belief`, `reading_time_ms`, `response_time_ms`, `device_type`, `screen_resolution`.
- Encoded in UTF-8 with BOM (`\uFEFF`) for direct Excel opening.

---

## Code Layout

Target Directory: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`

```
web-experimento/
├── .env.example
├── .env.local
├── .gitignore
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── postcss.config.js
├── next.config.mjs
├── README.md
├── public/
│   └── noticias/
│       ├── Noticia_01.jpg ... Noticia_25.jpg
│       ├── Noticia_26.png
│       └── Noticia_27.jpg, Noticia_28.jpg
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx (Experiment flow orchestrator)
│   │   ├── admin/
│   │   │   ├── page.tsx (Researcher Dashboard)
│   │   │   └── login/page.tsx
│   │   └── api/
│   │       ├── session/route.ts
│   │       ├── responses/route.ts
│   │       ├── admin/
│   │       │   ├── login/route.ts
│   │       │   ├── stats/route.ts
│   │       │   └── export-csv/route.ts
│   ├── components/
│   │   ├── WelcomeScreen.tsx
│   │   ├── ConsentScreen.tsx
│   │   ├── DemographicsScreen.tsx
│   │   ├── InductionScreen.tsx
│   │   ├── StimulusReadingScreen.tsx
│   │   ├── RatingScreen.tsx
│   │   ├── DebriefingScreen.tsx
│   │   ├── ThankYouScreen.tsx
│   │   └── AdminDashboard.tsx
│   ├── data/
│   │   └── stimuli.ts (All 28 news items & metadata)
│   ├── lib/
│   │   ├── supabase.ts
│   │   ├── experimentLogic.ts (screening, congruency, randomization)
│   │   └── timing.ts
│   └── types/
│       └── experiment.ts
└── supabase/
    └── schema.sql
```
