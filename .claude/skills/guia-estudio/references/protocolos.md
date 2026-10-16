# Protocolos de creación de apuntes

Un **protocolo** fija, para un pedido de material de estudio, qué fuentes mandan, hasta dónde
llega el contenido, cuánto mide y qué estructura tiene. La guía se mide contra **cómo se evalúa**
el tema, no contra el largo del libro.

- **Catálogo y lógica de recomendación:** `Scripts/estudio/protocolos.py` (única fuente de verdad;
  `nombres.py` y `estado.py` lo leen de ahí).
- **Datos de cada materia:** `[Año]/[Materia]/Perfil_Materia.md` (plantilla en
  `plantilla_perfil_materia.md`).
- **Este archivo:** cómo se hace la propuesta y qué lleva cada protocolo.

## 1. Regla: proponer siempre antes de crear

Cada vez que se pide un material de estudio (una guía, una unidad completa, material para un
parcial o final, una ficha, un cuadro, flashcards o un simulacro), **antes de escribir nada**:

1. **Identificá materia, unidad o clase y para qué evaluación es.** Si falta la materia, preguntá
   (regla del `AGENTS.md`).
2. **Leé o creá el perfil de la materia.**
   ```bash
   python Scripts/estudio/protocolos.py perfil --materia "<Materia>"
   ```
   Si no existe, creá `Perfil_Materia.md` con la plantilla. Completá lo que se sepa (memoria del
   proyecto, `Planificador_Parciales/`, programa, simulacros de la cátedra en `5_Evaluaciones/`) y
   preguntá el resto, sobre todo el **formato de la evaluación**.
3. **Generá la propuesta.**
   ```bash
   python Scripts/estudio/protocolos.py proponer --materia "<Materia>" --unidad <U05|C17|…> \
       [--evaluacion "<nombre en el perfil>"] [--final] [--pedido "<texto del pedido>"]
   ```
   El script arma la tabla de protocolos con pros y contras, marca uno como recomendado y dice
   por qué. También avisa si falta el perfil, el formato del examen o el material de clase.
4. **Ajustá la recomendación con lo que el script no ve** y decilo: si hay baterías de preguntas
   de la cátedra (empuja a B), si la clase todavía no se dio (A provisoria), si el usuario tiene
   poco tiempo (A + ficha), si el texto se pide leer completo (C).
5. **Presentá la propuesta al usuario** con el formato de la §2 y **esperá su elección**. Si la
   herramienta de preguntas (`AskUserQuestion`) está disponible, usala con el recomendado primero
   y «(Recomendado)» en la etiqueta.
6. **Registrá la elección:** campo `protocolo:` en la cabecera YAML de lo que generes. Si el
   usuario elige un protocolo distinto del habitual de la materia, preguntá si actualizar
   `protocolo_habitual` en el perfil.

**Pedidos en lote** (varias clases para el mismo parcial): una sola propuesta para todo el lote,
salvo que alguna clase tenga una situación distinta (por ejemplo, sin material de clase). Esa
diferencia se señala en la misma propuesta.

**Si el pedido ya nombra el protocolo** («haceme la versión de cursada»): igual mostrás la tabla,
en versión corta. Si tu recomendación coincide, seguís sin esperar. Si no coincide, explicás por
qué y preguntás.

## 2. Formato de la propuesta (en el chat)

```markdown
**Propuesta de protocolo — [Materia] · [Unidad/clase] · [Evaluación, fecha]**

[Tabla del script: Protocolo | Para qué | Extensión | A favor | En contra]

**Recomiendo: [Protocolo]**, porque [motivos: formato del examen, material de clase disponible,
tiempo hasta la fecha, pedido]. [Si aplica: «Después se puede ampliar a B/C sin rehacer».]

**Capas que sumaría:** [ficha de repaso / cuadro integrador / flashcards / simulacro, con su porqué].

¿Seguimos con [Protocolo] o preferís otro?
```

