# 📅 Planificador de Parciales

Página web autocontenida que, a partir de la fecha de cada entrega (parcial, TP, oral,
final), calcula **sesiones de repaso espaciado** hacia atrás y las muestra como una lista
ordenada por urgencia, con un panel de «Hoy te toca».

## Versiones

| Archivo | Datos | Dónde abrirlo | Persistencia |
|---------|-------|---------------|--------------|
| `index.html` | Lista inicial fija (`SEED`, tomada de Notion el 4/10/2026) + entregas que agregues a mano | Cualquier navegador (doble clic) | `localStorage` del navegador (clave `planificador_parciales_v1`) |
| `planificador_notion.html` | Base «📖 Tareas» de Notion, consultada en vivo y refrescada cada minuto | Como Artifact en claude.ai (necesita `window.claude` y el conector de Notion) | Sesiones tildadas en `localStorage` (`pp_done_v2`); último resultado cacheado (`pp_cache_v2`) |

Fuera de claude.ai, `planificador_notion.html` muestra los últimos datos cacheados y un
aviso de «Sin conexión a Notion».

## Reglas de repaso

En **exámenes y finales**, cada sesión dice qué hacer, en línea con las skills de estudio del repo:
los repasos intermedios son con el **mazo de flashcards** de la unidad (`/flashcards`) y el
**repaso final es el simulacro** en modo interactivo (`/simulacro`). En TPs, orales y actividades
las sesiones son repasos generales.

Días antes de la entrega en que se programa cada sesión:

| Tipo | `index.html` | `planificador_notion.html` |
|------|--------------|----------------------------|
| Examen / Final | 14, 7, 3, 1 | 14, 7, 3, 1 |
| Trabajo Práctico / Lección Oral | 7, 3, 1 | 7, 3, 1 |
| TP conceptual | — | 3, 1 |
| Actividad | 3, 1 | 3, 1 |
| Lectura | — | 1 |
| Otro tipo | 3, 1 | 3, 1 |

Para cambiar las reglas, editá la constante `OFFSETS` en el `<script>` de cada archivo.

## Base de Notion esperada

`planificador_notion.html` consulta la data source definida en la constante `DS` con estas
propiedades:

| Propiedad Notion | Tipo | Uso |
|------------------|------|-----|
| `Materia` | texto / select | Título de la tarjeta |
| `Tipo` | select | Elige la regla de `OFFSETS` |
| `Descripción` | texto | Subtítulo |
| `Entrega` | fecha | Fecha de la entrega (se usa el inicio) |
| `Cuándo` | select / estado | Las filas con valor `Terminado` se excluyen |

Si cambiás el nombre de alguna propiedad en Notion, actualizá la consulta `QUERY`.

## Actualizar la lista fija de `index.html`

Editá el arreglo `SEED`. Ojo: si el navegador ya tiene datos guardados, `SEED` se ignora;
para recargarlo, borrá la clave `planificador_parciales_v1` desde las herramientas de
desarrollador (Application → Local Storage).
