# Análisis del repositorio y oportunidades de mejora

*Relevamiento: octubre 2026 · 705 archivos versionados · ~1,8 GB en disco · historial git de ~1,6 GB.*

Las mejoras están ordenadas por prioridad. Ninguna de las de reorganización se aplicó
todavía: mover o borrar archivos es decisión del dueño del repositorio.

---

## 1. Prioridad alta

### 1.1 Visibilidad del repositorio y material con derechos de autor
- El repositorio es **público** en GitHub y contiene ~296 PDFs, la mayoría bibliografía
  de cátedra (Freud, Lacan, Papalia, Segal, Ruiz Vargas…), además de PPTs de clase,
  videos `.mp4` y podcasts `.m4a` de NotebookLM.
- La regla de `.gitignore` que debía protegerlos (`**/1_Bibliografia_Original/`) **no
  aplica a ningún archivo**: esa carpeta todavía no existe en ninguna materia, así que
  todo se subió igual.
- También hay trabajos con nombre propio y de compañeros, datos de una encuesta
  (`Estadística/6_Entregables/Inv_TPFinal_Datos.csv`) e IDs de carpetas de
  Google Drive en `Scripts/`.

**Recomendación:** pasar el repositorio a **privado** (Settings → General → Danger Zone →
Change visibility). Es reversible y resuelve el problema de inmediato. Después, migrar la
bibliografía a `1_Bibliografia_Original/` para que el `.gitignore` empiece a aplicar.

### 1.2 Tamaño del repositorio
- `.git` pesa ~1,6 GB. GitHub recomienda repositorios < 1 GB; clonar es lento y se acerca
  a los límites blandos.
- Los archivos más pesados: `09. Freud - La interpretación de los sueños` (75 MB), Ruiz
  Vargas cap. 2 (67 MB), PPT clase 11 de Procesos Básicos I (67 MB), 5 videos de
  NotebookLM (35–58 MB c/u), 2 podcasts (37–38 MB).

**Recomendación:** sacar del versionado PDFs/PPTs/videos/audio (que ya viven en Drive /
OneDrive) y, si se quiere achicar el historial, reescribirlo con `git filter-repo` (esto
reescribe commits: hacer backup antes). Alternativa: Git LFS solo para lo imprescindible.

### 1.3 Contradicción entre README y AGENTS.md *(corregido en este cambio)*
El README anterior pedía carpetas `/Bibliografía`, `/Resúmenes`, `/Flashcards`,
`/Entregables`, que `AGENTS.md` prohíbe explícitamente. Un agente que leyera el README
podía guardar archivos en el lugar equivocado. Además, el ejemplo de `AGENTS.md` ubicaba
Psicoanálisis en `1er Año`.

---

## 2. Organización de carpetas

### 2.1 Materias fuera del pipeline de 5 etapas
| Materia | Situación | Propuesta |
|---------|-----------|-----------|
| `1er Año/*` | Agrupado por `1er Cuatrimestre/` y `2do Cuatrimestre/` | **Decidido: se mantiene como archivo histórico, sin migrar** |
| ~~`2do Año/biologia`~~ | ✅ **Migrada** a `2do Año/Biología/` | — |
| ~~`2do Año/estadistica psicologia`~~ | ✅ **Migrada** a `2do Año/Estadística/` (TP en `6_Entregables/`) | — |
| ~~`2do Año/procesos basicos 2`~~ | ✅ **Migrada** a `2do Año/Procesos Básicos II/` | — |
| ~~`2do Año/Psicología Experimental`~~ | ✅ **Migrada** al pipeline con prefijo `Inv_` | — |
| ~~`2do Año/Psicoanálisis`~~ | ✅ **Migrada**: se eliminaron `biblio/`, `belucci/`, `clases/`, `lacan/` | — |
| ~~`2do Año/Psicología Evolutiva (1er Cuatri)`~~ | ✅ **Unificada** en `Psicología Evolutiva/` (Piaget `U05`, Desarrollo Cognitivo `U06`) | — |

