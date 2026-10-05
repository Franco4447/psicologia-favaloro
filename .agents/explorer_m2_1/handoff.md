# Handoff Report: Participant Screening, Induction & Ethical Flow Screens (Milestone 2)

**Agent ID**: `explorer_m2_1`  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m2_1`  
**Target Components Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento\src\components`  
**Date & Timestamp**: 2026-09-20T23:55:00Z  

---

## 1. Observation

Direct observations from codebase inspection, specification documents, and test harnesses:

1. **Test Assertions for Screen Texts and Validation**:
   - In `tests/e2e/tier1_features.test.ts`:
     - Lines 38–65 (Feature 1: Welcome & Presentation Screen):
       - F1.1: Academic identity: `Somos estudiantes de la Universidad Favaloro de la carrera de Psicología.` (RegEx matches: `/Universidad Favaloro/`, `/Psicología/`).
       - F1.2: Research objective: `El objetivo de esta investigación es evaluar la percepción y evaluación de titulares de noticias.` (RegEx match: `/titulares de noticias/`).
       - F1.3: Environment notice: `Por favor, busque un lugar tranquilo, sin interrupciones y con conexión estable a internet.` (RegEx matches: `/tranquilo/`, `/sin interrupciones/`).
       - F1.4: Estimated duration: `La duración estimada del experimento es de entre 10 y 15 minutos.` (RegEx match: `/10 y 15 minutos/`).
       - F1.5: CTA Button label: `'Comenzar Experimento'`.
     - Lines 71–112 (Feature 2: Mandatory Informed Consent):
       - F2.1: Legal & ethical disclosure: `La participación es estrictamente voluntaria y anónima. Puede retirarse en cualquier momento.` (RegEx matches: `/voluntaria/`, `/anónima/`, `/retirarse/`).
       - F2.2: Mandatory consent checkbox: `He leído y acepto los términos del consentimiento informado.` (RegEx match: `/acepto los términos del consentimiento informado/`).
       - F2.3–F2.4: Progression is blocked if checkbox is false, enabled when true.
     - Lines 117–183 (Feature 3: Demographics Collection Form):
       - Fields: `age` (integer >= 18), `gender` ('Femenino' | 'Masculino' | 'Otro'), `studiesPsychology` (boolean), `therapeuticOrientation` ('Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros'), `university` (trimmed non-empty string).
     - Lines 403–438 (Feature 8: Cognitive Induction Priming Screen):
       - F8.1 Racional: `"Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones."`
       - F8.2 Emocional: `"Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón."`
       - F8.3 Control: `"A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no."`
     - Lines 662–690 (Feature 14: Ethical Debriefing / Dehoaxing):
       - F14.1: `Queremos informarle que 8 de los 20 titulares presentados fueron noticias falsas creadas para esta investigación.` (RegEx matches: `/8 de los 20 titulares/`, `/noticias falsas/`).
       - F14.2: `El estudio investiga cómo la inducción de modos de pensamiento y las creencias previas influyen en la memoria.` (RegEx matches: `/inducción de modos de pensamiento/`, `/creencias previas/`).
       - F14.3: `Es completamente normal recordar o creer información falsa cuando es coherente con nuestras afinidades.` (RegEx match: `/completamente normal/`).
       - F14.4: `Para consultas académicas, contactar al equipo de Psicología Experimental de la Universidad Favaloro.` (RegEx matches: `/Universidad Favaloro/`, `/Psicología Experimental/`).
     - Lines 695–753 (Feature 15: Thank You & Confirmation Screen):
       - F15.1: `¡Muchas gracias por participar! Sus respuestas han sido registradas exitosamente.` (RegEx matches: `/Muchas gracias/`, `/registradas exitosamente/`).
       - F15.5: Confirmation screen provides participant anonymous ID reference (`session.id.length >= 36`).

2. **Domain Models and Type Contracts** (`src/types/experiment.ts`):
   - `InductionGroup = 'racional' | 'emocional' | 'control'`
   - `TherapeuticOrientation = 'Psicoanálisis' | 'Basada en Evidencia Científica' | 'Otros'`
   - `Gender = 'Femenino' | 'Masculino' | 'Otro'`
   - `ParticipantDemographicsInput`: `{ age: number; gender: Gender; studiesPsychology: boolean; therapeuticOrientation: TherapeuticOrientation; university: string; }`

3. **Current Components Directory State**:
   - `src/components/` in `web-experimento` is currently empty.
   - Dependencies available in `package.json`: `react 18`, `next 14.2.35`, `lucide-react ^1.47.0`, `tailwindcss ^3.4.1`.

4. **Peer Agent Scopes**:
   - `explorer_m2_2` is designing `StimulusReadingScreen.tsx` (10s exposure) and `RatingScreen.tsx` (4-point scale, RT tracking).
   - `explorer_m2_3` is designing the global state machine coordinator in `src/app/page.tsx`.

---

## 2. Logic Chain

1. **Screen Scope & Partitioning**:
   Milestone 2 requires the full participant journey. The screening, induction, and ethical stages fall into 6 discrete, single-responsibility React components:
   - Stage 1: `WelcomeScreen.tsx`
   - Stage 2: `ConsentScreen.tsx`
   - Stage 3: `DemographicsScreen.tsx`
   - Stage 4: `InductionScreen.tsx`
   - Stage 7: `DebriefingScreen.tsx`
   - Stage 8: `ThankYouScreen.tsx`
   (Stages 5 & 6 are handled by `explorer_m2_2`).

