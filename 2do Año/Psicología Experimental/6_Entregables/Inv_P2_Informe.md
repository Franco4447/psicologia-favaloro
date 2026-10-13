---
materia: Psicología Experimental
unidad: Inv_P2
tipo: entregable
fuentes:
- archivo: 6_Entregables/Inv_P2_DisenoExperimental.md
- archivo: 6_Entregables/Inv_P2_FeedbackDiseno.md
- archivo: 6_Entregables/web-experimento/src/data/stimuli.ts
- archivo: 6_Entregables/web-experimento/supabase/schema.sql
- archivo: 2_Textos_Extraidos/Inv_P2_*_Crudo.md
- archivo: 'Drive: Psicología Experimental - Favaloro (Estructura Artículo, Borrador
    Artículo, Pregunta, objetivos e hipótesis)'
skill: ninguna (redacción manual asistida)
generado: '2026-10-12'
hash_generado: b20c6dd2a3c1
---

# Efecto de la inducción de razón y de emoción sobre la formación de falsos recuerdos y falsas creencias a partir de noticias falsas ideológicamente congruentes

**Autores:** [completar con los integrantes del grupo]
**Cátedra:** Psicología Experimental · Universidad Favaloro · Parcial 2 (Investigación)
**Fecha:** [completar]

> **Estado del borrador.** Sigue la estructura que pidió el equipo (Resumen, Introducción, Antecedentes, Objetivos e hipótesis, Método, Resultados, Discusión, Conclusión). Están redactados Introducción, Antecedentes, Objetivos e hipótesis, Método y plan de análisis. *Resumen*, *Resultados*, *Discusión* y *Conclusión* se completan al cerrar la recolección (apartados **[PENDIENTE]**). Lo que está entre corchetes `[ ]` es una decisión o un dato que solo el equipo conoce.

---

## Resumen

**[PENDIENTE: se escribe al final, con N, resultados principales y conclusión. Máximo 250 palabras.]**

**Palabras clave:** noticias falsas, falsos recuerdos, falsas creencias, inducción emocional, procesamiento dual, efecto de congruencia

---

## Introducción

La circulación de información a través de medios digitales y redes sociales expone a las personas a contenidos cuya veracidad no siempre pueden comprobar. Las noticias falsas, es decir, contenido publicado en internet que imita el aspecto de las noticias legítimas pero es fabricado o extremadamente inexacto (Pennycook y Rand, 2021), pueden ser creídas y también distorsionar la memoria y la conducta de quienes las leen (Leon et al., 2023). El estudio de cómo se acepta, se comparte y se corrige la desinformación es hoy un campo amplio de la psicología (Greifeneder et al., 2021).

Dentro de ese campo interesa un fenómeno en particular, la formación de **falsos recuerdos**: recordar claramente haber visto o leído algo que no ocurrió. Su estudio importa porque, a diferencia de una creencia equivocada, un falso recuerdo se vive como una experiencia propia y puede orientar decisiones. Importa especialmente en una profesión como la psicología, cuya práctica tiene implicancias enormes para la salud y la economía (Leon et al., 2023).

Este trabajo pregunta si el modo de procesamiento que se induce antes de leer —basarse en la razón o en la emoción— modifica la formación de falsos recuerdos ante noticias falsas congruentes con lo que la persona ya piensa. Los antecedentes que justifican la pregunta se desarrollan a continuación.

---

## Antecedentes

### Falsos recuerdos, falsas creencias y monitoreo de la fuente

El marco de monitoreo de fuentes (Johnson et al., 1993) propone que los recuerdos no se almacenan con una etiqueta de origen: la persona *infiere* de dónde proviene lo que recuerda a partir de sus características. Es una extensión del monitoreo de la realidad, que consiste en discriminar entre recuerdos de eventos generados internamente (imaginados, pensados) y recuerdos de eventos percibidos externamente (Johnson et al., 1993). Cuando ese monitoreo falla, un evento nunca vivido puede quedar registrado como si lo hubiera sido.