### 2.2 Nombres de carpetas inconsistentes
*(2do año corregido: `Biología`, `Estadística`, `Procesos Básicos II`. Queda `1er Año`.)*
Mezcla de mayúsculas, acentos y abreviaturas: `biologia`, `estadistica psicologia`,
`procesos basicos 2`, `Psicología Experimental`, `Psico General`. Proponer un estándar
(p. ej. nombre oficial de la materia con mayúscula inicial y acentos: `Biología`,
`Estadística`, `Procesos Básicos II`).

### 2.3 Archivos sueltos o mal ubicados en `2do Año/`
- ~~`PROCESOS BÀSICOS II - CLASE 29-05-26_ … .pdf`~~ *(borrado: mismo texto que los
  apuntes de la clase 10, ya en `Procesos Básicos II/1_Bibliografia_Original/`)*.
- ~~Scripts de trabajo `check_wide.js`, `move_biblio.ps1`, `move_compendio.ps1`~~
  *(movidos a `Scripts/` y parametrizados: ya no tienen rutas fijas)*.
- ~~Pruebas: `test.md`, `test.docx`, `test.ps1`, `test_png.js`~~ *(borrados)*.

---

## 3. Duplicados y archivos temporales

- ~~**4 PDFs idénticos** de Belucci (05, 08, 15, 43)~~ *(borradas las copias de `belucci (1er cuatri)/`)*.
- ~~**47 archivos con prefijo `(2) ` o `2 - `**~~ en 2do año: eran versiones para imprimir
  (2 páginas por hoja); se movieron a `_imprimir/`. Quedan los de `1er Año`.
- **Versiones manuales** en `Psicoanálisis/3_Guias_de_Estudio/`: `U04_…_v10.docx`,
  `_v11.docx`, `_FINAL.docx` (ídem U05). Git ya guarda las versiones; dejar solo una.
- ~~**Temporales de exportación** que quedaron versionados~~ *(borrados)*: `*.docx.temp.md`,
  `*.docx.temp.md.ps1` (Psicoanálisis U04/U05, Evolutiva `_old`),
  `experimental_designs.pdf.temp.md`.
- ~~`Psicología Evolutiva/Resúmenes_Deprecados/_old/`: ~60 archivos obsoletos~~
  *(borrada la carpeta completa; sigue disponible en el historial de git)*.

`.gitignore` se amplió en este cambio para que estos temporales no vuelvan a subirse.

---

## 4. Calidad del contenido generado

### 4.1 Imágenes rotas en los textos extraídos
~130 enlaces `![](images/<hash>.jpg)` apuntan a una carpeta `images/` que no se subió:
- `Psicología Evolutiva/2_Textos_Extraidos/*` (U07 y U08: Papalia caps. 1, 3, 15, 16, 17; Piaget cap. 5)
- `Psicoanálisis/2_Textos_Extraidos/U04_T08…`, `U04_T19…`
- `Psicología Experimental/2_Textos_Extraidos/Inv_Schaefer_MusicEvokedEmotionsCurrentStudies_Crudo.md` (43)

**Opciones:** subir las imágenes a `2_Textos_Extraidos/_media/<crudo>/` y reescribir los
enlaces, o quitar los enlaces si las figuras no aportan.

