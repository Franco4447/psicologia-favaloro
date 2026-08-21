# Documento de Estudio Exhaustivo: Asociación y Correlación entre Variables (Clase 6)

---

## 1. Introducción al Estudio de la Relación entre Variables

Uno de los objetivos principales de la psicología y la psicopedagogía es descubrir cómo se relacionan los fenómenos del comportamiento y los procesos cognitivos. En el ámbito empírico, los investigadores constantemente se preguntan si el rendimiento académico guarda relación con las horas de sueño, si los estados depresivos están asociados con determinados estilos de vida, o si el nivel de ansiedad influye de forma directa en los errores cometidos en una prueba atencional.

A diferencia de las ciencias físicas, donde las relaciones entre variables suelen ser de carácter determinista (funciones exactas e ideales), en las ciencias del comportamiento imperan las regularidades estadísticas. Las observaciones manifiestan una configuración irregular debido a la presencia de múltiples factores incontrolables. Por lo tanto, no se buscan leyes matemáticas rígidas, sino la identificación de patrones de **covariación**, es decir, la tendencia a que los cambios en una variable se correspondan de forma sistemática con los cambios en otra.

---

## 2. La Covarianza como Medida de Co-variación Absoluta

Antes de abordar los coeficientes de correlación estandarizados, es metodológicamente necesario comprender la naturaleza de la **covarianza** ($S_{xy}$), que constituye el pilar estadístico de las medidas de asociación lineal.

### 2.1. Definición Formal y Fórmula Matemática

La covarianza es el promedio aritmético de los productos de las desviaciones de dos variables cuantitativas respecto a sus correspondientes medias aritméticas. Expresa el grado en que dos variables varían conjuntamente.

La fórmula de cálculo muestral se define formalmente como:


$$S_{xy} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n}$$

### 2.2. Interpretación de su Signo

El resultado numérico de la covarianza puede adoptar tres perfiles lógicos según la dirección de la relación:

* **$S_{xy} > 0$ (Covarianza Positiva):** Indica una relación directa entre las variables. Los sujetos que puntúan por encima de la media en la variable $X$ tienden también a puntuar por encima de la media en la variable $Y$ (y viceversa).
* **$S_{xy} < 0$ (Covarianza Negativa):** Indica una relación inversa. Los sujetos con puntuaciones elevadas en la variable $X$ tienden a presentar puntuaciones bajas en la variable $Y$.
* **$S_{xy} = 0$ (Covarianza Nula):** Indica la ausencia completa de una relación lineal entre ambas variables.

### 2.3. Limitación Métrica de la Covarianza

A pesar de su utilidad analítica para identificar la dirección de un patrón, la covarianza posee una grave deficiencia: es una medida de variabilidad absoluta y, por lo tanto, **su valor depende enteramente de las unidades de medida** en las que estén expresadas las variables originales.

Si modificamos la unidad de medida de una variable (por ejemplo, pasamos de medir la estatura en metros a medirla en centímetros), el valor numérico de la covarianza se alterará drásticamente, aunque la relación empírica entre los sujetos permanezca inalterada. Esta inestabilidad métrica impide utilizar la covarianza para cuantificar la *fuerza* o intensidad de la asociación.

---

## 3. Coeficiente de Correlación de Pearson ($r$)

Para solucionar la limitación de la covarianza, Karl Pearson desarrolló un índice estandarizado diseñado específicamente para evaluar la intensidad y dirección de la **correlación lineal** entre dos variables cuantitativas.

### 3.1. Definición Formal y Fórmula Matemática

El **coeficiente de correlación de Pearson** ($r_{xy}$) se define formalmente como la covarianza de dos variables dividida por el producto de sus respectivas desviaciones típicas. De este modo, se eliminan las unidades de medida originales y se obtiene una métrica adimensional pura.

$$r_{xy} = \frac{S_{xy}}{S_x \cdot S_y}$$

Sustituyendo la covarianza por su definición, la fórmula desarrollada se expresa como:


$$r_{xy} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2} \cdot \sqrt{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}}$$

### 3.2. Propiedades e Interpretación del Coeficiente de Pearson

Cualquier cálculo del coeficiente de Pearson satisface rigurosamente las siguientes propiedades algebraicas y lógicas:

* **Rango Rígido de Variación:** El valor de $r$ oscila de forma estricta dentro del intervalo cerrado de menos uno a uno:

$$-1 \le r_{xy} \le 1$$


