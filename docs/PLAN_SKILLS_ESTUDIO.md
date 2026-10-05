# Plan: skills de estudio del proyecto

Skills propias del repositorio (en `.claude/skills/`) que automatizan el pipeline de
[`AGENTS.md`](../AGENTS.md), apoyándose en las skills generales `pdf`, `pptx`, `docx` y `xlsx`.

## Arquitectura

```text
1_Bibliografia_Original ──/digitalizar──▶ 2_Textos_Extraidos ──/guia-estudio──▶ 3_Guias_de_Estudio
   (PDF, PPTX)            usa pdf + pptx      (*_Crudo.md, no se versiona)          (*_Guia.md)
                                                                                     │
                       ┌────────────────────────────┬────────────────────────────────┤
                       ▼                            ▼                                ▼
                  /exportar                    /flashcards                       /simulacro
            pandoc + plantilla              CSV Anki (usa xlsx)          .md + modo interactivo
       *_Guia.docx/.pdf + _imprimir/    4_Flashcards/*.csv          5_Evaluaciones/*_Simulacro.md
                                              ▲                                │
                                              └──── temas flojos ◀── *_Resultados.md

/estudiar-unidad  -> corre el pipeline completo de una unidad, salteando lo que ya existe
/estado-materia   -> tabla de qué unidades tienen guía / flashcards / simulacro
```

### Principios comunes

- **Una sola fuente de reglas:** cada skill lee `AGENTS.md` al empezar; nombres y rutas se
  generan con `Scripts/estudio/nombres.py`, nunca a mano.
- **Si falta materia o unidad, se pregunta** antes de guardar.
- **Trazabilidad:** todo `.md` generado lleva cabecera YAML (materia, unidad, tipo, fuentes,
  fecha, skill, `hash_generado`) y las guías citan página (`(Papalia, p. 412)`).
- **No pisar ediciones manuales:** antes de sobrescribir, `Scripts/estudio/frontmatter.py estado`
  compara el contenido con `hash_generado`; si fue editado a mano, se muestra el diff y se pregunta.
- **Procesamiento por partes:** textos largos se trabajan por capítulo o ~20 páginas, con
  mini-guías que después se integran; unidades enteras se reparten entre subagentes.
- **Todo local:** diagramas con mermaid-cli (sin servicios externos como kroki).
- **Al terminar:** validar nombres y enlaces y borrar temporales.

## Skills

| Skill | Entrada → Salida | Se apoya en | Detalles clave |
|-------|------------------|-------------|----------------|
| `/flashcards` | `*_Guia.md` (o `.docx`, o `*_Resultados.md`) → `4_Flashcards/*_Flashcards.csv` | — | Mezcla pregunta/respuesta + cloze; ID estable por tarjeta (Anki actualiza en vez de duplicar y conserva el progreso); mazo `Materia::Unidad`; etiquetas; validación del CSV y prueba de importación real con el paquete `anki`; modo lote |
| `/simulacro` | guías (+ exámenes previos / guía de lectura) → `5_Evaluaciones/*_Simulacro.md` | — | Estructura de tu cuestionario de Lacan: A opción múltiple · B V/F justificado · C distinciones finas · D desarrollo con rúbrica · E casos; clave al final con fuente; estilo calibrado por cátedra; **modo interactivo** que corrige y guarda `*_Resultados.md` (temas flojos + historial de intentos) |
| `/guia-estudio` | `*_Crudo.md` + diapositivas (+ guía de lectura) → `3_Guias_de_Estudio/*_Guia.md` | — | Plantilla de las mejores guías actuales; apuntes extendidos; citas de página; Mermaid `.mmd`+`.png` en `_media/`; chequeo de cobertura contra la fuente; procesamiento por partes |
| `/digitalizar` | PDF/PPTX → `2_Textos_Extraidos/*_Crudo.md` | `pdf`, `pptx` | `## Página N`; OCR (`spa`) si es escaneado; limpieza (guiones de corte, encabezados/pies); imágenes en `_media/<crudo>/`; informe de calidad |
| `/exportar` | `*_Guia.md` → `.docx` / `.pdf` / `_imprimir/` | `docx` | **pandoc + plantilla de estilos** (`reference.docx`); diagramas a PNG con ancho controlado; PDF con LibreOffice; borra temporales |
| `/estudiar-unidad` | unidad → pipeline completo | todas | Saltea etapas ya hechas; protege ediciones manuales |
| `/estado-materia` | materia → tabla de cobertura | — | Detecta guías sin flashcards/simulacro y textos sin guía |

## Integración con el Planificador

Las sesiones de repaso pasan a tener tarea concreta: repasos intermedios = mazo de
flashcards de la unidad; repaso final = simulacro. Los temas flojos de `*_Resultados.md`
generan un mazo extra.

## Etapas

| Etapa | Contenido | Estado |
|-------|-----------|--------|
| 1 | Base: `.gitignore` de textos extraídos, `Scripts/estudio/` (nombres, cabecera YAML, verificación de entorno), `Scripts/requirements.txt`, script de inicio para sesiones en la nube | ✅ |
| 2 | `/flashcards`: skill + `anki_csv.py` + `probar_anki.py`; pilotos Psicoanálisis C08 (36 tarjetas) y Biología C04 (60) | ✅ |
| 3 | `/simulacro`: skill + `simulacro.py` (validar / resultados con historial de intentos); piloto Psicoanálisis C08 (22 preguntas); ciclo simulacro → temas flojos → flashcards probado | ✅ |
| 4 | `/guia-estudio` (por partes, citas de página) | ⏳ |
| 5 | `/digitalizar` (limpieza y OCR) | ⏳ |
| 6 | `/exportar`, `/estudiar-unidad`, `/estado-materia`, documentación y PR | ⏳ |

**Criterio de éxito por etapa:** probar con material real (p. ej. Psicoanálisis C21–23,
Biología C04): la guía no pierde secciones ni ejemplos de la fuente, Anki importa el CSV
sin errores, y cada pregunta del simulacro es rastreable a su fuente.

## Decisiones tomadas

| Tema | Decisión |
|------|----------|
| Exportar a Word | pandoc + plantilla de estilos (`reference.docx`) |
| Flashcards | Mezcla pregunta/respuesta + cloze. Tipos de nota en español por defecto (`Básico` / `Respuesta anidada`), configurables para colecciones en inglés |
| Simulacro | Archivo `.md` + modo interactivo en el chat |
| Plataforma | Claude Code (nube y local). Compatibilidad con Antigravity: a revisar más adelante |
| Textos extraídos | `2_Textos_Extraidos/` ignorado por git: los nuevos quedan solo en la copia local |