Esta distinción permite separar dos fenómenos que la literatura sobre noticias falsas suele confundir. Un **falso recuerdo** es recordar claramente haber visto o leído un evento que no ocurrió. Una **falsa creencia** es creer que el evento sucedió sin recordar haberlo visto. Murphy et al. (2021) y Leon et al. (2023) los distinguen mediante una escala de cuatro opciones de memoria: recordar claramente el evento, no recordarlo pero creer que sucedió, recordarlo diferente y no recordarlo en absoluto. Este estudio adopta esa escala.

### Congruencia ideológica y sesgo de confirmación

El sesgo de confirmación designa la tendencia a buscar o interpretar la evidencia de maneras parciales hacia las creencias, expectativas o hipótesis preexistentes, en general sin que la persona lo advierta (Nickerson, 1998). Aplicado a la memoria, predice que los eventos falsos congruentes con lo que la persona ya piensa se aceptarán con más facilidad. Frenda et al. (2013) hallaron que las personas generaban falsos recuerdos de eventos políticos fabricados sobre todo cuando eran consistentes con su ideología, fenómeno conocido como *efecto de congruencia* (Leon et al., 2023).

Murphy et al. (2021) lo replicaron con otro tema: cuanto más negativas eran las actitudes de los participantes hacia el feminismo, más probable era que informaran un falso recuerdo de un evento fabricado que dejaba mal parado al movimiento, y viceversa. El resultado se mantuvo en un segundo experimento con historias menos ambiguas, en el que además se compararon las mismas historias con otro grupo protagonista (personas refugiadas) y el estudio se presentó como una investigación sobre noticias de la pandemia de COVID-19 (Murphy et al., 2021). Grady et al. (2021) mostraron que una advertencia previa elimina inicialmente el efecto de congruencia partidaria, pero que este reaparece dos semanas después, aunque los participantes ya sabían que los titulares eran falsos.

Leon et al. (2023) llevaron el paradigma a un debate más acotado: el de las corrientes de la psicología en Argentina. Con 326 personas alineadas con el psicoanálisis (PSA) o con las prácticas basadas en la evidencia (PBE) que vieron 12 noticias verdaderas y 8 fabricadas, hallaron que el grupo PBE recordaba o creía más las noticias falsas que dañaban al psicoanálisis y recordaba con mayor precisión las afirmaciones de las noticias que perjudicaban a su propia corriente. El grupo PSA, en cambio, no mostró efecto de alineación ideológica, lo que los autores interpretan como un desbalance en el compromiso entre las partes. En conjunto, **no observaron que el efecto de congruencia modificara la tasa de falsos recuerdos**, aunque sí que esta población decide guiada por la congruencia ideológica (Leon et al., 2023).

### Por qué estudiantes y profesionales de psicología

Leon et al. (2023) eligieron esta población por tres razones, que este estudio adopta. Primero, el efecto de congruencia se había observado sobre todo en grandes debates sociales (elecciones, referendos), y era una pregunta abierta si aparecía en un nicho profesional específico. Segundo, en Argentina la enseñanza de la psicología es un terreno polarizado: el currículo de la mayoría de las universidades públicas se orienta en un 49,8 % al psicoanálisis y solo en un 4,9 % a la terapia cognitivo-conductual (Fierro, 2015, como se citó en Leon et al., 2023), lo que genera un debate genuino entre quienes defienden el currículo y quienes piden incluir las prácticas basadas en la evidencia. Tercero, las distorsiones de memoria en quienes estudian o ejercen la psicología pueden incidir en las decisiones de la disciplina. Además, un debate con dos bandos identificables permite alinear las noticias falsas con la postura previa de cada participante.

### Procesamiento racional y emocional

