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
`1er Año/Psicoanálisis/1_Bibliografia_Original/Freud_Cap_1.pdf`

Si el usuario no especifica a qué materia corresponde un texto, **DEBES PREGUNTARLE** antes de proceder a guardarlo.

## Nomenclatura Estricta de Archivos

Al crear nuevos archivos generados, DEBES aplicar las siguientes convenciones de nombres para que Windows los ordene correctamente por Unidad:
- **Textos Extraídos**: `[Unidad]_[Autor]_[Capítulo]_Crudo.md` (Ej: `U07_Papalia_Cap15_Crudo.md`)
- **Guías de Estudio**: `[Unidad]_[Tema_Principal]_Guia.ext` (Ej: `U07_Adolescencia_Guia.docx`)
- **Flashcards**: `[Unidad]_[Tema]_Flashcards.csv` (Ej: `U07_Adolescencia_Flashcards.csv`)
- **Evaluaciones**: `[Unidad]_[Tema]_Simulacro.md` (Ej: `U07_Adolescencia_Simulacro.md`)

## Nivel de Detalle de los Apuntes (Regla Obligatoria)

Al generar resúmenes o guías de estudio, **SIEMPRE debes crear "Apuntes Extendidos"**. 
* **Extensión Máxima:** No debes sobre-sintetizar ni omitir detalles. El material generado debe funcionar como un reemplazo completo del libro original.
* **Profundidad:** Incluye todos los ejemplos relevantes, experimentos, estadísticas, casos de estudio y matices teóricos mencionados en la bibliografía fuente.
* **Formato:** Aunque apliques estructuras (como mapas conceptuales o glosarios), el cuerpo del desarrollo analítico debe ser exhaustivo y lo más detallado posible.
