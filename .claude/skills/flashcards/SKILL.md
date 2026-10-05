---
name: flashcards
description: Genera mazos de flashcards para Anki (CSV listo para importar) a partir de las guías de estudio del repositorio de Psicología, con IDs estables para que reimportar actualice en vez de duplicar. Usala siempre que el usuario pida flashcards, tarjetas, preguntas de repaso, un mazo de Anki o "repasar con tarjetas" de una guía, clase, unidad o materia, aunque no diga "Anki"; también para generar mazos en lote de las guías que todavía no tienen flashcards, o un mazo de temas flojos a partir de los resultados de un simulacro.
---

# Flashcards para Anki

Convierte una guía `*_Guia.md` de `3_Guias_de_Estudio/` en un mazo
`4_Flashcards/[Unidad]_[Tema]_Flashcards.csv` que Anki importa sin configurar nada
(el CSV trae separador, mazo, tipo de nota y etiquetas en sus encabezados).

## Antes de empezar

1. Leé `AGENTS.md` (reglas de carpetas y nombres; manda sobre esta skill).
2. Identificá la entrada y completá lo que falte:
   - **Guía concreta** (ruta o nombre): de la ruta salen año, materia y unidad.
   - **Materia + unidad/clase**: buscá la guía en `[Año]/[Materia]/3_Guias_de_Estudio/`.
     Si hay varias (p. ej. `C04_Cronobiologia_Guia.md`, `_Resumen_Guia`, `_SintesisProblemas_Guia`),
     usá la guía extendida (la que no tiene `_Resumen` ni `_Sintesis`) y sumá las otras solo
     si aportan contenido que falta.
   - **Lote** ("todas las guías de Psicoanálisis", "las que no tienen flashcards"): ver *Modo lote*.
   - **Guía solo en Word** (`*_Guia.docx` sin `.md`, como en Procesos Básicos II): convertila a
     Markdown en un temporal fuera del repo (`pandoc <guia>.docx -t gfm -o <tmp>/guia.md`) y
     trabajá sobre esa copia; el CSV usa como fuente el nombre del `.docx`.
   - Si no podés determinar la materia o la unidad, **preguntá** antes de generar.
3. Nombre de salida, siempre con el script (nunca a mano):
   ```bash
   python Scripts/estudio/nombres.py generar flashcards --unidad C08 --tema "Pulsión de muerte"
   ```
   Si la guía no tiene tema en el nombre (p. ej. `C##_Guia.md`), sacá el tema de su título `#`.
4. Si el CSV de salida **ya existe**:
   - Leé sus tarjetas con `python Scripts/estudio/anki_csv.py leer <csv>` y **reusá la misma
     `clave` para el mismo concepto**: así Anki actualiza esas tarjetas y conserva su historial
     de repaso. Solo inventá claves nuevas para conceptos nuevos.
   - Si `git status --porcelain <csv>` muestra cambios sin commitear, el usuario lo editó a mano:
     mostrale qué cambió y preguntá antes de sobrescribir.

## Generar las tarjetas

1. Leé la guía **completa** (y la fuente citada en su cabecera si existe y hace falta precisar).
   Para guías muy largas, trabajá por secciones `##` y juntá las tarjetas al final.
2. Leé `references/reglas_tarjetas.md` y aplicalas. Lo esencial:
   - una idea por tarjeta, pregunta que se entienda sola, respuesta breve;
   - mezcla de **básicas** (pregunta/respuesta, ~60–70 %) y **cloze** (~30–40 %, para
     definiciones, términos y datos que conviene evocar dentro de su contexto);
   - priorizá lo que la guía marca como importante ("lo que entra sí o sí", idea-fuerza,
     glosario, preguntas de examen), después distinciones entre conceptos, autores/obras,
     experimentos, casos y ejemplos;
   - cantidad orientativa: 1 tarjeta por concepto evaluable, típicamente 25–60 por guía.
     No rellenes: mejor menos tarjetas buenas.
