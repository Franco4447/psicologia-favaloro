---
name: simulacro
description: Arma simulacros de parcial (opción múltiple, verdadero/falso justificado, distinciones finas, desarrollo con rúbrica y casos) a partir de las guías de estudio del repositorio de Psicología, con la clave de respuestas al final y cada respuesta rastreable a su fuente; y toma el examen de forma interactiva en el chat, corrige, y guarda los resultados con los temas flojos. Usala siempre que el usuario pida un simulacro, examen de práctica, autoevaluación, preguntas tipo parcial, "tomame examen", "evaluame" o "quiero practicar para el parcial" de una clase, unidad o materia.
---

# Simulacros de parcial

Tres modos:
- **Archivo** (por defecto): genera `5_Evaluaciones/[Unidad]_[Tema]_Simulacro.md` para resolver por
  cuenta propia y corregir con la clave del final.
- **Interactivo** ("tomame examen", "evaluame"): hace las preguntas en el chat, corrige y guarda
  `5_Evaluaciones/[Unidad]_[Tema]_Resultados.md` con puntaje y temas flojos.
- **Corrección de respuestas escritas** ("corregime esto", pega o adjunta lo que escribió): corrige
  con la rúbrica por criterios y guarda los resultados igual que el modo interactivo.

**Practicar la escritura es lo que más rinde** cuando el examen es de desarrollo: las flashcards
entrenan recordar, pero no armar una respuesta de 10 renglones. Ahí el simulacro es la pieza clave.

## Antes de empezar

1. Leé `AGENTS.md` (reglas de carpetas y nombres; manda sobre esta skill).
2. Identificá el alcance: una guía, varias clases ("clases 4, 7 y 11"), una unidad o un parcial
   entero. Buscá las guías en `[Año]/[Materia]/3_Guias_de_Estudio/` (la extendida; las `_Resumen` /
   `_Sintesis` como complemento). Si están solo en `.docx`, convertilas con pandoc a un temporal
   fuera del repo. Si no queda claro de qué materia o unidad se trata, **preguntá**.
3. Buscá material de examen de la cátedra para **calibrar** el estilo y priorizar temas:
   `5_Evaluaciones/` (repasos, cuestionarios, casos, problemas), la guía de lectura de
   `1_Bibliografia_Original/` y las secciones "Para rendir", "Trampa de examen" o "Lo que entra sí o
   sí" de las guías. Leé `references/estilos_catedra.md`.
4. Averiguá el **formato del examen real** (tipo de preguntas, cantidad, extensión mínima como
   «10 renglones», tiempo, si hay elección de preguntas). Está en los apuntes del usuario, en la
   memoria o en la guía; si no, preguntá. El simulacro lo reproduce: mismas consignas, misma
   extensión, mismo tiempo.
5. Nombre de salida con el script (el tema resume el alcance):
   ```bash
   python Scripts/estudio/nombres.py generar simulacro --unidad C08 --tema "Pulsión de muerte y compulsión de repetición"
   ```
   Alcance de varias clases: código de rango (`C04_07_11`) o `Global_1erC` para todo el cuatrimestre.
6. Si el simulacro ya existe, `python Scripts/estudio/frontmatter.py estado <archivo>`; si dice
   `editado` o `sin-cabecera`, mostrá las diferencias y preguntá antes de sobrescribir.

## Modo archivo: generar el simulacro

1. Leé las guías completas. Hacé una lista de los temas evaluables con su ubicación
   (`C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md §2`): cada pregunta va a salir de uno de esos temas.
2. Escribí el examen con la estructura de `references/formato_simulacro.md`. Cantidad orientativa
   para una clase: A 8–10 · B 5–6 · C 3–4 · D 2 · E 0–2 (más para un parcial entero). Ajustá al
   estilo de la cátedra (p. ej., Estadística: más opción múltiple y casos; Psicoanálisis: más
   desarrollo y distinciones). Si el examen real es **solo de desarrollo**, el simulacro puede ser
   solo C y D: no rellenes con opción múltiple.
   - **Alcance de varias clases: intercalá.** Mezclá preguntas de clases distintas (no en orden de
     clase) e incluí al menos una **integradora** que obligue a comparar o conectar clases
     (estructuras, Freud ↔ Lacan). Así es el examen real y así se aprende a discriminar.
   - **Tiempo:** indicá el tiempo sugerido según el examen real (p. ej., 15–20 min por pregunta de
     desarrollo) y pedí resolverlo con reloj y sin material.
