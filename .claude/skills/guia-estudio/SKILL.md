---
name: guia-estudio
description: 'Escribe guías de estudio a partir de los textos extraídos, diapositivas, apuntes y bibliografía del repositorio de Psicología, con el protocolo que corresponda a cómo se evalúa el tema (cursada, desarrollo, extendido, oral, procedimental o lectura de investigación), citando páginas en APA, con diagramas Mermaid y control de cobertura. Antes de escribir siempre propone los protocolos con pros y contras y recomienda uno. Usala siempre que el usuario pida una guía, resumen, apunte, síntesis o "material para estudiar" de un texto, capítulo, clase o unidad, o que pase a guía un texto extraído o un PDF.'
---

# Guías de estudio

Produce la guía de `3_Guias_de_Estudio/` del **protocolo elegido** (`[Unidad]_[Tema]_Guia.md` para
el extendido; `_Cursada_Guia`, `_Desarrollo_Guia`, `_Oral_Guia`, `_Procedimental_Guia`,
`_Lectura_Guia` para los demás). Los protocolos están en `AGENTS.md` y en
`references/protocolos.md`; este archivo describe cómo trabajar las fuentes y escribir, y el
**detalle exhaustivo** de abajo es el del protocolo C (Extendido) y, acotado, el del B.

## Paso 0: proponer el protocolo (obligatorio)

Antes de leer fuentes en profundidad o escribir:

1. Leé `references/protocolos.md` y el perfil de la materia
   (`python Scripts/estudio/protocolos.py perfil --materia "<Materia>"`; si no existe, crealo con
   `references/plantilla_perfil_materia.md` y preguntá el formato del examen).
2. `python Scripts/estudio/protocolos.py proponer --materia "<Materia>" --unidad <Unidad> --pedido "<pedido>"`.
3. Presentá la propuesta en el chat (tabla de protocolos con pros y contras, recomendado con su
   porqué, capas que sumarías) y **esperá la elección**. Con `AskUserQuestion`, el recomendado
   va primero.
4. Seguí la estructura del protocolo elegido (§4 de `protocolos.md`) y agregá `protocolo:` a la
   cabecera YAML.

## Antes de empezar

1. Leé `AGENTS.md` (manda sobre esta skill).
2. Reuní las fuentes:
   - **Textos extraídos** `2_Textos_Extraidos/*_Crudo.md` (la fuente principal).
   - Si solo hay PDF/PPTX en `1_Bibliografia_Original/`, primero extraelo con la skill
     `/digitalizar` a `2_Textos_Extraidos/`.
   - **Diapositivas** de la clase (marcan qué priorizó el docente) y, si existen, la **guía de
     lectura** o evaluaciones de la cátedra (`5_Evaluaciones/`): definen "lo que entra sí o sí".
   - **Preguntas de la cátedra** (baterías de preguntas, consignas de parciales anteriores, apuntes
     del usuario con "preguntas de examen"): si existen, la guía se ordena **por pregunta** (ver
     la plantilla) y responde cada una.
   - **Formato del examen** (desarrollo, opción múltiple, oral; extensión mínima como «10
     renglones»): fija la extensión de las respuestas modelo. Si no lo sabés y hay preguntas de
     desarrollo, preguntalo.
   - Si no está claro de qué materia/unidad se trata, **preguntá**.
3. Nombre de salida con el script, con el tipo del protocolo elegido (`guia` para el extendido;
   `cursada`, `desarrollo`, `oral`, `procedimental`, `lectura`), tema = tema principal, sin truncar:
   ```bash
   python Scripts/estudio/nombres.py generar guia --unidad U05 --tema "Las intervenciones del analista"
   python Scripts/estudio/nombres.py generar cursada --unidad C17 --tema "Memoria"
   ```
4. Si la guía ya existe: `python Scripts/estudio/frontmatter.py estado <guia.md>`. Con `editado` o
   `sin-cabecera`, mostrá qué cambiaría y **preguntá** antes de sobrescribir (puede tener
   correcciones del usuario). Las guías hechas a mano anteriores (sin cabecera) se respetan.

## Procesar la fuente por partes

1. Plan de partes:
   ```bash
   python Scripts/estudio/fuente.py partes <crudo.md>            # ~4000 palabras por parte
   ```
2. Para cada parte, leé su texto completo (`fuente.py texto <crudo.md> --parte N`) y escribí
   **notas de parte** en un temporal fuera del repo: cada idea, argumento, ejemplo, caso, cita,
   cifra y término técnico, **con su página** (`p. 12`; si la fuente no tiene páginas, la sección).
   No resumas en esta etapa: anotá todo.
   - Fuentes muy largas (más de ~5 partes) o varias fuentes: repartí las partes entre subagentes,
     cada uno con estas mismas instrucciones, y que devuelvan sus notas de parte.
3. Recién con todas las notas, armá la guía integrada: el orden lo da la lógica del tema (o el de
   las diapositivas), no el corte en partes.

## Escribir la guía

Seguí `references/plantilla_guia.md`. Lo esencial:

- **Capas de lectura:** recuadros de fuente y avisos → idea-fuerza → **hilo conductor** (cómo se
  conectan los temas de la guía) → hoja de ruta → lo que entra sí o sí → una sección por pregunta.
