# Plantilla del simulacro

Estructura obligatoria (la valida `Scripts/estudio/simulacro.py`). Los IDs (`A1`, `B2`…) tienen que
coincidir entre el examen y la clave.

```markdown
# Simulacro — [Materia] · [Alcance]

> **Alcance:** [clases/unidades y textos que cubre] · **Tiempo sugerido:** [N] min ·
> **Formato:** [como el examen real, p. ej., «desarrollo, mínimo 10 renglones por respuesta»] ·
> **Puntaje:** A–C 1 punto c/u; D y E hasta 3 puntos c/u.
> Respondé primero sin mirar el material; después corregí con la clave del final y volvé a la guía
> solo en lo que falles.

## A) Opción múltiple

Marcá la opción correcta.

### A1. [Enunciado]
- a) [opción]
- b) [opción]
- c) [opción]
- d) [opción]

## B) Verdadero / Falso (justificá en una línea)

### B1. [Afirmación con un matiz que hay que saber]

## C) Distinciones finas

### C1. ¿Qué diferencia [X] de [Y]?

## D) Desarrollo

### D1. [Consigna tipo parcial: exponé / explicá / conectá]

## E) Casos y aplicación

### E1. [Situación nueva] [Consignas a), b)…]

---

## Clave de respuestas

### A1 — c
[Por qué es la correcta y por qué las otras no, en 1–3 líneas.] *(Fuente: C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md, §2)*

### B1 — Falso
[Justificación.] *(Fuente: …)*

### C1
[La distinción en 2–4 líneas.] *(Fuente: …)*

### D1
**Esqueleto:** 1. Tesis… 2. [concepto obligatorio] (Autor, año, p. N) 3. … 4. Articulación… 5. Cierre…

**Respuesta modelo:** [prosa con la extensión pedida, siguiendo el esqueleto].

**Rúbrica por criterios (para un 3):**
- **Tesis:** responde lo que pide la consigna desde la primera oración.
- **Conceptos obligatorios:** [lista: los que no pueden faltar].
- **Fuentes:** atribuye cada concepto a su autor/texto (sin confundir Freud con Lacan).
- **Articulación:** [la conexión que se espera: entre conceptos, entre clases, Freud ↔ Lacan].
- **Ejemplo:** [caso o ejemplo de la fuente que lo ilustra] *(si la consigna lo admite)*.
- **Cierre y extensión:** concluye volviendo a la consigna; cumple el mínimo de renglones.
- **Resta puntos:** [errores conceptuales típicos, la confusión de "no confundir"].

3 = cumple todos; 2 = falta uno no central o la articulación es floja; 1 = faltan conceptos
obligatorios; 0 = no responde la consigna o tiene un error conceptual grave. *(Fuente: …)*

### E1
[Resolución esperada.] *(Fuente: …)*
```

Notas:
- Opción múltiple con 4 opciones (a–d) o 5 (a–e) si la cátedra usa 5 (Estadística).
- Las secciones van según el examen real: si es solo de desarrollo, alcanza con C y D (el
  validador no exige A ni B). E es opcional.
- Alcance de varias clases: las preguntas van **intercaladas** (no agrupadas por clase) y al menos
  una D es integradora.
- Sin Markdown raro dentro de los encabezados `###` (el validador lee `### A1. Texto`).
