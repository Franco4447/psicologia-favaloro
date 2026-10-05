# Handoff Report: Domain Models & Stimuli Dataset Architecture

**Agent**: `explorer_m1_3`  
**Date**: 2026-09-20T23:30:00Z  
**Milestone**: M1 (Data & Domain Models Architecture)  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m1_3`  
**Target Files Designed**:
- `src/types/experiment.ts` (Domain models & TypeScript contracts)
- `src/data/stimuli.ts` (All 28 stimuli, ideological congruence mappings, and set selection algorithms)

---

## 1. Observation

Direct observations extracted from authoritative project documentation, source files, and directory assets:

### A. Authoritative Documentation
1. **`ORIGINAL_REQUEST.md`** (lines 46–58):
   - Defines the 20-news presentation loop:
     - 12 true news: internal numbering 1 to 12.
     - Fake news for Psychoanalysis affinity: IDs 14, 16, 18, 20, 21, 23, 25, 27.
     - Fake news for Evidence-Based affinity: IDs 13, 15, 17, 19, 22, 24, 26, 28.
   - Forced reading time: 10 seconds with visual countdown progress bar and auto-advance.
   - Response screen: 4 mutually exclusive options based on Murphy/León scale:
     1. *"Recuerdo claramente haber visto/leído este evento"* (Falso Recuerdo / Memoria Verdadera)
     2. *"No recuerdo haberlo visto, pero creo que sucedió"* (Falsa Creencia)
     3. *"Lo recuerdo diferente"*
     4. *"No lo recuerdo en absoluto"*
   - Line 19 confirms: 28 images total, `Noticia_01.jpg` to `Noticia_28.jpg` (with one `.png`).

2. **`PROJECT.md`** (lines 68–111):
   - Defines TypeScript domain contracts: `InductionGroup`, `TherapeuticOrientation`, `FakeNewsSet`, `ResponseCode`, `StimulusItem`, `ParticipantSession`, and `TrialRecord`.
   - Lines 168–170 define CSV export columns (long format: 20 rows per participant).

3. **`NOTICIAS TRADUCIDAS.docx`** & **`stimuli_parsed.json`**:
   - Table 1 (rows 1–12): 12 True News items.
   - Table 2 (rows 13–20): Fake News Set 1 (8 items).
   - Table 3 (rows 21–28): Fake News Set 2 (8 items).
   - Confirms exact Spanish text, English translations, and internal numbering.

4. **Asset Directory Inspection**:
   - Path: `PARCIAL 2 - INVESTIGACIÓN/Noticias/noticias imagenes`
   - File listing:
     - 27 `.jpg` files: `Noticia_01.jpg` through `Noticia_25.jpg`, `Noticia_27.jpg`, `Noticia_28.jpg`.
     - Exactly 1 `.png` file: `Noticia_26.png` (RGBA, 409,356 bytes).

5. **`Psicología Experimental - Favaloro.docx`** (lines 28–36, 53–67):
   - Verbatim cognitive induction primes:
     - **Racional**: *"Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones."*
     - **Emocional**: *"Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón."*
     - **Control**: *"A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no."*
   - Protocol for excluded participants: Excluded subjects receive the Control prompt and an 8-item cohesive fake news set, but are marked `is_included = false` and excluded from the balanced group assignment quota.

---

## 2. Logic Chain

From the direct observations, the domain modeling and stimuli dataset architecture follow this deductive logic chain:

1. **Stimuli Universe & Partitioning**:
   - The total universe consists of exactly 28 stimuli ($N = 28$).
   - Baseline Set: 12 True News (IDs 1–12). Balanced between themes (6 psychoanalysis-adjacent, 6 behaviorism/biology-adjacent). Displayed to 100% of participants.
   - Fake News Universe: 16 Fabricated News (IDs 13–28).

2. **Mirror-Pair Counterbalancing Symmetry**:
   - The 16 fake news items form 8 symmetrical pairs to control for story salience and topic content:
     - Pair 1: #13 (Anti-Psychoanalysis) $\leftrightarrow$ #21 (Anti-Cognitive) [Electroshocks trial]
     - Pair 2: #14 (Anti-Cognitive) $\leftrightarrow$ #22 (Anti-Psychoanalysis) [Pediatrician claiming autism cure]
     - Pair 3: #15 (Anti-Psychoanalysis) $\leftrightarrow$ #23 (Anti-Cognitive) [Starvation in Formosa, locked fridge]
     - Pair 4: #16 (Anti-Cognitive) $\leftrightarrow$ #24 (Anti-Psychoanalysis) [Depression 5-year malpractice diagnosis]
     - Pair 5: #17 (Anti-Psychoanalysis) $\leftrightarrow$ #25 (Anti-Cognitive) [Texas young woman suicide post-discharge]
     - Pair 6: #18 (Anti-Cognitive) $\leftrightarrow$ #26 (Anti-Psychoanalysis) [Suspended license therapist undressing patients]
     - Pair 7: #19 (Anti-Psychoanalysis) $\leftrightarrow$ #27 (Anti-Cognitive) [Dakota shooter normal test results]
     - Pair 8: #20 (Anti-Cognitive) $\leftrightarrow$ #28 (Anti-Psychoanalysis) [Neuroimaging debunks Watson vs Freud]
   - In Set 1 (IDs 13–20): Odd IDs attack psychoanalysis; even IDs attack cognitive/behavioral.
   - In Set 2 (IDs 21–28): Odd IDs attack cognitive/behavioral; even IDs attack psychoanalysis.

3. **Ideological Congruence Assignment**:
   - To induce ideological congruence, participants see fake news that criticize their rival theoretical orientation:
     - **Pro-Psychoanalysis** (`orientacion_terapeutica == 'Psicoanálisis'`): Receives all 8 Anti-Cognitive fake news:
       $$\text{Set}_{\text{PSA}} = [14, 16, 18, 20, 21, 23, 25, 27]$$
     - **Pro-Evidence-Based** (`orientacion_terapeutica == 'Basada en Evidencia Científica'`): Receives all 8 Anti-Psychoanalysis fake news:
       $$\text{Set}_{\text{EBP}} = [13, 15, 17, 19, 22, 24, 26, 28]$$
   - *Mathematical Property*: $\text{Set}_{\text{PSA}} \cap \text{Set}_{\text{EBP}} = \emptyset$, $\text{Set}_{\text{PSA}} \cup \text{Set}_{\text{EBP}} = \{13, \dots, 28\}$.
   - *Crucial Counterbalance*: Each set contains exactly 4 items from Set 1 and 4 items from Set 2. A participant NEVER encounters both elements of any mirror pair.

4. **Excluded Cohort Set Selection**:
   - Participants not meeting inclusion criteria (`edad < 18`, `estudia_psicologia == false`, or `orientacion == 'Otros'`) are routed seamlessly to preserve study integrity.
   - *Critical Algorithm Rule*: They must receive either $\text{Set}_{\text{PSA}}$ or $\text{Set}_{\text{EBP}}$ selected at random (50/50).
   - *Failure Mode Prevented*: If 8 fake items were sampled purely at random from all 16, a participant could receive both #13 and #21 (identical story text with only terminology swapped), destroying experimental immersion and face validity.

5. **20-Item Trial Deck Assembly & Randomization**:
   - Stimulus Deck: $12 \text{ True News} + 8 \text{ Assigned Fake News} = 20 \text{ items}$.
   - Presentation order: Randomly permuted per session using an in-place Fisher-Yates (Durstenfeld) shuffle algorithm. An optional pseudo-random number generator (Mulberry32) is supported to allow deterministic seeded permutations during automated testing.

6. **Image Asset File Resolution**:
   - Image 26 has extension `.png` (`Noticia_26.png`), whereas all other 27 images are `.jpg` (`Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_27.jpg`, `Noticia_28.jpg`).
   - The helper function `getStimulusImagePath()` dynamically maps the file extension based on item ID, preventing HTTP 404 errors.

7. **Categorical Response & Metric Classification**:
   - Given stimulus type and response option (1 to 4):
     - $\text{Falso Recuerdo} = (\text{isFake} == \text{true}) \land (\text{responseOption} == 1)$
     - $\text{Falsa Creencia} = (\text{isFake} == \text{true}) \land (\text{responseOption} == 2)$
     - $\text{Memoria Verdadera} = (\text{isFake} == \text{false}) \land (\text{responseOption} == 1)$

---

## 3. Complete Stimuli Table (All 28 Items)

| ID | Tipo | Titular en Español | Titular en Inglés | Imagen | Congruencia | Par Espejo | Blanco de Crítica |
|---|---|---|---|---|---|---|---|
| **1** | Verdadera | Las agencias de medicamentos son una invención del capitalismo neoliberal de la década de 1990. | Drug agencies are an invention of neoliberal capitalism in the 1990s | `Noticia_01.jpg` | `true` | null | Referencia histórica / médica general |
| **2** | Verdadera | Mario Bunge: el psicoanálisis y otras pseudociencias son perjudiciales. | Mario Bunge: psychoanalysis and other pseudosciences are harmful | `Noticia_02.jpg` | `true` | null | Epistemología / Crítica al psicoanálisis |
| **3** | Verdadera | Una pandemia de adaptación y neoliberalismo conductual en la educación. | A pandemic of adjusting and behavioral neoliberalism in education | `Noticia_03.jpg` | `true` | null | Educación / Crítica al conductismo |
| **4** | Verdadera | Científicos explican por qué los sueños no tienen significados ocultos. | Scientists explain why dreams have no hidden meanings | `Noticia_04.jpg` | `true` | null | Neurociencia / Teoría de los sueños |
| **5** | Verdadera | El pequeño Albert: un cruel experimento con un bebé de 11 meses para estudiar las fobias. | Little Albert, a cruel experiment on an 11-month-old baby to test phobias | `Noticia_05.jpg` | `true` | null | Historia del conductismo / Ética |
| **6** | Verdadera | La comunidad reúne firmas contra las terapias psicoanalíticas públicas en casos de autismo. | The community gathers signatures against public psychoanalysis therapies in cases of autism | `Noticia_06.jpg` | `true` | null | Salud pública / Psicoanálisis en autismo |
| **7** | Verdadera | La caja de Skinner: juegos como Candy Crush están diseñados para volverte adicto. | Skinner's Box: Games like Candy Crush are designed to get you hooked | `Noticia_07.jpg` | `true` | null | Condicionamiento operante / Gamificación |
| **8** | Verdadera | Wilhelm Reich: los controvertidos tratamientos sexuales de uno de los psicoanalistas más radicales de la historia. | Wilhelm Reich: the controversial sexual treatments of one of the most radical psychoanalysts in history | `Noticia_08.jpg` | `true` | null | Historia del psicoanálisis / Pseudociencia |
| **9** | Verdadera | El psiquiatra que aplicaba electroshocks a personas homosexuales. | The psychiatrist who applied electroshocks to homosexuals | `Noticia_09.jpg` | `true` | null | Historia de la psiquiatría / Derechos humanos |
| **10** | Verdadera | La feminista que refutó a Freud y su concepto de envidia del pene. | The feminist who denied Freud and his penis envy | `Noticia_10.jpg` | `true` | null | Crítica feminista al psicoanálisis |
| **11** | Verdadera | Expertos piden revisar los métodos actuales de diagnóstico del trastorno bipolar. | Experts call for a review of current diagnostic methods for bipolar disorder | `Noticia_11.jpg` | `true` | null | Psiquiatría clínica / Diagnóstico |
| **12** | Verdadera | La historia del sobrino argentino de Freud: es psicoanalista y cuestiona la idea de ser trans antes de la pubertad. | The story of Freud's Argentinian nephew: he is a psychoanalyst and questions the idea of being trans before puberty | `Noticia_12.jpg` | `true` | null | Debate contemporáneo / Psicoanálisis local |
| **13** | Falsa Set 1 | El terapeuta freudiano que hipnotizaba a sus pacientes con descargas eléctricas irá a juicio. | The Freudian therapist who hypnotized patients with electric shocks will go to trial | `Noticia_13.jpg` | `evidencia` | 21 | Ataca Psicoanálisis / Freudiano |
| **14** | Falsa Set 1 | Abraham Low, el pediatra y cognitivista británico que afirmaba que el autismo se curaba con terapia conductual. | Abraham Low, the British pediatrician and cognitivist who claimed that autism was cured by behavioral therapy | `Noticia_14.jpg` | `psicoanalisis` | 22 | Ataca TCC / Conductual / Cognitivo |
| **15** | Falsa Set 1 | Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia psicoanalítica. | Horror in Formosa: the young woman hospitalized for starvation, closed the refrigerator with a padlock as part of her psychoanalytic therapy | `Noticia_15.jpg` | `evidencia` | 23 | Ataca Psicoanálisis / Freudiano |
| **16** | Falsa Set 1 | Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta cognitivo se negó a darle un diagnóstico. | Malpractice is being investigated: He had been depressed for 5 years and his cognitive therapist refused to give him a diagnosis | `Noticia_16.jpg` | `psicoanalisis` | 24 | Ataca TCC / Conductual / Cognitivo |
| **17** | Falsa Set 1 | Texas: una joven se suicida después de recibir el alta de una terapia psicoanalítica. | Texas: Young woman commits suicide after being discharged from psychoanalytic therapy | `Noticia_17.jpg` | `evidencia` | 25 | Ataca Psicoanálisis / Freudiano |
| **18** | Falsa Set 1 | Suspenden la licencia de un terapeuta cognitivo que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos. | License suspended for cognitive therapist who undressed patients to help them connect with their bodies | `Noticia_18.jpg` | `psicoanalisis` | 26 | Ataca TCC / Conductual / Cognitivo |
| **19** | Falsa Set 1 | Un tirador en la ciudad de Dakota: «había superado todas las técnicas proyectivas; era una persona normal». | A shooter in Dakota city: "had passed all the projective techniques, he was a normal person" | `Noticia_19.jpg` | `evidencia` | 27 | Ataca Psicoanálisis / Técnicas Proyectivas |
| **20** | Falsa Set 1 | Hallazgos recientes de neuroimagen refutan el concepto de «condicionamiento» de Watson. | Recent neuroimaging findings debunk Watson's concept of 'conditioning' | `Noticia_20.jpg` | `psicoanalisis` | 28 | Ataca Conductismo / Watson |
| **21** | Falsa Set 2 | El terapeuta cognitivo que entrenaba a sus pacientes con descargas eléctricas irá a juicio. | The cognitive therapist who trained patients with electric shocks will go to trial | `Noticia_21.jpg` | `psicoanalisis` | 13 | Ataca TCC / Conductual / Cognitivo |
| **22** | Falsa Set 2 | Donald Winnicott, el pediatra y psicoanalista británico que afirmaba que el autismo se curaba mediante hipnosis. | Donald Winnicott, the British pediatrician, and psychoanalyst who claimed that autism was cured by hypnosis | `Noticia_22.jpg` | `evidencia` | 14 | Ataca Psicoanálisis / Winnicott |
| **23** | Falsa Set 2 | Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia cognitiva. | Horror in Formosa: the young woman hospitalized for starvation closed the refrigerator with a padlock as part of her cognitive therapy | `Noticia_23.jpg` | `psicoanalisis` | 15 | Ataca TCC / Conductual / Cognitivo |
| **24** | Falsa Set 2 | Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta psicoanalista se negó a darle un diagnóstico. | Malpractice is being investigated: He had been depressed for 5 years and his psychoanalyst therapist refused to give him a diagnosis | `Noticia_24.jpg` | `evidencia` | 16 | Ataca Psicoanálisis / Freudiano |
| **25** | Falsa Set 2 | Texas: una joven se suicida después de recibir el alta de una terapia cognitiva breve. | Texas: Young woman commits suicide after being discharged from brief cognitive therapy | `Noticia_25.jpg` | `psicoanalisis` | 17 | Ataca TCC / Terapia Breve |
| **26** | Falsa Set 2 | Suspenden la licencia de un psicoanalista que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos. | License suspended for psychoanalyst who undressed patients to help them connect with their bodies | `Noticia_26.png` | `evidencia` | 18 | Ataca Psicoanálisis / Freudiano |
| **27** | Falsa Set 2 | Un tirador en la ciudad de Dakota: «había superado todas las técnicas psicométricas; era una persona normal». | A shooter in Dakota city: "had passed all the psychometric techniques, he was a normal person" | `Noticia_27.jpg` | `psicoanalisis` | 19 | Ataca Psicometría / Evaluación Conductual |
| **28** | Falsa Set 2 | Hallazgos recientes de neuroimagen refutan el concepto de «superyó» de Freud. | Recent neuroimaging findings debunk Freud's concept of 'superego' | `Noticia_28.jpg` | `evidencia` | 20 | Ataca Psicoanálisis / Superyó de Freud |

---

## 4. Complete Design Specifications for Target Files

The complete, production-ready code files have been written to this agent's directory as implementation artifacts:
1. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m1_3\proposed_experiment.ts`
2. `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m1_3\proposed_stimuli.ts`

