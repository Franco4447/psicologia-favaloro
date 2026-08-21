# Documento de Estudio Exhaustivo: Introducción a la Estadística Aplicada a la Psicología y a la Psicopedagogía (Clase 1)

---

## 1. ¿Por qué estudiar estadística en psicología y psicopedagogía?

La introducción de la estadística dentro de las ciencias de la salud y del comportamiento responde a necesidades analíticas e investigativas concretas. En la práctica profesional e investigativa, se identifican dos escenarios fundamentales donde esta disciplina resulta indispensable:

* **Descripción de fenómenos complejos:** Para abordar múltiples problemas de investigación, es mandatorio recolectar y trabajar con un conjunto de números (más o menos grande) con el fin explícito de ordenar y describir con precisión el fenómeno que se está estudiando.


* **Generalización y extrapolación de resultados:** Surge la necesidad científica de extraer conclusiones generalizables a partir de nuestras observaciones empíricas directas, extendiendo dichas interpretaciones hacia aquellos casos potenciales o individuos que no han participado activamente en nuestros estudios.



### Contexto Histórico y Epistemológico

Etimológicamente, la palabra **estadística** procede del vocablo *estado*. Desde la antigüedad (como en los imperios romano y egipcio), las naciones realizaron recolecciones sistemáticas de datos para poseer un conocimiento preciso del número de sus habitantes y de sus posesiones (conocer el estado de la nación). Sin embargo, aquellas antiguas recolecciones carecían de capacidad predictiva: las conclusiones se agotaban en el propio conjunto de datos contados y medidos.

La estadística actual es el producto directo del encuentro y la mutua fecundación de dos ramas del saber que convergen formalmente en el siglo XIX:

1. La antigua estadística descriptiva gubernamental.


2. El cálculo de probabilidades.



Este encuentro incorporó el instrumento matemático adecuado para extrapolar conclusiones a entidades no observadas directamente. El desarrollo moderno de estas técnicas se cimentó sobre la formulación de la curva normal por Gauss, la aplicación pionera de Galton a los problemas de la herencia, y los desarrollos e institucionalización metodológica de Karl Pearson (1857-1936) y Ronald Fisher (1890-1962).

### Estadística Teórica vs. Estadística Aplicada

Es fundamental trazar la línea divisoria entre los dos modos de aproximación a esta ciencia:

* La **estadística teórica** se dedica de forma pura al estudio y desarrollo de los métodos y modelos formalmente válidos para la realización de resúmenes de datos y de inferencias.


* La **estadística aplicada** se enfoca en la selección, adopción y aplicación de esos métodos y modelos formales a campos reales del conocimiento empírico, tales como la psicología, la psicopedagogía o la sociología.



---

## 2. Grandes divisiones de la estadística: Descriptiva e Inferencial

Clásicamente, la estadística se divide en dos grandes ramas articuladas que reflejan tanto su evolución histórica como las fases lógicas de todo análisis empírico:

### 2.1. Estadística descriptiva

Se define formalmente como el conjunto de métodos orientados a organizar, representar, resumir y analizar la información contenida en un conjunto de datos brutos.

> 
> **Advertencia Conceptual:** Un estudio puramente descriptivo se agota de forma absoluta en el propio conjunto de datos observados. Las conclusiones obtenidas no se pueden extender legítimamente más allá de los individuos evaluados en esa muestra.
> 
> 

### 2.2. Estadística inferencial

Se define como el conjunto de métodos y modelos matemáticos que permiten extraer conclusiones, generalizaciones y extrapolaciones sobre las poblaciones de referencia a partir del análisis de muestras concretas, controlando rigurosamente un margen de error admisible. Para abordar la estadística inferencial es requisito indispensable incorporar nociones metodológicas del cálculo de probabilidades.

La estadística inferencial se subdivide en dos grandes estrategias operativas:

* **Estimación de parámetros:** Métodos que buscan aproximar los valores poblacionales desconocidos a partir de los datos muestrales calculados.


* **Contraste de hipótesis:** Procedimientos estructurados para decidir si una afirmación teórica sobre la población es compatible con la evidencia empírica recolectada en la muestra.



> 
> **Articulación de fases en la investigación:** Un estudio inferencial jamás se ejecuta de forma aislada; comienza obligatoriamente por una fase de descripción exhaustiva de los datos para luego, sobre esa base compacta, abordar el proceso inferencial.
> 
> 

