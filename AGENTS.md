---
description: Reglas de organización de archivos para la carrera de Psicología.
trigger: always_on
---

# Reglas de Organización de Archivos

Al descargar bibliografía, procesar PDFs, generar resúmenes o crear flashcards en este directorio, debes **SIEMPRE** respetar la estructura jerárquica de años y materias. 

**NUNCA** guardes archivos en una carpeta global de `/Bibliografía` o `/Resúmenes` en la raíz del proyecto.

## Estructura Secuencial de Carpetas (Pipeline)

El formato que debes utilizar y crear (si no existe) es el siguiente, dividido en 5 etapas secuenciales para cada materia:

```text
[Año de la Carrera]/[Nombre de la Materia]/
├── 1_Bibliografia_Original/  -> Para los PDFs, PPTs y textos originales descargados.
├── 2_Textos_Extraidos/       -> Para los archivos .md crudos generados post-OCR/extracción.
├── 3_Guias_de_Estudio/       -> Para los apuntes extendidos finales en .md y .docx.
│   └── _media/               -> Para guardar los diagramas Mermaid (.png) y otros assets.
├── 4_Flashcards/             -> Para los mazos CSV exportados para Anki.
└── 5_Evaluaciones/           -> Para los simulacros de parciales y tests.
```

**Ejemplo de uso correcto:**
`2do Año/Psicoanálisis/1_Bibliografia_Original/Freud_Cap_1.pdf`

Si el usuario no especifica a qué materia corresponde un texto, **DEBES PREGUNTARLE** antes de proceder a guardarlo.

## Nomenclatura Estricta de Archivos

Al crear nuevos archivos generados, DEBES aplicar las siguientes convenciones de nombres para que Windows los ordene correctamente por Unidad:
- **Textos Extraídos**: `[Unidad]_[Autor]_[Capítulo]_Crudo.md` (Ej: `U07_Papalia_Cap15_Crudo.md`)
- **Guías de Estudio**: `[Unidad]_[Tema_Principal]_Guia.ext` (Ej: `U07_Adolescencia_Guia.docx`)
- **Flashcards**: `[Unidad]_[Tema]_Flashcards.csv` (Ej: `U07_Adolescencia_Flashcards.csv`)
- **Evaluaciones**: `[Unidad]_[Tema]_Simulacro.md` (Ej: `U07_Adolescencia_Simulacro.md`)

### Detalle de los componentes del nombre

- **`[Unidad]`**: siempre con dos dígitos (`U01`…`U12`) para que el orden alfabético coincida con el orden de cursada.
  - Si la materia se organiza por **clases** en vez de unidades, usa `C01`, `C02`… (rangos: `C17_18`).
  - Para material que abarca toda la materia o un cuatrimestre: `Global_1erC`, `Global_2doC`. Para ejes que cruzan varias unidades: `Transversal_[Tema]`.
  - Si la bibliografía de la cátedra viene numerada, agrega el número de texto después de la unidad: `U04_T15_Freud_DueloYMelancolia_Crudo.md`.
- **`[Autor]` / `[Tema]` / `[Capítulo]`**: en PascalCase o con guiones bajos, **sin truncar palabras** (✅ `DueloYMelancolia`, ✅ `Duelo_y_Melancolia`, ❌ `Lasintervencionesdel`). Evita espacios, paréntesis y prefijos como `(2)` o `2 - `.
- **Sin sufijos de versión** (`_v10`, `_v11`, `_FINAL`): el historial lo guarda git. Al regenerar una guía, sobrescribe el archivo existente.

## Diagramas y Assets

- Cada diagrama se guarda en `3_Guias_de_Estudio/_media/` como par `.mmd` (fuente) + `.png` (render), con el mismo nombre base.
- Nombra los diagramas por guía, no por timestamp: `[Unidad]_[Tema]_[NN].png` (Ej: `U07_Adolescencia_01.png`).
- La guía `.md` debe referenciar el `.png` con ruta **relativa** (`![Etapas de Marcia](_media/U07_Adolescencia_01.png)`) además de, o en lugar de, el bloque ```` ```mermaid ````. **NUNCA** uses rutas absolutas de Windows (`C:\Users\...`).
- Las imágenes que salen del OCR de un texto extraído van en `2_Textos_Extraidos/_media/[Nombre_del_Crudo]/`, y los enlaces del `.md` crudo deben apuntar ahí.

## Archivos Temporales y Scripts Auxiliares

- Los intermedios de exportación (`*.temp.md`, `*.temp.md.ps1`, `test*.md`, `test*.docx`) se deben **borrar al terminar** la exportación. No los dejes en las carpetas de materias.
- Los scripts de utilidad (`.ps1`, `.js`, `.py`) van en `/Scripts`, nunca dentro de `[Año]/`. No escribas rutas absolutas de un equipo concreto: recibe las rutas como parámetro o usa rutas relativas a la raíz del repositorio.

## Carpetas Heredadas (Legacy)

Hay materias anteriores a este pipeline (todo `1er Año/`, y en `2do Año/` carpetas como `biologia/`, `estadistica psicologia/`, `procesos basicos 2/`, `Psicología Experimental/`, o `Psicoanálisis/biblio (1er cuatri)/`).
- **No las reorganices ni renombres por iniciativa propia**: propone la migración y espera confirmación del usuario.
- Cuando el usuario pida trabajar sobre una materia heredada, crea las carpetas del pipeline **dentro de esa materia** y guarda ahí solo el material nuevo.
- Si una materia se cursa en ambos cuatrimestres, usa **una sola carpeta de materia** y distingue los cuatrimestres con el código de unidad/clase o con `Global_1erC` / `Global_2doC`; no crees carpetas hermanas como `Materia (1er Cuatri)/`.

## Nivel de Detalle de los Apuntes (Regla Obligatoria)

Al generar resúmenes o guías de estudio, **SIEMPRE debes crear "Apuntes Extendidos"**. 
* **Extensión Máxima:** No debes sobre-sintetizar ni omitir detalles. El material generado debe funcionar como un reemplazo completo del libro original.
* **Profundidad:** Incluye todos los ejemplos relevantes, experimentos, estadísticas, casos de estudio y matices teóricos mencionados en la bibliografía fuente.
* **Formato:** Aunque apliques estructuras (como mapas conceptuales o glosarios), el cuerpo del desarrollo analítico debe ser exhaustivo y lo más detallado posible.
