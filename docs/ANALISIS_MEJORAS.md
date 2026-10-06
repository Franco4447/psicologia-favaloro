# Análisis del repositorio y oportunidades de mejora

*Actualizado: 6 de octubre de 2026 · 524 archivos versionados · `.git` de ~340 MB · repositorio público.*

Primero lo que sigue abierto, ordenado por prioridad; al final, el registro de lo resuelto.

---

## 1. Pendiente

### 1.1 Datos personales y de la sesión de Google en el historial
El mapa del plan de estudio era una página de Gemini guardada con «Guardar como…». El
`index.html` y la carpeta `plan_estudio_psicologia_files/` traían el correo de la cuenta de
Google con la que se exportó, claves de API de Google y un token de sesión (vencido), y se
publicaban en GitHub Pages. Ya se reemplazaron por un mapa autocontenido (ver 2.6), pero
**siguen en el historial de git**. Quitarlos de ahí requiere otra reescritura del historial
(`git filter-repo` + force-push).

### 1.2 Referencias de los PR en GitHub
Tras purgar la bibliografía del historial (ver 2.1), las referencias internas de los PR
#1–#9 (`refs/pull/*`) siguen apuntando a los commits viejos, y esos archivos siguen
accesibles por SHA. Solo GitHub Support puede eliminarlas: el pedido se envió el
5/10/2026. Al responder, verificar que los commits viejos den 404.

### 1.3 Diagramas Mermaid desconectados de las guías
39 `.png` de `_media/` (12 en Psicoanálisis, 27 en Evolutiva) tienen nombres de timestamp
(`mermaid_1786917962589_5.png`) y **no están referenciados desde ningún `.md`**: las guías
usan bloques ```` ```mermaid ```` y los PNG solo se usaron al exportar a Word. `AGENTS.md`
pide `[Unidad]_[Tema]_[NN].png` enlazado con ruta relativa desde la guía.

### 1.4 Imágenes rotas en los textos extraídos
335 enlaces `![](images/<hash>.jpg)` en 21 textos extraídos (Evolutiva, Psicoanálisis,
Experimental) apuntan a una carpeta `images/` que no existe. Los textos extraídos ya no se
versionan, así que afecta solo a la copia local. Opciones: recuperar las imágenes en
`2_Textos_Extraidos/_media/<crudo>/` y reescribir los enlaces, o quitar los enlaces.

### 1.5 Nombres de archivo
- **1er Año** conserva los nombres originales (con espacios, `(2) `, nombres propios):
  13 archivos versionados con prefijo `(2) ` en Neurociencias y Epistemología. `estado.py`
  no reconoce esos archivos porque no tienen código de unidad.
- **Procesos Básicos III / Pensamiento**: los 9 textos extraídos ya son `U03_…`, pero los
  PDF originales tienen nombres libres (`Clase 01 - Pensamiento.pdf`) y no hay guía.

### 1.6 Planificador de Parciales
- Dos implementaciones con lógica duplicada y reglas que ya divergen (`OFFSETS` de
  `planificador_notion.html` tiene «TP conceptual» y «Lectura»; `index.html` no).
- La lista `SEED` queda congelada al 4/10/2026; si ya hay datos en `localStorage`, nunca
  se vuelve a leer.

### 1.7 Material de estudio
- Flashcards: solo hay mazos de `C04` (Biología) y `C08` (Psicoanálisis); 8 simulacros en
  total. La mayoría de las guías no tiene ninguno de los dos.
- Guías sin escribir: Psicología Experimental U01–U05, Psicología Social U04, Procesos
  Básicos II y Pensamiento (Procesos Básicos III).

---

## 2. Resuelto

### 2.1 Bibliografía con derechos de autor en un repositorio público *(octubre 2026)*
`1_Bibliografia_Original/`, `2_Textos_Extraidos/` y el material de NotebookLM (282
archivos, ~1,4 GB) dejaron de versionarse y se **purgaron del historial** con
`git filter-repo` (por ID de blob) y force-push a `main`: el repositorio pasó de 1,7 GB a
~350 MB y sigue siendo el mismo y público. Viven solo en OneDrive.

### 2.2 Estructura de carpetas *(octubre 2026)*
Todo 2do Año sigue el pipeline (Biología, Estadística, Procesos Básicos II y III,
Experimental con prefijo `Inv_`, Psicoanálisis, Evolutiva unificada, Social). `1er Año`
migró la estructura: una carpeta por materia con sus etapas (se fusionaron Neurociencias y
LEO de ambos cuatrimestres y se creó `Antropología/`), sin renombrar archivos. Nombres de
carpeta normalizados (`Biología`, `Estadística`, `Procesos Básicos I/II`,
`Psicología General`).

### 2.3 Nomenclatura de guías y textos
- Las 19 guías de Psicoanálisis pasaron a `C##_[Tema]_Guia.md`; se quitaron los sufijos
  `_FINAL`, `_v10`, `_v11` (PR #4).
- Los textos extraídos de Belucci ya no truncan títulos (`move_biblio.ps1` corregido).
- Procesos Básicos III: Motivación `U01`, Aprendizaje `U02`, Pensamiento `U03`.

### 2.4 Duplicados y temporales
Copias idénticas de Belucci, temporales de exportación (`*.temp.md`), pruebas (`test*`) y
la carpeta `_old` de Evolutiva, borrados. Las versiones para imprimir de 2do Año están en
`_imprimir/`. `.gitignore` cubre temporales, credenciales, `node_modules/`, `__pycache__/`
y archivos de bloqueo de Office.

### 2.5 Scripts *(octubre 2026)*
- Scripts de mantenimiento movidos a `Scripts/` y parametrizados (sin rutas fijas).
- Scripts de Google Drive: reciben los IDs de carpeta por argumento, paginan, usan permiso
  de solo lectura, comparten `drive_comun.py` y `fetch_pdfs.py` descarga a
  `[Año]/[Materia]/1_Bibliografia_Original/` en vez de a una carpeta global.
- Los scripts de `Scripts/estudio/` funcionan en la consola de Windows (UTF-8) y detectan
  Tesseract instalado por usuario.

### 2.6 Mapa del plan de estudio *(octubre 2026)*
`index.html` es ahora un archivo autocontenido de ~110 KB (React y Tailwind desde CDN) con
el código propio del mapa, sin los ~7 MB de recursos de Google ni datos de la sesión. Se
borró `plan_estudio_psicologia_files/`. Sigue publicado en GitHub Pages.

### 2.7 Documentación
`README.md` y `AGENTS.md` coherentes entre sí (sin carpetas globales, códigos de unidad,
nombres sin truncar, diagramas, temporales, 1er Año, cómo subir commits que mueven muchos
archivos). `Scripts/README.md` y `Planificador_Parciales/README.md` describen sus
herramientas.
