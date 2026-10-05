# Handoff Report: Experimental Design Specification Mining

**Agent**: `spec_miner_survey_1`  
**Date**: 2026-09-20T23:25:00Z  
**Target Milestone**: Experimental Design Specification & Variable Flow  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\spec_miner_survey_1`  

---

## 1. Observation

Authoritative documents and reference files inspected directly on the filesystem:

### A. Core Request and Experimental Outline
1. **`ORIGINAL_REQUEST.md`** (lines 24–65, 71–87, 91–117):
   - **Independent Variable (VI)**: "Inducción a pensamiento emocional / racional / control" (3 inter-subject levels).
   - **Dependent Variable (VD)**: "Creación de falsos recuerdos (y falsas creencias) ante fake news".
   - **Controlled Intervening Variables**:
     - *Ideological Congruence*: "El participante elige afinidad terapéutica (Psicoanálisis vs. Basada en Evidencia) y se le muestran fake news alineadas a su ideología".
     - *Cognitive Deliberation Proxy*: "Tiempo de lectura y tiempo de respuesta como medida encubierta de esfuerzo cognitivo".
   - **Participant Flow**: Welcome -> Informed Consent -> Demographic Form -> Inclusion Check -> Induction Prompt -> 20-Trial Loop -> Debriefing -> Thank You.
   - **Inclusion Criterion**: "Si estudia psicología + elige Psicoanálisis o Basada en Evidencia -> participante incluido, se asigna a uno de los 3 grupos de inducción. Si NO cumple criterio -> recibe prompt de Control + set aleatorio de fake news, pero se marca como 'excluido' en los datos."
   - **Balancing Requirement**: "La distribución de participantes entre los 3 grupos se mantiene equilibrada (diferencia máxima de 2 entre el grupo más grande y el más pequeño en cualquier momento)".
   - **News Division**: 12 true news (IDs 1–12), 8 fake news for Psychoanalysis affinity (IDs 14, 16, 18, 20, 21, 23, 25, 27), 8 fake news for Evidence-Based affinity (IDs 13, 15, 17, 19, 22, 24, 26, 28). Total 28 stimuli.
   - **Presentation Dynamics**: 10-second forced reading display with visual progress bar and automatic transition; followed by untimed response screen with 4 options (Murphy/León scale) with response time recorded in milliseconds.

2. **`Psicología Experimental - Favaloro.docx`** (lines 11–26, 27–71):
   - Confirms course context: Universidad Favaloro, 2do Año, Cátedra de Psicología Experimental, Parcial 2 - Investigación.
   - General Objective: "determinar el efecto del tipo de inducción cognitiva (emocional, racional o control) sobre la creación de falsos recuerdos y falsas creencias tras la exposición a desinformación (fake news) congruente con las creencias previas en una población de adultos jóvenes qué sean profesionales o estudiantes en el ámbito de psicología."
   - Population target: "Masculinos y femeninos de entre 18 a 50 años".
   - Verbatim induction prompts:
     - **Racional**: *"Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones."*
     - **Emocional**: *"Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón."*
     - **Control**: *"A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no."*
   - Protocol for excluded participants (line 67): *"Las personas que no cumplen con el motivo de inclusión se les dará el enunciado de Grupo Control pero NO serán asignados a Grupo Control. Además se les asignará uno de los dos conjuntos de fake-news de forma aleatoria."* (They must NOT contaminate the quota balancing of valid Control participants).

3. **`experimento.docx`** (lines 8–13):
   - Justifies theoretical gap: Martel et al. (2020) measured false beliefs under emotion induction but did not measure false memories. León et al. (2023) studied false memories in psychology debate under passive exposure without emotional manipulation.
   - Highlights Source Monitoring Framework (Johnson et al., 1993): impulsive/emotional reading truncates source monitoring, leading to attribution of internal imaginings to external reality.
   - Establishes response time and reading time as objective proxies for System 1 (fast/intuitive) vs System 2 (slow/analytic) processing (Bago, Rand, & Pennycook, 2020).

4. **`Feedback_Diseño_Experimental.md`** (lines 21–39):
   - Mandates strict 4-point response scale to dissociate False Memory from False Belief:
     1. *"Recuerdo claramente haber visto/leído este evento"* -> **Falso Recuerdo** (when item is fake).
     2. *"No recuerdo haberlo visto, pero creo que sucedió"* -> **Falsa Creencia** (when item is fake).
     3. *"Lo recuerdo diferente"*.
     4. *"No lo recuerdo en absoluto"*.

5. **`NOTICIAS TRADUCIDAS.docx`** and **`noticias imagenes`**:
   - 12 True News: IDs 1 to 12.
   - 8 Fake News Set 1: IDs 13 to 20 (Odd numbers attack psychoanalysis; even numbers attack behaviorism/cognitivism).
   - 8 Fake News Set 2: IDs 21 to 28 (Odd numbers attack behaviorism/cognitivism; even numbers attack psychoanalysis).
   - Symmetrical congruency mapping:
     - **Psicoanálisis set**: News 14, 16, 18, 20, 21, 23, 25, 27 (all criticize cognitive/behavioral therapy or praise psychoanalysis alternatives).
     - **Basada en Evidencia set**: News 13, 15, 17, 19, 22, 24, 26, 28 (all criticize psychoanalytic therapy or Freud/projective techniques).
   - 28 image files: `Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_26.png` (**NOTE**: Noticia_26 has `.png` extension, while all others are `.jpg`), `Noticia_27.jpg`, `Noticia_28.jpg`.

---

## 2. Logic Chain

1. **Theoretical Gap & Hypotheses**:
   - Prior studies on cognitive induction (Martel et al., 2020) showed emotional priming increases credulity toward fake news (false beliefs), but never investigated if emotional priming can forge episodic false memories (*"I remember seeing this"*).
   - Prior studies on false memories in the psychology debate (León et al., 2023) demonstrated ideological congruence effects for false beliefs, but false memories remained low under passive reading.
   - The Source Monitoring Framework (Johnson et al., 1993) predicts that emotional induction impairs reflective source monitoring and generates vivid internal imagery, causing participants to confuse internal generation with external reality, thereby precipitating genuine false memories when the fake news aligns with their ideological worldview.
   - Deliberation time acts as a natural inhibitor of misinformation belief (Bago et al., 2020; Pennycook & Rand, 2021). Thus, recording presentation and response latency provides a crucial proxy of cognitive effort.

2. **Variable Operationalization**:
   - **Independent Variable (VI)**: Cognitive induction type (Between-subjects, 3 levels):
     - `emocional`: Prime emphasizing emotion and feelings as superior guides.
     - `racional`: Prime emphasizing logic and reason as superior guides.
     - `control`: Neutral prompt with no decision-mode framing.
   - **Dependent Variables (VD)**:
     - `Falso Recuerdo` rate: Proportion of fake news items answered with option 1 (*"Recuerdo claramente haber visto/leído este evento"*).
     - `Falsa Creencia` rate: Proportion of fake news items answered with option 2 (*"No recuerdo haberlo visto, pero creo que sucedió"*).
     - `Memoria Verdadera` rate: Baseline measure from true news items answered with option 1.
     - `Tiempo de Respuesta (TR)`: Milliseconds elapsed on the rating screen before submission (proxy for System 1 vs 2 processing).
   - **Controlled Intervening Variables**:
     - *Ideological Congruence*: Controlled by asking therapeutic orientation ("Psicoanálisis" vs "Basada en Evidencia Científica") and presenting news that are ideologically concordant (anti-opposing current).
     - *Stimulus Exposure Time*: Standardized at 10,000 ms with automated progression to ensure all participants inspect the stimulus for an equal duration before entering the deliberative choice phase.

3. **Participant Screening & Routing Logic**:
   - Screen 3 captures: `edad` (integer), `sexo` ('Femenino' | 'Masculino' | 'Otro'), `estudia_psicologia` ('Sí' | 'No'), `orientacion_terapeutica` ('Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros'), `universidad` (text).
   - **Inclusion Test**:
     - `is_included = (estudia_psicologia == 'Sí') && (orientacion_terapeutica in ['Psicoanálisis', 'Basada en Evidencia Científica']) && (edad >= 18)`.
   - **Routing Decision**:
     - If `is_included == true`:
       - `induction_group`: Assigned dynamically via balanced allocation algorithm (`racional`, `emocional`, or `control`).
       - `fake_news_set`: If `orientacion_terapeutica == 'Psicoanálisis'` -> Set `[14, 16, 18, 20, 21, 23, 25, 27]`. If `orientacion_terapeutica == 'Basada en Evidencia Científica'` -> Set `[13, 15, 17, 19, 22, 24, 26, 28]`.
       - Participant counts toward the balanced group quota.
     - If `is_included == false`:
       - `induction_group`: Forced display of the `control` prompt text.
       - `fake_news_set`: Random selection (50/50) between Psychoanalysis set or Evidence-based set.
       - Flagged in database as `incluido = false` with `exclusion_reason`.
       - **Crucial**: Excluded participants MUST NOT increment or be counted in the induction group balancing algorithm, preventing sample skew in the control condition.

4. **Stimulus Presentation & Timing Engine**:
   - Stimulus deck for each participant consists of exactly 20 items: 12 true news + 8 assigned fake news.
   - The 20 items are randomized in presentation order per participant session.
   - For each item $i \in [1..20]$:
     - **Phase 1 (Reading / Exposure)**:
       - Displays headline image (`/assets/noticias/Noticia_XX.jpg` or `Noticia_26.png`).
       - Duration: Exactly 10.0 seconds.
       - Visual feedback: Animated countdown progress bar spanning 0 to 10 seconds.
       - Transition: Automatic redirect to Phase 2 at $t = 10,000\text{ ms}$.
     - **Phase 2 (Evaluation / Response)**:
       - Displays the 4-point response radio group.
       - Timer begins at $t_0 = \text{Date.now()}$ upon mounting Phase 2.
       - Participant selects 1 option (validation required: button disabled until selection).
       - On clicking "Siguiente Noticia", reaction time $\Delta t = t_{\text{submit}} - t_0$ is recorded in milliseconds.
       - Answers and latency are recorded locally and batched / streamed to Supabase.

5. **Balanced Group Assignment Algorithm**:
   - Requirement: Max discrepancy between largest and smallest included group $\le 2$ at all times.
   - Implementation:
     - Read current counts of completed + active included participants: $C_{\text{racional}}, C_{\text{emocional}}, C_{\text{control}}$.
     - Let $C_{\min} = \min(C_{\text{racional}}, C_{\text{emocional}}, C_{\text{control}})$.
     - Pool of eligible groups = $\{ g \mid C_g = C_{\min} \}$.
     - Uniform random selection among eligible groups in the pool.
     - Updates group assignment atomically to avoid race conditions under concurrency.

6. **Ethical Protocols (Consent & Debriefing)**:
   - Initial Consent: Voluntary participation, anonymity guarantee, data used strictly for academic research at Universidad Favaloro.
   - Debriefing (Mandatory Dehoaxing):
     - Explicit disclosure that 8 of the 20 headlines presented were completely fabricated.
     - Explanation of the research question: evaluating how emotions and cognitive mindsets modulate susceptibility to misinformation.
     - Ethical reassurance: Informing participants that endorsing false news or false memories is a normal psychological cognitive bias, not a reflection of low intelligence or competence.
     - Provide contact details of the research team.

---

## 3. Features Discovered & Edge Cases

### Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Onboarding | Welcome & Academic Framing Screen | Introduces the experiment, Universidad Favaloro identity, instructions, recommendation to use computer and ensure 10 min quiet time. | None (Landing) | Rendered welcome screen, "Comenzar" button | N/A | `ORIGINAL_REQUEST.md` line 31, `Psicología Experimental - Favaloro.docx` line 42-45 |
| 2 | Ethics | Informed Consent Screen | Mandatory ethical consent form explaining study goals, voluntary participation, and anonymity. | Checkbox state (boolean) | Proceed enabled if checked; proceed blocked if unchecked | Warning alert if user attempts to submit without checking box | `ORIGINAL_REQUEST.md` line 32, `Psicología Experimental - Favaloro.docx` line 43 |
| 3 | Screening | Demographic Data Collection | Collects participant's age, gender, psychology student status, therapeutic orientation, and university. | `edad` (int), `sexo` (enum), `estudia_psicologia` (bool), `orientacion_terapeutica` (enum), `universidad` (text) | Validated demographic object passed to state/DB | Inline validation errors for missing fields or invalid age (<18) | `ORIGINAL_REQUEST.md` line 34-38, `Psicología Experimental - Favaloro.docx` line 48-52 |
| 4 | Screening | Inclusion / Exclusion Evaluation Logic | Hidden server/client rule assessing eligibility. Evaluates whether participant studies psychology and adheres to Psychoanalysis or Evidence-Based therapy. | `estudia_psicologia`, `orientacion_terapeutica`, `edad` | `is_included` (bool), `exclusion_reason` (string or null) | Gracefully routes excluded participants without revealing exclusion | `ORIGINAL_REQUEST.md` line 39-41, `Psicología Experimental - Favaloro.docx` line 53-55 |
| 5 | Experimental Engine | Balanced Induction Group Allocation | Dynamic algorithm assigning included participants to Racional, Emocional, or Control, maintaining max discrepancy <= 2 across groups. | Current group counts from database | Assigned group: `'racional'`, `'emocional'`, or `'control'` | Fallback to random assignment if DB count fetch fails | `ORIGINAL_REQUEST.md` line 42, 99, `Psicología Experimental - Favaloro.docx` line 58 |
| 6 | Experimental Engine | Excluded Participant Handling Protocol | Excluded participants are routed to receive the Control induction prompt and a random fake news set, but marked as excluded and not counted in balance quotas. | `is_included == false` | `induction_group = 'control'`, `is_included = false`, random fake news set | Excluded count kept separate from experimental quotas | `Psicología Experimental - Favaloro.docx` line 67, `ORIGINAL_REQUEST.md` line 41 |
| 7 | Experimental Engine | Ideological Congruence Stimulus Routing | Maps participant's therapeutic orientation to the congruent set of 8 fake news (attacking opposing orientation). | `orientacion_terapeutica` | Set 1 (IDs 14, 16, 18, 20, 21, 23, 25, 27) OR Set 2 (IDs 13, 15, 17, 19, 22, 24, 26, 28) | Throws error if orientation undefined | `ORIGINAL_REQUEST.md` line 49-50, `NOTICIAS TRADUCIDAS.docx` |
| 8 | Experimental Engine | Cognitive Induction Display Screen | Displays the condition-specific priming prompt (Racional, Emocional, or Control) verbatim as formulated by Martel / Levine. | `induction_group` | Verbatim text display and "Continuar a las noticias" button | Displays Control text as default fallback | `Psicología Experimental - Favaloro.docx` line 28-36, `ORIGINAL_REQUEST.md` line 43-45 |
| 9 | Experimental Engine | 20-Trial Stimulus Randomizer | Combines 12 true news items (1–12) with the 8 assigned fake news items and performs a Fisher-Yates shuffle for presentation order. | 12 true IDs + 8 assigned fake IDs | Array of 20 randomized item descriptors | Ensures exactly 20 items with no duplicates | `ORIGINAL_REQUEST.md` line 46-50, 75 |
| 10 | Stimulus Loop | Stimulus Reading Display (Phase 1) | Displays the news headline image for exactly 10 seconds with a real-time progress bar. | `noticia_id`, image asset | Image rendered, 10s countdown bar, auto-advances at 10.0s | Image fallback handling if asset fails to load | `ORIGINAL_REQUEST.md` line 52, 94 |
| 11 | Stimulus Loop | Asset Extension Resolver | Specifically resolves image paths, taking into account that `Noticia_26` is `.png` while all other 27 are `.jpg`. | `noticia_id` (1–28) | Correct path (`/assets/noticias/Noticia_26.png` vs `.jpg`) | Prevents broken image for item 26 | File inspection of `noticias imagenes/` |
| 12 | Stimulus Loop | 4-Point Response Scale (Phase 2) | Presents the 4 mutually exclusive memory/belief options per Murphy/León scale without time limit. | Radio selection (1–4) | Selected code and label | Button disabled until 1 option is selected | `ORIGINAL_REQUEST.md` line 53-57, `Feedback_Diseño_Experimental.md` line 29-34 |
| 13 | Stimulus Loop | Response Time Latency Tracker (RT) | Records response latency in milliseconds from mounting Phase 2 until answer submission button click. | Timer start ($t_0$) and submit click ($t_{\text{sub}}$) | `tiempo_respuesta_ms` (integer) | Non-negative integer validation | `ORIGINAL_REQUEST.md` line 28, 53, 107 |
| 14 | Ethics | Debriefing & Dehoaxing Screen | Reveals ethical truth: 8 news items were fabricated. Explains study rationale, normalizes false memory formation, protects self-esteem. | Session completion trigger | Rendered debriefing statement, educational explanation | Mandatory step before completion | `Psicología Experimental - Favaloro.docx` line 38, 68, `ORIGINAL_REQUEST.md` line 59 |
| 15 | Onboarding | Final Thank You & Confirmation Screen | Confirms successful data transmission, thanks participant, provides academic contact details. | Completed session | Farewell screen | Confirms cloud synchronization status | `ORIGINAL_REQUEST.md` line 60, `Psicología Experimental - Favaloro.docx` line 69 |
| 16 | Quality Control | Client Environment Telemetry | Captures participant screen resolution, user agent, browser language, and device category for data cleaning. | `window.navigator`, `window.screen` | Metadata JSON saved to participant record | Handled safely if navigator properties restricted | `ORIGINAL_REQUEST.md` line 79 |
| 17 | Persistence | Supabase Participant & Trial Data Store | Stores participant demographic session and 20 individual trial records into PostgreSQL tables. | Participant object, array of 20 trial responses | Persisted rows in Supabase | LocalStorage buffer / retry mechanism if network glitch occurs | `ORIGINAL_REQUEST.md` line 63-64, 79, 105 |
| 18 | Analytics | Password-Protected Researcher Dashboard | Protected admin view displaying total participant count, breakdown by group, inclusion breakdown, and export button. | Admin password / session | Dashboard UI with live aggregate metrics | Unauthorized HTTP 401/403 for wrong password | `ORIGINAL_REQUEST.md` line 83-84, 115-116 |
| 19 | Analytics | CSV Export Engine | Generates downloadable CSV formatted with 1 row per trial per participant (20 rows per participant) with all metadata. | Query over participant + trial tables | Downloadable UTF-8 CSV file (`experimento_datos.csv`) | Handles nulls or special characters properly | `ORIGINAL_REQUEST.md` line 83, 106, 116 |

---

### Edge Cases

| # | Feature | Input | Observed / Specified Behavior |
|---|---------|-------|-------------------------------|
| 1 | Screening | Participant indicates `edad < 18` | Validation blocks submission with message indicating that participants must be at least 18 years old to provide legal informed consent. |
| 2 | Screening | Participant selects `estudia_psicologia = 'No'` | Form validates; internally flags `is_included = false`, `exclusion_reason = 'no_estudia_psicologia'`. Participant proceeds through Control prompt and random fake news set. |
| 3 | Screening | Participant selects `orientacion_terapeutica = 'Otros'` | Form validates; internally flags `is_included = false`, `exclusion_reason = 'orientacion_otros'`. Participant proceeds through Control prompt and random fake news set. |
| 4 | Stimulus Loop | Image asset `Noticia_26` requested | System must resolve to `Noticia_26.png` instead of `.jpg`. If an asset fails to load, UI displays the verbatim headline text as fallback with a retry button to ensure stimulus is legible. |
| 5 | Stimulus Loop | Participant minimizes browser or switches tab during 10s reading phase | `document.visibilityState` changes. Timer should either pause or log `tab_switched = true` / `reading_interrupted = true` to allow researchers to filter distracted trials during statistical cleaning. |
| 6 | Stimulus Loop | Participant clicks response option in < 200 ms | Response recorded as submitted, but flag `rapid_response = true` can be appended for post-hoc reaction time outlier filtering. |
| 7 | Stimulus Loop | Participant leaves response screen open for > 15 minutes | Response is allowed to complete without throwing an error, but raw millisecond timestamp (> 900,000 ms) is recorded so outlier trimming (e.g. $\pm 3\text{ SD}$) can be performed in SPSS/R. |
| 8 | Group Allocation | Multiple participants enter demographic form simultaneously | Race condition in group counts. Allocation logic must perform an atomic query or increment on Supabase (e.g., RPC function `assign_balanced_group()`) so difference never exceeds 2. |
| 9 | Group Allocation | Excluded participant completes demographic form | Assigned to display Control prompt; fake news set randomly selected. Count of valid Control participants is NOT incremented, preserving balanced distribution across included experimental cells. |
| 10 | Stimulus Loop | Participant accidentally refreshes or presses F5 mid-experiment | Session state (participant ID, current trial index, assigned news deck, previous responses) should be cached in `sessionStorage` / `localStorage` to resume at current trial without losing data or creating orphan records. |
| 11 | Data Submission | Network disconnection when submitting trial responses | Responses are buffered in local browser storage. The UI displays a retry prompt before advancing to the debriefing screen, preventing data loss. |
| 12 | Dashboard | Unauthorized user navigates to `/dashboard` or `/admin` | Redirects to login prompt; requires secure researcher password specified in environment variables. |

---

## 4. Detailed Specification of Experimental Components

### 4.1. Demographic Variables & Schema
```typescript
interface ParticipantDemographics {
  participant_id: string; // UUID v4
  created_at: string;     // ISO UTC timestamp
  edad: number;           // Integer, min 18, max 100
  sexo: 'Femenino' | 'Masculino' | 'Otro';
  estudia_psicologia: boolean; // true = "Sí", false = "No"
  orientacion_terapeutica: 'Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros';
  universidad: string;    // Free text
  is_included: boolean;   // true if estudia_psicologia && orientacion in [Psicoanálisis, Basada en Evidencia]
  exclusion_reason: string | null; // e.g. "no_estudia_psicologia", "orientacion_otros", null
  induction_group: 'racional' | 'emocional' | 'control';
  fake_news_set: 'psicoanalisis' | 'evidencia';
  user_agent: string;
  screen_resolution: string; // e.g. "1920x1080"
  device_type: 'desktop' | 'mobile' | 'tablet';
  completed: boolean;
}
```

### 4.2. Trial Measurement Schema
```typescript
interface TrialResponse {
  trial_id: string;       // UUID v4
  participant_id: string; // UUID v4 foreign key
  noticia_id: number;     // 1 to 28
  tipo_noticia: 'verdadera' | 'fake';
  orden_presentacion: number; // 1 to 20
  tiempo_lectura_ms: number;  // Nominally 10,000 ms
  tiempo_respuesta_ms: number;// Delta t from phase 2 mount to submit (ms)
  respuesta_codigo: 1 | 2 | 3 | 4;
  respuesta_texto: string;
  // Computed variables for researcher convenience:
  es_falso_recuerdo: boolean;  // true if (tipo_noticia == 'fake' && respuesta_codigo == 1)
  es_falsa_creencia: boolean;  // true if (tipo_noticia == 'fake' && respuesta_codigo == 2)
  es_memoria_verdadera: boolean;// true if (tipo_noticia == 'verdadera' && respuesta_codigo == 1)
}
```

### 4.3. Stimuli Inventory & Congruence Table

#### True News (Noticias Verdaderas) — Shown to ALL participants (12 items):
- **Noticia 1**: *"Las agencias de medicamentos son una invención del capitalismo neoliberal de la década de 1990."* (`Noticia_01.jpg`)
- **Noticia 2**: *"Mario Bunge: el psicoanálisis y otras pseudociencias son perjudiciales."* (`Noticia_02.jpg`)
- **Noticia 3**: *"Una pandemia de adaptación y neoliberalismo conductual en la educación."* (`Noticia_03.jpg`)
- **Noticia 4**: *"Científicos explican por qué los sueños no tienen significados ocultos."* (`Noticia_04.jpg`)
- **Noticia 5**: *"El pequeño Albert: un cruel experimento con un bebé de 11 meses para estudiar las fobias."* (`Noticia_05.jpg`)
- **Noticia 6**: *"La comunidad reúne firmas contra las terapias psicoanalíticas públicas en casos de autismo."* (`Noticia_06.jpg`)
- **Noticia 7**: *"La caja de Skinner: juegos como Candy Crush están diseñados para volverte adicto."* (`Noticia_07.jpg`)
- **Noticia 8**: *"Wilhelm Reich: los controvertidos tratamientos sexuales de uno de los psicoanalistas más radicales de la historia."* (`Noticia_08.jpg`)
- **Noticia 9**: *"El psiquiatra que aplicaba electroshocks a personas homosexuales."* (`Noticia_09.jpg`)
- **Noticia 10**: *"La feminista que refutó a Freud y su concepto de envidia del pene."* (`Noticia_10.jpg`)
- **Noticia 11**: *"Expertos piden revisar los métodos actuales de diagnóstico del trastorno bipolar."* (`Noticia_11.jpg`)
- **Noticia 12**: *"La historia del sobrino argentino de Freud: es psicoanalista y cuestiona la idea de ser trans antes de la pubertad."* (`Noticia_12.jpg`)

#### Fake News for Psicoanálisis Affinity (Attacks Cognitive/Behavioral) (8 items):
- **Noticia 14**: *"Abraham Low, el pediatra y cognitivista británico que afirmaba que el autismo se curaba con terapia conductual."* (`Noticia_14.jpg`)
- **Noticia 16**: *"Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta cognitivo se negó a darle un diagnóstico."* (`Noticia_16.jpg`)
- **Noticia 18**: *"Suspenden la licencia de un terapeuta cognitivo que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos."* (`Noticia_18.jpg`)
- **Noticia 20**: *"Hallazgos recientes de neuroimagen refutan el concepto de 'condicionamiento' de Watson."* (`Noticia_20.jpg`)
- **Noticia 21**: *"El terapeuta cognitivo que entrenaba a sus pacientes con descargas eléctricas irá a juicio."* (`Noticia_21.jpg`)
- **Noticia 23**: *"Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia cognitiva."* (`Noticia_23.jpg`)
- **Noticia 25**: *"Texas: una joven se suicida después de recibir el alta de una terapia cognitiva breve."* (`Noticia_25.jpg`)
- **Noticia 27**: *"Un tirador en la ciudad de Dakota: 'había superado todas las técnicas psicométricas; era una persona normal'."* (`Noticia_27.jpg`)

#### Fake News for Basada en Evidencia Affinity (Attacks Psychoanalysis) (8 items):
- **Noticia 13**: *"El terapeuta freudiano que hipnotizaba a sus pacientes con descargas eléctricas irá a juicio."* (`Noticia_13.jpg`)
- **Noticia 15**: *"Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia psicoanalítica."* (`Noticia_15.jpg`)
- **Noticia 17**: *"Texas: una joven se suicida después de recibir el alta de una terapia psicoanalítica."* (`Noticia_17.jpg`)
- **Noticia 19**: *"Un tirador en la ciudad de Dakota: 'había superado todas las técnicas proyectivas; era una persona normal'."* (`Noticia_19.jpg`)
- **Noticia 22**: *"Donald Winnicott, el pediatra y psicoanalista británico que afirmaba que el autismo se curaba mediante hipnosis."* (`Noticia_22.jpg`)
- **Noticia 24**: *"Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta psicoanalista se negó a darle un diagnóstico."* (`Noticia_24.jpg`)
- **Noticia 26**: *"Suspenden la licencia de un psicoanalista que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos."* (`Noticia_26.png`) — **Important: `.png` format**
- **Noticia 28**: *"Hallazgos recientes de neuroimagen refutan el concepto de 'superyó' de Freud."* (`Noticia_28.jpg`)

---

## 5. Caveats

1. **Mobile Responsiveness vs Research Recommendation**:
   - The briefing notes state participants should be encouraged to use a desktop computer and spend 10 undisturbed minutes. While the platform should be fully responsive for mobile viewports, an initial recommendation banner or modal advising desktop usage should be presented on the Welcome screen.
2. **Reading Phase Interactivity**:
   - The specification states reading is 10 seconds with automatic progression. No manual "Avanzar antes" button is provided on Phase 1 to guarantee uniform stimulus exposure across participants.
3. **Reaction Time Noise**:
   - Reaction times recorded over the web can exhibit slight timing jitter due to JavaScript event loop lag. Using `performance.now()` provides sub-millisecond precision, far exceeding the precision required for psychological reaction time analyses.
4. **Data Privacy**:
   - No direct identifiers (names, emails, DNI) are captured, satisfying Argentine personal data protection (Ley 25.326) and academic ethics requirements for anonymous psychological testing.

---

## 6. Conclusion

The experimental design is completely specified across all dimensions:
- **Design**: $3 \times 1$ between-subjects (Cognitive Induction: Racional vs Emocional vs Control) with ideological congruence controlled through therapeutic affinity.
- **Stimuli**: 28 assets verified in `noticias imagenes/` (12 true, 16 fake split into 2 congruent decks of 8).
- **Flow**: 8 sequential stages from welcome and consent to 20 timed trials, ethical debriefing, and thank you screen.
- **Data & Export**: 20 rows per participant in CSV format, fully tracking memory classification, belief classification, and reaction latency in milliseconds.
- **Quota Balancing**: Explicit algorithm designed to keep included condition sizes balanced within $\le 2$ participants while isolating excluded participants.

---

## 7. Verification Method

To verify these findings independently:

1. **Verify Stimulus Images**:
   ```powershell
   Get-ChildItem -Path "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes"
   ```
   *Expected*: Exactly 28 files (`Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_26.png`, `Noticia_27.jpg`, `Noticia_28.jpg`).

2. **Verify Text Headlines and Numbering**:
   Examine `NOTICIAS TRADUCIDAS.docx` to confirm the exact Spanish wording and internal numbering (1–12 true, 13–28 fake).

3. **Verify Inclusion and Induction Prompts**:
   Inspect `ORIGINAL_REQUEST.md` (lines 30–60) and `Psicología Experimental - Favaloro.docx` (lines 27–36, 53–67) to confirm the verbatim wording of the 3 induction prompts and the rule that excluded participants receive Control prompt + random fake news set without being counted in the Control quota.