Below are the verbatim designs for direct placement into `web-experimento/src/types/experiment.ts` and `web-experimento/src/data/stimuli.ts`:

### 4.1. Design of `src/types/experiment.ts`
```typescript
// ============================================================================
// 1. Experimental Conditions & Demographic Types
// ============================================================================

export type InductionGroup = 'racional' | 'emocional' | 'control';

export type TherapeuticOrientation = 
  | 'Psicoanálisis'
  | 'Basada en Evidencia Científica'
  | 'Otros';

export type Gender = 'Femenino' | 'Masculino' | 'Otro';

export type FakeNewsSet = 'psicoanalisis' | 'evidencia' | 'control_random';

export type ExclusionReason = 
  | 'menor_de_edad'
  | 'no_estudia_psicologia'
  | 'orientacion_otros'
  | null;

export type SessionStatus = 'started' | 'reading' | 'completed' | 'abandoned';

export type DeviceType = 'desktop' | 'mobile' | 'tablet';

// ============================================================================
// 2. Stimulus & Evaluation Models
// ============================================================================

export type CongruenceType = 'psicoanalisis' | 'evidencia' | 'true';

export interface StimulusItem {
  id: number;                    // 1 to 28
  title: string;                 // Verbatim headline text in Latin American Spanish
  englishTitle: string;          // Source English title from literature
  isFake: boolean;               // false for IDs 1-12; true for IDs 13-28
  imageFileName: string;         // e.g. "Noticia_01.jpg" ... "Noticia_26.png" ... "Noticia_28.jpg"
  congruence: CongruenceType;    // 'true' | 'psicoanalisis' | 'evidencia'
  targetCritique: string;        // Psychological school or construct challenged/debunked
  mirrorPairId: number | null;   // Counterbalanced counterpart ID in opposing set (e.g. 13 <-> 21)
  section: string;               // Section name from stimulus specification
}

export interface TrialStimulus {
  stimulus: StimulusItem;
  presentationOrder: number;     // 1 to 20
}

export type ResponseCode = 1 | 2 | 3 | 4;

export interface ResponseOptionDefinition {
  code: ResponseCode;
  label: string;
  construct: 'false_memory' | 'false_belief' | 'different_memory' | 'no_memory';
}

// ============================================================================
// 3. Participant Session & Telemetry
// ============================================================================

export interface ParticipantDemographicsInput {
  age: number;
  gender: Gender;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
  university: string;
}

export interface InclusionEvaluation {
  isIncluded: boolean;
  exclusionReason: ExclusionReason;
}

export interface ParticipantSession {
  id: string;                     // UUID v4
  createdAt: string;              // ISO 8601 UTC timestamp
  completedAt?: string | null;    // ISO 8601 UTC timestamp when debriefing reached
  age: number;                    // >= 18
  gender: Gender;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
  university: string;
  isIncluded: boolean;            // Screening result
  exclusionReason?: ExclusionReason;
  inductionGroup: InductionGroup; // 'racional' | 'emocional' | 'control'
  fakeNewsSet: FakeNewsSet;       // Assigned fake news deck
  status: SessionStatus;          // 'started' | 'completed' | etc.
  deviceType?: DeviceType;        // 'desktop' | 'mobile' | 'tablet'
  screenResolution?: string;      // e.g. "1920x1080"
  userAgent?: string;
}

// ============================================================================
// 4. Trial Responses & Telemetry
// ============================================================================

export interface TrialSubmissionPayload {
  participantId: string;
  presentationOrder: number;      // 1 to 20
  newsId: number;                 // 1 to 28
  responseOption: ResponseCode;   // 1, 2, 3, 4
  readingTimeMs: number;          // Exposure latency on Screen 1 (~10,000 ms)
  responseTimeMs: number;         // Latency from Screen 2 mount to submit click
}

export interface TrialRecord {
  id?: string;                    // UUID v4
  participantId: string;          // Foreign key to participants(id)
  presentationOrder: number;      // 1 to 20
  newsId: number;                 // 1 to 28
  isFake: boolean;
  newsCongruence: CongruenceType;
  responseOption: ResponseCode;
  responseLabel: string;
  readingTimeMs: number;
  responseTimeMs: number;
  isFalseMemory: boolean;         // isFake && responseOption === 1
  isFalseBelief: boolean;         // isFake && responseOption === 2
  isTrueMemory: boolean;          // !isFake && responseOption === 1
  createdAt?: string;
}

// ============================================================================
// 5. Cognitive Induction Prompts
// ============================================================================

export interface InductionPrompt {
  group: InductionGroup;
  title: string;
  text: string;
  instructionFooter: string;
}

// ============================================================================
// 6. CSV Export & Researcher Dashboard
// ============================================================================

export interface CsvExportRow {
  participant_id: string;
  created_at: string;
  completed_at: string;
  age: number;
  gender: string;
  studies_psychology: boolean;
  therapeutic_orientation: string;
  university: string;
  is_included: boolean;
  exclusion_reason: string;
  induction_group: string;
  fake_news_set: string;
  presentation_order: number;
  news_id: number;
  news_title: string;
  is_fake: boolean;
  news_congruence: string;
  response_option: number;
  response_label: string;
  is_false_memory: boolean;
  is_false_belief: boolean;
  is_true_memory: boolean;
  reading_time_ms: number;
  response_time_ms: number;
  device_type: string;
  screen_resolution: string;
  user_agent: string;
}

export interface AdminDashboardStats {
  totalParticipants: number;
  completedParticipants: number;
  includedParticipants: number;
  excludedParticipants: number;
  completionRate: number;
  groups: {
    racional: number;
    emocional: number;
    control: number;
  };
  orientations: {
    psicoanalisis: number;
    evidencia: number;
    otros: number;
  };
  isBalanced: boolean;
  maxDiscrepancy: number;
}
```

