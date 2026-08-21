# Documento de Estudio Exhaustivo: Medidas de Posición y Tendencia Central (Clase 3)

---

## 1. Introducción a las Medidas de Posición

En el análisis de datos aplicado a la psicología y la psicopedagogía, la descripción de una variable no se agota con la organización de las tablas de frecuencia o sus representaciones gráficas. Cuando evaluamos a un individuo en un entorno clínico, educativo u organizacional, surge inmediatamente la necesidad metodológica de determinar la situación, estatus o ubicación de su puntuación particular con respecto al grupo normativo de referencia.

Para ilustrar esta necesidad, consideremos el siguiente interrogante práctico:

> **Problema de Aplicación:** ¿Cómo podría un psicopedagogo o un pediatra establecer si un recién nacido presenta un peso adecuado, elevado o bajo?

Una puntuación bruta aislada (por ejemplo, un peso de $2.500\text{ gramos}$ o una puntuación de $45$ en una escala de ansiedad) carece por completo de significado descriptivo intrínseco. Para dotarla de sentido, debemos transformar u ordenar dicha puntuación dentro de una distribución de observaciones de un grupo de control (como las tablas de crecimiento estandarizadas del Hospital Garrahan). Las herramientas estadísticas diseñadas específicamente para cumplir este propósito reciben el nombre formal de **medidas de posición** o **cuantiles**.

---

## 2. Cuantiles

Los **cuantiles** son índices o puntos métricos calculados a lo largo de la escala de medida de una variable cuantitativa (o cuasi-cuantitativa) que dividen a la distribución de observaciones, previamente ordenada de menor a mayor, en un número determinado de intervalos que contienen exactamente la misma proporción de frecuencias.

Dependiendo del número de partes iguales en las que se fragmente la distribución, los cuantiles adoptan diferentes denominaciones formalizadas:

### 2.1. Centiles o Percentiles ($C_k$ o $P_k$)

Son los 99 valores de la variable que dividen a la distribución ordenada de observaciones en 100 partes métricamente iguales, donde cada intervalo concentra exactamente el $1\%$ de los datos.

* *Definición Formal:* El percentil $k$ ($P_k$) es aquella puntuación de la escala que es superada por el $(100 - k)\%$ de las observaciones de la muestra y deja por debajo de sí al $k\%$ de las mismas.
* *Rango operativo:* El subíndice $k$ adopta valores enteros en el intervalo $[1, 99]$. Por ejemplo, el percentil 25 ($P_{25}$) es el valor de la variable que deja por debajo de sí al $25\%$ de los sujetos de la muestra y es superado por el $75\%$ restante.

### 2.2. Deciles ($D_k$)

Son los 9 puntos métricos que dividen a la distribución ordenada en 10 partes iguales, conteniendo cada intervalo el $10\%$ de las observaciones totales.

* *Rango operativo:* El subíndice $k$ se desplaza en el intervalo entero $[1, 9]$.
* *Equivalencia:* Existe una correspondencia matemática directa entre los deciles y los percentiles de orden cero:

$$D_1 = P_{10}; \quad D_2 = P_{20}; \quad \dots \quad D_9 = P_{90}$$



### 2.3. Cuartiles ($Q_k$)

Son los 3 valores de la variable que dividen a la distribución en 4 partes exactamente iguales, acumulando cada tramo el $25\%$ de las observaciones de la muestra.

* *Rango operativo:* El subíndice $k$ adopta valores en el conjunto $\{1, 2, 3\}$.
* *Equivalencias y correspondencias:*
* **Primer Cuartil ($Q_1$):** Deja por debajo de sí al $25\%$ de las observaciones. Equivale al percentil 25 ($P_{25}$).
* **Segundo Cuartil ($Q_2$):** Deja por debajo de sí al $50\%$ de las observaciones. Equivale al decil 5 ($D_5$) y al percentil 50 ($P_{50}$). Como se desarrollará más adelante, este punto coincide exactamente con la **mediana**.
* **Tercer Cuartil ($Q_3$):** Deja por debajo de sí al $75\%$ de las observaciones. Equivale al percentil 75 ($P_{75}$).



---

## 3. Rango Percentilar

