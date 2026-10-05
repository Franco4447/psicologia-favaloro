# Documento de Estudio Exhaustivo: Organización y Representación de Datos (Clase 2)

---

## 1. Introducción a la Estadística Descriptiva y la Inspección de Datos

Una vez recolectados los datos empíricos de una investigación en psicología o psicopedagogía, el analista se enfrenta a una matriz compuesta por un conjunto masivo de puntuaciones brutas. La **estadística descriptiva** aporta el instrumental formal diseñado para organizar, representar, resumir y analizar de forma relacional la información contenida en dicho conjunto.

Antes de ejecutar cualquier cálculo complejo de estadísticos muestrales o inferencias avanzadas, es un imperativo metodológico realizar una **inspección cuidadosa de los datos**. Cuando las muestras son pequeñas, una revisión visual directa puede revelar anomalías o puntuaciones atípicas. Sin embargo, a medida que el tamaño muestral ($N$) crece, el ojo humano pierde la capacidad de detectar patrones o errores a simple vista. Es allí donde se vuelve obligatorio condensar la información a través de dos herramientas fundamentales:

1. **Tablas de frecuencia**
2. **Representaciones gráficas**

---

## 2. Tablas de Frecuencia (Distribuciones de Frecuencia)

Una **tabla de frecuencias** es un dispositivo de reorganización de datos estructurado de forma relacional. Su objetivo es asociar a cada modalidad o valor de una variable el número de veces que se ha observado en la muestra, facilitando la interpretación inmediata de la distribución, la construcción de gráficas y la optimización de los cálculos aritméticos ulteriores.

### 2.1. Componentes Formales de una Tabla de Frecuencias

Para construir e interpretar una distribución de frecuencias completa, se deben dominar las siguientes métricas estadísticas elementales:

* **Valores de la variable ($X_i$):** Representa las modalidades exhaustivas y mutuamente excluyentes que adopta la variable en la muestra.
* **Frecuencia absoluta ($n_i$):** Es el número de veces que se repite el valor exacto o la categoría $X_i$ en el conjunto de las observaciones. Satisface la siguiente propiedad fundamental (donde $k$ es el número de categorías distintas):

$$\sum_{i=1}^{k} n_i = n \quad (\text{Tamaño total de la muestra})$$


* **Frecuencia relativa ($p_i$ o $f_i$):** Es el cociente o proporción entre la frecuencia absoluta de una categoría y el tamaño total de la muestra. Permite realizar comparaciones directas entre muestras de diferentes tamaños:

$$p_i = \frac{n_i}{n}$$



La suma de todas las frecuencias relativas en una muestra es formalmente igual a la unidad: $\sum p_i = 1$. Multiplicada por 100, expresa el **porcentaje** de observaciones ($c_i = p_i \cdot 100$).
* **Frecuencia absoluta acumulada ($N_i$):** Es la suma acumulada de las frecuencias absolutas de todos los valores inferiores o iguales a la categoría $X_i$. Su cálculo se formaliza secuencialmente como:

$$N_i = n_1 + n_2 + \dots + n_i = N_{i-1} + n_i$$


* **Frecuencia relativa acumulada ($P_i$):** Es el cociente entre la frecuencia absoluta acumulada y el tamaño total de la muestra ($P_i = N_i / n$), representando la proporción acumulada de observaciones. Multiplicada por 100, se transforma en el **porcentaje acumulado**.

> **Advertencia de Nivel Métrico:** El cálculo de las frecuencias acumuladas ($N_i$ y $P_i$) exige de forma obligatoria que los datos posean, como mínimo, un nivel de **escala ordinal**. Carece por completo de validez lógica acumular frecuencias en variables nominales (como la "carrera de estudio" o la "intención de voto"), dado que en ellas no existe una jerarquía o dirección matemática intrínseca que guíe el proceso de acumulación.

### 2.2. Agrupación de Datos en Intervalos

Cuando trabajamos con variables cuantitativas continuas (como el *Tiempo de Reacción*) o cuantitativas discretas con un rango muy amplio de valores, la confección de una tabla de valores individuales genera distribuciones extensas e inoperantes. En estos escenarios, se vuelve necesario agrupar los datos en **intervalos de clase**.

#### Conceptos Clave de la Agrupación por Intervalos:

* **Límites Aparentes o Informados:** Son los valores extremos que delimitan visualmente el intervalo tal como aparecen registrados en la tabla (ej. $10 - 14$, $15 - 19$). Dejan huecos o zonas de discontinuidad entre intervalos.
* **Límites Reales:** Son los puntos matemáticos verdaderos de continuidad que eliminan los vacíos entre intervalos adyacentes. Se calculan promediando el límite aparente superior de un intervalo con el límite aparente inferior del intervalo inmediato superior. Para puntuaciones enteras, se obtienen restando $0.5$ al límite aparente inferior y sumando $0.5$ al límite aparente superior (ej. el intervalo aparente $10 - 14$ posee los límites reales $9.5 - 14.5$).
* **Amplitud del Intervalo ($I$):** Es la distancia métrica existente entre el límite real superior ($L_{RS}$) y el límite real inferior ($L_{RI}$) de un mismo intervalo:

$$I = L_{RS} - L_{RI}$$


* **Punto Medio o Marca de Clase ($X_i$):** Es la puntuación central que representa matemáticamente a la totalidad de las observaciones contenidas dentro de ese intervalo específico. Se calcula como la semisuma de los límites del intervalo:

$$X_i = \frac{L_{RS} + L_{RI}}{2} = \frac{\text{Límite Aparente Superior} + \text{Límite Aparente Inferior}}{2}$$



#### Supuestos de la Distribución Intraintervalo (Botella et al., 2012)

Al condensar múltiples puntuaciones individuales diferentes dentro de un único intervalo común, se produce inevitablemente una pérdida de información de los valores específicos. Para poder operar aritméticamente con las tablas resultantes, la teoría estadística formal establece dos supuestos contrapuestos:

1. **Supuesto de Concentración en el Punto Medio:** Postula que todos los valores caídos dentro de un intervalo coinciden exactamente con la marca de clase ($X_i$). Es el supuesto estándar empleado por defecto para el cálculo de estadísticos descriptivos muestrales basados en tablas agrupadas (como la media aritmética).
2. **Supuesto de Distribución Uniforme (o de Continuidad):** Postula que las puntuaciones se distribuyen de manera homogénea y equidistante a lo largo de toda la extensión de la amplitud real del intervalo. Es el supuesto teórico que sustenta el cálculo de medidas de posición no central como los percentiles, cuartiles y deciles.

---

## 3. Representaciones Gráficas

Las **representaciones gráficas** son dispositivos analíticos e informáticos diseñados para sintetizar la información de las tablas de frecuencias en una figura o patrón visual geométrico. Su utilidad radica en que facilitan la identificación inmediata de la forma de la distribución, las tendencias y la variabilidad de los datos.

### 3.1. Gráfico de Torta (Pie Chart)

* **Variables de aplicación:** Variables de escala estrictamente **cualitativa (nominal)**.
* **Propiedades lógicas:** Expresa visualmente proporciones y porcentajes relativos a través de sectores circulares. El ángulo central de cada porción es directamente proporcional a la frecuencia absoluta de la categoría:

$$\text{Ángulo} = p_i \cdot 360^\circ$$


* **Interpretación:** La jerarquía o predominancia de un atributo se infiere de manera directa a partir del ancho o superficie de la porción correspondiente.

### 3.2. Gráfico de Barras (Bar Chart)

* **Variables de aplicación:** Variables **cualitativas**, **cuasi-cuantitativas (ordinales)**, o **cuantitativas discretas** que presentan pocos valores (como las puntuaciones de una escala tipo Likert de 5 puntos).
* **Construcción geométrica:** Sobre el eje de las abscisas ($X$) se disponen las categorías desglosadas. Sobre el eje de las ordenadas ($Y$) se elevan barras rectangulares cuya altura es igual a la frecuencia (absoluta o relativa) de la categoría.
* **Diferenciación conceptual según escala:** * Si la variable es cualitativa nominal, el orden de las barras en el eje $X$ es enteramente arbitrario.
* Si la variable es ordinal o cuantitativa discreta, el orden de las barras en el eje $X$ es rígido y debe respetar la jerarquía métrica de la escala. En las cuantitativas discretas, no solo importa el orden, sino también la distancia o unidad de medida que separa los puntos del eje.
* *Propiedad crítica:* Las barras se dibujan **separadas unas de otras**, reflejando la discontinuidad o naturaleza categórica de las modalidades medidas.



### 3.3. Histograma (Histogram)

* **Variables de aplicación:** Variables **cuantitativas continuas** (ej. *Tiempo de Reacción* o latencias de respuesta).
* **Construcción geométrica:** Se erige sobre los límites reales de los intervalos dispuestos en el eje horizontal ($X$). A diferencia del gráfico de barras, en el histograma los rectángulos se dibujan **completamente contiguos (pegados unos a otros)**, lo cual representa visualmente la continuidad subyacente de la variable empírica.
* **Propiedad del Área:** El área de cada rectángulo es la que representa formalmente la frecuencia de las observaciones. Cuando todos los intervalos poseen idéntica amplitud ($I$), la altura de la barra es directamente proporcional a la frecuencia.