* **Signo y Dirección:** El signo del coeficiente hereda directamente el sentido de la covarianza:
* **$r = +1$:** Expresa una **relación directamente proporcional** perfecta. Todos los puntos de la distribución se alinean de manera exacta sobre una línea recta con pendiente positiva.
* **$r = -1$:** Expresa una **relación inversamente proporcional** perfecta. Los datos se alinean milimétricamente sobre una recta con pendiente negativa.
* **$r = 0$:** Indica la ausencia total de correlación lineal.


* **Invarianza ante Transformaciones Lineales:** Si sometemos a las variables originales a transformaciones lineales positivas (por ejemplo, cambiar la escala de metros a pies o de kilogramos a libras), el valor numérico de $r_{xy}$ permanece completamente inalterado. Esto se debe a que las constantes de escala se cancelan mutuamente de forma perfecta en el numerador y el denominador.
* **Fuerza o Intensidad de la Asociación:** Siguiendo las directrices estandarizadas fijadas en los módulos prácticos, la magnitud absoluta de $r$ se interpreta bajo los siguientes umbrales:
* $0.1 < |r| < 0.3 \longrightarrow$ Correlación débil o pequeña.
* $0.3 < |r| < 0.5 \longrightarrow$ Correlación moderada.
* $|r| > 0.5 \longrightarrow$ Correlación fuerte o elevada.



### 3.3. Supuestos Teóricos Críticos para el Uso de Pearson

Para que la interpretación del coeficiente de Pearson sea metodológicamente válida, la matriz de datos debe satisfacer de forma simultánea cuatro condiciones estrictas:

1. **Nivel de Medición:** Ambas variables deben ser de naturaleza cuantitativa (escalas de intervalo o de razón).
2. **Relación Lineal:** La relación entre las variables debe ser lineal. Si la covariación subyacente adopta una morfología curvilínea o cuadrática, el coeficiente de Pearson fallará por completo, arrojando valores cercanos a cero a pesar de que exista una dependencia estrecha entre los fenómenos.
3. **Normalidad Bivariada:** Las observaciones deben proceder de una población con una distribución aproximadamente normal.
4. **Homocedasticidad:** La varianza de los residuos o puntuaciones de la variable $Y$ debe mantenerse constante y uniforme a lo largo de todos los valores potenciales de la variable $X$.

> **Advertencia Metodológica Fundamental:** El coeficiente de Pearson mide única y exclusivamente la relación lineal entre variables. Un valor de $r = 0$ no implica en absoluto que las variables sean independientes; únicamente certifica que no están vinculadas de forma lineal. Las variables podrían presentar una relación perfecta de tipo no lineal (curvilínea) que el coeficiente de Pearson es incapaz de capturar.

Un ejemplo clásico de este fenómeno en psicología experimental se presenta al analizar la relación entre el **nivel de activación fisiológica o estrés** (*Arousal*) y el **rendimiento cognitivo** en una tarea compleja (Valencia).

Si un investigador aplica el coeficiente de Pearson sobre estas variables, el programa informático arrojará un valor de $r \approx 0$. Un analista descuidado concluiría erróneamente que la activación no influye en la ejecución. Sin embargo, al inspeccionar el diagrama de dispersión, se constata una relación no lineal perfecta en forma de "U invertida": niveles excesivamente bajos de activación causan apatía y bajo rendimiento; a medida que la activación sube, el rendimiento alcanza su punto óptimo; pero si la activación continúa incrementándose hacia niveles de ansiedad extrema, el rendimiento colapsa. Al ser una función cuadrática y no una **relación lineal**, el estadístico de Pearson es metodológicamente inadecuado para este diseño.

---

## 4. Coeficiente de Correlación de Spearman ($\rho$ o $r_s$)

Cuando los supuestos teóricos de Pearson se ven vulnerados —especialmente la linealidad o el nivel de medición cuantitativo—, la estadística no paramétrica provee alternativas robustas basadas en el orden posicional de los datos.

### 4.1. Relaciones Monotónicas y Variables Ordinales

El **coeficiente de correlación de Spearman** se introduce específicamente para evaluar **relaciones monotónicas** entre dos variables. Una función monotónica es aquella donde las variables varían conjuntamente en una dirección constante (ambas aumentan o una aumenta mientras la otra disminuye), pero sin la restricción de que dicho cambio deba ser estrictamente lineal o seguir una tasa proporcional constante.

### 4.2. Condiciones de Aplicación

El uso de Spearman pasa a ser obligatorio bajo las siguientes circunstancias metodológicas:

* Al menos una de las dos variables bajo análisis posee un nivel de medición estrictamente **ordinal** (cuasi-cuantitativa, como los rangos jerárquicos o las escalas tipo Likert de percepción).
* Las variables son cuantitativas pero el diagrama de dispersión revela que la relación no es lineal, sino monotónica (curvilínea creciente o decreciente uniforme).
* Los datos violan flagrantemente el supuesto de normalidad o presentan valores atípicos severos. Spearman sortea esta limitación transformando las puntuaciones directas en rangos ordenados, neutralizando así el impacto desproporcionado de las distancias extremas. Su rango operativo e interpretación de fuerza y signo coinciden de forma exacta con los parámetros de Pearson (de -1 a 1).

---

## 5. Prueba de Chi-cuadrado ($\chi^2$) de Independencia

Cuando los fenómenos bajo estudio no presentan propiedades métricas cuantitativas ni de orden, sino que consisten en clasificaciones categóricas puras, el análisis de la asociación lineal pierde validez lógica. Para evaluar la relación entre dos variables cualitativas nominales, se recurre a la **prueba de chi-cuadrado** de independencia.

### 5.1. Lógica de las Frecuencias Observadas vs. Esperadas

La prueba de chi-cuadrado opera cruzando los datos de las dos variables categóricas en una cuadrícula bidimensional denominada **tabla de contingencia** o tabla de doble entrada. El procedimiento matemático contrasta de forma directa dos entidades:

* **Frecuencias Observadas ($f_O$ o $n_{ij}$):** Son las frecuencias reales de sujetos contabilizadas por el investigador en cada una de las casillas de la tabla de contingencia.
* **Frecuencias Esperadas ($f_E$ o $E_{ij}$):** Son las frecuencias teóricas de sujetos que *deberían registrarse* en cada casilla si las dos variables bajo estudio fueran absoluta y perfectamente independientes entre sí. Se calculan multiplicando los totales marginales de la fila y la columna correspondiente y dividiendo dicho producto por el tamaño total de la muestra ($n$).

### 5.2. Formulación de Hipótesis y Algoritmo Matemático

La prueba contrasta estadísticamente el siguiente par de hipótesis rivales:

* **Hipótesis Nula ($H_0$):** Las dos variables categóricas son independientes. No existe asociación alguna entre ellas en la población de origen.
* **Hipótesis Alternativa ($H_1$):** Las dos variables no son independientes; se encuentran asociadas de forma sistemática.

El estadístico de contraste se calcula formalmente mediante la sumatoria estandarizada de las distancias al cuadrado entre lo observado y lo esperado para la totalidad de las casillas de la tabla:


$$\chi^2 = \sum \frac{(f_O - f_E)^2}{f_E}$$

* **Criterio de Decisión:** Si las diferencias entre las frecuencias observadas y las esperadas por el azar son pequeñas, el valor de $\chi^2$ será cercano a cero, aportando evidencia a favor de la **independencia** ($H_0$). Por el contrario, si se registran discrepancias severas y sistemáticas entre las casillas reales y las teóricas, el valor de $\chi^2$ se inflará significativamente, guiando al investigador a rechazar la hipótesis nula y concluir que las variables están asociadas.

---

## 6. Control de la Interpretación: Correlación no implica Causalidad

> **Regla de Oro Epistemológica:** El hallazgo de un coeficiente de correlación elevado ($r$ o $\rho$ altos) o de una asociación significativa por chi-cuadrado jamás faculta al investigador para establecer una relación de causa y efecto entre las variables analizadas. **La correlación no implica causalidad**.

El coeficiente de correlación es una medida puramente matemática y ciega de co-variación simétrica; no posee la capacidad de dictaminar la dirección de una flecha causal. Cuando dos variables muestran un patrón de asociación estrecho, dicho comportamiento puede responder a tres explicaciones alternativas:

1. Que la variable $X$ sea la causa real de la variable $Y$.
2. Que la variable $Y$ sea la causa de la variable $X$ (causalidad inversa).
3. **El problema de la tercera variable (Relación Espuria):** Que ambas variables sigan un patrón de covariación idéntico debido únicamente a la influencia oculta de una tercera variable (variable de confusión o antecedente) que actúa como la causa común simultánea de ambas.

Imaginemos un estudio sociológico que recolecta datos a nivel nacional y halla una fuerte correlación lineal positiva entre el número de infracciones de tránsito cometidas por los ciudadanos y la gravedad de los accidentes vehiculares que sufren. Un analista ingenuo podría postular una causalidad directa e intervenir únicamente sancionando administrativamente las infracciones menores bajo el supuesto de que eso erradicará los accidentes graves.

Sin embargo, el análisis metodológico profundo revela que estamos ante una relación marcadamente espuria. Existe una tercera variable antecedente no medida en la correlación simple: el **consumo crónico de alcohol al volante**. El consumo de alcohol es la causa real que incrementa de forma independiente tanto la propensión a cometer infracciones viales como la vulnerabilidad a sufrir colisiones severas. Eliminar las infracciones sin desactivar la tercera variable común dejará la tasa de accidentes completamente intacta, demostrando el peligro de confundir correlación con causalidad.

