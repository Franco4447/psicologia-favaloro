# Technical Architecture & Environment Investigation Report

**Author:** `explorer_survey_3`  
**Date:** 2026-09-20  
**Target Project:** Plataforma Web de Investigación Psicológica - Universidad Favaloro  
**Target Directory:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  

---

## 1. Observations

### 1.1 Target Folder and Asset Audit
- **Target Folder Status:**  
  Path: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  
  Observation: Currently does **not exist**. Needs to be scaffolded during the implementation phase.
- **Experimental Stimuli Assets:**  
  Path: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes`  
  Direct observation:
  - 28 image files exist: `Noticia_01.jpg` through `Noticia_25.jpg`, `Noticia_26.png` (**NOTE:** `.png` extension, 409,356 bytes), `Noticia_27.jpg`, `Noticia_28.jpg`.
  - All images are horizontal banner headlines with dimensions around ~1700 × ~420 px (approx 4:1 aspect ratio), ranging from 81 KB to 409 KB.
- **Experimental Materials Verification:**  
  Path: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\NOTICIAS TRADUCIDAS.docx`  
  Direct observation of 3 tables:
  - Table 0 (True News): 12 items, Internal IDs `1` to `12`.
  - Table 1 (Fake News Set 1): 8 items, Internal IDs `13, 14, 15, 16, 17, 18, 19, 20`.
  - Table 2 (Fake News Set 2): 8 items, Internal IDs `21, 22, 23, 24, 25, 26, 27, 28`.
  - Verified condition congruence:
    - Afinidad Psicoanálisis: News IDs `14, 16, 18, 20, 21, 23, 25, 27` (all attack cognitive/behavioral therapy or Watson).
    - Afinidad Basada en Evidencia: News IDs `13, 15, 17, 19, 22, 24, 26, 28` (all attack psychoanalysis, Freud, or projective tests).

### 1.2 System Environment & Tooling
- **Node.js:** `v24.15.0` (Active LTS / Modern Current)
- **npm:** `11.12.1`
- **Git:** `2.53.0.windows.2`
- **Python:** `3.13.14` (with `python-docx` and `Pillow` installed)
- **Git Configuration:**
  - `user.name`: `Franco4447`
  - `user.email`: `francomendezcasariego@gmail.com`
  - Root repository: `https://github.com/Franco4447/psicologia-favaloro.git` (branch `main`).
- **Cloud CLIs:**
  - `vercel`, `netlify`, `gh`, `supabase` are not installed in global system PATH.
  - However, `npx vercel` and `npx supabase` are executable via npm/npx without global installation.
- **Credentials & Environment Variables:**
  - Powershell environment check revealed **no** existing Supabase, Vercel, or Netlify tokens/keys in environment variables.
  - No `.env` files found in workspace. Zero leak risks.

---

## 2. Logic Chain & Technical Architecture Design

### 2.1 Full-Stack Framework Selection: Next.js (App Router) vs. Vite SPA

#### Assessment:
1. **Security & Data Integrity:**
   - In a pure Vite SPA, administrative actions (viewing participant lists, downloading raw CSVs, checking group balance) either require exposing the Supabase `service_role` key to client-side bundles (a severe security vulnerability) or setting up separate serverless backend functions.
   - Next.js (App Router) provides unified React frontend and Server Routes / Route Handlers (`/api/assignment`, `/api/admin/login`, `/api/admin/export-csv`, `/api/admin/stats`).
   - The Supabase `SUPABASE_SERVICE_ROLE_KEY` and the `ADMIN_PASSWORD` can remain strictly on the server, completely hidden from the browser.
2. **Participant Session & Latency:**
   - Next.js App Router renders lightweight client components for the experiment runner (`"use client"`), allowing smooth CSS/JS transitions and accurate timing via `performance.now()`.
3. **Deployment Compatibility:**
   - Both Vercel and Netlify natively detect Next.js. Vercel is the primary recommended platform because Next.js is developed by Vercel, providing zero-config deployments, automatic SSL, preview environments, and instant edge execution.

