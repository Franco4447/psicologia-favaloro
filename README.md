# 🧠 Hub de Estudio: Licenciatura en Psicología · Universidad Favaloro

Repositorio personal de apuntes, guías de estudio, textos extraídos y herramientas de
planificación de la carrera. Está pensado para trabajar junto a agentes de IA
(Antigravity, Claude Code, etc.), que siguen las reglas de [`AGENTS.md`](AGENTS.md).

> **Fuente de verdad para agentes:** [`AGENTS.md`](AGENTS.md). Si este README y
> `AGENTS.md` se contradicen, manda `AGENTS.md`.

---

## 📁 Estructura del repositorio

```text
.
├── AGENTS.md                    -> Reglas obligatorias para agentes (estructura, nombres, nivel de detalle)
├── README.md                    -> Este archivo
├── docs/                        -> Documentación del proyecto (informe de mejoras, convenciones)
├── index.html                   -> Mapa interactivo del plan de estudio (exportado de Gemini Canvas)
├── plan_estudio_psicologia_files/  -> Recursos del mapa anterior (el código propio está en shim.html)
├── Planificador_Parciales/      -> Planificador de repasos espaciados para parciales y TPs
├── Scripts/                     -> Utilidades de Python para descargar material de Google Drive
├── 1er Año/                     -> Materias de 1er año (archivo histórico, por cuatrimestre; no se migra)
└── 2do Año/                     -> Materias de 2do año (todas en el pipeline)
```

### Estructura de cada materia (pipeline de 5 etapas)

Todo material **nuevo** se guarda dentro de su año y materia, siguiendo este pipeline
(ver detalle en [`AGENTS.md`](AGENTS.md)):

```text
[Año de la Carrera]/[Nombre de la Materia]/
├── 1_Bibliografia_Original/  -> PDFs, PPTs y textos originales (ignorado por git)
├── 2_Textos_Extraidos/       -> .md crudos post-OCR/extracción   (U07_Papalia_Cap15_Crudo.md, ignorado por git)
├── 3_Guias_de_Estudio/       -> Apuntes extendidos .md y .docx    (U07_Adolescencia_Guia.md)
│   ├── _media/               -> Diagramas Mermaid (.mmd + .png) y otros assets
│   └── _imprimir/            -> Versiones para imprimir (2 páginas por hoja)  (C05_..._Guia_Imprimir.pdf)
├── 4_Flashcards/             -> Mazos CSV para Anki               (U07_Adolescencia_Flashcards.csv)
├── 5_Evaluaciones/           -> Simulacros y problemas de práctica (U07_Adolescencia_Simulacro.md)
└── 6_Entregables/            -> (Opcional) TPs propios, consigna y datos (Inv_TPFinal_Consigna.pdf)
```

> ⚠️ No existen carpetas globales `/Bibliografía` ni `/Resúmenes` en la raíz: todo vive
> dentro de `[Año]/[Materia]/`.

### Estado actual por materia

| Año | Materia | ¿Sigue el pipeline? | Notas |
|-----|---------|---------------------|-------|
| 1er | Filosofía, Historia, LEO, Neurociencias, Psico General | ❌ | Agrupadas en `1er Cuatrimestre/` (estructura heredada) |
| 1er | Epistemología, LEO, Metodología, Neurociencias, Sociología, Procesos Básicos I | ❌ | Agrupadas en `2do Cuatrimestre/` (estructura heredada) |
| 2do | Psicoanálisis | ✅ | Migrada: bibliografía del 1er cuatri como `1erC_T[NN]_…`, clases como textos extraídos `C[NN]_Catedra_…`, resúmenes de Belucci y material de Lacan como guías `Transversal_…` |
| 2do | Psicología Evolutiva | ✅ | Unificada: Piaget y desarrollo cognitivo del 1er cuatri (`U05`, `U06`) junto a Adolescencia y Adultez (`U07`, `U08`) |
| 2do | Biología | ✅ | Migrada: diapositivas, guías extendidas, resúmenes y síntesis por clase (`C01`…`C11`), problemas en Evaluaciones |
| 2do | Estadística | ✅ | Migrada: guías por clase (`C01`…`C10`), material del 2do parcial (`C06_10_…`), TP final en `6_Entregables/` |
| 2do | Procesos Básicos II | ✅ | Migrada: guías por clase (`C05`…`C09`) y global de la segunda mitad |
| 2do | Psicología Experimental | ✅ | Migrada: bibliografía del trabajo de investigación (prefijo `Inv_`) |