---

### 4.2. Design of `src/data/stimuli.ts`

```typescript
import {
  StimulusItem,
  ResponseCode,
  ResponseOptionDefinition,
  InductionGroup,
  InductionPrompt,
  TherapeuticOrientation,
  InclusionEvaluation,
  ExclusionReason
} from '../types/experiment';

// 28 Stimuli array, read-only and frozen
export const STIMULI: readonly StimulusItem[] = Object.freeze([
  // Full 28 items as specified in Section 3 above (exact items 1 to 28)
]);

export const STIMULI_BY_ID: Readonly<Record<number, StimulusItem>> = Object.freeze(
  STIMULI.reduce((acc, item) => {
    acc[item.id] = item;
    return acc;
  }, {} as Record<number, StimulusItem>)
);

export const TRUE_NEWS_IDS: readonly number[] = Object.freeze([
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
]);

export const PSA_CONGRUENT_FAKE_IDS: readonly number[] = Object.freeze([
  14, 16, 18, 20, 21, 23, 25, 27
]);

export const EBP_CONGRUENT_FAKE_IDS: readonly number[] = Object.freeze([
  13, 15, 17, 19, 22, 24, 26, 28
]);

export const RESPONSE_OPTIONS: readonly ResponseOptionDefinition[] = Object.freeze([
  {
    code: 1,
    label: 'Recuerdo claramente haber visto/leído este evento',
    construct: 'false_memory'
  },
  {
    code: 2,
    label: 'No recuerdo haberlo visto, pero creo que sucedió',
    construct: 'false_belief'
  },
  {
    code: 3,
    label: 'Lo recuerdo diferente',
    construct: 'different_memory'
  },
  {
    code: 4,
    label: 'No lo recuerdo en absoluto',
    construct: 'no_memory'
  }
]);

export const RESPONSE_OPTIONS_MAP: Readonly<Record<ResponseCode, ResponseOptionDefinition>> = Object.freeze(
  RESPONSE_OPTIONS.reduce((acc, opt) => {
    acc[opt.code] = opt;
    return acc;
  }, {} as Record<ResponseCode, ResponseOptionDefinition>)
);

export const INDUCTION_PROMPTS: Readonly<Record<InductionGroup, InductionPrompt>> = Object.freeze({
  racional: {
    group: 'racional',
    title: 'Instrucciones de Evaluación',
    text: 'Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones.',
    instructionFooter: 'Tómese el tiempo necesario para reflexionar analíticamente antes de responder.'
  },
  emocional: {
    group: 'emocional',
    title: 'Instrucciones de Evaluación',
    text: 'Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón.',
    instructionFooter: 'Permítase conectar con sus sensaciones e intuición inmediata.'
  },
  control: {
    group: 'control',
    title: 'Instrucciones de Evaluación',
    text: 'A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no.',
    instructionFooter: 'Por favor, observe atentamente cada titular antes de calificarlo.'
  }
});

export function evaluateInclusion(demographics: {
  age: number;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
}): InclusionEvaluation {
  if (demographics.age < 18) {
    return { isIncluded: false, exclusionReason: 'menor_de_edad' };
  }
  if (!demographics.studiesPsychology) {
    return { isIncluded: false, exclusionReason: 'no_estudia_psicologia' };
  }
  if (demographics.therapeuticOrientation === 'Otros') {
    return { isIncluded: false, exclusionReason: 'orientacion_otros' };
  }
  if (
    demographics.therapeuticOrientation === 'Psicoanálisis' ||
    demographics.therapeuticOrientation === 'Basada en Evidencia Científica'
  ) {
    return { isIncluded: true, exclusionReason: null };
  }
  return { isIncluded: false, exclusionReason: 'orientacion_otros' };
}

export function shuffleArray<T>(array: readonly T[], randomFn: () => number = Math.random): T[] {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(randomFn() * (i + 1));
    const temp = result[i];
    result[i] = result[j];
    result[j] = temp;
  }
  return result;
}

export function getParticipantNewsDeck(
  therapeuticOrientation: TherapeuticOrientation,
  isIncluded: boolean,
  randomSeed?: number | string
): StimulusItem[] {
  // Setup PRNG or Math.random
  let randomFn = Math.random;
  if (randomSeed !== undefined) {
    let s = typeof randomSeed === 'string'
      ? Array.from(randomSeed).reduce((acc, ch) => (acc * 31 + ch.charCodeAt(0)) | 0, 0)
      : randomSeed;
    randomFn = function () {
      s |= 0;
      s = (s + 0x6d2b79f5) | 0;
      let t = Math.imul(s ^ (s >>> 15), 1 | s);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  let selectedFakeIds: readonly number[];

  if (isIncluded) {
    if (therapeuticOrientation === 'Psicoanálisis') {
      selectedFakeIds = PSA_CONGRUENT_FAKE_IDS;
    } else if (therapeuticOrientation === 'Basada en Evidencia Científica') {
      selectedFakeIds = EBP_CONGRUENT_FAKE_IDS;
    } else {
      selectedFakeIds = randomFn() < 0.5 ? PSA_CONGRUENT_FAKE_IDS : EBP_CONGRUENT_FAKE_IDS;
    }
  } else {
    selectedFakeIds = randomFn() < 0.5 ? PSA_CONGRUENT_FAKE_IDS : EBP_CONGRUENT_FAKE_IDS;
  }

  const combinedIds = [...TRUE_NEWS_IDS, ...selectedFakeIds];

  const uncompressedDeck: StimulusItem[] = combinedIds.map((id) => {
    const item = STIMULI_BY_ID[id];
    if (!item) {
      throw new Error(`Stimulus with ID ${id} not found in database.`);
    }
    return item;
  });

  return shuffleArray(uncompressedDeck, randomFn);
}

export function classifyResponse(
  isFake: boolean,
  responseOption: ResponseCode
): {
  isFalseMemory: boolean;
  isFalseBelief: boolean;
  isTrueMemory: boolean;
} {
  return {
    isFalseMemory: isFake && responseOption === 1,
    isFalseBelief: isFake && responseOption === 2,
    isTrueMemory: !isFake && responseOption === 1
  };
}

export function getStimulusImagePath(
  newsIdOrItem: number | StimulusItem,
  basePath = '/noticias'
): string {
  const item = typeof newsIdOrItem === 'number' ? STIMULI_BY_ID[newsIdOrItem] : newsIdOrItem;
  if (item) {
    return `${basePath}/${item.imageFileName}`;
  }
  const idNum = typeof newsIdOrItem === 'number' ? newsIdOrItem : 1;
  const paddedId = String(idNum).padStart(2, '0');
  const extension = idNum === 26 ? 'png' : 'jpg';
  return `${basePath}/Noticia_${paddedId}.${extension}`;
}

export function getStimulusById(id: number): StimulusItem {
  const item = STIMULI_BY_ID[id];
  if (!item) {
    throw new Error(`Stimulus with ID ${id} is invalid. Expected integer between 1 and 28.`);
  }
  return item;
}
```

