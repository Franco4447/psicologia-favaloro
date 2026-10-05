# Documento de Estudio Exhaustivo: Medidas de Variabilidad, Asimetría y Curtosis (Clase 4)

---

## 1. El Concepto de Variabilidad (o Dispersión)

En las ciencias del comportamiento, la descripción de un conjunto de datos resulta incompleta si únicamente se recurre a las medidas de tendencia central. Mientras que la media aritmética o la mediana sintetizan el valor típico o el "centro" de una distribución, las **medidas de variabilidad** (o dispersión) cuantifican el grado de separación, distanciamiento o heterogeneidad que presentan las observaciones entre sí o respecto a dicho valor central.

Estudiar la variabilidad permite responder a dos preguntas fundamentales en la investigación empírica: *¿Qué tanto se parecen mis datos?* y *¿Cuán diferentes son entre sí las observaciones?*

> **Advertencia Conceptual:** Dos muestras independientes pueden presentar exactamente la misma media aritmética y, sin embargo, poseer estructuras de datos radicalmente opuestas. Una media aritmética solo es matemáticamente un reflejo fiel de la realidad de una muestra cuando la variabilidad es baja; a mayor dispersión, la media pierde **representatividad** como valor típico.

Para demostrar la insuficiencia de la media por sí sola, consideremos el escenario planteado en la presentación de clase, donde se analizan las edades de tres grupos independientes de sujetos ($n$ idéntico para los tres casos):

* **Grupo 1:** Presenta una media de edad ($\bar{X}$) de $21.31\text{ años}$. Su edad mínima registrada es $18\text{ años}$ y la máxima es $25\text{ años}$. Su **varianza** es de $6.22$ y su **desviación estándar** es de $2.49$.
* **Grupo 2:** Presenta exactamente la misma media de edad ($\bar{X} = 21.31\text{ años}$), y los mismos límites absolutos (mínimo de $18$ y máximo de $25$). No obstante, su varianza es de $4.65$ y su desviación estándar es de $2.15$.
* **Grupo 3:** Comparte la misma media aritmética ($\bar{X} = 21.31\text{ años}$) y la misma edad mínima ($18\text{ años}$), pero registra una edad máxima de $51\text{ años}$. Su varianza se eleva drásticamente a $38.29$ y su desviación estándar a $6.19$.

**Interpretación Estadística:**

1. Al comparar el **Grupo 1** con el **Grupo 2**, observamos que, a pesar de compartir la media y los mismos valores extremos, el Grupo 2 posee una varianza menor ($4.65 < 6.22$). Esto demuestra que los sujetos del Grupo 2 están más concentrados o agrupados en torno a la media de $21.31$ años (mayor homogeneidad interna).
2. El **Grupo 3** ejemplifica el impacto desproporcionado de los **valores atípicos** (el sujeto de 51 años). La presencia de una sola puntuación extrema no compensada desplaza la variabilidad hacia arriba de manera exponencial ($S^2 = 38.29$), advirtiendo al investigador que en este grupo la media aritmética de $21.31$ es un descriptor deficiente y poco representativo de la muestra global.

---

## 2. Índices de Variabilidad Absoluta

Las medidas de variabilidad absoluta expresan la dispersión en las mismas unidades de medida en las que ha sido registrada la variable original (o en sus cuadrados). Se aplican de forma estricta sobre variables cuantitativas.

### 2.1. Amplitud Total o Rango ($A_T$)

Se define formalmente como la distancia métrica existente entre las dos puntuaciones extremas de la distribución de observaciones.

* **Fórmula:**

$$A_T = X_{\text{máx}} - X_{\text{mín}}$$


* **Desventaja Metodológica:** Es un índice altamente inestable. Debido a que su cálculo depende única y exclusivamente de los dos valores más extremos de la muestra, ignora por completo la distribución y el comportamiento de la totalidad de los datos intermedios. Su valor se altera drásticamente ante la aparición fortuita de un solo valor atípico.

### 2.2. Desviación Media ($DM$)