Hay un debate sobre *por qué* se cree en noticias falsas. Según la cuenta del razonamiento perezoso, las personas discriminan mal entre noticias verdaderas y falsas cuando no deliberan y se apoyan en la intuición. Según la del razonamiento motivado, la deliberación facilita la cognición protectora de la identidad y sirve para racionalizar lo congruente con la propia ideología (Bago et al., 2020). Bago et al. (2020), con un paradigma de dos respuestas, hallaron que la deliberación corregía los errores intuitivos: los participantes creían más los titulares falsos (no los verdaderos) en la primera respuesta, rápida, que en la respuesta final. Pennycook y Rand (2021) sostienen que la evidencia reciente contradice la narrativa de que la partisanía y el razonamiento motivado expliquen por qué se cae en noticias falsas. Pérez Santángelo y Solovey (2023), en cambio, encuentran que tanto la partisanía como la reflexión cognitiva juegan un papel importante en la aceptación de la desinformación. Ecker et al. (2022) concluyen que los factores que llevan a formar creencias falsas son múltiples: cognitivos (como el pensamiento intuitivo y las fallas de memoria), sociales (como confiar en las pistas de la fuente) y afectivos (como la influencia del ánimo en la credulidad). Visto así, las dos cuentas no serían excluyentes.

El factor afectivo cobra importancia con Martel et al. (2020). En su Estudio 1 (*N* = 409), una mayor emocionalidad al comienzo predecía más creencia en noticias falsas (pero no en reales). En el Estudio 2, que midió y manipuló la dependencia de la emoción frente a la razón en cuatro experimentos (*N* total = 3884), hallaron evidencia correlacional y causal de que apoyarse en la emoción aumenta la creencia en noticias falsas. La manipulación consistió en pedir a los participantes que evaluaran los titulares basándose en la emoción o en la razón, y los autores incluyeron un control de la manipulación y una medida del uso autoinformado de emoción y de razón. La inducción racional, en cambio, no mejoró la discriminación respecto del control; los autores lo atribuyen a que el grupo control ya se apoyaba más en la razón que en la emoción, algo que respaldan sus datos de control de la manipulación (Martel et al., 2020). Trevors et al. (2021) indujeron emociones positivas, negativas o ninguna antes de leer textos y hallaron que las emociones negativas, más que las positivas, favorecían la revisión de conocimientos erróneos sobre vacunas.

### El vacío que aborda este estudio

Hasta donde alcanza la bibliografía revisada, los estudios que manipulan experimentalmente la dependencia de la emoción o la razón (Martel et al., 2020) midieron el impacto sobre la *creencia* en noticias falsas, pero no sobre los *recuerdos*. Los estudios de falsos recuerdos por congruencia ideológica (Leon et al., 2023; Murphy et al., 2021) no manipularon el modo de procesamiento: midieron el efecto pasivo de la congruencia. Integrar ambos paradigmas permite preguntar si el modo de procesamiento inducido —racional o emocional— modula la probabilidad de formar falsos recuerdos ante noticias congruentes con la propia orientación teórica. Las falsas creencias ya están estudiadas con este tipo de inducción; se miden aquí como complemento, y el aporte principal está en los falsos recuerdos.

---

## Pregunta de investigación, objetivos e hipótesis

**Pregunta de investigación.** ¿Cuál es el efecto de la inducción al pensamiento racional y emocional sobre la creación de falsos recuerdos tras la exposición a *fake news* congruentes con la afinidad terapéutica, en personas adultas estudiantes o graduadas de Psicología [definir rango de edad y región]?

**Objetivo general.** Evaluar si la inducción previa a modos de procesamiento cognitivo diferenciados (racional, emocional y control) modifica la frecuencia de formación de falsos recuerdos ante la lectura de *fake news* congruentes con la afinidad terapéutica previa [de personas adultas, estudiantes o graduadas de Psicología].

**Objetivos específicos**