Es fundamental no confundir conceptualmente el término *percentil* con el término **rango percentilar**, dado que representan operaciones matemáticas inversas:

* Mientras que el **percentil** ($P_k$) es una *puntuación de la escala original* (un valor de $X$) asociado a un porcentaje acumulado prefijado $k$, el **rango percentilar** es el *porcentaje acumulado de datos* (un valor entre 0 y 100) que se encuentra por debajo de una puntuación bruta concreta dada ($X_i$).

> **Advertencia de Interpretación:** Al redactar un informe psicométrico o clínico, se debe evitar el error común de afirmar que un sujeto "obtuvo un percentil de 85 puntos". Lo correcto es reportar que "el sujeto obtuvo una puntuación directa cuyo rango percentilar es 85, lo que indica que sus capacidades se sitúan por encima del 85% de la población de referencia".

### 3.1. Supuestos Teóricos para el Cálculo de Cuantiles en Datos Agrupados

Cuando los datos se encuentran organizados en tablas de intervalos de clase, el cálculo exacto de un percentil o de un rango percentilar no puede realizarse por mero conteo de frecuencias discretas. En este escenario, la teoría estadística formal exige aplicar el **supuesto de distribución uniforme intraintervalo** (o supuesto de continuidad). Este principio postula que las observaciones contenidas dentro de un intervalo no se concentran en su punto medio, sino que se distribuyen de manera perfectamente homogénea, equidistante y continua a lo largo de toda la extensión de la amplitud real del intervalo ($I$).

Bajo este supuesto, el cálculo de cualquier cuantil se ejecuta mediante un proceso de **interpolación lineal**, localizando primero el intervalo crítico que contiene la frecuencia acumulada buscada y aplicando la estructura geométrica de proporcionalidad.

---

## 4. Representación Gráfica: El Diagrama de Caja (Boxplot)

El **diagrama de caja** (diseñado originalmente por John Tukey) constituye la síntesis gráfica por excelencia de las medidas de posición no centrales. Es un dispositivo analítico e informático bidimensional altamente eficiente para realizar la inspección visual de variables cuantitativas continuas.

### 4.1. Componentes Geométricos del Boxplot

Un diagrama de caja se construye formalmente a partir de cinco estadísticos descriptivos clave de la muestra:

* **La Caja Central:** Los límites inferior y superior de la caja rectangular están dictados de forma rígida por los valores del primer cuartil ($Q_1$) y del tercer cuartil ($Q_3$), respectivamente. Por lo tanto, la extensión total de la caja encierra de forma compacta al $50\%$ central de las observaciones de la muestra.
* **La Línea Interna:** Una línea recta horizontal (o vertical, según la orientación del gráfico) atraviesa el interior de la caja, señalando la posición exacta de la **mediana** ($Q_2$ o $P_{50}$).
* **El Rango Intercuartílico ($RI$ o $IQR$):** Es la distancia métrica existente entre el tercer y el primer cuartil:

$$RI = Q_3 - Q_1$$



Este índice cuantifica la magnitud de la caja y opera como una medida robusta de dispersión.
* **Los Bigotes (Whiskers):** Son líneas adyacentes que se proyectan de forma externa desde los extremos de la caja. Su extensión máxima está limitada por reglas matemáticas estrictas basadas en la dispersión interna para evitar ser arrastradas por anomalías:
* El bigote superior se extiende hasta el valor real observado más alto en la muestra que sea *menor o igual* al límite de la valla superior ($Q_3 + 1,5 \cdot RI$).
* El bigote inferior se extiende hasta el valor real observado más bajo en la muestra que sea *mayor o igual* al límite de la valla inferior ($Q_1 - 1,5 \cdot RI$).


* **Valores Atípicos (Outliers):** Cualquier observación empírica de la muestra cuyas puntuaciones brutas caigan más allá de los límites fijados por los bigotes ($> Q_3 + 1,5 \cdot RI$ o $< Q_1 - 1,5 \cdot RI$) se clasifica formalmente como un **valor atípico**. En el boxplot, estos datos no se asimilan dentro de los bigotes; se dibujan de forma aislada e individualizada mediante puntos, asteriscos o círculos, permitiendo al investigador detectar anomalías en la recolección de datos o subpoblaciones específicas.