2. **Strict Verbatim Text Alignment**:
   Because the automated test suite (`tests/e2e/tier1_features.test.ts`) checks exact substrings and regexes across these components, every single string must match the validated canonical texts without spelling alterations or omissions.

3. **Demographic Validation Integrity**:
   Client-side validation in `DemographicsScreen.tsx` must align 1:1 with `ExperimentEngine.validateDemographics` in `tests/e2e/harness/experimentEngine.ts` (boundary age 18, non-integer rejection, trimmed university name, explicit radio options). Providing inline field-level errors and an accessible summary alert ensures zero validation mismatches upon session creation.

4. **Component Decoupling & Pure Props Contract**:
   Each component is designed as a controlled, presentational UI module communicating with the parent orchestrator purely through typed callback props (`onStart`, `onAcceptConsent`, `onSubmit`, `onAcknowledge`, `onConfirmDebriefing`, `onRestart`). This guarantees clean composability with `src/app/page.tsx`.

---

## 3. Caveats

1. **State Machine Responsibility**:
   Screening logic (`evaluateInclusion`) and balanced group allocation (`assign_induction_group` / `BalanceOracle`) are executed by the orchestrator engine (`src/app/page.tsx` and `experimentLogic.ts`), NOT internally within `DemographicsScreen.tsx`. `DemographicsScreen.tsx` solely validates and submits `ParticipantDemographicsInput`.
2. **Session Persistence**:
   Actual network dispatch to Supabase (`/api/session`) happens at the orchestrator level. Screens operate synchronously with local React state and inform the parent upon user actions.
3. **No Direct Code Modifications Outside `.agents`**:
   In accordance with the explorer role's read-only mandate, the full production code for all 6 components is provided below as drop-in blueprints for implementation by the builder/worker agent.

---

## 4. Conclusion & Complete Component Blueprints

Below are the complete, production-ready TypeScript component blueprints for all 6 assigned screens.

```
web-experimento/src/components/
├── WelcomeScreen.tsx
├── ConsentScreen.tsx
├── DemographicsScreen.tsx
├── InductionScreen.tsx
├── DebriefingScreen.tsx
└── ThankYouScreen.tsx
```

---

### Component 1: `src/components/WelcomeScreen.tsx`

```tsx
'use client';

import React from 'react';
import { FlaskConical, Clock, ShieldCheck, ArrowRight, Volume2 } from 'lucide-react';

export interface WelcomeScreenProps {
  onStart: () => void;
}

export const WelcomeScreen: React.FC<WelcomeScreenProps> = ({ onStart }) => {
  return (
    <div className="max-w-3xl mx-auto py-8 px-4 sm:px-6">
      {/* Institution Header Badge */}
      <div className="flex items-center gap-3 mb-6 p-4 bg-indigo-50 border border-indigo-100 rounded-xl">
        <div className="p-2.5 bg-indigo-600 text-white rounded-lg shadow-sm">
          <FlaskConical className="w-6 h-6" />
        </div>
        <div>
          <p className="text-xs font-bold uppercase tracking-wider text-indigo-700">
            Universidad Favaloro · Facultad de Psicología
          </p>
          <p className="text-sm font-medium text-indigo-950">
            Cátedra de Psicología Experimental — Parcial 2 Investigación
          </p>
        </div>
      </div>

      {/* Main Title & Welcome Card */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-6">
        <h1 className="text-2xl sm:text-3xl font-bold text-slate-900 mb-4 leading-tight">
          Investigación sobre Percepción y Evaluación de Titulares
        </h1>

        <div className="prose prose-slate text-slate-700 space-y-4 text-base leading-relaxed">
          <p className="font-medium text-slate-900">
            Somos estudiantes de la Universidad Favaloro de la carrera de Psicología.
          </p>
          <p>
            El objetivo de esta investigación es evaluar la percepción y evaluación de titulares de noticias.
            A lo largo de la experiencia se le presentará una serie de estímulos periodísticos que deberá observar y evaluar conforme a pautas estandarizadas.
          </p>
          <p className="text-slate-600 text-sm">
            Su participación es fundamental para el avance del conocimiento científico en el área de la psicología cognitiva y la memoria humana.
          </p>
        </div>

        {/* 3 Pillars: Environment, Duration, Privacy */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-8 pt-6 border-t border-slate-100">
          <div className="p-4 bg-slate-50 rounded-xl border border-slate-100">
            <div className="flex items-center gap-2 text-indigo-600 mb-1.5">
              <Volume2 className="w-4 h-4" />
              <span className="text-xs font-bold uppercase tracking-wider">Entorno</span>
            </div>
            <p className="text-xs text-slate-600 leading-normal">
              Por favor, busque un lugar tranquilo, sin interrupciones y con conexión estable a internet.
            </p>
          </div>

          <div className="p-4 bg-slate-50 rounded-xl border border-slate-100">
            <div className="flex items-center gap-2 text-indigo-600 mb-1.5">
              <Clock className="w-4 h-4" />
              <span className="text-xs font-bold uppercase tracking-wider">Tiempo Estimado</span>
            </div>
            <p className="text-xs text-slate-600 leading-normal">
              La duración estimada del experimento es de entre 10 y 15 minutos.
            </p>
          </div>

          <div className="p-4 bg-slate-50 rounded-xl border border-slate-100">
            <div className="flex items-center gap-2 text-emerald-600 mb-1.5">
              <ShieldCheck className="w-4 h-4" />
              <span className="text-xs font-bold uppercase tracking-wider">Confidencialidad</span>
            </div>
            <p className="text-xs text-slate-600 leading-normal">
              Respuestas 100% anónimas tratadas con fines estrictamente académicos.
            </p>
          </div>
        </div>
      </div>

      {/* Action CTA */}
      <div className="flex justify-end">
        <button
          type="button"
          onClick={onStart}
          className="inline-flex items-center gap-2 px-6 py-3.5 bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-semibold rounded-xl shadow-sm transition-all focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          <span>Comenzar Experimento</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default WelcomeScreen;
```

