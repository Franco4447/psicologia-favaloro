# Plantilla del simulacro

Estructura obligatoria (la valida `Scripts/estudio/simulacro.py`). Los IDs (`A1`, `B2`…) tienen que
coincidir entre el examen y la clave.

```markdown
# Simulacro — [Materia] · [Alcance]

> **Alcance:** [clases/unidades y textos que cubre] · **Tiempo sugerido:** [N] min ·
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
**Esquema de respuesta modelo:** [puntos en orden].
**Rúbrica (para un 10):** [conceptos y conexiones que no pueden faltar; qué resta puntos]. *(Fuente: …)*

### E1
[Resolución esperada.] *(Fuente: …)*
```

Notas:
- Opción múltiple con 4 opciones (a–d) o 5 (a–e) si la cátedra usa 5 (Estadística).
- La sección E es opcional; las demás no.
- Sin Markdown raro dentro de los encabezados `###` (el validador lee `### A1. Texto`).
