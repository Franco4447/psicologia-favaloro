/**
 * Universidad Favaloro - Cátedra de Psicología Experimental
 * Parcial 2 - Investigación: Efecto de la Inducción Cognitiva sobre Falsos Recuerdos
 * 
 * Stimuli Database & Set Selection Algorithms
 * Target location: src/data/stimuli.ts
 */

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

// ============================================================================
// 1. Complete Stimuli Inventory (All 28 Items)
// ============================================================================

export const STIMULI: readonly StimulusItem[] = Object.freeze([
  // --------------------------------------------------------------------------
  // 1. Noticias verdaderas (True News) — IDs 1 to 12
  // Baseline real news items from 2017-2018 presented to all participants
  // --------------------------------------------------------------------------
  {
    id: 1,
    title: 'Las agencias de medicamentos son una invención del capitalismo neoliberal de la década de 1990.',
    englishTitle: 'Drug agencies are an invention of neoliberal capitalism in the 1990s',
    isFake: false,
    imageFileName: 'Noticia_01.jpg',
    congruence: 'true',
    targetCritique: 'Referencia histórica / médica general',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 2,
    title: 'Mario Bunge: el psicoanálisis y otras pseudociencias son perjudiciales.',
    englishTitle: 'Mario Bunge: psychoanalysis and other pseudosciences are harmful',
    isFake: false,
    imageFileName: 'Noticia_02.jpg',
    congruence: 'true',
    targetCritique: 'Epistemología / Crítica al psicoanálisis',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 3,
    title: 'Una pandemia de adaptación y neoliberalismo conductual en la educación.',
    englishTitle: 'A pandemic of adjusting and behavioral neoliberalism in education',
    isFake: false,
    imageFileName: 'Noticia_03.jpg',
    congruence: 'true',
    targetCritique: 'Educación / Crítica al conductismo',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 4,
    title: 'Científicos explican por qué los sueños no tienen significados ocultos.',
    englishTitle: 'Scientists explain why dreams have no hidden meanings',
    isFake: false,
    imageFileName: 'Noticia_04.jpg',
    congruence: 'true',
    targetCritique: 'Neurociencia / Teoría de los sueños',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 5,
    title: 'El pequeño Albert: un cruel experimento con un bebé de 11 meses para estudiar las fobias.',
    englishTitle: 'Little Albert, a cruel experiment on an 11-month-old baby to test phobias',
    isFake: false,
    imageFileName: 'Noticia_05.jpg',
    congruence: 'true',
    targetCritique: 'Historia del conductismo / Ética',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 6,
    title: 'La comunidad reúne firmas contra las terapias psicoanalíticas públicas en casos de autismo.',
    englishTitle: 'The community gathers signatures against public psychoanalysis therapies in cases of autism',
    isFake: false,
    imageFileName: 'Noticia_06.jpg',
    congruence: 'true',
    targetCritique: 'Salud pública / Psicoanálisis en autismo',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 7,
    title: 'La caja de Skinner: juegos como Candy Crush están diseñados para volverte adicto.',
    englishTitle: "Skinner's Box: Games like Candy Crush are designed to get you hooked",
    isFake: false,
    imageFileName: 'Noticia_07.jpg',
    congruence: 'true',
    targetCritique: 'Condicionamiento operante / Gamificación',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 8,
    title: 'Wilhelm Reich: los controvertidos tratamientos sexuales de uno de los psicoanalistas más radicales de la historia.',
    englishTitle: 'Wilhelm Reich: the controversial sexual treatments of one of the most radical psychoanalysts in history',
    isFake: false,
    imageFileName: 'Noticia_08.jpg',
    congruence: 'true',
    targetCritique: 'Historia del psicoanálisis / Pseudociencia',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 9,
    title: 'El psiquiatra que aplicaba electroshocks a personas homosexuales.',
    englishTitle: 'The psychiatrist who applied electroshocks to homosexuals',
    isFake: false,
    imageFileName: 'Noticia_09.jpg',
    congruence: 'true',
    targetCritique: 'Historia de la psiquiatría / Derechos humanos',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 10,
    title: 'La feminista que refutó a Freud y su concepto de envidia del pene.',
    englishTitle: 'The feminist who denied Freud and his penis envy',
    isFake: false,
    imageFileName: 'Noticia_10.jpg',
    congruence: 'true',
    targetCritique: 'Crítica feminista al psicoanálisis',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 11,
    title: 'Expertos piden revisar los métodos actuales de diagnóstico del trastorno bipolar.',
    englishTitle: 'Experts call for a review of current diagnostic methods for bipolar disorder',
    isFake: false,
    imageFileName: 'Noticia_11.jpg',
    congruence: 'true',
    targetCritique: 'Psiquiatría clínica / Diagnóstico',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },
  {
    id: 12,
    title: 'La historia del sobrino argentino de Freud: es psicoanalista y cuestiona la idea de ser trans antes de la pubertad.',
    englishTitle: "The story of Freud's Argentinian nephew: he is a psychoanalyst and questions the idea of being trans before puberty",
    isFake: false,
    imageFileName: 'Noticia_12.jpg',
    congruence: 'true',
    targetCritique: 'Debate contemporáneo / Psicoanálisis local',
    mirrorPairId: null,
    section: '1. Noticias verdaderas (True News)'
  },

  // --------------------------------------------------------------------------
  // 2. Noticias falsas – Conjunto 1 (Fake News Set 1) — IDs 13 to 20
  // Odd IDs: Attack Psychoanalysis (Congruent to Evidence-Based)
  // Even IDs: Attack Cognitive/Behavioral (Congruent to Psychoanalysis)
  // --------------------------------------------------------------------------
  {
    id: 13,
    title: 'El terapeuta freudiano que hipnotizaba a sus pacientes con descargas eléctricas irá a juicio.',
    englishTitle: 'The Freudian therapist who hypnotized patients with electric shocks will go to trial',
    isFake: true,
    imageFileName: 'Noticia_13.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Freudiano',
    mirrorPairId: 21,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 14,
    title: 'Abraham Low, el pediatra y cognitivista británico que afirmaba que el autismo se curaba con terapia conductual.',
    englishTitle: 'Abraham Low, the British pediatrician and cognitivist who claimed that autism was cured by behavioral therapy',
    isFake: true,
    imageFileName: 'Noticia_14.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Conductual / Cognitivo',
    mirrorPairId: 22,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 15,
    title: 'Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia psicoanalítica.',
    englishTitle: 'Horror in Formosa: the young woman hospitalized for starvation, closed the refrigerator with a padlock as part of her psychoanalytic therapy',
    isFake: true,
    imageFileName: 'Noticia_15.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Freudiano',
    mirrorPairId: 23,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 16,
    title: 'Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta cognitivo se negó a darle un diagnóstico.',
    englishTitle: 'Malpractice is being investigated: He had been depressed for 5 years and his cognitive therapist refused to give him a diagnosis',
    isFake: true,
    imageFileName: 'Noticia_16.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Conductual / Cognitivo',
    mirrorPairId: 24,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 17,
    title: 'Texas: una joven se suicida después de recibir el alta de una terapia psicoanalítica.',
    englishTitle: 'Texas: Young woman commits suicide after being discharged from psychoanalytic therapy',
    isFake: true,
    imageFileName: 'Noticia_17.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Freudiano',
    mirrorPairId: 25,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 18,
    title: 'Suspenden la licencia de un terapeuta cognitivo que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos.',
    englishTitle: 'License suspended for cognitive therapist who undressed patients to help them connect with their bodies',
    isFake: true,
    imageFileName: 'Noticia_18.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Conductual / Cognitivo',
    mirrorPairId: 26,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 19,
    title: 'Un tirador en la ciudad de Dakota: «había superado todas las técnicas proyectivas; era una persona normal».',
    englishTitle: 'A shooter in Dakota city: "had passed all the projective techniques, he was a normal person"',
    isFake: true,
    imageFileName: 'Noticia_19.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Técnicas Proyectivas',
    mirrorPairId: 27,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },
  {
    id: 20,
    title: 'Hallazgos recientes de neuroimagen refutan el concepto de «condicionamiento» de Watson.',
    englishTitle: "Recent neuroimaging findings debunk Watson's concept of 'conditioning'",
    isFake: true,
    imageFileName: 'Noticia_20.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca Conductismo / Watson',
    mirrorPairId: 28,
    section: '2. Noticias falsas – Conjunto 1 (Fake News Set 1)'
  },

  // --------------------------------------------------------------------------
  // 3. Noticias falsas – Conjunto 2 (Fake News Set 2) — IDs 21 to 28
  // Odd IDs: Attack Cognitive/Behavioral (Congruent to Psychoanalysis)
  // Even IDs: Attack Psychoanalysis (Congruent to Evidence-Based)
  // --------------------------------------------------------------------------
  {
    id: 21,
    title: 'El terapeuta cognitivo que entrenaba a sus pacientes con descargas eléctricas irá a juicio.',
    englishTitle: 'The cognitive therapist who trained patients with electric shocks will go to trial',
    isFake: true,
    imageFileName: 'Noticia_21.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Conductual / Cognitivo',
    mirrorPairId: 13,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 22,
    title: 'Donald Winnicott, el pediatra y psicoanalista británico que afirmaba que el autismo se curaba mediante hipnosis.',
    englishTitle: 'Donald Winnicott, the British pediatrician, and psychoanalyst who claimed that autism was cured by hypnosis',
    isFake: true,
    imageFileName: 'Noticia_22.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Winnicott',
    mirrorPairId: 14,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 23,
    title: 'Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia cognitiva.',
    englishTitle: 'Horror in Formosa: the young woman hospitalized for starvation closed the refrigerator with a padlock as part of her cognitive therapy',
    isFake: true,
    imageFileName: 'Noticia_23.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Conductual / Cognitivo',
    mirrorPairId: 15,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 24,
    title: 'Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta psicoanalista se negó a darle un diagnóstico.',
    englishTitle: 'Malpractice is being investigated: He had been depressed for 5 years and his psychoanalyst therapist refused to give him a diagnosis',
    isFake: true,
    imageFileName: 'Noticia_24.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Freudiano',
    mirrorPairId: 16,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 25,
    title: 'Texas: una joven se suicida después de recibir el alta de una terapia cognitiva breve.',
    englishTitle: 'Texas: Young woman commits suicide after being discharged from brief cognitive therapy',
    isFake: true,
    imageFileName: 'Noticia_25.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca TCC / Terapia Breve',
    mirrorPairId: 17,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 26,
    title: 'Suspenden la licencia de un psicoanalista que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos.',
    englishTitle: 'License suspended for psychoanalyst who undressed patients to help them connect with their bodies',
    isFake: true,
    imageFileName: 'Noticia_26.png', // NOTE: CRITICAL VARIATION - THIS ASSET IS A PNG FILE
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Freudiano',
    mirrorPairId: 18,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 27,
    title: 'Un tirador en la ciudad de Dakota: «había superado todas las técnicas psicométricas; era una persona normal».',
    englishTitle: 'A shooter in Dakota city: "had passed all the psychometric techniques, he was a normal person"',
    isFake: true,
    imageFileName: 'Noticia_27.jpg',
    congruence: 'psicoanalisis',
    targetCritique: 'Ataca Psicometría / Evaluación Conductual',
    mirrorPairId: 19,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  },
  {
    id: 28,
    title: 'Hallazgos recientes de neuroimagen refutan el concepto de «superyó» de Freud.',
    englishTitle: "Recent neuroimaging findings debunk Freud's concept of 'superego'",
    isFake: true,
    imageFileName: 'Noticia_28.jpg',
    congruence: 'evidencia',
    targetCritique: 'Ataca Psicoanálisis / Superyó de Freud',
    mirrorPairId: 20,
    section: '3. Noticias falsas – Conjunto 2 (Fake News Set 2)'
  }
]);

