# Materiales de parcial: repaso e integración

La guía extendida sirve para **entender** y como reemplazo del texto. Para **rendir** hacen falta
además materiales cortos que integren y que obliguen a recordar. Las 8 guías del 2.º parcial de
Psicoanálisis suman unas 85.000 palabras: sin estas capas no se repasan en los últimos días.

| Capa | Archivo | Para qué | Cuándo se hace |
|---|---|---|---|
| Texto original | `1_Bibliografia_Original/` | consultar | — |
| Guía extendida | `[Unidad]_[Tema]_Guia.md` | entender, reemplazar el texto | siempre |
| Ficha de repaso | `[Unidad]_[Tema]_Repaso_Guia.md` | repasar en 15 minutos | guía de más de ~5.000 palabras, o antes de un parcial |
| Cuadro integrador | `Transversal_[Eje]_Guia.md` | comparar entre clases | el parcial abarca varias clases sobre categorías paralelas |
| Flashcards | `4_Flashcards/` | evocar a diario | siempre (`/flashcards`) |
| Simulacro | `5_Evaluaciones/` | practicar la escritura | antes de cada parcial (`/simulacro`) |

Nombres con el script:
```bash
python Scripts/estudio/nombres.py generar repaso --unidad C13 --tema "Estructura y tiempos de la neurosis"
python Scripts/estudio/nombres.py generar guia --unidad Transversal_EstructurasClinicas
```
(Para un eje transversal el código de unidad es `Transversal_[Eje]` y no lleva `--tema`.)

Las dos llevan cabecera YAML como cualquier guía (`tipo: guia`, `fuentes` = las guías de las que
salen, `skill: guia-estudio`) y se exportan con `/exportar`. Su contenido sale **solo de las guías**
(y de sus fuentes): nada nuevo de memoria.

## Ficha de repaso (`_Repaso_Guia.md`)

Máximo **2 páginas** en Word (~900–1.200 palabras). Exportala con `--sin-saltos`.

~~~markdown
# [Clase] — [Tema] · Ficha de repaso

> **Idea-fuerza:** [la misma de la guía, en 2 líneas]

![Diagrama](_media/[el diagrama principal de la guía].png)

## Esqueletos de respuesta

**P1. [consigna resumida]**
1. Tesis… 2. … 3. … (los mismos esqueletos de la guía, uno por pregunta)

## No confundir

| X | Y | Criterio |
|---|---|---|

## Citas que conviene saber

- «…» (T[NN], p. N) — para qué sirve en una respuesta.

## Autoevaluación rápida

1. [5–8 preguntas cortas]
~~~

## Cuadro integrador (`Transversal_[Eje]_Guia.md`)

Cuando un parcial cruza varias clases que tratan **categorías paralelas** (estructuras clínicas,
escuelas, teorías del yo, modelos del aparato psíquico, pruebas estadísticas…), las preguntas
suelen pedir **comparar**. El cuadro integrador las reúne:

1. **Columnas** = las categorías (p. ej., histeria · obsesión · fobia · perversión · psicosis ·
   bordes). **Filas** = los ejes de comparación que usa la cátedra (p. ej., mecanismo —represión,
   desmentida, forclusión—, relación con la castración y con el Otro, angustia, síntoma, fantasma,
   transferencia, dirección de la cura). Cada celda: 1–2 líneas con su cita (`C15 §2; T10 p. 3`).
2. Debajo del cuadro, **una sección por fila**: el eje explicado de punta a punta, comparando
   (así sirve de respuesta modelo para "compare X e Y en cuanto a…").
3. **Lista "No confundir" transversal**: los pares que cruzan clases (represión / desmentida /
   forclusión; inhibición / síntoma; angustia señal / automática; transferencia / repetición;
   interpretación / construcción; interrupción / fin de análisis), con el criterio que los
   distingue y dónde está en cada guía.
4. **2–4 preguntas integradoras** con esqueleto y respuesta modelo.
5. Un diagrama de la lógica de conjunto.

Si el cuadro excede el ancho de página, partilo en dos tablas (las columnas de un lado, las
del otro) en vez de achicar la letra.

## Plan de repaso hasta el examen

Cuando hay fecha de examen (la dice el usuario, está en el Planificador `Planificador_Parciales/`
o en la memoria), proponé un calendario en el chat (no hace falta archivo):

- **Todos los días:** flashcards de las clases ya vistas (repaso espaciado de Anki, 15–20 min).
- **Primera mitad del tiempo:** una clase cada 1–2 días: leer la guía (el desarrollo ampliado solo
  donde haga falta), reconstruir los esqueletos sin mirar, autoevaluación.
- **Segunda mitad:** ficha de repaso + cuadro integrador; simulacros **intercalados** (preguntas de
  varias clases mezcladas, con tiempo); después de cada simulacro, el mazo de temas flojos.
- **Últimos 2 días:** solo fichas, cuadro y temas flojos; nada nuevo.
- Coincidí con las sesiones del Planificador (14, 7, 3 y 1 días antes) para los simulacros.