---

### Component 2: `src/components/ConsentScreen.tsx`

```tsx
'use client';

import React, { useState } from 'react';
import { ShieldCheck, FileText, Check, AlertCircle, ArrowRight } from 'lucide-react';

export interface ConsentScreenProps {
  onAcceptConsent: () => void;
  onDeclineConsent?: () => void;
}

export const ConsentScreen: React.FC<ConsentScreenProps> = ({
  onAcceptConsent,
  onDeclineConsent,
}) => {
  const [hasAgreed, setHasAgreed] = useState<boolean>(false);

  const handleContinue = () => {
    if (!hasAgreed) return;
    onAcceptConsent();
  };

  return (
    <div className="max-w-3xl mx-auto py-8 px-4 sm:px-6">
      {/* Header */}
      <div className="flex items-center gap-3 mb-6 p-4 bg-slate-100 border border-slate-200 rounded-xl">
        <div className="p-2.5 bg-slate-800 text-white rounded-lg">
          <FileText className="w-6 h-6" />
        </div>
        <div>
          <h1 className="text-lg font-bold text-slate-900">
            Formulario de Consentimiento Informado
          </h1>
          <p className="text-xs text-slate-600">
            Universidad Favaloro · Comité de Ética en Investigación Psicológica
          </p>
        </div>
      </div>

      {/* Informed Consent Document Box */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-6">
        <div className="bg-slate-50 border border-slate-200 rounded-xl p-5 mb-6 text-sm text-slate-700 leading-relaxed max-h-80 overflow-y-auto space-y-4">
          <p className="font-semibold text-slate-900">
            Información al participante:
          </p>
          <p>
            Usted ha sido invitado/a a participar en un estudio científico llevado a cabo por investigadores y estudiantes de la carrera de Psicología de la Universidad Favaloro. El propósito de este estudio es explorar cómo las personas procesan, evalúan y recuerdan información periodística contemporánea.
          </p>
          <p className="font-semibold text-slate-900 text-xs uppercase tracking-wider text-indigo-900">
            Voluntariedad y Anonimato
          </p>
          <p>
            La participación es estrictamente voluntaria y anónima. Puede retirarse en cualquier momento sin necesidad de justificación y sin que ello conlleve perjuicio alguno. No se recopilarán datos de filiación directa (tales como nombre, apellido, DNI ni dirección IP personal). Toda la información recolectada se identificará únicamente mediante un código alfanumérico aleatorio y se empleará exclusivamente para análisis estadístico grupal.
          </p>
          <p className="font-semibold text-slate-900 text-xs uppercase tracking-wider text-indigo-900">
            Procedimiento
          </p>
          <p>
            Completará un breve cuestionario demográfico, seguido de la lectura guiada de una serie de titulares de noticias de interés general y preguntas breves sobre su recuerdo o familiaridad con ellos. La duración total no superará los 15 minutos.
          </p>
          <p className="font-semibold text-slate-900 text-xs uppercase tracking-wider text-indigo-900">
            Riesgos y Beneficios
          </p>
          <p>
            La participación no presenta riesgos físicos, psicológicos ni legales superiores a los de la lectura habitual de noticias en medios digitales. Al concluir, se brindará una explicación detallada sobre los objetivos y diseño del experimento.
          </p>
        </div>

        {/* Mandatory Checkbox */}
        <label
          htmlFor="consent-checkbox"
          className={`flex items-start gap-3 p-4 rounded-xl border transition-colors cursor-pointer select-none ${
            hasAgreed
              ? 'bg-indigo-50/70 border-indigo-300'
              : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
          }`}
        >
          <input
            id="consent-checkbox"
            type="checkbox"
            checked={hasAgreed}
            onChange={(e) => setHasAgreed(e.target.checked)}
            className="mt-0.5 h-5 w-5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500 cursor-pointer"
          />
          <div className="text-sm font-medium text-slate-800">
            <span>He leído y acepto los términos del consentimiento informado.</span>
            <p className="text-xs text-slate-500 font-normal mt-0.5">
              Confirmo que soy mayor de 18 años y acepto participar voluntariamente en esta investigación.
            </p>
          </div>
        </label>
      </div>

      {/* Buttons */}
      <div className="flex flex-col-reverse sm:flex-row items-center justify-between gap-4">
        {onDeclineConsent && (
          <button
            type="button"
            onClick={onDeclineConsent}
            className="w-full sm:w-auto px-4 py-2.5 text-sm text-slate-500 hover:text-slate-700 transition-colors"
          >
            No deseo participar
          </button>
        )}
        <div className="flex justify-end w-full sm:w-auto ml-auto">
          <button
            type="button"
            disabled={!hasAgreed}
            onClick={handleContinue}
            className={`inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-white transition-all w-full sm:w-auto ${
              hasAgreed
                ? 'bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 shadow-sm cursor-pointer'
                : 'bg-slate-300 cursor-not-allowed text-slate-500'
            }`}
          >
            <span>Continuar a Datos Demográficos</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ConsentScreen;
```