### 3.4. Histograma + Densidad

Constituye una variante analítica avanzada donde el histograma clásico es suavizado mediante la superposición de una línea continua curva curva llamada **curva de densidad estimulada** (generalmente basada en algoritmos de suavizado por Kernel). Esta línea modela los contornos de la distribución eliminando las irregularidades de los peldaños de los intervalos, lo que permite evaluar de forma directa la similitude empírica del constructo con modelos matemáticos ideales como la curva normal.

### 3.5. Polígono de Frecuencias

Es una representación lineal que se forma uniendo mediante segmentos de recta los puntos de intersección entre las marcas de clase (eje $X$) y sus respectivas frecuencias absolutas o relativas (eje $Y$). Para "cerrar" el polígono geométrico sobre el eje horizontal, se asume la existencia de dos intervalos hipotéticos adicionales con frecuencia cero: uno al inicio y otro al final de la distribución.

### 3.6. Diagrama de Tallo y Hojas (Stem-and-Leaf Display)

Desarrollado originalmente por John Tukey, es un híbrido metodológico entre una tabla y un gráfico. Permite visualizar simultáneamente el perfil gráfico de la distribución y preservar de forma intacta los valores numéricos brutos originales de la muestra.

* **Tallo (Stem):** Formado por los dígitos principales delanteros del número (ej. las decenas). Se disponen verticalmente en una columna a la izquierda separados por una línea.
* **Hoja (Leaf):** Formada por los dígitos secundarios finales (ej. las unidades). Se disponen horizontalmente a la derecha de su respectivo tallo en orden creciente.

---

## 4. Convenciones Gráficas y Control de la Tendenciosidad

Las representaciones gráficas poseen un alto impacto cognitivo y visual, lo que las vuelve susceptibles de sufrir **manipulaciones o distorsiones intencionadas** orientadas a sobredimensionar o minimizar fenómenos empíricos.

> **Advertencia Metodológica sobre Tendenciosidad (Botella et al., 2012):** Una alteración arbitraria en la escala de los ejes puede cambiar radicalmente la percepción visual de un lector sobre la variabilidad de un fenómeno. Alargar desproporcionadamente el eje $Y$ respecto al eje $X$ genera una ilusión visual de cambios abruptos y alta dispersión, mientras que acortar el eje $Y$ disfraza las variaciones reales, haciendo que los datos parezcan estables o planos. Otra práctica espuria común es el truncamiento del eje de ordenadas (no iniciar el eje $Y$ en el valor cero real), lo cual distorsiona la proporcionalidad geométrica de las barras.

### Convenciones Estándar para Gráficos Científicos:

Para mitigar la tendenciosidad y unificar criterios, se aplican las directrices internacionales adoptadas por la APA y la teoría estadística:

* **La Regla de los Tres Cuartos (o Proporción Áurea):** La altura del eje de las ordenadas ($Y$) debe equivaler aproximadamente a tres cuartas partes ($75\%$) o a cuatro quintas partes ($80\%$) de la longitud del eje de las abscisas ($X$). Esta convención mantiene una armonía visual estandarizada.
* **Etiquetado Exhaustivo:** Todo gráfico debe portar un título explicativo autónomo, una identificación unívoca de las unidades de medida en ambos ejes y, de ser necesario, referencias sobre el origen de los datos perdidos.

---

## 5. Propiedades Fundamentales de las Distribuciones de Frecuencia

Al examinar globalmente el perfil morfológico de una distribución de frecuencias o de un histograma, la teoría estadística define cuatro propiedades o características macro que describen por completo el comportamiento de los datos:

1. **Tendencia Central:** Identifica el punto o zona de la escala métrica donde tiende a concentrarse el mayor volumen de las observaciones acumuladas (medido mediante estadísticos como la media, la mediana o el modo).
2. **Variabilidad o Dispersión:** Describe el grado de separación, distanciamiento o heterogeneidad que presentan las puntuaciones de los sujetos respecto al centro de la distribución.
3. **Asimetría o Sesgo (Skewness):** Mide el grado en que los datos se reparten equilibradamente a ambos lados del centro de la distribución.
* **Asimetría Simétrica:** Las observaciones se distribuyen de forma idéntica a la derecha e izquierda del valor central.
* **Asimetría Positiva (Sesgo a la derecha):** Las frecuencias más altas se concentran en los valores bajos de la escala, extendiéndose una "cola" longitudinal de datos hacia las puntuaciones altas.
* **Asimetría Negativa (Sesgo a la izquierda):** Las frecuencias elevadas se ubican en la zona alta de la escala, proyectándose la cola de la distribución hacia los valores inferiores.