3. Reglas de calidad:
   - **Todo sale de las guías/fuentes**: nada de datos de memoria. Las menciones de autores y
     textos en consignas y respuestas modelo van en APA 7 (`guia-estudio/references/citas_apa.md`). Cada respuesta de la clave
     cita su fuente: `*(Fuente: C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md, §2)*`.
   - Opción múltiple: una sola correcta; distractores **plausibles** sacados de los errores típicos
     y confusiones que marca la guía (no opciones absurdas); variá la posición de la correcta.
   - Verdadero/falso: afirmaciones que prueben matices (no obviedades); la clave justifica.
   - Desarrollo: consignas como las del parcial real (si la guía trae las preguntas de la cátedra,
     usalas o reformulalas); la clave trae el **esqueleto** de la respuesta (el mismo de la guía),
     una **respuesta modelo** de la extensión pedida y la **rúbrica por criterios** de
     `references/formato_simulacro.md` (tesis, conceptos obligatorios, fuentes, articulación,
     ejemplo, cierre y extensión).
   - Casos: situaciones nuevas (no copiar ejemplos de la guía) que exijan aplicar los conceptos.
4. Escribí el archivo con cabecera (materia, unidad, tipo `simulacro`, fuentes, skill
   `simulacro`) usando `Scripts/estudio/frontmatter.py`:
   ```python
   import sys; sys.path.insert(0, "Scripts/estudio")
   import frontmatter
   frontmatter.escribir(ruta, {"materia": "Psicoanálisis", "unidad": "C08", "tipo": "simulacro",
       "fuentes": [{"archivo": "3_Guias_de_Estudio/C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md"}], "skill": "simulacro"}, cuerpo)
   ```
5. Validá y corregí hasta que no haya errores (y revisá los avisos):
   ```bash
   python Scripts/estudio/simulacro.py validar <simulacro.md>
   ```
6. Releé la clave contra las guías: cada respuesta correcta tiene que estar respaldada por la fuente
   citada, y ninguna otra opción tiene que poder defenderse como correcta.

## Modo interactivo: tomar el examen

1. Si no existe un simulacro para ese alcance, generalo primero (modo archivo). Si existe, usalo.
2. Explicá cómo va a ser (cantidad de preguntas, secciones, que puede decir "no sé") y preguntá si
   quiere el examen completo o solo algunas secciones.
3. Hacé **una pregunta por vez** (o un bloque corto de opción múltiple). **No muestres la clave**
   ni des pistas antes de que responda.
4. Corregí cada respuesta apenas la da: correcta/incorrecta, la explicación breve de la clave y la
   fuente para repasar. Puntaje: A, B y C valen 1 (B sin justificación correcta = 0,5); D y E se
   puntúan de 0 a 3 con la rúbrica por criterios (decí criterio por criterio qué estuvo y qué
   faltó para el 3). Sé exigente como un docente, pero
   reconocé lo que está bien.
5. Al terminar, armá un JSON temporal (fuera del repo) con cada respuesta —`id`, `puntaje`, `max`,
   `tema` (el tema evaluado, corto y reconocible), `fuente` y un `comentario` breve— y generá los
   resultados:
   ```bash
   python Scripts/estudio/simulacro.py resultados <tmp>/respuestas.json
   ```
   Si ya había resultados de ese simulacro, el script agrega el intento nuevo sin borrar el anterior.
6. Cerrá con: puntaje, temas flojos y el próximo paso concreto: *flashcards de los temas flojos*
   (skill `/flashcards` con el `_Resultados.md`) y releer las secciones citadas. Borrá el JSON.

## Modo corrección de respuestas escritas

Para cuando el usuario resolvió un simulacro (o una pregunta de la guía) por escrito:

1. Identificá cada consigna y su clave (del simulacro o, si es una pregunta de la guía, su esqueleto
   y respuesta modelo).
2. Corregí cada respuesta con la **rúbrica por criterios**: para cada criterio, ✓ / parcial / ✗ con
   una línea de por qué, citando lo que escribió. Contá los renglones o palabras frente al mínimo.
3. Devolvé: puntaje (0–3 por pregunta), lo mejor de la respuesta, **qué agregar para el 3** (en
   concreto: el concepto, la cita o la conexión que faltó y dónde está en la guía) y, si hay
   errores conceptuales, la corrección con su fuente.
4. Proponé reescribir la respuesta peor puntuada y volver a corregirla.
5. Guardá los resultados como en el modo interactivo (paso 5), con un tema flojo por cada
   criterio que falló.

## Al terminar (modo archivo), informá

Ruta del simulacro, cantidad de preguntas por sección, resultado de la validación y cómo usarlo:
resolverlo sin mirar el material y corregir con la clave, o pedir "tomame este simulacro" para el
modo interactivo.
