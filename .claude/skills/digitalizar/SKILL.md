---
name: digitalizar
description: 'Convierte la bibliografía original del repositorio de Psicología (PDFs con texto, PDFs escaneados, artículos a dos columnas, diapositivas en PDF o PowerPoint) en textos extraídos Markdown con marcas de página, OCR en español cuando hace falta, limpieza (palabras cortadas, encabezados repetidos) e informe de calidad. Usala siempre que el usuario pida pasar a texto, digitalizar, extraer, transcribir u "OCR" un PDF, libro, capítulo, apunte o PowerPoint, o cuando otra tarea (una guía, flashcards) necesite un texto que solo existe como PDF/PPTX.'
---

# Digitalizar bibliografía

Convierte `1_Bibliografia_Original/*.pdf|.pptx` en `2_Textos_Extraidos/[Unidad]_[Autor]_[Capítulo]_Crudo.md`,
la entrada de `/guia-estudio`.

> Los textos extraídos **no se suben a git** (están en `.gitignore`: son copias completas de
> material con derechos de autor). Quedan solo en la copia local.

## Antes de empezar

1. Leé `AGENTS.md` (manda sobre esta skill).
2. Verificá el entorno una vez por sesión: `python Scripts/estudio/verificar_entorno.py`
   (para OCR hace falta Tesseract con el idioma español `spa`).
3. Identificá materia, unidad/clase, autor y capítulo. Si no están claros, **preguntá** antes de
   guardar. Si el PDF no está en `1_Bibliografia_Original/`, guardalo ahí primero (nombre según
   `AGENTS.md`: `[Autor][Año].pdf`, `[Cuatri]_T[NN]_[Autor]_[Titulo].pdf` o `C[NN]_Diapositivas_[Tema].ext`).
4. Nombre de salida con el script:
   ```bash
   python Scripts/estudio/nombres.py generar crudo --unidad U04 --texto 15 --autor Freud --tema "Duelo y melancolía"
   python Scripts/estudio/nombres.py generar crudo --unidad C04 --autor Diapositivas --tema Cronobiologia
   ```
5. Si el crudo ya existe y tiene cabecera, `frontmatter.py estado`; si fue editado a mano
   (correcciones de OCR), **preguntá** antes de sobrescribir.

## Extraer

```bash
python Scripts/estudio/extraer.py <entrada.pdf|.pptx> <salida_Crudo.md> --titulo "15. Freud - Duelo y melancolía" [opciones]
```

| Situación | Opciones |
|---|---|
| PDF con texto (artículo, apunte) | ninguna: detecta solo las páginas a dos columnas |
| PDF escaneado (libro fotocopiado) | ninguna: OCR automático en las páginas sin texto (~6 s por página) |
| Texto en inglés o mezclado | `--idioma eng` o `--idioma spa+eng` |
| Diapositivas (PDF apaisado o `.pptx`) | detecta solas; en PowerPoint aplica OCR a las imágenes de diapositivas sin texto. Usá `--idioma spa+eng` si las figuras están en inglés |
| Libro largo: un capítulo por vez | `--paginas 45-78` y un crudo por capítulo |
| Guardar las figuras | `--imagenes` → `2_Textos_Extraidos/_media/<crudo>/`, enlazadas en el texto |
| OCR forzado (texto de la capa PDF roto) | `--ocr si` |

El script escribe `## Página N` (o `## Diapositiva N`) para poder citar, une palabras cortadas por
guion, rearma los párrafos, quita encabezados/pies repetidos y números de página, y deja en la cabecera
YAML el método (`texto` / `ocr` / `pptx`) y un informe de calidad.

`## Página N` es la página **del PDF**. En escaneos con dos páginas del libro por hoja, una página
del PDF contiene dos del libro: si hace falta citar la página impresa, anotala en el crudo (el número
suele aparecer en el texto) o aclaralo en la guía.

## Revisar la calidad

1. Leé el informe que imprime el script:
   - **Revisar a mano**: páginas con OCR de confianza baja (< 75 %) o con texto raro.
   - **Sin texto**: páginas en blanco, solo imágenes o diagramas.
2. Abrí 2–3 de esas páginas en el crudo y comparalas con el PDF:
   - Si el OCR es malo por idioma: repetí con `--idioma` correcto.
   - Si una página a dos columnas salió mezclada: repetí solo ese rango y avisá.
   - Errores puntuales de OCR en términos clave (nombres propios, conceptos): corregilos en el crudo.
   - Notas al pie de libros escaneados (p. ej., Amorrortu) suelen salir con ruido: no hace falta
     limpiarlas salvo que aporten contenido.
3. En diapositivas, lo que dicen los **gráficos o fotos** no siempre se recupera: si una diapositiva
   importante quedó "sin texto", mirá la imagen (`--imagenes`) y describila en el crudo.

## Al terminar, informá

Ruta del crudo, páginas y palabras, cuántas por OCR y la confianza media, páginas a revisar, y el
siguiente paso natural: `/guia-estudio` con ese texto. Recordá que el crudo no se sube a git.