Es el promedio aritmético de los valores absolutos de las desviaciones de cada una de las observaciones con respecto a la media aritmética de la muestra.

* **Fórmula:**

$$DM = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n}$$



> **¿Por qué se requiere el uso de valores absolutos?** Por propiedad algebraica fundamental de la media, sabemos que la suma de las desviaciones directas de los datos respecto a su media siempre es igual a cero ($\sum(X_i - \bar{X}) = 0$), dado que las distancias positivas y negativas se cancelan mutuamente de forma perfecta. Para anular este efecto y poder cuantificar la distancia real media, la estadística recurre a dos soluciones: tomar el valor absoluto (lo que da origen a la Desviación Media) o elevar las desviaciones al cuadrado (lo que da origen a la Varianza).

### 2.3. Varianza ($S^2$)

Se define formalmente como el promedio de los cuadrados de las desviaciones de todas las observaciones de la muestra con respecto a su media aritmética.

* **Fórmula para datos brutos:**

$$S^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n}$$


* **Propiedades lógicas:** Al elevar las diferencias al cuadrado, se penalizan con mayor fuerza matemática aquellas puntuaciones que se distancian excesivamente de la media aritmética.
* **Limitación Métrica:** Debido a la elevación al cuadrado de las desviaciones, la unidad de medida final de la varianza queda expresada en términos cuadráticos (por ejemplo, si medimos la edad en "años", la varianza se expresará en "años al cuadrado"), lo cual carece de una interpretación clínica o intuitiva directa.

### 2.4. Desviación Típica o Estándar ($S$ o $DE$)

Es la raíz cuadrada positiva de la varianza. Se introduce metodológicamente para subsanar la distorsión métrica de las unidades cuadráticas de la varianza.

* **Fórmula:**

$$S = \sqrt{S^2} = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n}}$$


* **Utilidad:** Al aplicar la raíz cuadrada, la métrica de la dispersión retorna exactamente a la **unidad de medida original** de la variable (ej. años, puntos psicométricos, milisegundos), convirtiéndose en el estadístico de dispersión más utilizado para acompañar a la media aritmética en los reportes científicos.

---

## 3. Índices de Variabilidad Relativa

Cuando un investigador necesita comparar la dispersión de dos muestras cuyas variables han sido medidas en unidades completamente diferentes (por ejemplo, comparar la variabilidad del Peso en kilogramos frente a la Inteligencia en puntos de CI), o cuando las variables comparten la misma unidad pero sus **medias aritméticas son marcadamente diferentes**, las medidas de variabilidad absoluta pierden validez comparativa. En estos casos, es obligatorio recurrir a medidas de variabilidad relativa.

### 3.1. Coeficiente de Variación ($CV$)

Es una medida de dispersión relativa que expresa la magnitud de la desviación típica como un porcentaje directo de la media aritmética de la distribución.

* **Fórmula:**

$$CV = \frac{S}{|\bar{X}|} \cdot 100$$


* **Interpretación:** El $CV$ opera directamente como un **índice de representatividad de la media**. Cuanto más alto es el porcentaje del $CV$, mayor es la heterogeneidad interna de la muestra y, por ende, menos representativa resulta la media aritmética calculada.
* **Supuesto Metodológico Crítico:** El cálculo y la interpretación del Coeficiente de Variación exigen de forma obligatoria que la variable bajo análisis esté medida, como mínimo, en una **escala de razón** (donde el cero es absoluto y denota ausencia total de la característica). Si se aplica sobre escalas intervalares con ceros arbitrarios (como la temperatura en grados Celsius o puntuaciones de pruebas psicométricas donde obtener cero no implica "cero inteligencia"), el valor del $CV$ carece de validez lógica y matemática.

---

## 4. Variabilidad en Variables Cualitativas

Las medidas de dispersión tradicionales ($S^2$, $S$, $CV$) asumen propiedades métricas cuantitativas que no existen en los niveles de medición nominal u ordinal. Para resolver la necesidad de cuantificar la variabilidad en categorías puramente cualitativas (por ejemplo, la diversidad de diagnósticos clínicos en una muestra de pacientes o las orientaciones vocacionales en una escuela), se introduce la noción de entropía.

