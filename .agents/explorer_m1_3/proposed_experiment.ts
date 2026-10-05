/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Parcial 2 - Investigación: Efecto de la Inducción Cognitiva sobre Falsos Recuerdos
 * 
 * Domain Models & Type Definitions
 * Target location: src/types/experiment.ts
 */

// ============================================================================
// 1. Experimental Conditions & Demographic Types
// ============================================================================

/**
 * Three-level between-subjects independent variable: Cognitive Induction
 * - 'racional': Prime emphasizing logical, analytical reasoning
 * - 'emocional': Prime emphasizing emotional, intuitive feelings
 * - 'control': Neutral baseline instructions
 */
export type InductionGroup = 'racional' | 'emocional' | 'control';

/**
 * Self-reported therapeutic orientation of the participant
 * Used to evaluate inclusion criteria and determine ideological congruence.
 */
export type TherapeuticOrientation = 
  | 'Psicoanálisis'
  | 'Basada en Evidencia Científica'
  | 'Otros';

/**
 * Self-reported gender of the participant
 */
export type Gender = 'Femenino' | 'Masculino' | 'Otro';

/**
 * Fake news set assigned to the participant
 * - 'psicoanalisis': 8 fake news attacking cognitive/behavioral therapy (IDs: 14, 16, 18, 20, 21, 23, 25, 27)
 * - 'evidencia': 8 fake news attacking psychoanalysis/Freudian theory (IDs: 13, 15, 17, 19, 22, 24, 26, 28)
 * - 'control_random': Random cohesive selection of PSA or EBP set for excluded participants
 */
export type FakeNewsSet = 'psicoanalisis' | 'evidencia' | 'control_random';

/**
 * Reason for screening exclusion
 */
export type ExclusionReason = 
  | 'menor_de_edad'
  | 'no_estudia_psicologia'
  | 'orientacion_otros'
  | null;

/**
 * Current lifecycle status of an experimental session
 */
export type SessionStatus = 'started' | 'reading' | 'completed' | 'abandoned';

/**
 * Client device category detected via user-agent / screen properties
 */
export type DeviceType = 'desktop' | 'mobile' | 'tablet';

// ============================================================================
// 2. Stimulus & Evaluation Models
// ============================================================================

/**
 * Ideological congruence classification:
 * - 'psicoanalisis': Fake news confirming psychoanalytic worldview (attacks CBT)
 * - 'evidencia': Fake news confirming evidence-based worldview (attacks psychoanalysis)
 * - 'true': Real baseline news from 2017-2018 (shown to all participants)
 */
export type CongruenceType = 'psicoanalisis' | 'evidencia' | 'true';

/**
 * Individual stimulus headline item (28 items total in the experiment universe)
 */
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

/**
 * Trial stimulus wrapper attaching presentation order for a session
 */
export interface TrialStimulus {
  stimulus: StimulusItem;
  presentationOrder: number;     // 1 to 20
}

/**
 * 4-Point categorical response options (Murphy et al., 2021 / León et al., 2023 scale)
 * 1: Recuerdo claramente haber visto/leído este evento (Falso Recuerdo / Memoria Verdadera)
 * 2: No recuerdo haberlo visto, pero creo que sucedió (Falsa Creencia)
 * 3: Lo recuerdo diferente
 * 4: No lo recuerdo en absoluto
 */
export type ResponseCode = 1 | 2 | 3 | 4;

export interface ResponseOptionDefinition {
  code: ResponseCode;
  label: string;
  construct: 'false_memory' | 'false_belief' | 'different_memory' | 'no_memory';
}

// ============================================================================
// 3. Participant Session & Telemetry
// ============================================================================

/**
 * Demographic data submitted by the participant in Screen 3
 */
export interface ParticipantDemographicsInput {
  age: number;
  gender: Gender;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
  university: string;
}

/**
 * Screening evaluation result
 */
export interface InclusionEvaluation {
  isIncluded: boolean;
  exclusionReason: ExclusionReason;
}

/**
 * Complete participant session record persisted in Supabase `participants` table
 */
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

/**
 * Single trial submission payload from client
 */
export interface TrialSubmissionPayload {
  participantId: string;
  presentationOrder: number;      // 1 to 20
  newsId: number;                 // 1 to 28
  responseOption: ResponseCode;   // 1, 2, 3, 4
  readingTimeMs: number;          // Exposure latency on Screen 1 (~10,000 ms)
  responseTimeMs: number;         // Latency from Screen 2 mount to submit click
}

/**
 * Complete trial record persisted in Supabase `responses` table
 */
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

/**
 * Long-format row for researcher CSV export (20 rows per participant)
 * Encoded with UTF-8 BOM for seamless import into Excel, SPSS, R, Jamovi.
 */
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

/**
 * Aggregate summary metrics for Admin Dashboard
 */
export interface AdminDashboardStats {
  totalParticipants: number;
  completedParticipants: number;
  includedParticipants: number;
  excludedParticipants: number;
  completionRate: number;         // percentage (0-100)
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
  isBalanced: boolean;            // max discrepancy <= 2 across included induction groups
  maxDiscrepancy: number;
}