// ============================================================================
// 2. Lookups & Partitioned ID Subsets
// ============================================================================

/** Fast map indexing stimulus items by their numerical ID (1 to 28) */
export const STIMULI_BY_ID: Readonly<Record<number, StimulusItem>> = Object.freeze(
  STIMULI.reduce((acc, item) => {
    acc[item.id] = item;
    return acc;
  }, {} as Record<number, StimulusItem>)
);

/**
 * 12 True news baseline IDs shown to every participant
 */
export const TRUE_NEWS_IDS: readonly number[] = Object.freeze([
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
]);

/**
 * 8 Fake news IDs ideologically congruent with Psychoanalysis
 * (Attacks cognitive, behavioral, or psychometric methods)
 */
export const PSA_CONGRUENT_FAKE_IDS: readonly number[] = Object.freeze([
  14, 16, 18, 20, 21, 23, 25, 27
]);

/**
 * 8 Fake news IDs ideologically congruent with Evidence-Based Practice
 * (Attacks psychoanalysis, Freudian theory, or projective tests)
 */
export const EBP_CONGRUENT_FAKE_IDS: readonly number[] = Object.freeze([
  13, 15, 17, 19, 22, 24, 26, 28
]);

// ============================================================================
// 3. Response Scale Definitions (Murphy / León 4-Point Scale)
// ============================================================================