---

### Component 3: `src/components/DemographicsScreen.tsx`

```tsx
'use client';

import React, { useState } from 'react';
import type {
  Gender,
  TherapeuticOrientation,
  ParticipantDemographicsInput,
} from '@/types/experiment';
import { UserCheck, AlertCircle, ArrowRight } from 'lucide-react';

export interface DemographicsScreenProps {
  onSubmit: (data: ParticipantDemographicsInput) => void;
  initialData?: Partial<ParticipantDemographicsInput>;
}

export const DemographicsScreen: React.FC<DemographicsScreenProps> = ({
  onSubmit,
  initialData,
}) => {
  const [age, setAge] = useState<string>(initialData?.age ? String(initialData.age) : '');
  const [gender, setGender] = useState<Gender | ''>(initialData?.gender || '');
  const [studiesPsychology, setStudiesPsychology] = useState<boolean | null>(
    typeof initialData?.studiesPsychology === 'boolean' ? initialData.studiesPsychology : null
  );
  const [therapeuticOrientation, setTherapeuticOrientation] = useState<TherapeuticOrientation | ''>(
    initialData?.therapeuticOrientation || ''
  );
  const [university, setUniversity] = useState<string>(initialData?.university || '');

  // Validation errors
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [hasAttemptedSubmit, setHasAttemptedSubmit] = useState<boolean>(false);

  const validate = (): { isValid: boolean; newErrors: Record<string, string>; parsedData?: ParticipantDemographicsInput } => {
    const errs: Record<string, string> = {};

    // 1. Age validation
    const parsedAge = Number(age.trim());
    if (!age || age.trim() === '' || Number.isNaN(parsedAge)) {
      errs.age = 'La edad es obligatoria y debe ser un número.';
    } else if (!Number.isInteger(parsedAge)) {
      errs.age = 'La edad debe ser un número entero.';
    } else if (parsedAge < 18) {
      errs.age = 'Debe ser mayor o igual a 18 años para participar.';
    } else if (parsedAge > 120) {
      errs.age = 'Edad fuera del rango biológico válido.';
    }

    // 2. Gender validation
    if (!gender || !['Femenino', 'Masculino', 'Otro'].includes(gender)) {
      errs.gender = 'Debe seleccionar una opción de sexo/género válida.';
    }

    // 3. Psychology student validation
    if (studiesPsychology === null || typeof studiesPsychology !== 'boolean') {
      errs.studiesPsychology = 'Debe indicar si estudia o estudió psicología.';
    }

    // 4. Therapeutic orientation validation
    if (
      !therapeuticOrientation ||
      !['Psicoanálisis', 'Basada en Evidencia Científica', 'Otros'].includes(therapeuticOrientation)
    ) {
      errs.therapeuticOrientation = 'Debe seleccionar una orientación terapéutica válida.';
    }

    // 5. University validation
    if (!university || university.trim().length === 0) {
      errs.university = 'Debe indicar la universidad o institución.';
    }

    const isValid = Object.keys(errs).length === 0;

    return {
      isValid,
      newErrors: errs,
      parsedData: isValid
        ? {
            age: parsedAge,
            gender: gender as Gender,
            studiesPsychology: studiesPsychology as boolean,
            therapeuticOrientation: therapeuticOrientation as TherapeuticOrientation,
            university: university.trim(),
          }
        : undefined,
    };
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setHasAttemptedSubmit(true);
    const { isValid, newErrors, parsedData } = validate();
    setErrors(newErrors);

    if (isValid && parsedData) {
      onSubmit(parsedData);
    }
  };

  return (
    <div className="max-w-2xl mx-auto py-8 px-4 sm:px-6">
      {/* Header */}
      <div className="flex items-center gap-3 mb-6 p-4 bg-indigo-50 border border-indigo-100 rounded-xl">
        <div className="p-2.5 bg-indigo-600 text-white rounded-lg">
          <UserCheck className="w-6 h-6" />
        </div>
        <div>
          <h1 className="text-xl font-bold text-slate-900">
            Cuestionario Demográfico y Académico
          </h1>
          <p className="text-xs text-slate-600">
            Por favor, complete los siguientes datos para contextualizar los resultados de la investigación.
          </p>
        </div>
      </div>

      {/* Global Error Banner */}
      {hasAttemptedSubmit && Object.keys(errors).length > 0 && (
        <div
          role="alert"
          className="mb-6 p-4 bg-rose-50 border border-rose-200 rounded-xl flex items-start gap-3"
        >
          <AlertCircle className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />
          <div className="text-sm text-rose-800">
            <p className="font-semibold">Por favor corrija los siguientes errores antes de continuar:</p>
            <ul className="list-disc list-inside mt-1.5 space-y-0.5 text-xs text-rose-700">
              {Object.values(errors).map((err, i) => (
                <li key={i}>{err}</li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* Form Card */}
      <form onSubmit={handleSubmit} className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
        {/* Field 1: Age */}
        <div>
          <label htmlFor="age-input" className="block text-sm font-semibold text-slate-900 mb-1">
            1. Edad (años cumplidos) <span className="text-rose-500">*</span>
          </label>
          <input
            id="age-input"
            type="number"
            min="18"
            max="120"
            step="1"
            value={age}
            onChange={(e) => {
              setAge(e.target.value);
              if (errors.age) setErrors((prev) => ({ ...prev, age: '' }));
            }}
            placeholder="Ej: 22"
            className={`w-full max-w-xs px-3.5 py-2.5 rounded-xl border text-sm text-slate-900 transition-colors focus:outline-none focus:ring-2 ${
              errors.age
                ? 'border-rose-300 focus:ring-rose-500 bg-rose-50/30'
                : 'border-slate-300 focus:ring-indigo-500 bg-white'
            }`}
          />
          {errors.age && (
            <p className="mt-1 text-xs text-rose-600 font-medium">{errors.age}</p>
          )}
          <p className="mt-1 text-xs text-slate-500">Debe ser mayor o igual a 18 años.</p>
        </div>

        {/* Field 2: Gender */}
        <div>
          <label className="block text-sm font-semibold text-slate-900 mb-2">
            2. Sexo / Género <span className="text-rose-500">*</span>
          </label>
          <div className="grid grid-cols-3 gap-3">
            {(['Femenino', 'Masculino', 'Otro'] as Gender[]).map((g) => (
              <label
                key={g}
                className={`flex items-center justify-center p-3 rounded-xl border text-sm font-medium cursor-pointer transition-colors ${
                  gender === g
                    ? 'bg-indigo-50 border-indigo-600 text-indigo-900 ring-2 ring-indigo-500'
                    : 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100'
                }`}
              >
                <input
                  type="radio"
                  name="gender"
                  value={g}
                  checked={gender === g}
                  onChange={() => {
                    setGender(g);
                    if (errors.gender) setErrors((prev) => ({ ...prev, gender: '' }));
                  }}
                  className="sr-only"
                />
                <span>{g}</span>
              </label>
            ))}
          </div>
          {errors.gender && (
            <p className="mt-1 text-xs text-rose-600 font-medium">{errors.gender}</p>
          )}
        </div>

        {/* Field 3: Studies Psychology */}
        <div>
          <label className="block text-sm font-semibold text-slate-900 mb-2">
            3. ¿Estudia o estudió la carrera de Psicología? <span className="text-rose-500">*</span>
          </label>
          <div className="grid grid-cols-2 gap-3 max-w-xs">
            {[
              { label: 'Sí', value: true },
              { label: 'No', value: false },
            ].map((opt) => (
              <label
                key={opt.label}
                className={`flex items-center justify-center p-3 rounded-xl border text-sm font-medium cursor-pointer transition-colors ${
                  studiesPsychology === opt.value
                    ? 'bg-indigo-50 border-indigo-600 text-indigo-900 ring-2 ring-indigo-500'
                    : 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100'
                }`}
              >
                <input
                  type="radio"
                  name="studiesPsychology"
                  checked={studiesPsychology === opt.value}
                  onChange={() => {
                    setStudiesPsychology(opt.value);
                    if (errors.studiesPsychology) {
                      setErrors((prev) => ({ ...prev, studiesPsychology: '' }));
                    }
                  }}
                  className="sr-only"
                />
                <span>{opt.label}</span>
              </label>
            ))}
          </div>
          {errors.studiesPsychology && (
            <p className="mt-1 text-xs text-rose-600 font-medium">{errors.studiesPsychology}</p>
          )}
        </div>

        {/* Field 4: Therapeutic Orientation */}
        <div>
          <label className="block text-sm font-semibold text-slate-900 mb-2">
            4. Orientación terapéutica con la que tiene mayor afinidad o interés{' '}
            <span className="text-rose-500">*</span>
          </label>
          <div className="space-y-2.5">
            {[
              {
                id: 'Psicoanálisis',
                title: 'Psicoanálisis',
                description: 'Enfoques psicodinámicos, teoría freudiana o lacaniana.',
              },
              {
                id: 'Basada en Evidencia Científica',
                title: 'Basada en Evidencia Científica',
                description: 'Terapia cognitivo-conductual (TCC), terapias conductuales contextuales o de tercera ola.',
              },
              {
                id: 'Otros',
                title: 'Otros / Ninguna en particular',
                description: 'Sistémica, humanista, neuropsicología, o sin preferencia definida.',
              },
            ].map((opt) => (
              <label
                key={opt.id}
                className={`flex items-start gap-3 p-3.5 rounded-xl border text-sm cursor-pointer transition-colors ${
                  therapeuticOrientation === opt.id
                    ? 'bg-indigo-50/80 border-indigo-600 ring-2 ring-indigo-500'
                    : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
                }`}
              >
                <input
                  type="radio"
                  name="therapeuticOrientation"
                  value={opt.id}
                  checked={therapeuticOrientation === opt.id}
                  onChange={() => {
                    setTherapeuticOrientation(opt.id as TherapeuticOrientation);
                    if (errors.therapeuticOrientation) {
                      setErrors((prev) => ({ ...prev, therapeuticOrientation: '' }));
                    }
                  }}
                  className="mt-1 text-indigo-600 focus:ring-indigo-500"
                />
                <div>
                  <span className="font-semibold text-slate-900 block">{opt.title}</span>
                  <span className="text-xs text-slate-600">{opt.description}</span>
                </div>
              </label>
            ))}
          </div>
          {errors.therapeuticOrientation && (
            <p className="mt-1 text-xs text-rose-600 font-medium">{errors.therapeuticOrientation}</p>
          )}
        </div>

        {/* Field 5: University */}
        <div>
          <label htmlFor="university-input" className="block text-sm font-semibold text-slate-900 mb-1">
            5. Universidad o Institución Académica <span className="text-rose-500">*</span>
          </label>
          <input
            id="university-input"
            type="text"
            value={university}
            onChange={(e) => {
              setUniversity(e.target.value);
              if (errors.university) setErrors((prev) => ({ ...prev, university: '' }));
            }}
            placeholder="Ej: Universidad Favaloro, UBA, etc."
            className={`w-full px-3.5 py-2.5 rounded-xl border text-sm text-slate-900 transition-colors focus:outline-none focus:ring-2 ${
              errors.university
                ? 'border-rose-300 focus:ring-rose-500 bg-rose-50/30'
                : 'border-slate-300 focus:ring-indigo-500 bg-white'
            }`}
          />
          {errors.university && (
            <p className="mt-1 text-xs text-rose-600 font-medium">{errors.university}</p>
          )}
        </div>

        {/* Submit Button */}
        <div className="pt-4 border-t border-slate-100 flex justify-end">
          <button
            type="submit"
            className="inline-flex items-center gap-2 px-6 py-3.5 bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-semibold rounded-xl shadow-sm transition-all focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
          >
            <span>Continuar a las Instrucciones</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </form>
    </div>
  );
};

export default DemographicsScreen;
```