---

## 3. Conceptos básicos fundamentales

Para estructurar la metodología estadística aplicada, se debe fijar con precisión matemática el vocabulario base de las entidades, las propiedades y los valores en juego:

### 3.1. Población de individuos (o entidades estadísticas)

Es el conjunto de todos los elementos, entes o unidades que cumplen una o varias características específicas de interés para la investigación. Los elementos que componen una población se denominan **individuos** o **entidades estadísticas**, y no se limitan a personas; pueden ser animales, objetos, instituciones o, simplemente, abstracciones numéricas.

### 3.2. Muestra de individuos

Es cualquier subconjunto de elementos que pertenecen a una población previamente delimitada.

> 
> **El principio de representatividad:** El objetivo prioritario de la investigación empírica es extraer conclusiones sobre la población basándose en la muestra. Este objetivo solo se alcanza plenamente si la muestra es estadísticamente *representativa* de la población. Para asegurar dicha propiedad, existe el campo del *muestreo*, el cual estudia los procedimientos científicos de extracción muestral orientados a maximizar la representatividad y evitar sesgos sistemáticos. Las conclusiones jamás pueden exceder el marco de la población de referencia definida.
> 
> 

### 3.3. Variable o característica

Se define como cualquier fenómeno o propiedad observable en los individuos de una población que presenta diferentes modalidades (variaciones) entre dichos individuos.

### 3.4. Variable estadística

Es la representación formal, simbólica y codificada del fenómeno observable (= variable). Una característica pasa a ser una variable estadística únicamente cuando es sometida a un proceso estructurado de **medición**.

### 3.5. Población de observaciones

Es el conjunto de todos los valores numéricos que puede adoptar una variable estadística determinada sobre la totalidad de los individuos que conforman la población.

> 
> **Nota Teórica:** Es vital comprender que sobre una misma población de individuos definida, un investigador puede delimitar y medir múltiples características distintas y, en consecuencia, puede definir muchas poblaciones de observaciones diferentes.
> 
> 

### 3.6. Muestra de observaciones

Es el conjunto concreto de valores que toma una variable estadística específica sobre los elementos que integran una muestra de individuos seleccionada. Constituye el corpus numérico real con el cual opera el analista de datos.

### 3.7. Parámetro

Es una característica constante o fija que describe numéricamente a una población de observaciones dada. Al ser valores fijos pero generalmente desconocidos (debido a la imposibilidad de evaluar a toda la población), se representan convencionalmente mediante letras griegas (por ejemplo, la media poblacional $\mu$, la desviación típica poblacional $\sigma$, o el porcentaje poblacional $\pi$).

### 3.8. Estadístico

Es una característica variable que describe numéricamente a una muestra de observaciones. Su valor fluctúa de una muestra a otra debido al azar muestral. Se simbolizan formalmente con letras latinas (por ejemplo, la media muestral $\bar{X}$, la desviación típica muestral $S$, o el porcentaje muestral $P$).

### 3.9. Estimador

Se denomina estimador a aquel estadístico muestral cuyos valores se consideran matemáticamente próximos al parámetro poblacional homólogo. En la lógica de la investigación, el proceso metodológico sigue una secuencia bidireccional cronológica:


$$\text{Fase 1: Obtención empírica de Estadísticos (Muestra)} \longrightarrow \text{Fase 2: Uso como Estimadores} \longrightarrow \text{Inferencia de Parámetros (Población)}$$

---

## 4. Medición y teoría de escalas

### 4.1. Fundamentos lógicos de la medición

La **medición** es formalmente definida como la conexión matemática e instrumental entre un **sistema relacional empírico** (las propiedades o modalidades observables en el mundo real) y un **sistema relacional numérico** (los números y las propiedades lógicas y aritméticas que rigen entre ellos). Medir consiste en atribuir números a las modalidades de una variable (= característica) de acuerdo con reglas lógicas preestablecidas.

Para que un proceso de medición sea matemáticamente válido, la asignación de números debe respetar obligatoriamente el principio de **homomorfismo**. Esto implica que las relaciones verificables entre las modalidades empíricas de los objetos deben quedar fielmente reflejadas y preservadas en las relaciones de los números asignados. Los modelos específicos desarrollados para operativizar estas representaciones numéricas legítimas bajo condiciones matemáticas estrictas se denominan **escalas de medida**.