Mostrá solo los protocolos que tengan sentido para el caso (por ejemplo, F no aplica a un parcial
de opción múltiple). Mínimo dos opciones, para que la elección sea real.

## 3. Reglas comunes a todos los protocolos

- **Prioridad de fuentes:** (1) lo que se dio en clase (diapositivas, apuntes del usuario,
  baterías de preguntas); (2) el programa (contenidos y bibliografía obligatoria de la unidad);
  (3) el formato de la evaluación; (4) el texto, para explicar y citar. En C, el texto manda.
- **Citas en APA 7** (`citas_apa.md`), nombres con `nombres.py`, cabecera YAML con
  `frontmatter.escribir` (incluye `protocolo:`), diagramas en `_media/`, nada inventado.
- **Mapa de origen al principio:** tabla de temas con su origen (**Clase** / **Programa** /
  **Solo libro**) y la sección donde están.
- **Declarar lo que queda afuera** en el recuadro de aviso, con la ruta de la guía que sí lo tiene
  (si existe).
- **Marcar lo provisorio:** si la clase no se dictó o faltan diapositivas o apuntes, decirlo al
  principio y proponer actualizar cuando lleguen.
- **No regenerar lo editado a mano** (`frontmatter.py estado`).

## 4. Catálogo

Los pros, contras y extensiones resumidos están en `protocolos.py`. Acá va la estructura de cada uno.

### A. Cursada — `[Unidad]_[Tema]_Cursada_Guia.md`

- **Alcance:** la intersección entre el programa y lo dado en clase; lo del programa que no se dio
  va en versión breve, marcado «Programa».
- **Estructura:** fuentes y aviso → idea-fuerza → mapa (programa / clase / sección) → una sección
  por tema (explicación breve, esqueleto de respuesta, «no confundir») → «Para rendir» en el
  formato real del examen (con respuestas) → referencias.
- **Extensión:** 2.000–3.500 palabras por clase. **Word:** `--sin-saltos`.
- **Verificación:** que cada tema del programa de la unidad esté (o se diga por qué no) y que cada
  dato tenga cita.

### B. Desarrollo — `[Unidad]_[Tema]_Desarrollo_Guia.md`

- **Alcance:** lo de A más lo que pidan las preguntas de la cátedra; ordenada **por pregunta**
  cuando hay baterías.
- **Estructura:** la de `plantilla_guia.md` (hilo conductor, hoja de ruta, «lo que entra sí o sí»,
  por pregunta: esqueleto → respuesta modelo con la extensión mínima del examen → «no confundir»),
  con un **desarrollo ampliado acotado** a lo que sostiene la respuesta, citas textuales que
  conviene saber y articulación entre autores.
- **Extensión:** 5.000–8.000 palabras por clase o bloque. **Word:** `--indice`.
- **Verificación:** cobertura de las preguntas (cada una respondida) más que del texto completo.

### C. Extendido — `[Unidad]_[Tema]_Guia.md` (sufijo histórico)

- **Alcance:** todo el texto fuente: ejemplos, casos, experimentos, cifras y matices.
- **Estructura:** `plantilla_guia.md` completa, con el desarrollo ampliado exhaustivo.
- **Extensión:** sin tope. **Word:** `--indice`.
- **Verificación:** `fuente.py cobertura` hasta que solo falte ruido.
- **Cuándo:** final integral, texto que la cátedra pide leer completo y no se dio, o a pedido.
  Las guías anteriores a los protocolos son de este tipo.

### D. Oral — `[Unidad]_[Tema]_Oral_Guia.md`

- **Alcance:** lo que entra en el tiempo de la exposición, priorizado por la consigna.
- **Estructura:** consigna y pautas (tiempo, apoyo visual) → guion por bloques con minutos
  (apertura, desarrollo, cierre) → esquema o diapositivas sugeridas → preguntas probables con
  respuesta breve → conceptos que conviene poder definir → referencias.
