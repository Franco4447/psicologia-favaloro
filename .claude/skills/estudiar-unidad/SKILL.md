---
name: estudiar-unidad
description: 'Prepara una unidad o clase completa del repositorio de Psicología de punta a punta: digitaliza la bibliografía que falte, escribe la guía extendida, la exporta a Word, arma flashcards para Anki y un simulacro, salteando lo que ya existe y sin pisar ediciones manuales. Usala cuando el usuario pida "preparame la unidad X", "armame todo para el parcial de…", "quiero estudiar la clase N", o el material completo de un tema, en vez de una sola pieza.'
---

# Preparar una unidad completa

Orquesta las demás skills. Cada paso se hace **siguiendo la skill correspondiente** (leé su
`SKILL.md` cuando llegues a ese paso); esta skill solo decide el orden y qué se saltea.

## 1. Diagnóstico

1. Leé `AGENTS.md`. Identificá materia y unidad/clase (si hay dudas, **preguntá**).
2. Corré `python Scripts/estudio/estado.py "<Materia>"` y mirá la fila de esa unidad.
3. Revisá `1_Bibliografia_Original/` para saber qué textos y diapositivas corresponden a la unidad
   (y la guía de lectura de la cátedra, si existe).
4. Mostrale al usuario el plan antes de empezar: qué existe, qué se va a generar, qué se saltea y
   cuánto puede tardar (OCR de libros escaneados: ~6 s por página; guías de textos largos: varias
   partes). Esperá su confirmación.

## 2. Pipeline (saltear lo que ya existe)

| Paso | Skill | Se hace si… |
|---|---|---|
| a. Texto | `/digitalizar` | hay PDF/PPTX de la unidad sin su `*_Crudo.md` |
| b. Guía | `/guia-estudio` | no hay guía extendida `.md` de la unidad, o el usuario pide rehacerla |
| c. Word | `/exportar` | la guía `.md` no tiene `.docx` (con `--pdf` / `--imprimir` si lo pidió) |
| d. Flashcards | `/flashcards` | no hay `*_Flashcards.csv` de la unidad |
| e. Simulacro | `/simulacro` | no hay `*_Simulacro.md` de la unidad |
| f. Ficha de repaso | `/guia-estudio` (`materiales_de_parcial.md`) | la guía supera ~5.000 palabras y no hay `*_Repaso_Guia.md` |

- **Nunca sobrescribas** algo editado a mano (`frontmatter.py estado` → `editado` o
  `sin-cabecera`) ni un `.docx` existente sin preguntar.
- Si la unidad tiene varios textos largos, hacé una guía por texto o una integrada según lo que
  pida el usuario; para muchos textos, repartí la extracción y las notas de parte entre subagentes.
- Si un paso falla (falta Tesseract, pandoc…), seguí con los demás y avisá al final.

## Modo parcial (varias clases)

Cuando el pedido es "armame todo para el parcial" o abarca varias clases:

1. Averiguá **fecha y formato del examen** (tipo de preguntas, extensión mínima, qué clases
   entran y cuáles no). Está en los apuntes del usuario, el Planificador o la memoria; si no,
   preguntá. Guardalo en la memoria del proyecto.
2. Corré el pipeline de la sección 2 **por clase**. Si la cátedra dio baterías de preguntas, cada
   guía se ordena por pregunta (`/guia-estudio`, plantilla).
3. Agregá los **materiales integradores** (`guia-estudio/references/materiales_de_parcial.md`):
   cuadro integrador `Transversal_[Eje]_Guia.md` si las clases tratan categorías paralelas, y
   fichas de repaso de las guías largas.
4. Un **simulacro integrador** del parcial entero (`/simulacro`, alcance `C13_23` o `Global_2doC`),
   con las preguntas intercaladas y el formato real del examen.
5. **Plan de repaso** hasta la fecha (en el chat), según `materiales_de_parcial.md`.

**Si queda poco tiempo**, priorizá lo que más rinde para la nota: (1) cuadro integrador y "no
confundir", (2) esqueletos y fichas de repaso, (3) simulacros con corrección, (4) flashcards. El
diseño del Word y las guías del formato anterior pueden esperar a después del parcial.

## 3. Cierre

1. `python Scripts/estudio/estado.py "<Materia>"` de nuevo: la fila de la unidad debería quedar
   completa.
2. Resumí lo generado (rutas, extensión de la guía, cobertura, cantidad de tarjetas y preguntas).
3. Proponé cómo usarlo en el tiempo que queda hasta el parcial, en línea con el **Planificador**
   (`Planificador_Parciales/`) y el plan de repaso de `materiales_de_parcial.md`: flashcards todos
   los días; reconstruir esqueletos sin mirar; simulacros intercalados con corrección de las
   respuestas escritas ("corregime esto"); después, el mazo de temas flojos.