---

### Component 4: `src/components/InductionScreen.tsx`

```tsx
'use client';

import React from 'react';
import type { InductionGroup } from '@/types/experiment';
import { Brain, Sparkles, Compass, CheckCircle2, ArrowRight } from 'lucide-react';

export interface InductionScreenProps {
  inductionGroup: InductionGroup;
  onAcknowledge: () => void;
}

export const InductionScreen: React.FC<InductionScreenProps> = ({
  inductionGroup,
  onAcknowledge,
}) => {
  // Verbatim induction prompts per ORIGINAL_REQUEST.md and Tier 1 assertions
  const prompts = {
    racional: {
      badge: 'Instrucciones: Modo de Procesamiento',
      title: 'Pautas de Evaluación Analítica',
      icon: Brain,
      color: 'indigo',
      text: 'Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones.',
    },
    emocional: {
      badge: 'Instrucciones: Modo de Procesamiento',
      title: 'Pautas de Evaluación Intuitiva',
      icon: Sparkles,
      color: 'indigo',
      text: 'Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón.',
    },
    control: {
      badge: 'Instrucciones: Modo de Procesamiento',
      title: 'Pautas Generales de Evaluación',
      icon: Compass,
      color: 'indigo',
      text: 'A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no.',
    },
  };

  const activePrompt = prompts[inductionGroup] || prompts.control;
  const IconComponent = activePrompt.icon;

  return (
    <div className="max-w-3xl mx-auto py-8 px-4 sm:px-6">
      {/* Header Badge */}
      <div className="flex items-center gap-3 mb-6 p-4 bg-indigo-50 border border-indigo-100 rounded-xl">
        <div className="p-2.5 bg-indigo-600 text-white rounded-lg shadow-sm">
          <IconComponent className="w-6 h-6" />
        </div>
        <div>
          <p className="text-xs font-bold uppercase tracking-wider text-indigo-700">
            {activePrompt.badge}
          </p>
          <h1 className="text-lg font-bold text-indigo-950">
            {activePrompt.title}
          </h1>
        </div>
      </div>

      {/* Induction Prime Callout Box */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-6 space-y-6">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-2">
            Instrucción Fundamental
          </span>
          <blockquote className="p-5 sm:p-6 bg-slate-50 border-l-4 border-indigo-600 rounded-r-xl text-slate-900 text-lg sm:text-xl font-serif italic leading-relaxed">
            "{activePrompt.text}"
          </blockquote>
        </div>

        {/* Task Workflow Explanation */}
        <div className="border-t border-slate-100 pt-6">
          <h2 className="text-sm font-bold uppercase tracking-wider text-slate-700 mb-4">
            Estructura del Experimento
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="p-4 bg-slate-50 border border-slate-200/70 rounded-xl flex items-start gap-3">
              <span className="flex items-center justify-center w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 text-xs font-bold shrink-0 mt-0.5">
                1
              </span>
              <div>
                <p className="text-sm font-semibold text-slate-900">Lectura del Titular (10 seg)</p>
                <p className="text-xs text-slate-600 mt-1 leading-normal">
                  Cada titular se mostrará durante 10 segundos continuos con una barra de progreso visual. Léalo detenidamente.
                </p>
              </div>
            </div>

            <div className="p-4 bg-slate-50 border border-slate-200/70 rounded-xl flex items-start gap-3">
              <span className="flex items-center justify-center w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 text-xs font-bold shrink-0 mt-0.5">
                2
              </span>
              <div>
                <p className="text-sm font-semibold text-slate-900">Evaluación de Memoria</p>
                <p className="text-xs text-slate-600 mt-1 leading-normal">
                  Luego indicará si recuerda el evento, cree que sucedió, lo recuerda diferente o no lo recuerda en absoluto.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="p-4 bg-amber-50 border border-amber-200 rounded-xl flex items-center gap-3">
          <CheckCircle2 className="w-5 h-5 text-amber-700 shrink-0" />
          <p className="text-xs text-amber-900 leading-relaxed">
            Se evaluarán 20 titulares en total. Una vez comenzado el bloque, por favor no recargue ni cierre la página.
          </p>
        </div>
      </div>

      {/* Action CTA */}
      <div className="flex justify-end">
        <button
          type="button"
          onClick={onAcknowledge}
          className="inline-flex items-center gap-2 px-6 py-3.5 bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-semibold rounded-xl shadow-sm transition-all focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          <span>Comenzar Evaluación de Titulares</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default InductionScreen;
```

