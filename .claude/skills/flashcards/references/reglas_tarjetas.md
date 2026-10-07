# Reglas para escribir buenas flashcards

Basadas en el principio de información mínima: cada tarjeta evoca **un** recuerdo
concreto. Las tarjetas largas o ambiguas se olvidan y se terminan salteando.

## 1. Una idea por tarjeta

❌ ¿Qué dice Freud en *Más allá del principio de placer*?
✅ ¿Qué fenómeno clínico lleva a Freud a postular un "más allá" del principio de placer?
   → La compulsión de repetición (sueños traumáticos, transferencia, juego infantil).

## 2. La pregunta se entiende sola

Incluí el contexto (autor, teoría, unidad) en el frente: la tarjeta va a aparecer mezclada
con las de otras materias.

❌ ¿Qué es la represión?
✅ En Freud, ¿qué es la **represión** (*Verdrängung*)?

## 3. Respuestas breves

Máximo 2–3 líneas. Si la respuesta es una lista larga, dividila:
- listas de hasta 3 elementos: una sola tarjeta;
- listas más largas: una cloze con un hueco por elemento (`{{c1::}}`, `{{c2::}}`…) o
  varias tarjetas ("¿Cuál es la primera fase…?").

## 4. Cuándo usar cloze y cuándo básica

| Usar **cloze** | Usar **básica** |
|---|---|
| Definiciones con términos técnicos | Preguntas de "por qué" y "cómo" |
| Datos dentro de una frase (autor, año, obra) | Distinciones entre conceptos |
| Elementos de una lista o secuencia | Aplicación a un caso o ejemplo |
| Fórmulas o pasos | Comparaciones (X vs. Y) |

En una cloze, el hueco debe ser lo importante (el término, no un artículo), y la frase
debe dar pistas suficientes para una única respuesta correcta.

## 5. Tipos de tarjeta que más rinden en examen

- **Definición**: "¿Qué es X en [autor]?"
- **Distinción**: "¿Qué diferencia X de Y?" (síntoma vs. inhibición, neurosis vs. psicosis,
  ritmo circadiano vs. ultradiano, error tipo I vs. tipo II)
- **Autor ↔ concepto ↔ obra**: "¿En qué texto introduce Freud…?"
- **Experimento**: diseño, variable manipulada y resultado (Tolman, Tinbergen, libre curso)
- **Caso / ejemplo**: "¿Qué ilustra el caso de…?"
- **Aplicación**: "Ante [situación], ¿qué prueba estadística corresponde y por qué?"
- **Pregunta de examen**: si la guía tiene preguntas tipo examen, convertirlas en tarjetas
  con respuesta breve (etiqueta `clave-examen`).
- **Esqueleto de respuesta**: si la guía trae esqueletos, una cloze por pregunta con un hueco por
  punto (`1. {{c1::Tesis…}}<br>2. {{c2::…}}`) y la consigna en el frente (etiquetas
  `clave-examen` y `esqueleto`). Entrena el orden de la respuesta, no solo los conceptos sueltos.
- **No confundir**: cada par de la tabla de distinciones o de los recuadros "⚠ No confundir" de
  la guía, como básica "¿Qué distingue X de Y?" → el criterio (etiqueta `distincion`).
- **Integradora**: si hay cuadro integrador (`Transversal_[Eje]_Guia.md`), una tarjeta por celda
  importante ("En la perversión, ¿cuál es el mecanismo frente a la castración?").

## 6. Fidelidad a la fuente

- Todo lo que dice la respuesta tiene que estar en la guía (o en la fuente que cita).
  No agregues datos de memoria.
- Respetá la terminología de la cátedra (si la guía dice "fantasma", no lo cambies por "fantasía").
- Si la guía cita la fuente, ponela al final del dorso en APA 7: `<i>(Papalia et al., 2012, p. 412)</i>`,
  `<i>(Freud, 1894/1991, p. 6)</i>`.

## 7. Formato

- HTML simple: `<b>`, `<i>`, `<br>`, `<ul><li>…</li></ul>`. Nada de Markdown (`**`, `#`).
- Sin imágenes por ahora.
- Fórmulas: texto plano legible (`z = (X − μ) / σ`) o MathJax de Anki (`\(z = \frac{X-\mu}{\sigma}\)`).