### 4.2 Diagramas Mermaid desconectados de las guías
Los `.png` de `_media/` (12 en Psicoanálisis, 27 en Evolutiva) **no están referenciados
desde ningún `.md`**: las guías usan bloques ```` ```mermaid ```` y los PNG solo se usan al
exportar a `.docx`. Además, los nombres son timestamps (`mermaid_1786917962589_5.png`),
imposibles de relacionar con su guía. Ver la nueva regla en `AGENTS.md` → *Diagramas y
Assets*.

### 4.3 Nomenclatura
- `Psicoanálisis/3_Guias_de_Estudio/` usa `C01_Guia.md` … `C24_Guia.md` (sin tema) y
  `U04_Psicoanalisis_Guia_FINAL.md`. Sugerido: `C01_Epistemologia_Guia.md`, etc.
- `Psicoanálisis/2_Textos_Extraidos/` trunca títulos al quitar espacios
  (`U05_T27_Belucci_Lasintervencionesdel_Crudo.md`,
  `U04_T04_T01_Belucci_Introducciónaldiagnóstico_Crudo.md`). El script `move_biblio.ps1`
  que los generó tomaba solo las 3 primeras palabras y borraba los espacios *(corregido:
  ahora usa PascalCase sin acentos y título completo; los 29 crudos afectados ya se
  renombraron, y `U04_T04_T01_Belucci…` pasó a `U04_T01_…`)*.
- Archivos de otros formatos sin convención: `piaget - guia estudio completa.md`,
  `clase 08 - piaget preoperatorio.md`, `Clase 01 - Estadistica Psicología.md`.

### 4.4 Etapa 4 (Flashcards) vacía
`5_Evaluaciones/` ya tiene material en Biología, Estadística y Psicoanálisis, pero ninguna
materia tiene `4_Flashcards/`, aunque hay guías aptas (p. ej. las C01–C24 de Psicoanálisis
o las C01–C10 de Estadística). Generar flashcards de las guías existentes aprovecharía mejor
el trabajo ya hecho.

---

## 5. Herramientas

### 5.1 Mapa del plan de estudio (`index.html` + `plan_estudio_psicologia_files/`)
- Es una página de Gemini guardada con «Guardar como…»: ~6 MB de recursos de Google
  (`gtm.js`, `editor.main.js`, `m=_b`, etc.) y un `index.html` de 1 MB. El código propio
  está solo en `shim.html`.
- La página guardada incluye datos de la sesión de Google con la que se exportó (cuenta,
  tokens de sesión). Conviene revisarla y no publicarla tal cual.
- **Propuesta:** extraer el mapa a un `plan_estudio/index.html` autocontenido (HTML + CSS +
  JS propio, sin dependencias de Google) y borrar la carpeta `_files`. Ventajas: liviano,
  editable, publicable con GitHub Pages.

### 5.2 Planificador de Parciales
- Dos implementaciones con lógica duplicada y reglas que ya divergen (`OFFSETS` de
  `planificador_notion.html` tiene «TP conceptual» y «Lectura»; `index.html` no).
- En `index.html`, `sessionsFor()` tiene un comentario sobre mover sesiones vencidas a
  hoy que no está implementado, y variables sin uso (`t`, `orig`).
- La lista `SEED` queda congelada al 4/10/2026; si ya hay datos en `localStorage`, nunca
  se vuelve a leer.

### 5.3 Scripts de Drive
- `fetch_pdfs.py` guarda en una carpeta global `…\Psicología\Bibliografía`, contra lo que
  pide `AGENTS.md`.
- Rutas absolutas e IDs de carpeta escritos en el código; no hay argumentos de línea de
  comandos ni `requirements.txt`.
- Sin paginación (`nextPageToken` se pide pero no se usa): carpetas con > 100 archivos
  quedan incompletas.
- Scope `drive` completo cuando alcanza con `drive.readonly`.

---

## 6. Documentación *(aplicado en este cambio)*

- `README.md` reescrito: estructura real, tabla de estado por materia, flujo de estudio
  con entradas/salidas, herramientas y qué se versiona.
- `AGENTS.md`: ejemplo corregido (`2do Año/Psicoanálisis`), y nuevas secciones sobre
  códigos de unidad (`U`, `C`, `T`, `Global`, `Transversal`), nombres sin truncar, sin
  sufijos de versión, diagramas y assets, temporales, scripts y carpetas heredadas.
- `Scripts/README.md` y `Planificador_Parciales/README.md` nuevos.
- `.gitignore`: temporales de exportación, `node_modules/`, `__pycache__/`, archivos de
  bloqueo de Office (`~$*`).

## 7. Próximos pasos sugeridos

1. Pasar el repo a privado.
2. ~~Borrar temporales, `test*` y la carpeta `_old`~~ ✅ hecho.
3. ~~Migrar Psicología Experimental, Procesos Básicos II, Biología, Estadística y las
   carpetas viejas de Psicoanálisis al pipeline~~ ✅ hecho. Unificada también Psicología Evolutiva. Todo 2do año sigue el pipeline; `1er Año/` queda como archivo histórico.
4. Corregir `fetch_pdfs.py` (destino por materia, paginación, argumentos).
5. Generar `4_Flashcards/` a partir de las guías de Psicoanálisis C01–C24.
6. Decidir sobre bibliografía/videos en git y, si corresponde, limpiar el historial.
