---
name: simulacro
description: Arma simulacros de parcial (opción múltiple, verdadero/falso justificado, distinciones finas, desarrollo con rúbrica y casos) a partir de las guías de estudio del repositorio de Psicología, con la clave de respuestas al final y cada respuesta rastreable a su fuente; y toma el examen de forma interactiva en el chat, corrige, y guarda los resultados con los temas flojos. Usala siempre que el usuario pida un simulacro, examen de práctica, autoevaluación, preguntas tipo parcial, "tomame examen", "evaluame" o "quiero practicar para el parcial" de una clase, unidad o materia.
---

# Simulacros de parcial

Dos modos:
- **Archivo** (por defecto): genera `5_Evaluaciones/[Unidad]_[Tema]_Simulacro.md` para resolver por
  cuenta propia y corregir con la clave del final.
- **Interactivo** ("tomame examen", "evaluame"): hace las preguntas en el chat, corrige y guarda
  `5_Evaluaciones/[Unidad]_[Tema]_Resultados.md` con puntaje y temas flojos.

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
4. Nombre de salida con el script (el tema resume el alcance):
   ```bash
   python Scripts/estudio/nombres.py generar simulacro --unidad C08 --tema "Pulsión de muerte y compulsión de repetición"
   ```
   Alcance de varias clases: código de rango (`C04_07_11`) o `Global_1erC` para todo el cuatrimestre.
5. Si el simulacro ya existe, `python Scripts/estudio/frontmatter.py estado <archivo>`; si dice
   `editado` o `sin-cabecera`, mostrá las diferencias y preguntá antes de sobrescribir.

## Modo archivo: generar el simulacro

1. Leé las guías completas. Hacé una lista de los temas evaluables con su ubicación
   (`C08_Guia.md §2`): cada pregunta va a salir de uno de esos temas.
2. Escribí el examen con la estructura de `references/formato_simulacro.md`. Cantidad orientativa
   para una clase: A 8–10 · B 5–6 · C 3–4 · D 2 · E 0–2 (más para un parcial entero). Ajustá al
   estilo de la cátedra (p. ej., Estadística: más opción múltiple y casos; Psicoanálisis: más
   desarrollo y distinciones).
3. Reglas de calidad:
   - **Todo sale de las guías/fuentes**: nada de datos de memoria. Cada respuesta de la clave
     cita su fuente: `*(Fuente: C08_Guia.md, §2)*`.
   - Opción múltiple: una sola correcta; distractores **plausibles** sacados de los errores típicos
     y confusiones que marca la guía (no opciones absurdas); variá la posición de la correcta.
   - Verdadero/falso: afirmaciones que prueben matices (no obviedades); la clave justifica.
   - Desarrollo: consignas como las del parcial real; la clave trae **esquema de respuesta modelo
     y rúbrica "para un 10"** (qué conceptos y conexiones no pueden faltar).
   - Casos: situaciones nuevas (no copiar ejemplos de la guía) que exijan aplicar los conceptos.
4. Escribí el archivo con cabecera (materia, unidad, tipo `simulacro`, fuentes, skill
   `simulacro`) usando `Scripts/estudio/frontmatter.py`:
   ```python
   import sys; sys.path.insert(0, "Scripts/estudio")
   import frontmatter
   frontmatter.escribir(ruta, {"materia": "Psicoanálisis", "unidad": "C08", "tipo": "simulacro",
       "fuentes": [{"archivo": "3_Guias_de_Estudio/C08_Guia.md"}], "skill": "simulacro"}, cuerpo)
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
   puntúan de 0 a 3 con la rúbrica (decí qué faltó para el 3). Sé exigente como un docente, pero
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

## Al terminar (modo archivo), informá

Ruta del simulacro, cantidad de preguntas por sección, resultado de la validación y cómo usarlo:
resolverlo sin mirar el material y corregir con la clave, o pedir "tomame este simulacro" para el
modo interactivo.