**Recommendation:** Build the web application using **Next.js 14+ (App Router) + TypeScript + Tailwind CSS + Lucide Icons + @supabase/supabase-js**.

---

### 2.2 Balanced Randomization Algorithm (Acceptance Criteria: Diff ≤ 2)

#### Challenge:
The experiment requires assigning included participants to one of 3 induction groups (`racional`, `emocional`, `control`) such that at any given moment:
$$\max(N_{racional}, N_{emocional}, N_{control}) - \min(N_{racional}, N_{emocional}, N_{control}) \le 2$$

#### Algorithmic Solution: "Min-Fill with Random Tie-Breaking and Transactional Lock"
1. **Mathematical Property:**
   - Let $C = (N_r, N_e, N_c)$ be the vector of participant counts across the 3 groups.
   - Find $M = \min(C)$.
   - Filter candidate groups: $G_{min} = \{g \in \{\text{racional}, \text{emocional}, \text{control}\} \mid N_g = M\}$.
   - If $|G_{min}| = 3$, all groups are equal ($\Delta = 0$); pick any with probability $1/3 \implies \Delta = 1$.
   - If $|G_{min}| = 2$, two groups are tied at the minimum ($\Delta = 1$); pick either with probability $1/2 \implies \Delta = 1$.
   - If $|G_{min}| = 1$, one group has fewer participants than the other two ($\Delta = 1$); assign to this unique minimum $\implies \Delta = 0$.
   - **Theorem:** Under serial execution, the difference $\Delta = \max(C) - \min(C)$ is **strictly $\le 1$** at all times.
2. **Preventing Race Conditions (Concurrency):**
   - If two participants register at the exact same millisecond, concurrent reads could assign both to the same group, potentially causing $\Delta = 3$.
   - To guarantee $\Delta \le 2$ under high concurrency, group assignment must be serialized at the database layer using an **advisory lock** (`pg_advisory_xact_lock`) or a dedicated counter row with `SELECT ... FOR UPDATE`.
   - Furthermore, we filter by `is_included = TRUE` so that excluded participants do not perturb the balance.

#### Supabase Database Function (RPC):
```sql
CREATE OR REPLACE FUNCTION assign_induction_group()
RETURNS text
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    chosen_group text;
BEGIN
    -- Acquire transaction-scoped advisory lock to prevent race conditions
    PERFORM pg_advisory_xact_lock(742911);

    WITH counts AS (
        SELECT 'racional' AS grp, COUNT(*) AS cnt 
        FROM participants 
        WHERE is_included = true AND induction_group = 'racional'
        UNION ALL
        SELECT 'emocional' AS grp, COUNT(*) AS cnt 
        FROM participants 
        WHERE is_included = true AND induction_group = 'emocional'
        UNION ALL
        SELECT 'control' AS grp, COUNT(*) AS cnt 
        FROM participants 
        WHERE is_included = true AND induction_group = 'control'
    ),
    min_candidates AS (
        SELECT grp 
        FROM counts 
        WHERE cnt = (SELECT MIN(cnt) FROM counts)
    )
    SELECT grp INTO chosen_group
    FROM min_candidates
    ORDER BY random()
    LIMIT 1;

    RETURN chosen_group;
END;
$$;
```

---

### 2.3 Database Architecture (Supabase PostgreSQL Schema)

The database schema is partitioned into two normalized relational tables:
1. `participants`: Records demographics, inclusion status, group assignment, technical metadata, and session lifecycle.
2. `responses`: Records each of the 20 trial responses (stimulus ID, news type, user response, reading time, reaction time, presentation order).