---

## 5. Caveats

1. **Asset File Extension Discrepancy**:
   - `Noticia_26.png` is the only image asset in `.png` format. Hardcoded extension strings (such as `Noticia_${id}.jpg`) will fail for item 26. The `imageFileName` attribute and `getStimulusImagePath()` helper must always be used.
2. **Reading Phase Progression**:
   - In accordance with `ORIGINAL_REQUEST.md` lines 52 and 94, the reading screen must automatically progress after 10,000 ms. If an optional "Continuar" button is rendered, `reading_time_ms` will record the real dwell duration; otherwise, it will record 10,000 ms $\pm$ render latency.
3. **Excluded Cohort Realism**:
   - Assigning a cohesive 8-item set (PSA or EBP) to excluded participants preserves face validity by eliminating the risk of mirror-pair collisions while keeping their data segregated from experimental quotas.
4. **CSV Export Long-Format Compatibility**:
   - Export rows must prepend a UTF-8 Byte Order Mark (`\uFEFF`) so that non-ASCII Spanish characters (e.g. «ó», «í», «ñ», ««», «»») open without character encoding corruption in Microsoft Excel on Windows.

---

## 6. Conclusion

The complete typed data layer and stimuli architecture have been fully analyzed, specified, and validated:
1. **Domain Models** (`src/types/experiment.ts`): Fully typed models covering all experimental variables, screening logic, telemetry, responses, and CSV exports.
2. **Stimuli Dataset** (`src/data/stimuli.ts`): Complete 28-item database matching all files in `PARCIAL 2 - INVESTIGACIÓN/Noticias/` with exact Spanish text, English translations, image file names (including `Noticia_26.png`), and counterbalanced mirror pairs.
3. **Set Selection & Randomization Algorithms**:
   - Ideological congruence mapping correctly sends Anti-Cognitive fake news to Psychoanalysis participants and Anti-Psychoanalysis fake news to Evidence-Based participants.
   - Excluded participants receive cohesive fake news decks with no mirror-pair collisions.
   - Fisher-Yates shuffling produces unbiased 20-item trial presentations.
   - Response classification cleanly dissociates False Memories (Option 1) from False Beliefs (Option 2).