### 4.2. Niveles o escalas de medición (Clasificación de Stevens)

Siguiendo la influyente taxonomía propuesta por Stanley Smith Stevens (1946), se identifican cuatro niveles jerárquicos de escalas de medición. Cada nivel superior posee las propiedades del nivel anterior e incorpora nuevas restricciones y operaciones matemáticas permitidas:

#### 4.2.1. Escala Nominal

Es el nivel más básico de medición. Se utiliza cuando la característica bajo estudio consiste puramente en la clasificación de los individuos en categorías mutuamente excluyentes que denotan atributos diferenciables.

* **Información deducible:** Relaciones de igualdad o diferencia ($=$ o $\neq$). Si dos entidades comparten el mismo número, pertenecen a la misma categoría; si tienen números distintos, pertenecen a categorías diferentes.


* **Propiedades numéricas:** Los números asignados actúan exclusivamente como meros códigos de identificación, etiquetas o símbolos. No expresan magnitud, dirección ni orden jerárquico. Podrían sustituirse por letras o palabras sin alterar la escala.


* **Transformaciones admisibles:** Cualquier aplicación inyectiva (cualquier cambio uno a uno de los códigos numéricos) es perfectamente admisible, dado que no rompe la estructura clasificatoria subyacente.



> 
> **Advertencia Crítica para el Análisis por Computadora:** Los programas y paquetes estadísticos modernos procesan ciegamente cualquier número introducido en una matriz. El software no distingue de forma autónoma la naturaleza de la escala y operará aritméticamente según las instrucciones del algoritmo. Por ejemplo, si se asigna el código `1` a Varones y `2` a Mujeres, la computadora puede calcular una media aritmética de `1.5`, pero dicho resultado carece por completo de significado real. Lo que pueda inferirse legítimamente a partir de esos números es responsabilidad exclusiva del investigador que interpreta los resultados.
> 
> 

#### 4.2.2. Escala Ordinal

Este nivel se alcanza cuando la característica medida, además de permitir la clasificación en categorías exhaustivas y excluyentes, presenta un orden o jerarquía interna intrínseca a su naturaleza empírica.

* **Información deducible:** Relaciones lógicas de orden de tipo "mayor que" o "menor que" ($>$ o $<$). Permite determinar si un individuo posee una propiedad en mayor o menor grado que otro.


* **Propiedades numéricas:** Los números expresan orden posicional relativo, pero no cuantifican la distancia métrica real entre las posiciones. Es decir, no se puede asumir que la diferencia de magnitud entre el rango 1 y el rango 2 sea numéricamente equivalente a la diferencia entre el rango 2 y el rango 3.


* **Transformaciones admisibles:** Funciones estrictamente crecientes. Cualquier transformación matemática que preserve rigurosamente el orden jerárquico original de los datos (por ejemplo, multiplicar por 5 y sumar 8, o aplicar una función monotónica) es admisible. Transformaciones que alteren el orden (como multiplicar por un número negativo) están prohibidas.



#### 4.2.3. Escala Intervalar (o de Intervalos)

Este nivel se presenta cuando la característica posee una unidad de medida estandarizada y constante que permite cuantificar con exactitud matemática la distancia o diferencia real entre dos valores cualesquiera de la variable.

* **Información deducible:** Igualdad o desigualdad de diferencias o intervalos numéricos. Se puede afirmar de forma válida que la distancia entre una puntuación de 20 y una de 30 es exactamente igual a la distancia entre 40 y 50.


* **La naturaleza del cero (0):** El origen de la escala incorpora un **cero arbitrario** o relativo. Esto significa que el valor cero no implica en absoluto la ausencia de la característica medida. Es un punto de referencia convencional fijado históricamente (como los $0^\circ\text{C}$ de la escala Celsius de temperatura o el origen cronológico de un calendario).


* **Transformaciones admisibles:** Transformaciones lineales positivas que adopten formalmente la estructura matemática:



$$Y = a + b \cdot X \quad (\text{donde } b > 0)$$


Estas funciones permiten cambiar tanto la escala de la unidad de medida ($b$) como el origen arbitrario ($a$), manteniendo intacta la constancia de las relaciones de distancia entre los intervalos.