3. Escribí las tarjetas en un JSON **temporal fuera del repositorio** (en el scratchpad o en
   un directorio temporal), con este formato:
   ```json
   [{"clave": "pulsion-de-muerte-def", "tipo": "basica",
     "frente": "¿Qué es la <b>pulsión de muerte</b> según Freud (1920)?",
     "dorso": "Tendencia a reducir la tensión a cero, retorno a lo inorgánico.",
     "tags": ["definicion"]},
    {"clave": "fort-da", "tipo": "cloze",
     "frente": "El juego del {{c1::fort-da}} muestra la {{c2::repetición}} de una experiencia displacentera.",
     "dorso": "Más allá del principio de placer (1920).", "tags": ["ejemplo"]}]
   ```
   - `clave`: minúsculas y guiones, describe el concepto (no el número de tarjeta).
   - Formato con HTML (`<b>`, `<i>`, `<br>`, `<ul><li>`), **no Markdown** (Anki no lo renderiza).
   - `tags` opcionales por tipo de contenido: `definicion`, `distincion`, `autor`, `ejemplo`,
     `experimento`, `caso`, `clave-examen`.
4. Construí el CSV (agrega encabezados, mazo `Materia::Unidad`, etiquetas de materia, unidad y
   fuente, y valida):
   ```bash
   python Scripts/estudio/anki_csv.py construir <tmp>/tarjetas.json \
     --materia "Psicoanálisis" --unidad C08 --fuente C08_PulsionDeMuerte_Guia.md \
     --salida "2do Año/Psicoanálisis/4_Flashcards/C08_PulsionDeMuerte_Flashcards.csv"
   ```
   Si devuelve errores, corregí el JSON y repetí.
5. Verificá:
   ```bash
   python Scripts/estudio/anki_csv.py validar <csv>      # obligatorio
   python Scripts/estudio/probar_anki.py <csv>           # si está instalado el paquete anki
   ```
   Revisá los avisos (frentes duplicados, tarjetas demasiado largas) y corregí los que tengan sentido.
6. Releé 5–10 tarjetas al azar contra la guía: ¿la respuesta es correcta y está en la fuente?
7. Borrá el JSON temporal.

## Modo lote

Para "todas las guías que no tienen flashcards" de una materia (o de todo `2do Año`):

1. Listá las guías `*_Guia.md` (o `*_Guia.docx` sin `.md`) de `3_Guias_de_Estudio/` (sin `_Resumen`/`_Sintesis`, que
   se usan como complemento) y descartá las que ya tienen su `*_Flashcards.csv`.
2. Mostrale al usuario la lista y cuántos mazos se van a generar antes de arrancar.
3. Si son más de 3, repartí las guías entre subagentes (una o pocas guías cada uno), cada
   uno siguiendo esta skill completa. Al final corré `anki_csv.py validar` sobre todos los CSV.

## Mazo de temas flojos (desde un simulacro)

Si la entrada es un `5_Evaluaciones/*_Resultados.md` (lo genera `/simulacro`):

1. Leé su cabecera (`python Scripts/estudio/frontmatter.py ver <resultados.md>`): `temas_flojos`
   trae cada tema con su `fuente` (guía y sección) y las `preguntas` donde falló. En la tabla
   "Detalle" del intento más reciente, el comentario de esas preguntas dice **qué** confundió.
2. Hacé tarjetas solo de esos temas, buscando el contenido en las secciones citadas, y apuntá
   a la confusión concreta (si confundió terror con angustia, una tarjeta de distinción
   terror/angustia/miedo, no una definición suelta). 3–6 tarjetas por tema.
3. Nombre con tema `TemasFlojos` (p. ej. `C08_TemasFlojos_Flashcards.csv`), etiqueta
   `temas-flojos` en todas, y **claves con prefijo `flojo-`** (`flojo-angustia-miedo-terror`):
   si una clave coincidiera con una del mazo principal de la unidad, Anki pisaría esa tarjeta.

## Tipos de nota de Anki

Los nombres dependen del idioma con que se creó la colección de Anki del usuario:

| Idioma de la colección | Básica | Cloze |
|---|---|---|
| Español (predeterminado) | `Básico` | `Respuesta anidada` |
| Inglés | `Basic` | `Cloze` |

Si al importar Anki dice que no encuentra el tipo de nota, regenerá con
`--tipo-basico Basic --tipo-cloze Cloze` (o las variables `ANKI_TIPO_BASICO` / `ANKI_TIPO_CLOZE`).

## Al terminar, informá

- Ruta del CSV, cantidad de tarjetas (básicas / cloze) y resultado de la validación.
- Cómo importarlo: en Anki, **Archivo → Importar** y elegir el CSV; la configuración ya viene
  en el archivo. Reimportar una versión nueva actualiza las tarjetas existentes.
- Avisos que quedaron sin resolver, si los hay.