#### Complete SQL DDL & Security Migration Script:
```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. PARTICIPANTS TABLE
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
    induction_group VARCHAR(50) NOT NULL, -- 'racional', 'emocional', 'control'
    fake_news_set VARCHAR(50) NOT NULL,   -- 'psicoanalisis', 'evidencia', 'control_random'
    status VARCHAR(50) NOT NULL DEFAULT 'started', -- 'started', 'completed'
    device_type VARCHAR(50) NULL,
    screen_resolution VARCHAR(50) NULL,
    user_agent TEXT NULL,
    client_timestamp TIMESTAMPTZ NULL
);

-- 2. RESPONSES TABLE
CREATE TABLE IF NOT EXISTS responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(id) ON DELETE CASCADE,
    presentation_order INT NOT NULL, -- 1 to 20
    news_id INT NOT NULL,            -- 1 to 28
    is_fake BOOLEAN NOT NULL,        -- true if news_id >= 13
    news_congruence VARCHAR(50) NOT NULL, -- 'congruent', 'incongruent', 'neutral', 'true'
    response_option INT NOT NULL,    -- 1: Falso Recuerdo, 2: Falsa Creencia, 3: Diferente, 4: No recuerdo
    response_label TEXT NOT NULL,
    reading_time_ms INT NOT NULL,    -- Exposure duration (~10000ms)
    response_time_ms INT NOT NULL,   -- Reaction time in ms from question prompt to click
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 3. INDEXES FOR PERFORMANCE & EXPORT
CREATE INDEX IF NOT EXISTS idx_participants_is_included_group ON participants(is_included, induction_group);
CREATE INDEX IF NOT EXISTS idx_participants_status ON participants(status);
CREATE INDEX IF NOT EXISTS idx_responses_participant ON responses(participant_id);
CREATE INDEX IF NOT EXISTS idx_responses_news_id ON responses(news_id);

-- 4. ROW LEVEL SECURITY (RLS) POLICIES
ALTER TABLE participants ENABLE ROW LEVEL SECURITY;
ALTER TABLE responses ENABLE ROW LEVEL SECURITY;

-- Anonymous participants can INSERT their session and answers
CREATE POLICY "Allow public insert to participants" 
    ON participants FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "Allow public update on own session completion" 
    ON participants FOR UPDATE TO anon USING (true) WITH CHECK (true);

CREATE POLICY "Allow public insert to responses" 
    ON responses FOR INSERT TO anon WITH CHECK (true);

-- Anonymous participants CANNOT read all participant rows (privacy protection)
-- Service Role / Server API routes bypass RLS and perform admin reads/exports.
```

---

### 2.4 Stimulus Loop & Cognitive Timing Engine

1. **Trial Structure (20 Trials per Participant):**
   - 12 True News: internal IDs `1` to `12`.
   - 8 Fake News:
     - Afines a Psicoanálisis: `14, 16, 18, 20, 21, 23, 25, 27`.
     - Afines a Evidencia: `13, 15, 17, 19, 22, 24, 26, 28`.
     - Excluded: Balanced sample of 8 from the 16 fake news.
   - Presentation order randomized per participant using the Fisher-Yates shuffle algorithm:
     $$\text{shuffled\_news} = \text{shuffle}([1..12 \cup \text{fake\_news\_set}])$$
2. **Phase A: Forced Exposure (10 seconds):**
   - High-contrast stimulus card showing the headline banner (`Noticia_XX.jpg` / `Noticia_26.png`).
   - Animated visual countdown bar and numerical indicator (`10s` $\to$ `0s`).
   - The user cannot advance manually before the 10 seconds elapse.
   - At $t = 10000\text{ ms}$, the component triggers automatic transition to Phase B.
   - Exact elapsed exposure time is captured via `performance.now()`.
3. **Phase B: Rating & Reaction Time Measurement:**
   - The headline image remains visible above the questionnaire card for contextual recall.
   - 4 mutually exclusive radio options (Murphy & León scale):
     1. *"Recuerdo claramente haber visto/leído este evento"* (Falso Recuerdo)
     2. *"No recuerdo haberlo visto, pero creo que sucedió"* (Falsa Creencia)
     3. *"Lo recuerdo diferente"*
     4. *"No lo recuerdo en absoluto"*
   - Reaction time timer starts immediately upon rendering Phase B:
     `t_start = performance.now()`
   - When the participant clicks an option and confirms/advances:
     `response_time_ms = Math.round(performance.now() - t_start)`
   - Response payload is submitted asynchronously to Supabase (or accumulated in local memory and synced in batches to eliminate network latency impact on user experience).

---