### 4.1. Entropía ($H$)

La **entropía** es un índice estadístico que mide el grado de incertidumbre, diversidad o dispersión cualitativa presente en una distribución de frecuencias categórica.

* **Propiedades lógicas:** * **Entropía Mínima ($H = 0$):** Se alcanza cuando existe una homogeneidad absoluta en los datos. Esto ocurre cuando el $100\%$ de las observaciones de la muestra caen dentro de una **única categoría** cualitativa (incertidumbre nula).
* **Entropía Máxima:** Se alcanza cuando la muestra exhibe la máxima heterogeneidad posible. Esto sucede cuando las observaciones se distribuyen de manera perfectamente **uniforme o equitativa** entre todas las categorías disponibles, lo que significa que las probabilidades de pertenecer a una categoría u otra son exactamente iguales.



---

## 5. Medidas de Distribución y Forma

Una vez que el analista dispone de información precisa sobre la tendencia central y la variabilidad de sus observaciones, el siguiente paso metodológico consiste en evaluar la estructura global de la distribución. Las **medidas de forma** determinan si los datos se reparten de manera equilibrada y cómo se posicionan en comparación con un modelo matemático de referencia ideal: la distribución normal.

### 5.1. El Modelo de la Distribución Normal (Gaussiana)

De acuerdo con las pautas fijadas en los módulos prácticos, la **distribución normal** constituye el marco de referencia por excelencia para el análisis de variables continuas en psicología. Sus propiedades teóricas determinantes son:

* **Simetría:** Es perfectamente simétrica respecto a su eje central.
* **Morfología:** Adopta una configuración en forma de campana (campana de Gauss).
* **Coincidencia Central:** En una distribución normal pura, la media aritmética, la mediana y la moda coinciden exactamente en el mismo punto del eje horizontal.
* **Comportamiento de las Frecuencias:** La mayor densidad de las observaciones se concentra en las inmediaciones directas del valor medio, y las frecuencias decrecen de manera progresiva y asintótica a medida que nos distanciamos de dicho centro hacia los extremos (colas).

---

## 6. Asimetría o Sesgo (Skewness)

La **asimetría** es el grado en que los datos de una muestra se distribuyen de forma equilibrada por encima y por debajo de la tendencia central. El índice estadístico estandarizado se denota formalmente como $As$.

### 6.1. Tipos de Asimetría y Relaciones de Tendencia Central

#### 6.1.1. Simetría ($As = 0$)

Las observaciones de la muestra se reparten de manera idéntica a la derecha y a la izquierda del valor central.

* *Relación matemática:*

$$\text{Media} = \text{Mediana} = \text{Moda}$$



#### 6.1.2. Asimetría Positiva o Sesgo a la Derecha ($As > 0$)

Ocurre cuando las frecuencias más altas de la variable se concentran marcadamente en los **valores bajos** de la escala, proyectándose una "cola" longitudinal de datos rezagados hacia las puntuaciones elevadas de la derecha.

* *Relación matemática de orden:*

$$\text{Moda} < \text{Mediana} < \text{Media}$$



> **Analogía Teórica de Botella (Examen Difícil):** Imaginemos la aplicación de un examen de estadística con un nivel de complejidad extremadamente alto. El resultado empírico natural será una acumulación masiva de alumnos reprobados con calificaciones muy bajas (concentración de frecuencias al inicio de la escala) y solo unos pocos estudiantes destacados que logran notas altas. La representación gráfica de este fenómeno exhibirá una marcada asimetría positiva.

#### 6.1.3. Asimetría Negativa o Sesgo a la Izquierda ($As < 0$)

Se presenta cuando las frecuencias más elevadas se agrupan en la **zona alta de la escala**, extendiéndose la cola de la distribución hacia las puntuaciones inferiores de la izquierda.

* *Relación matemática de orden:*

$$\text{Media} < \text{Mediana} < \text{Moda}$$