#### 4.2.4. Escala de Razón (o de Cocientes)

Constituye el nivel más alto y completo en la jerarquía de la medición. Satisface todas las propiedades de las escalas de intervalo pero soluciona de forma absoluta la limitación del punto de origen.

* **Información deducible:** Igualdad o desigualdad de razones o cocientes matemáticos. Permite establecer proporciones numéricas directas con validez lógica.


* **La naturaleza del cero (0):** Incorpora un **cero absoluto** y verdadero. El valor numérico cero denota la ausencia total e inequívoca de la característica o propiedad que se está evaluando.


* **Transformaciones admisibles:** Multiplicación exclusiva por una constante positiva:



$$Y = b \cdot X \quad (\text{donde } b > 0)$$


Debido a que el origen de la escala es fijo e inamovible (el cero absoluto no puede desplazarse), la única variación permitida consiste en alterar la unidad de medida (por ejemplo, pasar la medición de distancias de metros a centímetros, o de tiempo de segundos a minutos), lo cual preserva de forma perfecta la proporcionalidad de las razones métricas.



---

## 5. Clasificación general y notación de las variables

### 5.1. Clasificación según la naturaleza de sus valores

De acuerdo con las restricciones lógicas y metodológicas que imponen sus modalidades y escalas de procedencia, las variables se agrupan en tres categorías macro:

1. 
**Variables Cualitativas:** Son aquellas cuyas modalidades expresan meros atributos, categorías cualitativas o etiquetas no numéricas. Corresponden de forma unívoca al nivel métrico de la **escala nominal**.


2. 
**Variables Cuasi-cuantitativas:** Son aquellas que denotan un orden, rango o jerarquía explícita entre sus elementos, sin llegar a cuantificar diferencias numéricas uniformes. Corresponden al nivel métrico de la **escala ordinal**.


3. 
**Variables Cuantitativas:** Son aquellas cuyas modalidades expresan de forma inherente cantidades numéricas con propiedades métricas reales. Corresponden a los niveles superiores de medición (**escalas de intervalo y de razón**). Atendiendo al número de valores potenciales que pueden adoptar dentro de su rango de variación, se subdividen de forma estricta en:


* **Variables Discretas:** Son aquellas que adoptan exclusivamente valores aislados. Fijados dos valores consecutivos cualesquiera dentro de la escala, es conceptualmente imposible que la variable asuma una puntuación intermedia.


* **Variables Continuas:** Son aquellas que pueden adoptar potencialmente infinitos valores intermedios dentro de cualquier intervalo de la escala.





> 
> **Diferenciación conceptual fundamental:** No se debe confundir los valores discretos con los valores enteros, aunque operativamente suelan coincidir en la práctica. En el caso de las variables continuas, el hecho de que observemos un conjunto finito de valores discretizados en una matriz responde únicamente a los límites de precisión del instrumento de medición físico o psicométrico empleado, y no a la naturaleza del fenómeno subyacente.
> 
> 

### 5.2. Reglas de Notación Estadística Estándar

Para transcribir de forma limpia y formal el análisis estadístico algebraico, se aplican las siguientes convenciones de notación matemática:

* Una variable bajo estudio se simboliza genéricamente con letras mayúsculas latinas (típicamente $X$, $Y$ o $Z$).


* Un valor observado particular dentro de un grupo homogéneo se representa añadiendo un único subíndice alfabético: la expresión $X_i$ indica de forma precisa el valor numérico concreto adoptado por la variable $X$ para el individuo o unidad de observación que ocupa la posición ordinal $i$.


* Cuando la investigación involucra la recolección de datos distribuidos en **múltiples grupos diferenciados**, se hace estrictamente necesario recurrir a una notación estructurada mediante **doble subíndice** de la forma:



$$X_{ij}$$


Donde los subíndices se definen formalmente de la siguiente manera:


* El segundo subíndice ($j$) identifica de forma unívoca al **grupo o condición** al que pertenece el dato.


* El primer subíndice ($i$) identifica el número de orden de la **observación o sujeto individual** dentro de ese grupo específico $j$.


* *Ejemplo de aplicación analítica:* El símbolo formal $X_{23}$ representa la puntuación del segundo sujeto ($i=2$) perteneciente al tercer grupo ($j=3$) en la variable $X$.