4. **Curtosis o Apuntalamiento:** Cuantifica el grado de concentración o acumulación de observaciones en la región central de la distribución, comparándola de forma estandarizada con el modelo de la curva normal.
* **Mesocúrtica:** Distribución con un nivel de apuntalamiento idéntico al de la distribución normal estándar.
* **Leptocúrtica:** Distribución marcadamente apuntada y elevada en su centro, denotando una alta concentración de datos en la zona media.
* **Platicúrtica:** Distribución aplanada y con baja concentración central, donde las frecuencias se dispersan de forma más homogénea a lo largo de los extremos.



---

## 6. Información Complementaria: El Perfil Ortogonal

Cuando un profesional de la psicología o psicopedagogía necesita representar gráficamente y comparar de forma simultánea los resultados obtenidos por un sujeto (o un grupo) en **múltiples mediciones o test diferentes** (ej. evaluar Percepción, Memoria, Atención y Funciones Ejecutivas en un mismo reporte), se enfrenta a un obstáculo métrico: cada prueba utiliza unidades de medida y escalas de puntuación bruta distintas.

Para solucionar esto, se recurre al **perfil ortogonal**. Esta técnica exige realizar una transformación matemática lineal previa sobre la totalidad de las puntuaciones de la matriz para convertirlas a una métrica común estandarizada denominada universalmente **puntaje Z** (puntuaciones tipificadas que expresan cuántas desviaciones típicas se aleja un sujeto de la media de referencia). Una vez estandarizados los datos, se grafican los constructos uno al lado del otro en el eje horizontal y se unen mediante segmentos de recta las puntuaciones estandarizadas del individuo, permitiendo una interpretación diagnóstica de las fortalezas y debilidades relativas del paciente.

---

## 7. Bloque Práctico de Aplicación: Instrumentación en el Entorno Jamovi

Para operativizar los conceptos teóricos explicados en investigaciones reales, la práctica contemporánea recurre al software estadístico **Jamovi** (una interfaz gráfica intuitiva basada en el motor de lenguaje de programación R, de código libre y gratuito).

### 7.1. Configuración de Variables y Tipos de Datos en Jamovi

Al importar o digitalizar una matriz de datos en Jamovi, el analista debe verificar rigurosamente que el programa reconozca de manera correcta el nivel de medición asignado a cada columna. Jamovi utiliza tres etiquetas operativas principales:

* `Nominal` (representado por un icono de tres círculos de colores): Para variables cualitativas sin orden intrínseco.
* `Ordinal` (representado por un icono de barras en escalera): Para variables cuasi-cuantitativas ordenadas.
* `Continuous` (representado por una regla graduada métrica): Para variables cuantitativas (tanto discretas de amplio rango como continuas).

### 7.2. Secuencia de Ejecución para Análisis Descriptivo y Gráfico

Para generar de forma automatizada las tablas y gráficos revisados en este módulo, se ejecuta la siguiente ruta operativa dentro del entorno del software:

1. Acceder a la pestaña principal de **`Analyses`** en la barra de herramientas superior.
2. Hacer clic en el botón **`Exploration`** y seleccionar la opción **`Descriptives`**.
3. En el panel de configuración desplegado, trasladar las variables de interés desde el cuadro de lista izquierdo hacia el cuadro denominado **`Variables`**.
4. Para desglosar y separar el comportamiento de una variable según grupos o condiciones (como evaluar la depresión según el género), trasladar la variable clasificatoria al cuadro **`Split by`**.
5. Desplegar el menú inferior de **`Plots`** (Gráficos) y marcar las casillas correspondientes según la naturaleza de la variable:
* Para variables categóricas (`Nominal` o `Ordinal`), seleccionar **`Bar plot`**.
* Para variables cuantitativas (`Continuous`), seleccionar **`Histogram`** y, si se desea modelar la forma continua de la distribución, activar la opción **`Density`**.



---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 2: Organización y representación de datos). Ediciones Pirámide.
* Sarli, L. (2026). *Organización y representación de datos* (Material didáctico de la Clase 2).
* Speranza, T. B. (2026). *Organización de datos e introducción a Jamovi* (Guías de Trabajos Prácticos 1 y 2).