El plan de migración propuesto está en [`docs/ANALISIS_MEJORAS.md`](docs/ANALISIS_MEJORAS.md).

---

## 🛠️ Flujo de estudio recomendado

| Paso | Qué se hace | Entrada → Salida |
|------|-------------|------------------|
| 1. Digitalización | Convertir PDFs/PPTs a Markdown (skill `pdf-to-markdown` u OCR) | `1_Bibliografia_Original/` → `2_Textos_Extraidos/*_Crudo.md` |
| 2. Guía de estudio | Generar **apuntes extendidos** con la skill **`/guia-estudio`** (por partes, con citas de página, diagramas y control de cobertura contra la fuente) | `2_Textos_Extraidos/` → `3_Guias_de_Estudio/*_Guia.md` |
| 3. Exportación | Pasar la guía a `.docx`/`.pdf` prolijo con `export-study-material` | `*_Guia.md` → `*_Guia.docx` (+ diagramas en `_media/`) |
| 4. Estudio activo | Crear tarjetas Anki con la skill **`/flashcards`** (Claude Code) | `*_Guia.md` → `4_Flashcards/*_Flashcards.csv` |
| 5. Autoevaluación | Simulacro de parcial con la skill **`/simulacro`** (archivo, o «tomame examen» en modo interactivo) | `*_Guia.md` → `5_Evaluaciones/*_Simulacro.md` (+ `*_Resultados.md`) |
| 6. Planificación | Cargar fechas de parciales en el [Planificador](Planificador_Parciales/README.md) | Notion «Tareas» → sesiones de repaso |

### Prompts reutilizables

- [`docs/prompts/Estadistica_DocumentoPorClase_Prompt.txt`](docs/prompts/Estadistica_DocumentoPorClase_Prompt.txt): prompt para
  fusionar *presentación de clase + bibliografía* en un documento de estudio exhaustivo.
  Sirve como plantilla para cualquier materia.

---

## 🧰 Herramientas incluidas

### Skills de estudio *(en construcción)*
Skills de Claude Code para digitalizar, armar guías, flashcards y simulacros siguiendo `AGENTS.md`.
Plan y estado: [`docs/PLAN_SKILLS_ESTUDIO.md`](docs/PLAN_SKILLS_ESTUDIO.md).

### Mapa del plan de estudio (`index.html`)
Mapa interactivo de las materias de la carrera, exportado desde Gemini Canvas, con
arrastre tipo Miro (mouse y táctil). El código propio está en
`plan_estudio_psicologia_files/shim.html`; el resto de esa carpeta son dependencias
descargadas por el navegador al guardar la página. Abrir `index.html` en el navegador.

### Planificador de Parciales (`Planificador_Parciales/`)
Calcula sesiones de repaso espaciado (−14, −7, −3, −1 días) para cada entrega.
Dos versiones: una local con `localStorage` y otra sincronizada con Notion.
Ver [`Planificador_Parciales/README.md`](Planificador_Parciales/README.md).

### Scripts de Google Drive (`Scripts/`)
Autenticación OAuth y descarga de PDFs desde carpetas de Drive.
Ver [`Scripts/README.md`](Scripts/README.md).

---

## 🔗 Integración con Google Drive

1. **Google Drive para Escritorio (recomendado):** instala la app oficial para que Drive
   aparezca como unidad local (ej. `G:\`). El agente puede leer los PDFs desde ahí y
   guardar los derivados en este repositorio.
2. **Descarga selectiva:** descarga los PDFs de la semana dentro de
   `[Año]/[Materia]/1_Bibliografia_Original/`.
3. **API de Drive:** usa los scripts de `Scripts/` (requiere credenciales OAuth propias).

El acceso directo local `Google Drive Acceso.url` está ignorado por git (`*.url`), así que
solo existe en la copia local de OneDrive.

---

## 🔒 Qué se versiona y qué no

- **Sí:** textos extraídos, guías de estudio, flashcards, simulacros, herramientas.
- **No:** credenciales (`gdrive_credentials.json`, `gdrive_token.json`, `.env`), accesos
  directos, archivos temporales de exportación (`*.temp.md`, `*.temp.md.ps1`) y la
  bibliografía original con derechos de autor (`1_Bibliografia_Original/`).

---
*Este archivo sirve como contexto base para que personas y agentes comprendan la
estructura y el propósito del repositorio.*
