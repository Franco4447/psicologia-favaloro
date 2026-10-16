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
├── AGENTS.md                    -> Reglas obligatorias para agentes (estructura, nombres, protocolos de apuntes)
├── README.md                    -> Este archivo
├── docs/                        -> Documentación del proyecto (informe de mejoras, convenciones)
├── index.html                   -> Mapa interactivo del plan de estudio (autocontenido; publicado en GitHub Pages)
├── Planificador_Parciales/      -> Planificador de repasos espaciados para parciales y TPs
├── Scripts/                     -> Utilidades: skills de estudio (estudio/), Google Drive y mantenimiento
├── 1er Año/                     -> Materias de 1er año (archivo histórico, en el pipeline)
└── 2do Año/                     -> Materias de 2do año (todas en el pipeline)
```

### Estructura de cada materia (pipeline de 5 etapas)

Todo material **nuevo** se guarda dentro de su año y materia, siguiendo este pipeline
(ver detalle en [`AGENTS.md`](AGENTS.md)):

```text
[Año de la Carrera]/[Nombre de la Materia]/
├── Perfil_Materia.md         -> Formato de cada evaluación y protocolo de apuntes habitual
├── 1_Bibliografia_Original/  -> PDFs, PPTs y textos originales (ignorado por git)
├── 2_Textos_Extraidos/       -> .md crudos post-OCR/extracción   (U07_Papalia_Cap15_Crudo.md, ignorado por git)
├── 3_Guias_de_Estudio/       -> Guías del protocolo elegido .md y .docx (C17_Memoria_Cursada_Guia.md, U07_Adolescencia_Guia.md)
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
| 1er | Antropología, Epistemología, Filosofía, Historia, LEO, Metodología, Neurociencias, Procesos Básicos I, Psicología General, Sociología | ✅ | Archivo histórico: una carpeta por materia, nombres por cuatrimestre (`Global_1erC`, `Global_2doC`) o clase (`C21`); la bibliografía conserva sus nombres originales |
| 2do | Psicoanálisis | ✅ | Migrada: bibliografía del 1er cuatri como `1erC_T[NN]_…`, clases como textos extraídos `C[NN]_Catedra_…`, resúmenes de Belucci y material de Lacan como guías `Transversal_…` |
| 2do | Psicología Evolutiva | ✅ | Unificada: Piaget y desarrollo cognitivo del 1er cuatri (`U05`, `U06`) junto a Adolescencia y Adultez (`U07`, `U08`). 4.º parcial (`C17`…`C23`): guía extendida y versión de cursada por clase, fichas de repaso, cuadro integrador, flashcards y simulacro integrador |
| 2do | Biología | ✅ | Migrada: diapositivas, guías extendidas, resúmenes y síntesis por clase (`C01`…`C11`), problemas en Evaluaciones |
| 2do | Estadística | ✅ | Migrada: guías por clase (`C01`…`C10`), material del 2do parcial (`C06_10_…`), TP final en `6_Entregables/` |
| 2do | Procesos Básicos II | ✅ | Migrada: guías por clase (`C05`…`C09`) y global de la segunda mitad |
| 2do | Psicología Experimental | ✅ | Migrada: bibliografía del trabajo de investigación (prefijo `Inv_`); Parcial 1 y Parcial 2 en `6_Entregables/` (`Inv_Actividad1_`, `Inv_P2_`). La plataforma web del experimento vive en [`psicologia-experimental-web`](https://github.com/Franco4447/psicologia-experimental-web) |
| 2do | Psicología Social | ✅ | Migrada: guías de la Unidad 3, resúmenes de clase (`C01`…`C03`), TPs en `6_Entregables/` |
| 2do | Procesos Básicos III | ✅ | Migrada: guías de motivación (`U01`), aprendizaje (`U02`: Biwer y Stanton) y pensamiento (`U03`: introducción, teorías del razonamiento, razonamiento probabilístico y solución de problemas), consigna en `6_Entregables/` |

Psicología Evolutiva, Psicoanálisis, Procesos Básicos III y Psicología Experimental ya tienen
su `Perfil_Materia.md`; las demás lo reciben la primera vez que se pide material.

El plan de migración propuesto está en [`docs/ANALISIS_MEJORAS.md`](docs/ANALISIS_MEJORAS.md).

---

## 📐 Protocolos de apuntes

No todo apunte tiene que reemplazar al libro: cada material de estudio se hace con un
**protocolo** que se ajusta a **cómo se evalúa** el tema y al material de clase disponible.
Cada vez que se pide un material (guía, unidad, ficha, flashcards, simulacro), el agente
**propone los protocolos con sus pros y contras y recomienda uno**, y espera la elección.

| Protocolo | Para qué evaluación | Extensión orientativa | Archivo |
|---|---|---|---|
| A. Cursada | Opción múltiple, V/F, abiertas breves | 2.000–3.500 palabras por clase | `[Unidad]_[Tema]_Cursada_Guia.md` |
| B. Desarrollo | Desarrollo con extensión mínima; baterías de preguntas | 5.000–8.000 por clase o bloque | `…_Desarrollo_Guia.md` |
| C. Extendido | Final integral; texto que se pide leer completo; a pedido | Sin tope (reemplaza el texto) | `…_Guia.md` (sufijo histórico) |
| D. Oral | Lección oral, exposición, coloquio | 1.500–3.000 por tema | `…_Oral_Guia.md` |
| E. Procedimental | Problemas: estadística, metodología | Según los procedimientos | `…_Procedimental_Guia.md` |
| F. Lectura de investigación | Artículos para TP, informe o monografía | 500–1.000 por artículo | `[Unidad]_[Autor]_[Tema]_Lectura_Guia.md` |

- **La recomendación** sale del **perfil de la materia** (`[Año]/[Materia]/Perfil_Materia.md`:
  formato y fecha de cada evaluación, protocolo habitual, fuentes de la cátedra) y del material
  de clase encontrado:
  `python Scripts/estudio/protocolos.py proponer --materia "Psicología Evolutiva" --unidad C17`.
- **Sirve para cualquier materia**, ya cursada, en curso o por cursar: el perfil se crea con la
  plantilla la primera vez que se pide material.
- **Agregar o ajustar un protocolo** es editar el catálogo de `Scripts/estudio/protocolos.py` y
  su estructura en [`protocolos.md`](.claude/skills/guia-estudio/references/protocolos.md);
  los nombres de archivo y el estado de cada materia se actualizan solos.
- Las reglas completas están en [`AGENTS.md`](AGENTS.md) → «Protocolos de Apuntes».

---

## 🛠️ Flujo de estudio recomendado

| Paso | Qué se hace | Entrada → Salida |
|------|-------------|------------------|
| 1. Digitalización | Convertir PDFs (con texto o escaneados) y PowerPoint a Markdown con la skill **`/digitalizar`** | `1_Bibliografia_Original/` → `2_Textos_Extraidos/*_Crudo.md` |
| 2. Guía de estudio | Elegir el **protocolo** (el agente propone opciones con pros y contras) y escribir la guía con la skill **`/guia-estudio`** (citas APA con página, diagramas, mapa de origen de los temas) | `2_Textos_Extraidos/` + diapositivas y apuntes → `3_Guias_de_Estudio/*_Guia.md` |
| 3. Exportación | Pasar la guía a Word (y PDF / versión para imprimir) con la skill **`/exportar`** | `*_Guia.md` → `*_Guia.docx` (+ `.pdf`, `_imprimir/`) |
| 4. Estudio activo | Crear tarjetas Anki con la skill **`/flashcards`** (Claude Code) | `*_Guia.md` → `4_Flashcards/*_Flashcards.csv` |
| 5. Autoevaluación | Simulacro de parcial con la skill **`/simulacro`** (archivo, o «tomame examen» en modo interactivo) | `*_Guia.md` → `5_Evaluaciones/*_Simulacro.md` (+ `*_Resultados.md`) |
| 6. Planificación | Cargar fechas de parciales en el [Planificador](Planificador_Parciales/README.md): en exámenes, los repasos dicen *flashcards* y el final *simulacro* | Notion «Tareas» → sesiones de repaso |

### Prompts reutilizables

- [`docs/prompts/Estadistica_DocumentoPorClase_Prompt.txt`](docs/prompts/Estadistica_DocumentoPorClase_Prompt.txt): prompt para
  fusionar *presentación de clase + bibliografía* en un documento de estudio exhaustivo
  (equivale al protocolo C, Extendido). Sirve como plantilla para cualquier materia.

---

## 🧰 Herramientas incluidas

### Skills de estudio (Claude Code)
Skills propias del repo (`.claude/skills/`) que siguen `AGENTS.md`. Se usan pidiéndolas en lenguaje
natural ("haceme flashcards de la clase 8 de Psicoanálisis", "tomame el simulacro", "¿qué me falta de
Biología?") o con su nombre:

| Skill | Qué hace |
|---|---|
| `/digitalizar` | PDF (con texto o escaneado, a dos columnas) o PowerPoint → texto extraído con OCR y limpieza |
| `/guia-estudio` | Propone el protocolo y escribe la guía (cursada, desarrollo, extendida, oral, procedimental o de lectura) con citas APA, diagramas y control de cobertura |
| `/exportar` | Guía → Word con plantilla de estilos, PDF y versión 2 páginas por hoja |
| `/flashcards` | Guía → mazo CSV para Anki (reimportar actualiza sin duplicar) |
| `/simulacro` | Guías → simulacro con clave; modo interactivo que corrige y registra temas flojos |
| `/estado-materia` | Qué tiene y qué le falta a cada unidad, y con qué protocolo está hecha cada guía |
| `/estudiar-unidad` | Todo lo anterior para una unidad o un parcial, con una sola propuesta de protocolo, salteando lo que ya existe |

Primera vez en tu PC: `pip install -r Scripts/requirements.txt` y
`python Scripts/estudio/verificar_entorno.py --probar` (dice qué más instalar: pandoc, LibreOffice,
Tesseract, mermaid-cli). En la nube se instala solo. Diseño y decisiones:
[`docs/PLAN_SKILLS_ESTUDIO.md`](docs/PLAN_SKILLS_ESTUDIO.md).

### Mapa del plan de estudio (`index.html`)
Mapa interactivo de las materias de la carrera y sus correlatividades, con arrastre tipo
Miro (mouse y táctil). Se generó con Gemini Canvas y se extrajo a un único archivo
autocontenido (React y Tailwind desde CDN), sin los scripts ni los datos de la sesión de
Google que traía la página guardada. Abrir `index.html` en el navegador o en
<https://franco4447.github.io/psicologia-favaloro/>.

### Planificador de Parciales (`Planificador_Parciales/`)
Calcula sesiones de repaso espaciado (−14, −7, −3, −1 días) para cada entrega. Una sola
página: abierta como Artifact en claude.ai lee las entregas de Notion; abierta con doble clic
o en GitHub Pages usa una lista fija más las entregas que agregues.
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

- **Sí:** guías de estudio, flashcards, simulacros, herramientas.
- **No:** logs de agentes (`.agents/`), datos de encuestas con respuestas sensibles, credenciales (`gdrive_credentials.json`, `gdrive_token.json`, `.env`), accesos
  directos, archivos temporales de exportación (`*.temp.md`, `*.temp.md.ps1`) y la
  bibliografía original (`1_Bibliografia_Original/`) y los textos extraídos (`2_Textos_Extraidos/`):
  ambos tienen derechos de autor y viven solo en OneDrive.

---
*Este archivo sirve como contexto base para que personas y agentes comprendan la
estructura y el propósito del repositorio.*