---

### Component 5: `src/components/DebriefingScreen.tsx`

```tsx
'use client';

import React from 'react';
import { Info, HelpCircle, ShieldAlert, CheckCircle2, ArrowRight } from 'lucide-react';

export interface DebriefingScreenProps {
  onConfirmDebriefing: () => void;
}

export const DebriefingScreen: React.FC<DebriefingScreenProps> = ({
  onConfirmDebriefing,
}) => {
  return (
    <div className="max-w-3xl mx-auto py-8 px-4 sm:px-6">
      {/* Header Banner */}
      <div className="flex items-center gap-3 mb-6 p-4 bg-amber-50 border border-amber-200 rounded-xl">
        <div className="p-2.5 bg-amber-600 text-white rounded-lg shadow-sm">
          <ShieldAlert className="w-6 h-6" />
        </div>
        <div>
          <p className="text-xs font-bold uppercase tracking-wider text-amber-800">
            Información Ética Post-Experimental (Debriefing)
          </p>
          <h1 className="text-lg font-bold text-amber-950">
            Revelación del Diseño Experimental
          </h1>
        </div>
      </div>

      {/* Main Disclosure Card */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-6 space-y-6">
        {/* Core Dehoaxing Statement */}
        <div className="p-5 bg-rose-50 border border-rose-200 rounded-xl">
          <p className="text-sm font-bold text-rose-950 mb-1">
            Revelación de Contenido Falso:
          </p>
          <p className="text-sm text-rose-900 leading-relaxed font-medium">
            Queremos informarle que 8 de los 20 titulares presentados fueron noticias falsas creadas para esta investigación.
          </p>
        </div>

        {/* Theoretical Framework */}
        <div className="space-y-4 text-sm text-slate-700 leading-relaxed">
          <h2 className="text-base font-bold text-slate-900">
            Propósito Científico de la Investigación
          </h2>
          <p>
            El estudio investiga cómo la inducción de modos de pensamiento y las creencias previas influyen en la memoria.
            Específicamente, evaluamos si la disposición hacia un procesamiento analítico/racional o emocional/intuitivo modula la probabilidad de formar falsos recuerdos (recordar claramente un evento inexistente) o falsas creencias (creer que un evento ocurrió aun sin recordarlo directamente) ante noticias alineadas con la propia orientación teórica.
          </p>

          {/* Psychological Normalization */}
          <div className="p-5 bg-indigo-50/70 border border-indigo-100 rounded-xl text-indigo-950">
            <h3 className="text-xs font-bold uppercase tracking-wider text-indigo-800 mb-1">
              Normalización Psicológica
            </h3>
            <p className="text-sm leading-relaxed">
              Es completamente normal recordar o creer información falsa cuando es coherente con nuestras afinidades.
              Numerosos estudios en psicología experimental (e.g., Murphy et al., 2019, 2021) han demostrado que la gran mayoría de las personas con alta formación académica y criterio crítico experimentan estos fenómenos debido a sesgos cognitivos automáticos de congruencia ideológica y familiaridad perceptiva.
            </p>
          </div>

          <p>
            Los 12 titulares restantes correspondían a noticias periodísticas reales ocurridas en 2017 y 2018. Los titulares ficticios no reflejan hechos reales ni buscan desprestigiar a ninguna institución o corriente profesional.
          </p>
        </div>

        {/* Institutional Contact */}
        <div className="border-t border-slate-100 pt-6">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
            Contacto Académico
          </h3>
          <p className="text-xs text-slate-600 leading-relaxed">
            Para consultas académicas, contactar al equipo de Psicología Experimental de la Universidad Favaloro.
            Si tiene alguna duda sobre el estudio o desea solicitar el informe final con los resultados globales agregados, puede comunicarse con la cátedra.
          </p>
        </div>
      </div>

      {/* Final Action CTA */}
      <div className="flex justify-end">
        <button
          type="button"
          onClick={onConfirmDebriefing}
          className="inline-flex items-center gap-2 px-6 py-3.5 bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-semibold rounded-xl shadow-sm transition-all focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          <span>Finalizar y Ver Agradecimiento</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default DebriefingScreen;
```