- **Extensión:** 1.500–3.000 palabras. **Word:** `--sin-saltos`.

### E. Procedimental — `[Unidad]_[Tema]_Procedimental_Guia.md`

- **Alcance:** los procedimientos que se evalúan.
- **Estructura:** árbol de decisión → por procedimiento: cuándo se usa, supuestos, pasos, fórmula,
  ejemplo resuelto completo, cómo se informa (APA), errores típicos → ejercicios de práctica con
  solución → referencias.
- **Verificación:** recalcular cada ejemplo (con Python si hace falta) antes de entregarlo.

### F. Lectura de investigación — `[Unidad]_[Autor]_[Tema]_Lectura_Guia.md` (unidad `Inv` para trabajos)

- **Alcance:** un artículo o capítulo por ficha.
- **Estructura:** referencia APA → pregunta e hipótesis → método (participantes, diseño,
  instrumentos) → resultados principales (con estadísticos) → conclusiones y limitaciones → citas
  textuales útiles con página → para qué sirve en el trabajo.
- **Extensión:** 500–1.000 palabras.

## 5. Capas derivadas

Las capas (ficha de repaso, cuadro integrador, flashcards, simulacro) también se proponen, pero
lo que se elige es la **guía base** y el **alcance**:

| Opción | A favor | En contra |
|---|---|---|
| Desde la guía del protocolo elegido (por ejemplo, Cursada) | Coincide con lo que se evalúa; menos material | Puede faltar algo del libro |
| Desde la guía extendida | Cubre todo | Mucho volumen; mezcla lo central con lo accesorio |
| Solo temas flojos (desde `_Resultados.md`) | Máximo rendimiento por minuto | Requiere haber hecho un simulacro |

Las flashcards y los simulacros siguen el formato del examen del perfil (opción múltiple y V/F
para A; desarrollo con rúbrica para B; preguntas del tribunal para D; ejercicios para E).

## 6. Perfil de materia

`[Año]/[Materia]/Perfil_Materia.md`: cabecera YAML con los datos y notas libres debajo. Campos:

| Campo | Qué es |
|---|---|
| `materia`, `anio`, `estado` | Nombre, año de la carrera y estado (`por_cursar`, `cursando`, `cursada`) |
| `docente` | Docente a cargo |
| `protocolo_habitual` | Clave de `protocolos.py` que se usa si no hay otra señal |
| `evaluaciones` | Lista con `nombre`, `fecha`, `formato` (`respuesta_corta`, `desarrollo`, `oral`, `problemas`, `trabajo_escrito`, `final_integral`, `sin_definir`), `detalle`, `unidades` y `estado` (`pendiente`, `rendida`) |
| `fuentes_catedra` | Dónde están las diapositivas, los apuntes y las preguntas |
| `programa` | Ruta o enlace del programa |

- **Materias que se cursan o se cursarán:** el perfil se crea la primera vez que se pide material
  y se actualiza cuando se conoce una fecha o un formato.
- **Materias ya cursadas (1er Año):** `estado: cursada`; el protocolo habitual suele ser C
  (consulta) o B (final).

## 7. Cómo agregar o ajustar un protocolo

1. Agregá o editá la entrada en `PROTOCOLOS` de `Scripts/estudio/protocolos.py`: nombre, sufijo,
   extensión, para qué, pros, contras, si usa la plantilla completa y opciones de Word. Si
   corresponde a un formato de evaluación nuevo, sumalo a `FORMATOS`.
2. Describí su estructura en la §4 de este archivo.
3. Si necesita una plantilla propia, creala en `references/`.
4. `nombres.py` y `estado.py` lo toman solos. Probá:
   `python Scripts/estudio/protocolos.py listar` y `python Scripts/estudio/nombres.py generar <clave> --unidad U01 --tema Prueba`.
5. Anotá el cambio en el `AGENTS.md` si cambia la nomenclatura.