1. Describir la frecuencia de formación de falsos recuerdos ante la lectura de *fake news* congruentes con la afinidad terapéutica previa de los participantes.
2. Comparar la frecuencia de formación de falsos recuerdos entre los participantes sometidos a inducción emocional, inducción racional y los del grupo control.
3. Explorar si el efecto del tipo de inducción sobre la formación de falsos recuerdos varía según la afinidad terapéutica previa (psicoanálisis o práctica basada en evidencia).

Objetivos complementarios, que se derivan de las variables que la plataforma registra:

4. Describir y comparar entre grupos la frecuencia de falsas creencias (medida complementaria).
5. Analizar si el tiempo de respuesta, tomado como indicador del esfuerzo cognitivo, se relaciona con la frecuencia de falsos recuerdos y si difiere entre inducciones.

> **Sobre la congruencia.** Todas las noticias falsas que ve cada participante son congruentes con su afinidad terapéutica; la congruencia es entonces una **constante del diseño** y no una variable. Por eso este estudio *no* tiene como objetivo estimar el efecto de la congruencia ni su interacción con la inducción. Lo que sí varía entre participantes es la afinidad terapéutica (psicoanálisis o práctica basada en evidencia), y el objetivo 3 la analiza.

**Hipótesis**

- **H1.** Los participantes sometidos a inducción **emocional** presentarán una mayor frecuencia de falsos recuerdos ante *fake news* que los sometidos a inducción **racional** y que los del **grupo control**.
- **H2.** El efecto del tipo de inducción sobre la formación de falsos recuerdos **variará según la afinidad terapéutica previa** de los participantes.

**Hipótesis y análisis complementarios** (propuestos a partir de la bibliografía; confirmar con el equipo):

- **C1.** El patrón de H1 se repetirá en las falsas creencias (Martel et al., 2020).
- **C2.** Los recuerdos verdaderos no diferirán entre grupos: la inducción afectaría la aceptación de lo falso pero no la de lo verdadero (Bago et al., 2020).
- **C3.** Los participantes del grupo Emoción responderán más rápido que los del grupo Razón, y un menor tiempo de respuesta se asociará con más falsos recuerdos. La lógica es la del monitoreo de fuentes: una codificación apresurada o heurística impide registrar los detalles contextuales de la fuente y favorece atribuir como real lo imaginado (Johnson et al., 1993).
- **C4 (verificación de la manipulación).** El uso autoinformado de emoción será mayor en el grupo Emoción, y el de razón, en el grupo Razón (Martel et al., 2020).

---

## Método

### Diseño

Experimento en línea con diseño entre sujetos de un factor, **inducción** (Razón, Emoción, Control), con asignación aleatoria balanceada. La variable dependiente principal es el número de falsos recuerdos; las complementarias son el número de falsas creencias, el de recuerdos verdaderos y el tiempo de respuesta. La afinidad terapéutica (psicoanálisis o práctica basada en evidencia) determina qué noticias falsas recibe cada participante y se usa como variable de agrupación en el análisis.

**Congruencia constante.** Cada participante recibe solo noticias falsas congruentes con su afinidad. El equipo tomó esa decisión por tres razones: (a) la inducción emocional podría no ser suficiente para crear un falso recuerdo si la noticia no es congruente; (b) se preserva la validez ecológica, porque las noticias falsas reales no operan sobre temas neutros para quien las lee; y (c) con la congruencia constante, las diferencias entre inducciones pueden atribuirse al modo de procesamiento y no a la afinidad con la noticia. El costo es que el diseño no permite comparar, dentro de una misma persona, noticias congruentes con incongruentes.

### Participantes

**Criterios de inclusión.** Ser estudiante o graduado/a de la carrera de Psicología; tener [18 años o más / entre 18 y 65 años: definir]; manifestar afinidad con el psicoanálisis o con las terapias basadas en evidencia científica, lo que permite seleccionar las noticias falsas de acuerdo con esa afinidad.

**Criterios de exclusión.** Presentar una condición o diagnóstico que afecte significativamente los procesos de memoria y pueda interferir con la tarea, o una dificultad visual no corregida que impida realizar la lectura dentro del tiempo de exposición.