- **Respuesta modelo con esqueleto:** en cada pregunta, primero el **esqueleto** (tesis, conceptos
  obligatorios con autor/texto/página, articulación, ejemplo, cierre) y después la respuesta en
  prosa con la extensión del formato del examen, siguiendo el esqueleto. El estudiante memoriza el
  esqueleto y reconstruye la prosa; no memoriza un texto ajeno. Después, el **desarrollo
  ampliado** con todo lo que dice la fuente.
- **No confundir:** en cada pregunta, la confusión típica y el criterio que la resuelve; al final,
  la tabla de distinciones.
- **Recuadros:** las citas en bloque con etiqueta (`🔑`, `🎯 Para el parcial`, `Esqueleto`,
  `⚠ No confundir`, `▸ Complemento`, `Aviso sobre las fuentes`…) salen de color en Word. La tabla
  de etiquetas está en la plantilla.
- **Avisos de fuentes:** si un texto está incompleto, no asignado, viene de una transcripción con
  OCR o faltan los apuntes de una clase, decilo en un recuadro de aviso al principio.

- **Exhaustiva (protocolo C; en B, solo lo que sostiene cada respuesta; en A, D, E y F, lo que
  pide su estructura):** cada ejemplo, caso clínico, experimento, cifra y distinción de la fuente tiene
  su lugar. Los casos se cuentan con detalle (qué pasó, qué hizo el analista/el experimentador,
  qué concluye el autor).
- **Citas en normas APA 7** en todo dato o tesis: `(Belucci, 2014, p. 12)`,
  `(Freud, 1894/1991, p. 6)`; las referencias completas, en APA, en el recuadro `Fuentes` del
  principio. Reglas y ejemplos en `references/citas_apa.md`. Las citas textuales van entre comillas
  y con página. No inventes páginas ni datos de edición. No agregues un recuadro "Cómo se cita".
- **Fiel a la fuente:** nada de agregar teoría de memoria. Si conectás con otra clase o texto del
  repo, decí cuál (`→ conecta con C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md §4`).
- **Terminología de la cátedra** y términos en el idioma original entre paréntesis (*Zwang*).
- **Diagramas Mermaid:** uno de la lógica de toda la guía y uno por cada pregunta difícil
  (secuencias, tiempos, relaciones, clasificaciones); ninguno decorativo. Texto de nodos sin
  comillas dobles internas.
- **Contenido externo marcado:** lo que no está en los textos asignados (otra obra del autor, la
  teoría general) va con **▸ Complemento**, para que el estudiante lo contraste con su cuaderno.
- Cabecera YAML con `frontmatter.escribir` (materia, unidad, tipo `guia`, `protocolo`, `fuentes`
  con archivo y páginas, skill `guia-estudio`):
  ```python
  import sys; sys.path.insert(0, "Scripts/estudio")
  import frontmatter
  frontmatter.escribir(ruta, {"materia": "Psicoanálisis", "unidad": "U05", "tipo": "guia",
      "protocolo": "extendido",
      "fuentes": [{"archivo": "2_Textos_Extraidos/U05_T27_..._Crudo.md", "paginas": "1-21"}],
      "skill": "guia-estudio"}, cuerpo)
  ```

## Verificar

1. Diagramas → `.mmd` + `.png` en `_media/` y la imagen referenciada en la guía:
   ```bash
   python Scripts/estudio/diagramas.py <guia.md>
   ```
2. Cobertura contra la fuente (exhaustiva en C; en los demás protocolos, revisá solo que esté
   todo lo del programa y de la clase):
   ```bash
   python Scripts/estudio/fuente.py cobertura <crudo.md> [...] --guia <guia.md>
   ```
   Revisá **cada** faltante: si es un caso, ejemplo, autor o concepto de la fuente, agregalo; si es
   ruido (una palabra suelta entre comillas), ignoralo. Repetí hasta que lo que falte sea solo
   ruido. Todas las citas "p. N" tienen que existir en la fuente (el script avisa si no).
3. Nombre: `python Scripts/estudio/nombres.py validar <guia.md>`.
4. Releé la guía de punta a punta como estudiante: ¿se entiende sin el original? ¿falta algún
   paso del argumento? ¿Cada pregunta tiene esqueleto, respuesta de la extensión pedida y "no
   confundir"? ¿El hilo conductor nombra todas las preguntas?
5. Borrá las notas de parte temporales.

## Materiales de parcial (cuando aplica)

Leé `references/materiales_de_parcial.md`. Según el caso, ofrecé o hacé:

- **Ficha de repaso** (`[Unidad]_[Tema]_Repaso_Guia.md`, 2 páginas) si la guía supera ~5.000
  palabras o se acerca un parcial.
- **Cuadro integrador** (`Transversal_[Eje]_Guia.md`) si el parcial abarca varias clases sobre
  categorías paralelas (estructuras clínicas, escuelas, modelos…).
- **Plan de repaso** en el chat si hay fecha de examen.

Para guías del formato anterior (sin hilo conductor ni esqueletos; `estado.py` las lista), no las
regeneres solas: ofrecé actualizarlas agregando las secciones que faltan sin tocar el resto.

## Al terminar, informá

Ruta, protocolo usado, extensión (palabras) frente a la fuente y frente a la orientativa del protocolo, cobertura final, diagramas generados y próximos
pasos posibles: `/flashcards` y `/simulacro` de la guía, exportarla a Word (`/exportar`, con
`--indice` si es larga) y los materiales de parcial que apliquen.