---

## 5. Medidas de Resumen y Tendencia Central

Dentro de la estadística descriptiva, las **medidas de resumen** son índices numéricos diseñados para condensar la información de una distribución de frecuencias masiva en unos pocos valores numéricos representativos.

La primera subfamilia de estos índices son las **medidas de tendencia central**. Su objetivo prioritario es sintetizar un conjunto entero de datos mediante un único valor numérico representativo que describa el "centro", la localización o el valor típico de la distribución de observaciones. Las tres medidas de tendencia central clásicas y de uso obligatorio en las ciencias del comportamiento son la media aritmética, la mediana y la moda.

---

## 6. Media Aritmética ($\bar{X}$)

La **media aritmética** es la medida de tendencia central más utilizada y conceptualmente análoga al centro de gravedad o punto de equilibrio mecánico de un sistema de pesos físicos.

### 6.1. Definición Formal y Fórmulas

Se obtiene sumando de forma exhaustiva la totalidad de los valores numéricos observados en la variable y dividiendo dicho agregado por el tamaño total de la muestra ($n$).

* **Para datos brutos (sin tabular):**

$$\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}$$


* **Para datos organizados en tablas de frecuencias (frecuencias absolutas):**

$$\bar{X} = \frac{\sum_{i=1}^{k} X_i \cdot n_i}{n}$$



*(Donde $X_i$ representa la puntuación individual o la **marca de clase** si el intervalo está agrupado, $n_i$ es su respectiva frecuencia absoluta, y $k$ es el número de categorías o intervalos).*

### 6.2. Propiedades Algebraicas de la Media (Botella et al., 2012)

La media aritmética posee propiedades matemáticas únicas derivadas de los mínimos cuadrados que sustentan los modelos de la estadística inferencial avanzada:

#### Propiedad 1: La suma de las desviaciones es cero

La suma de las desviaciones de un conjunto de observaciones respecto a su media aritmética es formalmente igual a cero.


$$\sum_{i=1}^{n} (X_i - \bar{X}) = 0$$

Aplicando las propiedades distributivas del operador sumatorio ($\sum$):


$$\sum_{i=1}^{n} (X_i - \bar{X}) = \sum_{i=1}^{n} X_i - \sum_{i=1}^{n} \bar{X}$$


Dado que $\bar{X}$ es un valor constante para una muestra dada, la suma de una constante reproducida $n$ veces equivale a multiplicar la constante por $n$:


$$\sum_{i=1}^{n} X_i - n\bar{X}$$


Por definición, sabemos que $\bar{X} = \frac{\sum X_i}{n}$, lo que implica que $n\bar{X} = \sum X_i$. Sustituyendo este término en la ecuación:


$$\sum_{i=1}^{n} X_i - \sum_{i=1}^{n} X_i = 0 \quad \blacksquare$$

#### Propiedad 2: Propiedad de los Mínimos Cuadrados

La suma de los cuadrados de las desviaciones de los valores de una variable respecto a su media aritmética es menor que respecto a cualquier otro valor constante $a$.


$$\sum_{i=1}^{n} (X_i - \bar{X})^2 < \sum_{i=1}^{n} (X_i - a)^2 \quad (\text{para cualquier } a \neq \bar{X})$$

#### Propiedad 3: Transformaciones Lineales

Si sometemos a los valores de una variable $X$ a una transformación lineal matemática de la forma $Y_i = b \cdot X_i + a$ (donde $b$ representa una constante de multiplicación y $a$ una constante de adición), la nueva media aritmética de la variable transformada $\bar{Y}$ será exactamente igual a esa misma transformación lineal aplicada sobre la media de la variable original:


$$\bar{Y} = b \cdot \bar{X} + a$$

#### Propiedad 4: Combinación Lineal de Medias (Media Ponderada)

Si disponemos de la media aritmética de una variable calculada en múltiples grupos independientes, la media total o combinada de la muestra global ($\bar{X}_T$) es igual a la **media ponderada** de las medias de cada subgrupo, donde el factor de ponderación es el tamaño muestral ($n_j$) de cada uno.