> **A resolver.** El formulario exige tener 18 años o más (acepta hasta 120) y no pregunta provincia ni lugar de residencia. Si los criterios finales incluyen un tope de edad o una región, hay que aplicarlos al analizar, y la región no se puede verificar con los datos recolectados.

**Participantes excluidos del análisis.** Quienes no cumplían los criterios (incluida la opción «Otros / Ninguna en particular» de afinidad) completaban igualmente la tarea con la consigna del grupo Control y un conjunto de noticias falsas elegido al azar entre los dos disponibles, pero la plataforma los registraba como excluidos y no integran ningún grupo ni la muestra analizada.

**Reclutamiento.** Muestreo no probabilístico por acercamiento voluntario: el enlace al experimento se difundió por WhatsApp y circuló entre potenciales participantes, con una convocatoria dirigida a estudiantes y graduados/as de Psicología mayores de 18 años. [Completar fechas de difusión y si hubo incentivo.]

**Muestra.** Participaron [N total] personas, de las cuales [n incluidas] cumplieron los criterios (Razón: [n]; Emoción: [n]; Control: [n]). Edad: *M* = [ ], *DE* = [ ], rango [ ]. Género: [n] femenino, [n] masculino, [n] otro. Afinidad: [n] psicoanálisis, [n] práctica basada en evidencia. Instituciones: [UBA, UNLZ, UFLO, otras].

### Materiales