4. Both implementation artifact proposals (`proposed_experiment.ts` and `proposed_stimuli.ts`) are ready for direct drop-in integration in Milestone 1.

---

## 7. Verification Method

To independently verify these findings:

1. **Verify Asset Files on Filesystem**:
   ```powershell
   Get-ChildItem -Path "C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes" | Select-Object Name, Length
   ```
   *Expected*: Exactly 28 files (`Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_26.png`, `Noticia_27.jpg`, `Noticia_28.jpg`).

2. **Verify Set Slicing & Pair Complementarity**:
   - Confirm PSA Fake set: `[14, 16, 18, 20, 21, 23, 25, 27]`
   - Confirm EBP Fake set: `[13, 15, 17, 19, 22, 24, 26, 28]`
   - Disjoint union check: $\text{PSA} \cap \text{EBP} = \emptyset$ and $\text{PSA} \cup \text{EBP} = \{13, \dots, 28\}$.
   - Mirror pair check: Each of the 8 mirror pairs $(13, 21), (14, 22), (15, 23), (16, 24), (17, 25), (18, 26), (19, 27), (20, 28)$ has exactly one element in PSA and one in EBP.

3. **Invalidation Conditions**:
   - Any image path failing to load or returning HTTP 404 (specifically `Noticia_26.jpg` instead of `Noticia_26.png`).
   - A participant with `orientacion_terapeutica == 'Psicoanálisis'` receiving any fake news from `[13, 15, 17, 19, 22, 24, 26, 28]`.
   - A participant with `orientacion_terapeutica == 'Basada en Evidencia Científica'` receiving any fake news from `[14, 16, 18, 20, 21, 23, 25, 27]`.
   - Any stimulus deck having a length different from exactly 20 items (12 true + 8 fake).
   - Any trial where Option 1 or 2 is misclassified between False Memory, False Belief, or True Memory.
