# 📅 Planificador de Parciales

Página web autocontenida (`index.html`) que, a partir de la fecha de cada entrega (parcial, TP,
oral, final), calcula **sesiones de repaso espaciado** hacia atrás y las muestra como una lista
ordenada por urgencia, con un panel de «Hoy te toca».

## Dos modos, una sola página

La página detecta dónde se abre:

| Dónde | Datos | Persistencia |
|-------|-------|--------------|
| **Como Artifact en claude.ai** (existe `window.claude`) | Base «📖 Tareas» de Notion, consultada en vivo y refrescada cada minuto (necesita el conector de Notion) | Última respuesta cacheada (`pp_cache_v2`) |
| **Doble clic o GitHub Pages** | Lista fija `SEED` más las entregas que agregues desde la página | Entregas propias y quitadas (`pp_local_v3`) |

En los dos, las sesiones tildadas se guardan en el `localStorage` del navegador (`pp_done_v2`).
Si en claude.ai no hay conexión con Notion, se muestran los últimos datos cacheados con un aviso.

La versión anterior de la página local (clave `planificador_parciales_v1`) se migra sola la
primera vez: sus entregas propias y sus sesiones tildadas pasan al formato nuevo.

## Reglas de repaso

En **exámenes y finales**, cada sesión dice qué hacer, en línea con las skills de estudio del repo:
los repasos intermedios son con el **mazo de flashcards** de la unidad (`/flashcards`) y el
**repaso final es el simulacro** en modo interactivo (`/simulacro`). En los demás tipos las
sesiones son repasos generales.

Días antes de la entrega en que se programa cada sesión (constante `OFFSETS`):

| Tipo | Sesiones |
|------|----------|
| Examen / Final | 14, 7, 3, 1 |
| Trabajo Práctico / Lección Oral | 7, 3, 1 |
| TP conceptual / Actividad | 3, 1 |
| Lectura | 1 |
| Otro tipo | 3, 1 |

## Base de Notion esperada

El modo claude.ai consulta la data source definida en la constante `DS` con estas propiedades:

| Propiedad Notion | Tipo | Uso |
|------------------|------|-----|
| `Materia` | texto / select | Título de la tarjeta |
| `Tipo` | select | Elige la regla de `OFFSETS` |
| `Descripción` | texto | Subtítulo |
| `Entrega` | fecha | Fecha de la entrega (se usa el inicio) |
| `Cuándo` | select / estado | Las filas con valor `Terminado` se excluyen |

Si cambiás el nombre de alguna propiedad en Notion, actualizá la consulta `QUERY`.

## Actualizar la lista fija del modo local

Agregá entregas al arreglo `SEED`: aparecen aunque el navegador ya tenga datos guardados. Las que
quitaste desde la página no vuelven a aparecer.