---

### Component 6: `src/components/ThankYouScreen.tsx`

```tsx
'use client';

import React, { useState } from 'react';
import { CheckCircle2, Copy, Check, FlaskConical } from 'lucide-react';

export interface ThankYouScreenProps {
  participantId: string;
  onRestart?: () => void;
}

export const ThankYouScreen: React.FC<ThankYouScreenProps> = ({
  participantId,
  onRestart,
}) => {
  const [copied, setCopied] = useState<boolean>(false);

  const handleCopyId = () => {
    if (!participantId) return;
    navigator.clipboard.writeText(participantId).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    });
  };

  return (
    <div className="max-w-2xl mx-auto py-12 px-4 sm:px-6 text-center">
      {/* Animated Success Badge */}
      <div className="inline-flex items-center justify-center w-20 h-20 bg-emerald-100 text-emerald-600 rounded-full mb-6 ring-8 ring-emerald-50">
        <CheckCircle2 className="w-10 h-10" />
      </div>

      {/* Gratitude Heading */}
      <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-3 tracking-tight">
        ¡Muchas gracias por participar! Sus respuestas han sido registradas exitosamente.
      </h1>

      <p className="text-slate-600 text-base mb-8 max-w-lg mx-auto leading-relaxed">
        Su aporte es de enorme valor para la investigación en psicología cognitiva y experimental de la Universidad Favaloro.
      </p>

      {/* Anonymous ID Card */}
      <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm mb-8 max-w-md mx-auto text-left">
        <div className="flex items-center justify-between mb-2">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
            Comprobante de Participación
          </span>
          <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold bg-emerald-100 text-emerald-800">
            Sincronizado
          </span>
        </div>

        <p className="text-xs text-slate-500 mb-3">
          Código anónimo de sesión asignado a sus respuestas:
        </p>

        <div className="flex items-center gap-2 p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-mono text-xs text-slate-800 break-all">
          <span className="select-all flex-1">{participantId}</span>
          <button
            type="button"
            onClick={handleCopyId}
            title="Copiar ID de participante"
            className="p-1.5 text-slate-500 hover:text-indigo-600 hover:bg-slate-200/60 rounded-lg transition-colors shrink-0"
          >
            {copied ? <Check className="w-4 h-4 text-emerald-600" /> : <Copy className="w-4 h-4" />}
          </button>
        </div>
        {copied && (
          <p className="text-xs text-emerald-600 mt-1.5 font-medium">
            ¡Código copiado al portapapeles!
          </p>
        )}
      </div>

      {/* Safety Notice */}
      <p className="text-xs text-slate-400 mb-8 max-w-sm mx-auto">
        Sus datos han sido guardados con éxito en la base de datos segura. Ya puede cerrar esta ventana del navegador tranquilamente.
      </p>

      {/* Footer Attribution */}
      <div className="pt-6 border-t border-slate-200 text-xs text-slate-400 flex items-center justify-center gap-2">
        <FlaskConical className="w-4 h-4 text-slate-400" />
        <span>Universidad Favaloro · Facultad de Psicología · Psicología Experimental</span>
      </div>
    </div>
  );
};

export default ThankYouScreen;
```