export const RESPONSE_OPTIONS: readonly ResponseOptionDefinition[] = Object.freeze([
  {
    code: 1,
    label: 'Recuerdo claramente haber visto/leído este evento',
    construct: 'false_memory' // Or true_memory on real news
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

// ============================================================================
// 4. Cognitive Induction Verbatim Prompts
// ============================================================================

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

// ============================================================================
// 5. Screening & Inclusion Evaluation Algorithm
// ============================================================================

/**
 * Evaluates whether a participant meets the academic inclusion criteria:
 * 1. Must be >= 18 years of age.
 * 2. Must be an active student or practitioner of Psychology (`studiesPsychology === true`).
 * 3. Must declare affinity with either 'Psicoanálisis' or 'Basada en Evidencia Científica'.
 * 
 * Participants answering 'Otros' or not studying psychology are routed through the
 * Control condition with a cohesive fake set, but marked as excluded to prevent quota skew.
 */
export function evaluateInclusion(demographics: {
  age: number;
  studiesPsychology: boolean;
  therapeuticOrientation: TherapeuticOrientation;
}): InclusionEvaluation {
  if (demographics.age < 18) {
    return {
      isIncluded: false,
      exclusionReason: 'menor_de_edad'
    };
  }

  if (!demographics.studiesPsychology) {
    return {
      isIncluded: false,
      exclusionReason: 'no_estudia_psicologia'
    };
  }

  if (demographics.therapeuticOrientation === 'Otros') {
    return {
      isIncluded: false,
      exclusionReason: 'orientacion_otros'
    };
  }

  if (
    demographics.therapeuticOrientation === 'Psicoanálisis' ||
    demographics.therapeuticOrientation === 'Basada en Evidencia Científica'
  ) {
    return {
      isIncluded: true,
      exclusionReason: null
    };
  }

  return {
    isIncluded: false,
    exclusionReason: 'orientacion_otros'
  };
}

// ============================================================================
// 6. Set Selection & Randomization Algorithms
// ============================================================================

/**
 * Simple pseudo-random number generator (Mulberry32) for deterministic testing.
 * When seed is omitted, Math.random is used.
 */
function createPrng(seed?: number | string): () => number {
  if (seed === undefined) {
    return Math.random;
  }
  let s = typeof seed === 'string' 
    ? Array.from(seed).reduce((acc, ch) => (acc * 31 + ch.charCodeAt(0)) | 0, 0)
    : seed;
  return function () {
    s |= 0;
    s = (s + 0x6d2b79f5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * Generic Fisher-Yates (Durstenfeld) array shuffle algorithm.
 * Guarantees an unbiased, uniform random permutation of elements.
 */
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

/**
 * Assembles the tailored 20-news stimulus deck for a given participant session:
 * 
 * 1. Collects the 12 True News items (IDs 1-12).
 * 2. Selects the 8 Fake News items:
 *    - If participant is included and adheres to 'Psicoanálisis':
 *      -> assigns the 8 Anti-Cognitive fake items: [14, 16, 18, 20, 21, 23, 25, 27]
 *    - If participant is included and adheres to 'Basada en Evidencia Científica':
 *      -> assigns the 8 Anti-Psychoanalysis fake items: [13, 15, 17, 19, 22, 24, 26, 28]
 *    - If participant is excluded (e.g. orientation 'Otros' or non-psychology):
 *      -> assigns one cohesive set of 8 items (PSA or EBP) selected at random (50/50).
 *      -> CRITICAL: Never randomly draws 8 items from the 16 fake items independently,
 *         which would cause mirror-pair collisions (e.g., showing both #13 and #21).
 * 3. Combines the 20 items (12 true + 8 fake).
 * 4. Applies a complete Fisher-Yates shuffle to randomize presentation order.
 * 
 * @param therapeuticOrientation Participant's stated orientation
 * @param isIncluded Whether participant satisfied the screening criteria
 * @param randomSeed Optional seed for reproducible automated testing
 * @returns Array of 20 randomized StimulusItem objects
 */
export function getParticipantNewsDeck(
  therapeuticOrientation: TherapeuticOrientation,
  isIncluded: boolean,
  randomSeed?: number | string
): StimulusItem[] {
  const prng = createPrng(randomSeed);

  let selectedFakeIds: readonly number[];

  if (isIncluded) {
    if (therapeuticOrientation === 'Psicoanálisis') {
      selectedFakeIds = PSA_CONGRUENT_FAKE_IDS;
    } else if (therapeuticOrientation === 'Basada en Evidencia Científica') {
      selectedFakeIds = EBP_CONGRUENT_FAKE_IDS;
    } else {
      // Fallback for safety
      selectedFakeIds = prng() < 0.5 ? PSA_CONGRUENT_FAKE_IDS : EBP_CONGRUENT_FAKE_IDS;
    }
  } else {
    // Excluded participant: Choose between cohesive PSA set or EBP set with 50% probability
    // to preserve narrative coherence and avoid mirror-pair collisions.
    selectedFakeIds = prng() < 0.5 ? PSA_CONGRUENT_FAKE_IDS : EBP_CONGRUENT_FAKE_IDS;
  }

  // Combine 12 true news IDs + 8 assigned fake news IDs = exactly 20 items
  const combinedIds = [...TRUE_NEWS_IDS, ...selectedFakeIds];

  if (combinedIds.length !== 20) {
    throw new Error(`Expected exactly 20 news items, but received ${combinedIds.length}`);
  }

  // Map IDs to full StimulusItem objects
  const uncompressedDeck: StimulusItem[] = combinedIds.map((id) => {
    const item = STIMULI_BY_ID[id];
    if (!item) {
      throw new Error(`Stimulus with ID ${id} not found in database.`);
    }
    return item;
  });

  // Perform Fisher-Yates shuffle
  return shuffleArray(uncompressedDeck, prng);
}

// ============================================================================
// 7. Telemetry & Metric Classification Helpers
// ============================================================================

/**
 * Classifies a participant's response according to the experimental design:
 * - False Memory: Option 1 on Fake news
 * - False Belief: Option 2 on Fake news
 * - True Memory: Option 1 on True news
 */
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

/**
 * Resolves the public URL path for a stimulus image asset.
 * Automatically accounts for the unique `.png` extension of Noticia_26.
 * 
 * @param newsIdOrItem Number (1-28) or StimulusItem object
 * @param basePath Base path where assets are hosted (default: '/noticias')
 * @returns Fully qualified relative URL (e.g. "/noticias/Noticia_01.jpg" or "/noticias/Noticia_26.png")
 */
export function getStimulusImagePath(
  newsIdOrItem: number | StimulusItem,
  basePath = '/noticias'
): string {
  const item = typeof newsIdOrItem === 'number' ? STIMULI_BY_ID[newsIdOrItem] : newsIdOrItem;

  if (item) {
    return `${basePath}/${item.imageFileName}`;
  }

  // Fallback if numerical ID given not found in registry
  const idNum = typeof newsIdOrItem === 'number' ? newsIdOrItem : 1;
  const paddedId = String(idNum).padStart(2, '0');
  const extension = idNum === 26 ? 'png' : 'jpg';
  return `${basePath}/Noticia_${paddedId}.${extension}`;
}

/**
 * Retrieves a stimulus item by numerical ID with bounds checking
 */
export function getStimulusById(id: number): StimulusItem {
  const item = STIMULI_BY_ID[id];
  if (!item) {
    throw new Error(`Stimulus with ID ${id} is invalid. Expected integer between 1 and 28.`);
  }
  return item;
}