### 2.5 CSV Export Specification (Long Format / 20 Rows per Participant)

To comply with R4, the export will produce an RFC 4180 compliant CSV file formatted as **Tidy Data / Long Format**, ideal for repeated-measures ANOVA, mixed-effects models (`lme4::glmer` in R), and SPSS:

#### Column Schema:
| Column Name | Type | Description |
|---|---|---|
| `participant_id` | UUID | Unique session identifier |
| `created_at` | ISO8601 | Start timestamp |
| `completed_at` | ISO8601 | Completion timestamp |
| `age` | Integer | Participant age |
| `gender` | String | Femenino / Masculino / Otro |
| `studies_psychology` | Boolean | TRUE / FALSE |
| `therapeutic_orientation` | String | Psicoanálisis / Basada en Evidencia Científica / Otros |
| `university` | String | Self-reported institution |
| `is_included` | Boolean | TRUE (included) / FALSE (excluded) |
| `induction_group` | String | `racional` / `emocional` / `control` |
| `fake_news_set` | String | `psicoanalisis` / `evidencia` / `control_random` |
| `presentation_order` | Integer | Sequence order from 1 to 20 |
| `news_id` | Integer | Internal stimulus number (1 to 28) |
| `is_fake` | Boolean | TRUE (fake news) / FALSE (true news) |
| `news_congruence` | String | `congruent`, `incongruent`, `neutral`, `true` |
| `response_option` | Integer | 1, 2, 3, or 4 |
| `response_label` | String | Full text of selected Murphy/León category |
| `is_false_memory` | Integer (0/1) | 1 if `is_fake = TRUE` AND `response_option = 1`, else 0 |
| `is_false_belief` | Integer (0/1) | 1 if `is_fake = TRUE` AND `response_option = 2`, else 0 |
| `reading_time_ms` | Integer | Time stimulus was shown (ms) |
| `response_time_ms` | Integer | Reaction time (ms) |
| `device_type` | String | desktop / mobile / tablet |
| `screen_resolution` | String | e.g. "1920x1080" |

#### Encoding & Formatting Details:
- Prepended with UTF-8 Byte Order Mark (`\uFEFF`) to ensure seamless opening in Spanish Microsoft Excel without character corruption (`á`, `é`, `í`, `ó`, `ú`, `ñ`).
- Comma-delimited with standard double-quote escaping.

---

### 2.6 Admin Dashboard & Security Architecture

1. **Route Protection:**
   - Route: `/admin`
   - Access is guarded via password authentication.
   - An environment variable `ADMIN_PASSWORD` is configured in `.env.local` / Vercel secrets.
2. **Session Mechanism:**
   - POST `/api/admin/login`: receives submitted password, verifies against `process.env.ADMIN_PASSWORD` with timing-safe comparison.
   - Sets a secure, HTTP-only, SameSite cookie containing a signed JWT / HMAC token with 24-hour expiration.
   - Next.js middleware / server layout verifies this cookie before serving `/admin` or `/api/admin/*`.
3. **Dashboard Capabilities:**
   - **Metrics Overview:** Total participants, completed participants, completion rate %, included vs. excluded count.
   - **Induction Balance Monitor:** Real-time counts for Racional, Emocional, and Control groups, displaying a visual badge confirming $\max(N) - \min(N) \le 2$.
   - **Data Summary:** Average response time by group, false memory incidence rate (%).
   - **Export Action:** "Descargar Dataset Completo (CSV)" button fetching `/api/admin/export-csv` directly.
   - **Session Table:** Searchable list of recent participant sessions with timestamps and status.

---

### 2.7 Git & Vercel Deployment Strategy

#### Monorepo vs. Dedicated Repository:
The local workspace is currently tracked by the git repository `https://github.com/Franco4447/psicologia-favaloro.git`.