> **Analogía Teórica de Botella (Examen Fácil):** Consideremos ahora el escenario opuesto: un examen excesivamente sencillo donde imperan los aprobados con notas sobresalientes y los exámenes perfectos. La gran mayoría de los datos se concentrará en el extremo superior de la escala de notas, mientras que unos pocos alumnos con rendimientos inusuales formarán una cola delgada orientada hacia las calificaciones bajas. Este perfil morfológico corresponde a una asimetría negativa.

---

## 7. Curtosis o Apuntalamiento (Kurtosis)

La **curtosis** es un indicador estadístico que cuantifica el grado de concentración o acumulación de observaciones en la región central de la curva, evaluando qué tan plana o "picuda" es la distribución en comparación con una distribución normal estándar. El índice de curtosis se denota formalmente como $Cr$.

### 7.1. Clasificación de las Distribuciones según su Curtosis

#### 7.1.1. Distribución Mesocúrtica ($Cr = 0$)

Presenta un nivel de apuntalamiento e inflexión intermedio, idéntico al perfil de la distribución normal estándar. Las observaciones se distribuyen de acuerdo con las expectativas teóricas de la campana de Gauss tradicional.

#### 7.1.2. Distribución Leptocúrtica ($Cr > 0$)

Es una curva marcadamente **"picuda" y elevada** en su región central. Denota una altísima concentración de puntuaciones en torno a la media y colas habitualmente pesadas, lo que indica que una gran proporción de los sujetos comparten valores sumamente similares en el centro de la escala.

#### 7.1.3. Distribución Platicúrtica ($Cr < 0$)

Es una curva caracterizada por un perfil **achatado o plano**. Indica una baja concentración de observaciones en la zona central; las frecuencias se dispersan de manera más uniforme e igualitaria a lo largo de los diferentes intervalos de la escala de medición.

---

## 8. Bloque Práctico Instrumental: Operativización en Jamovi

Para llevar a la práctica el análisis de la variabilidad y las propiedades de forma de una matriz de datos en investigaciones psicológicas, se detalla a continuación la ruta de ejecución dentro del software informático **Jamovi**:

### Pasos Operativos para la Obtención de Índices de Forma y Variabilidad:

1. Abrir el programa Jamovi e importar o cargar la base de datos de trabajo (ej. `db_bienestar_adolescente`).
2. Dirigirse a la barra de pestañas superior y hacer clic en el botón de **`Analyses`**.
3. Seleccionar la opción **`Exploration`** y posteriormente hacer clic en el comando **`Descriptives`**.
4. En el panel de configuración que se despliega a la izquierda, trasladar la variable cuantitativa continua objeto de estudio (ej. `depresion_PHQ_puntaje`) hacia el cuadro rotulado como **`Variables`**.
5. Desplegar el submenú denominado **`Statistics`** haciendo clic sobre su flecha correspondiente.
6. Dentro del apartado de estadísticas de dispersión, tildar de forma obligatoria las casillas:
* `Variance` (Varianza)
* `Std. deviation` (Desviación estándar)
* `Range` (Amplitud o rango)


7. Localizar dentro del mismo panel la subsección denominada **`Distribution`** y activar activamente las opciones:
* `Skewness` (para calcular el índice de asimetría $As$)
* `Kurtosis` (para calcular el índice de apuntalamiento $Cr$)


8. *Visualización Gráfica Complementaria:* Desplegar el menú inferior de **`Plots`** y activar simultáneamente las casillas **`Histogram`** y **`Density`** para superponer la curva continua suavizada sobre los intervalos reales de la muestra, permitiendo una inspección visual directa de la asimetría y curtosis calculadas numéricamente.

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 4: Medidas de posición y dispersión; Capítulo 7: Medidas de asimetría y curtosis). Ediciones Pirámide.
* Sarli, L. (2026). *Variabilidad y medidas de distribución* (Material didáctico de la Clase 4).
* Speranza, T. B. (2026). *Medidas de variabilidad y formas de la distribución* (Guía de Trabajos Prácticos 4).