---

## 7. Guía de Selección de Coeficientes e Implementación en Jamovi

Para operativizar estos conceptos en diseños de investigación reales, la Lic. Trinidad B. Speranza fija los criterios de selección de pruebas según la escala métrica de los datos y detalla su ejecución informática en el software **Jamovi**.

### 7.1. Cuadro de Decisión Metodológica

Para determinar con exactitud qué prueba estadística se debe activar, el analista debe identificar la naturaleza de la intersección de sus dos variables de interés:

| Variable 1 | Variable 2 | Prueba Estadística de Elección | Indicador Clave en Jamovi |
| --- | --- | --- | --- |
| **Cuantitativa** | **Cuantitativa** *(y cumple supuestos)* | Coeficiente de Correlación de **Pearson** | Valor $r$ y Signo ($+$ o $-$) |
| **Cuantitativa** | **Cuantitativa** *(no lineal / asimétrica)* | Coeficiente de Correlación de **Spearman** | Valor $\rho$ o $r_s$ y Signo |
| **Ordinal** | **Ordinal** o **Cuantitativa** | Coeficiente de Correlación de **Spearman** | Valor $\rho$ o $r_s$ y Signo |
| **Categoría / Nominal** | **Categoría / Nominal** | Prueba de **Chi-cuadrado** ($\chi^2$) de Independencia | Valor $\chi^2$ y Tabla de Contingencia |

### 7.2. Interpretación Unificada del P-valor (Significancia)

Independientemente de si se ejecuta Pearson, Spearman o Chi-cuadrado, el criterio probabilístico para dictaminar si la asociación hallada en la muestra es real o producto del mero azar muestral se rige de forma estricta por el **p-valor** (denotado como `p` en los reportes de Jamovi):

* **`p <= 0.05`:** El resultado es estadísticamente significativo. Se rechaza la hipótesis de independencia ($H_0$), confirmando que las variables están asociadas en la población de origen con un margen de confianza del $95\%$.
* **`p > 0.05`:** El resultado no es significativo. No se puede descartar que la asociación observada se deba al azar; por lo tanto, se asume la independencia de las variables.

### 7.3. Rutas Operativas en el Entorno Jamovi

#### Para Coeficientes de Pearson y Spearman (Variables Cuantitativas u Ordinales):

1. Ingresar a Jamovi y cargar la base de datos de trabajo.
2. Hacer clic en la pestaña superior de **`Analyses`** y pulsar el botón **`Regression`**.
3. Dentro del menú desplegable, seleccionar la opción **`Correlation Matrix`**.
4. Trasladar simultáneamente las variables bajo estudio hacia el cuadro de la derecha rotulado como **`Variables`**.
5. En el panel de opciones inferior denominado **`Correlation Coefficients`**, marcar de forma estratégica las casillas según el diseño: `Pearson` o `Spearman`.
6. *Inspección Visual Obligatoria:* Dentro del apartado **`Plots`**, activar la casilla **`Correlation matrix`** para generar de forma automatizada un diagrama de dispersión que permita verificar visualmente la linealidad de los datos.

#### Para la Prueba de Chi-cuadrado (Variables Categoríales Nominales):

1. Dirigirse a la pestaña de **`Analyses`** y pulsar el botón **`Frequencies`**.
2. Dentro de las opciones desplegadas, seleccionar **`Contingency Tables`** $\rightarrow$ **`Independent Samples`**.
3. Asignar una de las variables categóricas (ej. `Género`) al cuadro de **`Rows`** (Filas) y la otra variable categórica (ej. `Tipo de Diagnóstico`) al cuadro de **`Columns`** (Columnas).
4. Desplegar el panel inferior denominado **`Statistics`** y verificar que la casilla **`Chi-squared`** se encuentre activada por defecto.
5. Desplegar el panel de **`Cells`** y activar la casilla **`Expected`** dentro del apartado de frecuencias para permitir que el programa visualice y compare de forma directa las frecuencias observadas frente a las esperadas teóricas en la tabla de contingencia de resultados.

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 5: Correlación lineal). Ediciones Pirámide.
* Sarli, L. (2026). *Asociación entre variables: Covarianza y Correlación de Pearson* (Material didáctico de la Clase 6). Universidad Favaloro.
* Speranza, T. B. (2026). *Asociación entre variables cuantitativas y categoriales en Jamovi* (Guía de Trabajo Práctico 6).