---

## 6. Fuentes de variación en la investigación empírica

En cualquier estudio enfocado en la psicología o psicopedagogía, las puntuaciones y registros numéricos finales obtenidos reflejan fluctuaciones constantes. Estas variaciones empíricas proceden directamente de dos fuentes de variación de naturaleza contrapuesta:

* **Fuentes de Variación Fortuitas:** Hacen referencia a todas aquellas variaciones aleatorias, imprevistas e imprevisibles que resultan del azar, de factores ambientales incontrolables o de fluctuaciones transitorias intrínsecas a los sujetos durante la medición (constituyen el denominado error de medida aleatorio).


* **Fuentes de Variación Sistemáticas:** Hacen referencia a las variaciones previsibles, constantes y estructuradas que responden a una causa conocida o controlada de forma directa bajo el diseño metodológico de la investigación (por ejemplo, las variaciones inducidas deliberadamente por la aplicación de un programa de entrenamiento cognitivo o por características estables de los sujetos como su nivel de inteligencia o edad).



---

## Bloque Integrador de Aplicación: Ejemplos Analíticos de Investigación

Para comprender de forma holística la interconexión entre los objetivos de un estudio, la delimitación de las variables y el nivel de escala que regula su tratamiento, se exponen a continuación los cuatro casos clásicos de investigación desarrollados en la bibliografía de consulta:

* **Diseño y Contexto:** Una corporación encarga a un psicólogo la evaluación de los rasgos psicológicos de su plantilla de mandos intermedios con vistas a seleccionar candidatos idóneos para una promoción ejecutiva de alta responsabilidad. Se administran diversos inventarios estandarizados.


* **Variables bajo análisis:** El constructo central medido es el *Grado de Patrón A de Comportamiento* (un patrón tipificado por respuestas al estrés, sentido de urgencia cronológica y presiones competitivas).


* **Propiedades Métricas:** Se determina como una variable cuantitativa medida a nivel de **Escala de Intervalo**.


* **Tipo de Estudio Estadístico:** Es **exclusivamente descriptivo**. Las operaciones analíticas y las interpretaciones finales se agotan y concluyen por completo en la estructuración de los datos del grupo específico de mandos intermedios evaluados, sin intenciones de extrapolar el conocimiento a otras poblaciones de trabajadores externos.



* **Diseño y Contexto:** Un experimento formal diseñado para evaluar rigurosamente la efectividad de una técnica psicoterapéutica cognitivo-conductual (inoculación de estrés) para mitigar el impacto adaptativo del medio, controlando el posible papel modulador de variables cognitivas y educativas de los sujetos.


* **Estructura Metodológica:** Se seleccionan inicialmente 40 sujetos que sufren de estrés y se dividen de forma estrictamente aleatoria en dos grupos homogéneos de 20 participantes cada uno : un Grupo Experimental (entrenado en la técnica) y un Grupo Control (sin entrenamiento). Se evalúan diversas características al inicio y tras seis meses de seguimiento.


* **Matriz y Clasificación de Variables:**
1. 
*Grupo de Pertenencia:* Variable Cualitativa $\longrightarrow$ **Escala Nominal**.


2. 
*Nivel Cultural/Estudios* (Ninguno, Primarios, Secundarios, Universitarios): Variable Cuasi-cuantitativa $\longrightarrow$ **Escala Ordinal**.


3. 
*Inteligencia del sujeto* (Medida mediante la escala métrica estandarizada del Test de Wechsler): Variable Cuantitativa $\longrightarrow$ **Escala de Intervalo**.


4. 
*Nivel de Estrés Percibido* (Puntuaciones psicométricas arrojadas por inventarios clínicos específicos): Variable Cuantitativa $\longrightarrow$ **Escala de Intervalo**.




* **Tipo de Estudio Estadístico:** Es de **naturaleza inferencial**. A partir de las puntuaciones de la muestra real de 40 individuos, el objetivo científico es generalizar la eficacia clínica de la intervención hacia el universo total de la especie humana que padece situaciones análogas de estrés.



* **Diseño y Contexto:** Un estudio experimental de laboratorio enfocado en desglosar las fases cronométricas latentes del procesamiento humano de la información a través de tareas simples de discriminación de estímulos.