**Plataforma.** El experimento se presentó en una aplicación web propia (Next.js, con base de datos en Supabase y despliegue en Vercel; código en https://github.com/Franco4447/psicologia-experimental-web). Las respuestas se guardan de forma asíncrona, con un búfer en el navegador para tolerar cortes de conexión.

**Estímulos.** Banco de 28 titulares traducidos al español a partir de los de Leon et al. (2023), cada uno presentado como una imagen con el titular, en un formato parecido al de un *feed* de noticias, como en el estudio original: 12 noticias verdaderas y 16 falsas. [Aclarar el origen de las imágenes, por ejemplo si fueron generadas con IA.] Las falsas se organizan en dos conjuntos de 8:

- *Congruentes con el psicoanálisis*: atacan a la terapia cognitivo-conductual (IDs 14, 16, 18, 20, 21, 23, 25 y 27).
- *Congruentes con la práctica basada en evidencia*: atacan al psicoanálisis (IDs 13, 15, 17, 19, 22, 24, 26 y 28).

Cada noticia falsa de un conjunto tiene un «espejo» en el otro, con la misma estructura y la corriente invertida. Por ejemplo: «El terapeuta freudiano que hipnotizaba a sus pacientes con descargas eléctricas irá a juicio» y «El terapeuta cognitivo que entrenaba a sus pacientes con descargas eléctricas irá a juicio». Cada participante recibe las 12 verdaderas y las 8 falsas congruentes con su afinidad (20 noticias en total) y nunca ambos miembros de un par espejo.

**Escala de memoria.** Para cada noticia, la pregunta «¿Recuerda haber visto o leído este evento con anterioridad?» con cuatro opciones, adaptadas de Murphy et al. (2021) y Leon et al. (2023): (1) *Recuerdo claramente haber visto/leído este evento*; (2) *No recuerdo haberlo visto, pero creo que sucedió*; (3) *Lo recuerdo diferente*; (4) *No lo recuerdo en absoluto*.

**Consignas de inducción.** Adaptación al español de las instrucciones de Martel et al. (2020):

- *Razón*: «Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones.»
- *Emoción*: la misma consigna con los términos invertidos (emoción y sentimientos en lugar de razón y lógica).
- *Control*: «A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no.»

**Verificación de la manipulación.** Al terminar la tarea: (a) solo en los grupos Razón y Emoción, una pregunta de elección forzada (*Emoción* o *Razón*) sobre en qué se les pidió confiar; y (b) en todos los grupos, dos ítems de escala de 1 (*Nada*) a 5 sobre en qué medida usaron la emoción y la razón al evaluar las noticias. Sigue la lógica del control de la manipulación de Martel et al. (2020).

**Cuestionario sociodemográfico.** Edad, género (femenino, masculino, otro), si estudia o estudió Psicología, afinidad terapéutica (psicoanálisis, basada en evidencia científica, otros / ninguna en particular), universidad, condición de memoria y dificultad visual.

### Procedimiento

1. **Bienvenida y consentimiento informado.** Se informa que la actividad dura unos 10-15 minutos, que es voluntaria, que se puede abandonar en cualquier momento y que los datos se analizan de forma grupal con fines académicos.
2. **Cuestionario sociodemográfico.** Al completarlo se registra al participante.
3. **Asignación al grupo.** Una función de la base de datos asigna el grupo con menos participantes incluidos y desempata al azar, bajo un candado transaccional para evitar condiciones de carrera. Así los tres grupos quedan balanceados.
4. **Inducción.** El participante lee la consigna de su grupo.
5. **Tarea de noticias.** 20 ensayos en orden aleatorio (Fisher-Yates), cada uno con dos fases: *lectura* obligatoria de 15 s con barra de progreso, sin posibilidad de avanzar antes, y *evaluación* con la escala de memoria, sin límite de tiempo. La plataforma registra el tiempo de lectura y el tiempo de respuesta en milisegundos. Como la lectura es de duración fija, el indicador de esfuerzo cognitivo es el tiempo de respuesta.
6. **Verificación de la manipulación.**
7. **Debriefing.** Se informa que 8 de los 20 titulares eran noticias falsas creadas para la investigación y se explica el propósito del estudio.
8. **Agradecimiento.**

### Variables y medidas

| Variable | Definición operacional | Rango |
|---|---|---|
| Falso recuerdo (principal) | Elegir la opción 1 ante una noticia **falsa** | 0-8 por participante |
| Falsa creencia (complementaria) | Elegir la opción 2 ante una noticia **falsa** | 0-8 por participante |
| Recuerdo verdadero | Elegir la opción 1 ante una noticia **verdadera** | 0-12 por participante |
| Tiempo de respuesta | Tiempo hasta confirmar la respuesta en la pantalla de evaluación; se promedia por participante y se expresa en segundos | continua |
| Uso de emoción / de razón | Ítems de 1 a 5 de la verificación de la manipulación | 1-5 |

### Consideraciones éticas

El estudio implica un riesgo psicológico leve: la exposición a noticias falsas puede generar malestar o confusión sobre qué información es verdadera. Además, hay un **ocultamiento parcial de información**: no se informa de entrada que el objetivo es medir la formación de falsos recuerdos y falsas creencias, porque saberlo podría alertar a los participantes y sesgar las respuestas, y la consigna del grupo Control presenta los titulares como reales. Ese ocultamiento es aceptable porque se resuelve con un debriefing inmediato que identifica las noticias falsas y explica el propósito real del estudio, de modo que nadie se retire con información falsa tomada por verdadera. Leon et al. (2023) aplicaron una advertencia similar una semana después; aquí el diseño es de una sola sesión, así que se entrega al final de la misma.

La participación fue voluntaria, previa lectura y aceptación del consentimiento informado y con confirmación de ser mayor de 18 años. Se informó la posibilidad de retirarse sin consecuencias y de solicitar la exclusión de las respuestas mientras fuera posible identificarlas. Los datos se tratan de forma confidencial y se analizan en conjunto.

### Plan de análisis

Los datos se exportan de la base de datos en una tabla con una fila por participante, restringida a los participantes incluidos, con edad, género, universidad (con las variantes de escritura unificadas), grupo de inducción, afinidad terapéutica, respuestas de la verificación de la manipulación, recuentos de falsos recuerdos, falsas creencias y recuerdos verdaderos, y tiempo de respuesta promedio en segundos.

- **Descriptivos** por grupo de inducción y por afinidad: medias, desviaciones estándar y proporciones. Primero, la descripción de la muestra, con el porcentaje de cada afinidad dentro de cada grupo.
- **Verificación de la manipulación (C4):** comparación entre grupos del uso autoinformado de emoción y de razón, y porcentaje de aciertos en la pregunta de elección forzada. Quienes no recuerden su consigna se analizarán por separado como análisis de sensibilidad **[definir el criterio de depuración antes de ver los resultados]**.
- **Efecto de la inducción (H1, C1, C2):** como los recuentos son acotados (0-8 y 0-12), modelos de regresión binomial o de Poisson con el grupo como predictor, con contrastes planeados Emoción contra Razón y contra Control; alternativamente, prueba de Kruskal-Wallis si no se cumplen los supuestos. Se informan tamaños del efecto e intervalos de confianza.
- **Variación según afinidad (H2):** interacción entre grupo de inducción y afinidad terapéutica.
- **Tiempo de respuesta (C3):** comparación entre grupos (ANOVA de un factor o Kruskal-Wallis) y relación con el recuento de falsos recuerdos.

---

## Resultados

**[PENDIENTE: completar con el análisis de los datos exportados del panel de administración.]**

Estructura prevista:

1. **Descripción de la muestra** y flujo de participantes (reclutados, excluidos y analizados), con esta tabla:

| Grupo | *n* | % psicoanálisis | % práctica basada en evidencia |
|---|---|---|---|
| Razón | [ ] | [ ] | [ ] |
| Emoción | [ ] | [ ] | [ ] |
| Control | [ ] | [ ] | [ ] |

2. Verificación de la manipulación.
3. Falsos recuerdos por grupo de inducción (tabla de medias y *DE*, contrastes planeados, tamaños del efecto).
4. Variación del efecto según la afinidad terapéutica.
5. Falsas creencias y recuerdos verdaderos por grupo.
6. Tiempo de respuesta por grupo y su relación con los falsos recuerdos.

---

## Discusión

**[PENDIENTE: se redacta con los resultados.]**

Ejes a desarrollar:

- **Lectura de los resultados** frente a cada hipótesis y frente a lo hallado por Martel et al. (2020), Bago et al. (2020) y Leon et al. (2023).
- **Mecanismo.** Discutir con el marco de monitoreo de fuentes (Johnson et al., 1993) si una inducción emocional favorece que lo imaginado se registre como visto, y su relación con los factores cognitivos, sociales y afectivos descritos por Ecker et al. (2022).
- **Diferencias entre afinidades.** Retomar el desbalance que Leon et al. (2023) hallaron entre el grupo PSA y el grupo PBE.
- **Generalización.** La muestra es de estudiantes y graduados de psicología; discutir qué implica para otras poblaciones, por ejemplo para las personas que consultan a un profesional y deben decidir qué información tomar de él.

**Limitaciones**

- Todas las noticias falsas son congruentes con la afinidad de cada participante; el diseño no permite estimar el efecto de la congruencia, como sí hacen Leon et al. (2023).
- **Tiempo de lectura.** Leon et al. (2023) dieron un máximo de 30 s para responder y evaluaron la memoria en dos días, con una semana de diferencia; aquí hay 15 s de lectura obligatoria seguidos de respuesta sin límite, en una sola sesión.
- El diseño implica un ocultamiento parcial de información (ver Consideraciones éticas).
- La muestra, reclutada por [medio], limita la generalización.
- La verificación de la manipulación se basa en autoinforme.
- La frase de contexto de Martel et al. (2020) («titulares de noticias reales de 2017-2018») solo se presenta al grupo Control.
- Origen de las imágenes de las noticias: [aclarar].

**Líneas futuras.** Diseños factoriales con una variable más manipulada entre sujetos: (1) advertencias × inducción (razón o emoción), siguiendo a Grady et al. (2021), para ver si el efecto protector de una advertencia sobrevive a una inducción emocional; (2) procesamiento intuitivo frente a deliberado como factor entre sujetos, ya que se ha estudiado dentro del mismo sujeto (Bago et al., 2020); (3) noticias a favor y en contra de una ideología, para estudiar el efecto de la compatibilidad; y (4) la predisposición emocional o racional como variable continua de personalidad. Queda abierta una pregunta de la discusión del equipo: si entrenar procedimientos lógicos hasta automatizarlos haría detectar noticias falsas incluso al leer rápido y juzgar de forma intuitiva **[identificar el trabajo en que se basa]**.

---

## Conclusión

**[PENDIENTE: se redacta al cerrar la Discusión.]**

---

## Referencias

Bago, B., Rand, D. G., y Pennycook, G. (2020). Fake news, fast and slow: Deliberation reduces belief in false (but not true) news headlines. *Journal of Experimental Psychology: General*. Advance online publication. https://doi.org/10.1037/xge0000729

Ecker, U. K. H., Lewandowsky, S., Cook, J., Schmid, P., Fazio, L. K., Brashier, N., Kendeou, P., Vraga, E. K., y Amazeen, M. A. (2022). The psychological drivers of misinformation belief and its resistance to correction. *Nature Reviews Psychology, 1*, 13-29. https://doi.org/10.1038/s44159-021-00006-y

Frenda, S. J., Knowles, E. D., Saletan, W., y Loftus, E. F. (2013). False memories of fabricated political events. *Journal of Experimental Social Psychology, 49*(2), 280-286. https://doi.org/10.1016/j.jesp.2012.10.013

Grady, R. H., Ditto, P. H., y Loftus, E. F. (2021). Nevertheless, partisanship persisted: Fake news warnings help briefly, but bias returns with time. *Cognitive Research: Principles and Implications, 6*, Artículo 52. https://doi.org/10.1186/s41235-021-00315-z

Greifeneder, R., Jaffé, M. E., Newman, E. J., y Schwarz, N. (Eds.). (2021). *The psychology of fake news: Accepting, sharing, and correcting misinformation*. Routledge. https://doi.org/10.4324/9780429295379

Johnson, M. K., Hashtroudi, S., y Lindsay, D. S. (1993). Source monitoring. *Psychological Bulletin, 114*(1), 3-28. https://doi.org/10.1037/0033-2909.114.1.3

Leon, C. S., Bonilla, M., Brusco, L. I., Forcato, C., y Urreta Benítez, F. (2023). Fake news and false memory formation in the psychology debate. *IBRO Neuroscience Reports, 15*, 24-30. https://doi.org/10.1016/j.ibneur.2023.06.002

Martel, C., Pennycook, G., y Rand, D. G. (2020). Reliance on emotion promotes belief in fake news. *Cognitive Research: Principles and Implications, 5*, Artículo 47. https://doi.org/10.1186/s41235-020-00252-3

Murphy, G., Murray, E., y Gough, D. (2021). Attitudes towards feminism predict susceptibility to feminism-related fake news. *Applied Cognitive Psychology, 35*(5), 1182-1192. https://doi.org/10.1002/acp.3851

Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology, 2*(2), 175-220. https://doi.org/10.1037/1089-2680.2.2.175

Pennycook, G., y Rand, D. G. (2021). The psychology of fake news. *Trends in Cognitive Sciences, 25*(5), 388-402. https://doi.org/10.1016/j.tics.2021.02.007

Pérez Santángelo, A., y Solovey, G. (2023). Understanding belief in political statements using a model-driven experimental approach: A registered report. *Scientific Reports, 13*, Artículo 21205. https://doi.org/10.1038/s41598-023-47939-3

Trevors, G., Bohn-Gettler, C., y Kendeou, P. (2021). The effects of experimentally induced emotions on revising common vaccine misconceptions. *Quarterly Journal of Experimental Psychology*. https://doi.org/10.1177/17470218211017840