$$\bar{X}_T = \frac{n_1 \cdot \bar{X}_1 + n_2 \cdot \bar{X}_2 + \dots + n_g \cdot \bar{X}_g}{n_1 + n_2 + \dots + n_g} = \frac{\sum_{j=1}^{g} n_j \cdot \bar{X}_j}{\sum_{j=1}^{g} n_j}$$

Un investigador en psicología laboral desea calcular una puntuación combinada de *Estrés Total* basada en dos dimensiones evaluadas de forma independiente: *Estrés Laboral* (con un peso metodológico del $70\%$, $b_1 = 0,7$) y *Estrés Personal* (con un peso del $30\%$, $b_2 = 0,3$).

* Media de Estrés Laboral ($\bar{X}_1$) = $6,0$
* Media de Estrés Personal ($\bar{X}_2$) = $4,6$

La media de la nueva variable combinada se calcula de forma directa aplicando la propiedad lineal:


$$\bar{X}_{\text{Estrés Total}} = (0,7 \cdot 6,0) + (0,3 \cdot 4,6) = 4,2 + 1,38 = 5,58$$


Este resultado demuestra que no se requiere recalcular la matriz de puntuaciones individuales de los sujetos para hallar la nueva media del constructo compuesto.

---

## 7. Mediana ($M_d$)

La **mediana** es una medida de tendencia central posicional de carácter netamente ordinal.

### 7.1. Definición y Propiedades

Se define formalmente como aquella puntuación o valor de la escala que es superado por la mitad ($50\%$) de las observaciones de la muestra, pero no por la otra mitad. Corresponde de forma unívoca al **percentil 50** ($P_{50}$) y al segundo cuartil ($Q_2$).

### 7.2. Ventaja Metodológica de la Mediana: La Robustez

A diferencia de la media aritmética, la mediana es una **medida robusta**. Esto significa que su valor es inmune y permanece inalterado ante la presencia de **valores extremos no compensados** o puntuaciones marcadamente atípicas en los extremos de la distribución. La media aritmética se ve fuertemente arrastrada y sesgada hacia la dirección de cualquier valor extremo debido a que en su fórmula interviene la magnitud cuantitativa de cada dato bruto. La mediana, al ser un índice posicional, solo atiende al número de observaciones ordenadas que se sitúan a su izquierda y a su derecha, ignorando las distancias métricas de los extremos.

---

## 8. Moda ($M_o$)

La **moda** es la medida de tendencia central más simple y la única aplicable de forma legítima sobre cualquier nivel métrico, incluyendo las variables cualitativas medidas bajo una **escala nominal**.

### 8.1. Definición y Clasificación Morfológica

Se define como aquel valor, categoría o modalidad que se presenta con la **mayor frecuencia absoluta** en el conjunto de datos recopilados. Dependiendo del perfil de la distribución de frecuencias, una muestra puede clasificarse como:

* **Unimodal:** Presenta un único valor que concentra la máxima frecuencia de la distribución.
* **Bimodal o Multimodal:** Se identifican dos o más puntuaciones sustancialmente separadas en la escala que comparten la misma frecuencia máxima.
* **Amodal:** No existe ninguna moda debido a que todos los valores de la variable registran exactamente la misma frecuencia absoluta (distribución uniforme).

---

## 9. Criterios de Elección entre Media, Mediana y Moda

La selección de la medida de tendencia central más adecuada para describir de forma fidedigna el comportamiento típico de una muestra no es una decisión arbitraria; responde a restricciones ligadas al nivel de medición de la variable y a la simetría de los datos brutos.

### 9.1. Condiciones para la Selección de la Media Aritmética

La media aritmética constituye la opción prioritaria por defecto debido a su estabilidad matemática, siempre y cuando se satisfagan de forma simultánea los siguientes supuestos teóricos:

* El nivel de medición de la variable debe ser **cuantitativo** (escalas de intervalo o de razón).
* La distribución de los datos debe ser relativamente **simétrica**, es decir, las diferencias entre las puntuaciones deben encontrarse equilibradas a ambos lados del centro, garantizando la ausencia de valores extremos o atípicos.

### 9.2. Condiciones para la Selección de la Mediana