* **Estructura Metodológica:** Un único sujeto experimental es sometido a la tarea «Tipo C» de Donders a lo largo de 30 ensayos sucesivos. En cada ensayo se le presenta aleatoriamente uno de dos estímulos visuales posibles: el sujeto posee la instrucción estricta de presionar un botón tan rápido como le sea posible únicamente si se presenta el estímulo objetivo, y debe abstenerse de emitir respuesta alguna si aparece el estímulo alternativo. Dado que el sujeto exhibe variabilidad en sus ejecuciones por causas fortuitas, se colectan las 30 mediciones temporales.


* **Propiedades Métricas:** La variable medida es el *Tiempo de Reacción*, expresado de forma continua en fracciones de segundo o milisegundos. Corresponde estrictamente al nivel métrico de **Escala de Razón**, dado que el cero absoluto representa la ausencia teórica completa de tiempo invertido, habilitando la comparación de proporciones matemáticas legítimas.


* **Tipo de Estudio Estadístico:** Es **inferencial**. A partir del análisis del subconjunto de los 30 ensayos reales observados, el investigador busca inferir las propiedades estables de la ejecución potencial e infinita del proceso cognitivo de ese sujeto bajo esa condición particular.



* **Diseño y Contexto:** Un estudio sociológico masivo orientado a estimar y predecir con exactitud científica el resultado final de una consulta de referéndum nacional que se celebrará próximamente.


* **Estructura Metodológica:** Ante la imposibilidad absoluta por costes económicos y logísticos de entrevistar a la población nacional completa, se recurre a la extracción de una muestra representativa de 3.000 ciudadanos seleccionados estratégicamente de todas las comunidades autónomas y franjas etarias del territorio.


* **Propiedades Métricas:** La variable central recolectada es la *Intención de Voto*, la cual admite dos modalidades discretas excluyentes que denotan atributos diferenciables: SÍ / NO. Se clasifica como una variable cualitativa medida a nivel de **Escala Nominal**.


* **Tipo de Estudio Estadístico:** Es marcadamente **inferencial**. El analista procesa estadísticamente las frecuencias descriptivas de la muestra (los porcentajes de respuestas afirmativas o negativas de los 3.000 encuestados) con el fin explícito de emplearlos como estimadores para generalizar el parámetro poblacional real y predecir el comportamiento político de la nación completa.



---

## 7. Introducción al entorno operativo: La Matriz de Datos

En el ejercicio contemporáneo de la estadística aplicada a la psicología y a la psicopedagogía, la totalidad de los cálculos complejos y el procesamiento de grandes volúmenes de información se canalizan por medio de computadoras a través de programas especializados organizados en **paquetes estadísticos**. El punto de partida instrumental e informático para estructurar cualquier análisis de datos es la configuración de una **matriz de datos**.

### Estructura Geométrica de una Matriz de Datos

Una matriz es una disposición rectangular regular de números y códigos organizados bajo dos ejes coordenados rígidos:

* **Las Filas:** Cada fila horizontal de la matriz representa a un **sujeto individual**, unidad de observación o entidad estadística del estudio de forma unívoca.


* **Las Columnas:** Cada columna vertical representa a una **variable estadística** o característica particular medida sobre dichos elementos.



### El Tratamiento Estadístico de los Datos Perdidos (Missing Values)

Durante la ejecución empírica de investigaciones de campo o clínicas, es frecuente que por razones externas o accidentales (un sujeto que se abstiene de responder una pregunta en una encuesta, el fallo temporal de un sensor de laboratorio, o la inasistencia de un paciente a una sesión de evaluación) no se logre recolectar el dato de una variable específica para un individuo determinado. En el diseño de la matriz, esta casilla vacía no se rellena con valores arbitrarios ni con el número cero. Se designa formalmente bajo la categoría de **dato perdido** (*missing value*). Los paquetes estadísticos modernos requieren que estas ausencias queden codificadas bajo un formato especial para que los algoritmos matemáticos las excluyan de forma correcta durante los cálculos descriptivos o inferenciales, evitando así la introducción de sesgos métricos que invaliden la investigación.

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 1: Conceptos generales). Ediciones Pirámide.


* Sarli, L. (2026). *Introducción a la estadística aplicada a la Psicología y a la Psicopedagogía* (Material didáctico de la Clase 1).