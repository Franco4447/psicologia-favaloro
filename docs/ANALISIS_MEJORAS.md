# Análisis del repositorio y oportunidades de mejora

*Actualizado: 6 de octubre de 2026 · 480 archivos versionados · `.git` de ~307 MB · repositorio público.*

Primero lo que sigue abierto, ordenado por prioridad; al final, el registro de lo resuelto.

---

## 1. Pendiente

### 1.1 Referencias de los PR en GitHub
Tras las dos reescrituras del historial (ver 2.1 y 2.6), las referencias internas de los PR
#1–#13 (`refs/pull/*`) siguen apuntando a los commits viejos, y lo purgado (bibliografía,
datos de la sesión de Google) sigue accesible por SHA. Solo GitHub Support puede
eliminarlas: el pedido se envió el 5/10/2026 y se amplió el 6/10 con la segunda purga. Al
responder, verificar que los commits viejos den 404.

### 1.2 Pendientes menores de nombres y textos (solo en la copia local)
- **Psicología Social**: `U03_Baron_Citas02_Crudo.md` y `U03_Baron_Citas03_Crudo.md` están
  vacíos (0 KB): volver a extraerlos o borrarlos.
- **Bibliografía de 1er Año**: conserva sus nombres y subcarpetas originales.

### 1.3 Material de estudio
- Flashcards: solo hay mazos de `C04` (Biología) y `C08` (Psicoanálisis); 8 simulacros en
  total. La mayoría de las guías no tiene ninguno de los dos.
- Guías sin escribir: Psicología Experimental U01–U05, Psicología Social U04 y Procesos
  Básicos II. Las 4 guías de Pensamiento (Procesos Básicos III, `U03`) todavía no tienen
  flashcards ni simulacro.

---

## 2. Resuelto

### 2.1 Bibliografía con derechos de autor en un repositorio público *(octubre 2026)*
`1_Bibliografia_Original/`, `2_Textos_Extraidos/` y el material de NotebookLM (282
archivos, ~1,4 GB) dejaron de versionarse y se **purgaron del historial** con
`git filter-repo` (por ID de blob) y force-push a `main`: el repositorio pasó de 1,7 GB a
~350 MB y sigue siendo el mismo y público. Viven solo en OneDrive. El 6/10 también se purgó
el video de NotebookLM de Neurociencias (42 MB), que había quedado fuera de una carpeta
`NotebookLM/`.

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
El mapa era una página de Gemini guardada con «Guardar como…»: el `index.html` y
`plan_estudio_psicologia_files/` traían el correo de la cuenta de Google con la que se
exportó, claves de API de Google y un token de sesión (vencido), y se publicaban en GitHub
Pages. `index.html` es ahora un archivo autocontenido de ~110 KB (React y Tailwind desde
CDN) con el código propio del mapa, sin los ~7 MB de recursos de Google ni datos de la
sesión, y sigue publicado en GitHub Pages. Las versiones viejas y la carpeta se
**purgaron del historial** (6/10/2026, `git filter-repo` conservando los 62 commits).

### 2.7 Diagramas, imágenes y nombres *(octubre 2026)*
- Los 39 diagramas con nombre de timestamp (`mermaid_1786…png`): 24 de Evolutiva pasaron a
  `U07_Adolescencia_NN` / `U08_Adultez_NN` y quedaron enlazados desde su guía; 3 eran copias
  idénticas; los 12 de Psicoanálisis eran de los Word `_v10` ya borrados y se quitaron.
- Textos extraídos (solo locales): 27 copias con nombre truncado borradas en Psicoanálisis y
  344 enlaces a una carpeta `images/` inexistente reemplazados por una marca visible (las
  imágenes eran recortes de otra herramienta y no se pueden reconstruir).
- Psicología Social: se borraron los 12 fragmentos de `2_Textos_Extraidos/Paginados/`, de una
  extracción anterior. Los de Bandura y Walters y los de Pecino y Sánchez repetían el crudo
  completo (con peor OCR); de los de Baron y Byrne se rescataron las leyendas y los rótulos
  de las 20 figuras del capítulo, que ahora están en `U03_BaronByrne_Cap4_Crudo.md`.
- Procesos Básicos III: bibliografía como `[Autor][Año].pdf` y `U0N_Diapositivas_…`, textos
  de Motivación como `U01_…_Crudo.md`, y tres trabajos propios movidos a `6_Entregables/`.
- 1er Año: 88 archivos renombrados con `Global_1erC` / `Global_2doC` o `C[NN]`, versiones
  para imprimir en `_imprimir/`, Neurociencias sin subcarpetas por parcial, y 14 archivos
  ajenos (diapositivas de la cátedra, apuntes de compañeros, extractos) movidos a
  `1_Bibliografia_Original/`.

### 2.8 Planificador de Parciales *(octubre 2026)*
Las dos páginas (`index.html` local y `planificador_notion.html`) tenían la lógica duplicada y
reglas que ya divergían. Ahora hay una sola `index.html` que lee Notion si se abre como Artifact
en claude.ai y, si no, usa la lista fija y las entregas propias. Las reglas de repaso son las
mismas en ambos modos, las entregas nuevas de `SEED` aparecen aunque haya datos guardados, y
los datos del formato anterior se migran solos.

### 2.9 Documentación
`README.md` y `AGENTS.md` coherentes entre sí (sin carpetas globales, códigos de unidad,
nombres sin truncar, diagramas, temporales, 1er Año, cómo subir commits que mueven muchos
archivos). `Scripts/README.md` y `Planificador_Parciales/README.md` describen sus
herramientas.