El uso de la mediana pasa a ser obligatorio e idóneo bajo los siguientes escenarios:

* Cuando la variable cuantitativa presenta una marcada **asimetría o sesgo** producida por la existencia de valores extremos no compensados (ya que la media se encontraría distorsionada y no reflejaría el valor típico).
* Cuando el nivel de medición de la variable es estrictamente **ordinal** (cuasi-cuantitativa), escala donde carece de sentido lógico realizar sumas aritméticas pero sí es válido ordenar las posiciones relativas.

### 9.3. Condiciones para la Selección de la Moda

La moda se adopta como estadístico de elección bajo circunstancias específicas:

* Cuando el nivel de medición de la variable es de carácter **nominal** (cualitativa). En variables como "género", "profesión" o "diagnóstico clínico", es conceptualmente imposible calcular una media o una mediana; el único descriptor central legítimo es identificar la categoría mayoritaria.
* Cuando la distribución presenta intervalos abiertos en sus extremos y la mediana se encuentra incluida dentro de alguno de ellos, imposibilitando la interpolación métrica exacta de otros cuantiles.

---

## Bloque Práctico de Simulación: El Impacto de la Dispersión en los Estadísticos Descriptivos

Para consolidar la lógica matemática que rige la elección de estos estadísticos descriptivos, se expone un ejercicio analítico basado en los datos de rendimiento académico extraídos de las Guías de Trabajos Prácticos.

Un equipo psicopedagógico evalúa las calificaciones finales obtenidas en un examen de estadística por dos muestras independientes de estudiantes ($n = 5$ por grupo). Las matrices de datos brutos registran las siguientes distribuciones de notas:

* **Grupo A (Puntuaciones):** $10, \quad 3, \quad 3, \quad 4, \quad 10$
* **Grupo B (Puntuaciones):** $6, \quad 6, \quad 6, \quad 6, \quad 6$

#### 1. Análisis Analítico del Grupo A:

Para calcular la **media aritmética** de este grupo, procedemos a la sumatoria y división estandarizada:


$$\bar{X}_A = \frac{10 + 3 + 3 + 4 + 10}{5} = \frac{30}{5} = 6,0$$

Para hallar la **mediana**, ordenamos previamente las puntuaciones de forma creciente ($3, 3, 4, 10, 10$) y localizamos la posición central ($\frac{n+1}{2} = 3^\circ$ posición):


$$M_{d_A} = 4,0$$

*Interpretación Diagnóstica:* Aunque la media aritmética del Grupo A es $6,0$ (una nota de aprobación), este valor se encuentra inflado debido al impacto de las dos notas máximas ($10$), distorsionando la realidad del grupo. La mediana ($4,0$) actúa aquí como un descriptor más realista, advirtiendo que la mitad de los alumnos se encuentra por debajo de dicha nota.

#### 2. Análisis Analítico del Grupo B:

Calculamos la media aritmética y la mediana de forma directa para el Grupo B:


$$\bar{X}_B = \frac{6 + 6 + 6 + 6 + 6}{5} = \frac{30}{5} = 6,0$$

$$M_{d_B} = 6,0$$

#### 3. Conclusión Metodológica sobre la Dispersión:

Este caso demuestra una regularidad analítica crítica: **dos grupos pueden presentar exactamente la misma media aritmética ($\bar{X} = 6,0$) pero poseer estructuras internas radicalmente opuestas**. Mientras que el Grupo B exhibe una variabilidad nula (homogeneidad absoluta), el Grupo A presenta una alta dispersión y polarización.

Esto demuestra que las medidas de tendencia central son insuficientes por sí solas para describir una muestra; deben ser escoltadas obligatoriamente por **medidas de dispersión** (como el rango, la varianza y la desviación típica) para evaluar el grado de representatividad que posee la media calculada.

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 3: Medidas de tendencia central; Capítulo 4: Medidas de posición y dispersión). Ediciones Pirámide.
* Sarli, L. (2026). *Medidas de posición y medidas de resumen* (Material didáctico de la Clase 3).
* Speranza, T. B. (2026). *Estadística descriptiva y propiedades de las medidas resumidas* (Guía de Trabajos Prácticos 3).