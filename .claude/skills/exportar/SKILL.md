---
name: exportar
description: 'Exporta guías de estudio del repositorio de Psicología (*_Guia.md) a Word con una plantilla de estilos prolija, con los diagramas Mermaid como imágenes del tamaño justo, y opcionalmente a PDF y a una versión para imprimir 2 páginas por hoja. Usala siempre que el usuario pida pasar una guía a Word, .docx, PDF, "para imprimir", "para llevar al parcial" o "exportar", o cuando termine una guía nueva y quiera el documento final.'
---

# Exportar guías a Word / PDF

```bash
python Scripts/estudio/exportar.py <guia.md> [--pdf] [--imprimir] [--indice] [--forzar]
```

| Opción | Genera |
|---|---|
| (ninguna) | `[Unidad]_[Tema]_Guia.docx` junto a la guía |
| `--pdf` | además `[Unidad]_[Tema]_Guia.pdf` (con LibreOffice) |
| `--imprimir` | además `_imprimir/[Unidad]_[Tema]_Guia_Imprimir.pdf`: A4 apaisado, 2 páginas por hoja (implica `--pdf`) |
| `--indice` | índice al principio del Word (Word pide "actualizar campos" al abrirlo; en el PDF no aparece completo) |

## Pasos

1. Leé `AGENTS.md`. La entrada es una guía `*_Guia.md` de `3_Guias_de_Estudio/`; si el usuario
   nombra la clase o el tema, buscala ahí.
2. Si ya existe el `.docx` (o el `.pdf`), **preguntá antes de reemplazarlo**: puede tener retoques
   hechos en Word, o ser una versión anterior hecha con otra herramienta. Con permiso, `--forzar`.
3. Corré el script. Antes de convertir:
   - renderiza los diagramas (`diagramas.py`): `.mmd` + `.png` en `_media/` y la imagen en la guía;
   - en Word va la imagen, no el código Mermaid, con ancho ajustado a la página (máx. 16 × 20 cm);
   - usa la plantilla `Scripts/estudio/plantillas/plantilla_guia.docx` (Calibri, títulos en color,
     márgenes de 2,2 cm). Para cambiar el estilo de todas las guías, editá esa plantilla en Word.
4. Verificá el resultado: que el `.docx` abra, que las tablas y diagramas estén, y si hubo PDF,
   que la cantidad de páginas sea razonable (`pdfinfo`). Los intermedios se borran solos (van a un
   directorio temporal); no dejes `*.temp.md` en las carpetas de materias.
5. Si falta pandoc o LibreOffice, `python Scripts/estudio/verificar_entorno.py --probar` dice cómo
   instalarlos.

## Al terminar, informá

Archivos generados con su ruta, cantidad de páginas del PDF y de hojas para imprimir, y si quedó
algún diagrama o imagen sin encontrar (aparece como "[Imagen no encontrada: …]" en el Word).