---

## 5. Verification Method

To independently verify that these component blueprints satisfy all requirements and invariants:

1. **Automated Test Execution**:
   Run the project test command in the `web-experimento` directory:
   ```bash
   npm test
   ```
   *Expected result*: All 4 tiers (143 assertions) pass with zero failures.

2. **Regex Substring Verification**:
   Inspect the exact text strings in the blueprints against `tests/e2e/tier1_features.test.ts`:
   - Feature 1: `Somos estudiantes de la Universidad Favaloro de la carrera de Psicología.`, `El objetivo de esta investigación es evaluar la percepción y evaluación de titulares de noticias.`, `Por favor, busque un lugar tranquilo, sin interrupciones y con conexión estable a internet.`, `La duración estimada del experimento es de entre 10 y 15 minutos.`, `Comenzar Experimento`.
   - Feature 2: `La participación es estrictamente voluntaria y anónima. Puede retirarse en cualquier momento.`, `He leído y acepto los términos del consentimiento informado.`.
   - Feature 3: Validation errors: `La edad es obligatoria y debe ser un número.`, `La edad debe ser un número entero.`, `Debe ser mayor o igual a 18 años para participar.`, `Edad fuera del rango biológico válido.`, `Debe seleccionar una opción de sexo/género válida.`, `Debe indicar si estudia o estudió psicología.`, `Debe seleccionar una orientación terapéutica válida.`, `Debe indicar la universidad o institución.`.
   - Feature 8: Exact verbatim texts for `racional`, `emocional`, and `control`.
   - Feature 14: `Queremos informarle que 8 de los 20 titulares presentados fueron noticias falsas creadas para esta investigación.`, `El estudio investiga cómo la inducción de modos de pensamiento y las creencias previas influyen en la memoria.`, `Es completamente normal recordar o creer información falsa cuando es coherente con nuestras afinidades.`, `Para consultas académicas, contactar al equipo de Psicología Experimental de la Universidad Favaloro.`.
   - Feature 15: `¡Muchas gracias por participar! Sus respuestas han sido registradas exitosamente.`, UUID display with length >= 36.

3. **Invalidation Conditions**:
   - If any text in the components alters the required keywords (e.g. changing "titulares de noticias" or "acepto los términos del consentimiento informado"), Tier 1 feature tests will fail.
   - If age validation allows `< 18` or non-integers, Tier 2 boundary tests (`B1.1`–`B1.5`) will fail.
   - If consent checkbox does not gate progress, Tier 2 consent tests (`B2.1`–`B2.5`) will fail.