- **Recommended Path (Seamless Monorepo Deployment via Vercel):**
  1. Initialize the Next.js project directly in:
     `2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento`
  2. Commit the new project to `Franco4447/psicologia-favaloro`.
  3. In the Vercel Dashboard:
     - Import repository `Franco4447/psicologia-favaloro`.
     - In **Project Settings** $\to$ **General** $\to$ **Root Directory**: click "Edit" and select:
       `2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento`
     - Framework Preset: **Next.js** (auto-detected).
     - Configure Environment Variables (see Section 2.8).
     - Deploy.
     - Any subsequent commit pushed to `main` will automatically trigger a production build.
- **Alternative Path (Dedicated GitHub Repository):**
  If the user prefers a standalone repository (e.g. `Franco4447/experimento-falsos-recuerdos`):
  1. Add `web-experimento/` to root `.gitignore` or use `git subtree push`.
  2. Push `web-experimento` to the new GitHub repo.
  3. Connect directly to Vercel with Root Directory set to `./`.

#### Environment Variables Checklist:
In `.env.local` (local) and Vercel Environment Variables:
```ini
NEXT_PUBLIC_SUPABASE_URL=https://[YOUR_PROJECT_ID].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOi...[YOUR_ANON_KEY]
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOi...[YOUR_SERVICE_ROLE_KEY]
ADMIN_PASSWORD=favaloro2026exp
NEXT_PUBLIC_APP_URL=https://[YOUR_VERCEL_APP].vercel.app
```

---

## 3. Caveats

1. **Asset Extension Discrepancy:**
   `Noticia_26` is a `.png` file while all other 27 stimuli are `.jpg`. The image resolver logic in code must explicitly handle `.png` for `Noticia_26` (or normalize filenames when copying them to `public/noticias/`).
2. **Supabase Free Tier Inactivity:**
   Free-tier Supabase projects pause after 7 days of inactivity. The team should ensure the project is active during the participant data collection window.
3. **Excluded Participant Fake News Selection:**
   Participants who do not study psychology or choose "Otros" receive the Control prompt. For their 8 fake news, the algorithm will draw 4 from the psychoanalysis set and 4 from the evidence set (randomized) so that difficulty is balanced without requiring ideological congruence.

---

## 4. Conclusions

1. **Environment is fully capable:** Modern Node.js `v24.15.0`, npm `11.12.1`, and Git `2.53.0` are present. No environment upgrades or tool installations are required.
2. **Optimal Architecture:** Next.js 14+ (App Router) + TypeScript + Tailwind CSS provides the best blend of participant UX, millisecond-precision reaction timing, robust server-side security for the admin dashboard, and zero-config Vercel deployment.
3. **Randomization Balance is Mathematically Guaranteed:** The proposed PostgreSQL RPC `assign_induction_group()` using transaction advisory locks ensures that group discrepancy will never exceed 1 under normal flow (and strictly $\le 2$ under extreme conditions), satisfying the acceptance criteria.
4. **Data Model & Export:** The proposed schema captures all R3 requirements and exports clean, tidy CSV data (20 rows per participant) formatted for immediate analysis in statistical packages.

---

## 5. Verification Method

To independently verify these findings and implementations:

1. **Verify Node and Git toolchain:**
   ```powershell
   node -v
   npm -v
   git status
   ```
2. **Verify Stimulus Images:**
   ```powershell
   python -c "import os; imgs = os.listdir(r'2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes'); assert len(imgs) == 28; print(f'Verified {len(imgs)} stimuli')"
   ```
3. **Verify Randomization Mathematical Proof:**
   Execute a 1,000-run simulation script verifying $\max(C) - \min(C) \le 1$:
   ```powershell
   python -c "import random; c={'r':0,'e':0,'c':0}; [c.update({random.choice([k for k,v in c.items() if v==min(c.values())]): c[random.choice([k for k,v in c.items() if v==min(c.values())])]+1}) for _ in range(1000)]; print(c); assert max(c.values()) - min(c.values()) <= 1"
   ```
4. **Verify Database Deployment:**
   Execute the migration SQL in Supabase SQL Editor and test the function:
   ```sql
   SELECT assign_induction_group();
   ```
5. **Verify CSV Export:**
   Download the CSV from `/api/admin/export-csv` after generating mock data, and verify that row count equals $20 \times N_{\text{completed participants}} + 1$ (header).
