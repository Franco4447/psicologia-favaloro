# Documento de Estudio Exhaustivo: Estadística Inferencial, Distribuciones Muestrales y Contraste de Hipótesis (Clase 8)

---

## 1. El Tránsito de la Muestra a la Población: Conceptos Fundamentales

El objetivo último de la **estadística inferencial** es la extensión y generalización de las conclusiones obtenidas a partir de una muestra hacia la **población de referencia** de la cual procede. Para comprender la estructura matemática que posibilita este salto analítico, es obligatorio diferenciar con precisión tres niveles conceptuales de entidades estadísticas:

* **Estadístico:** Es cualquier función matemática calculada sobre los valores de una **muestra de observaciones**. Al ser una propiedad muestral, su valor es inherentemente variable, ya que fluctúa de una muestra a otra debido al azar inherente a la extracción. Convencionalmente, se representa mediante letras latinas (por ejemplo, la media muestral $\bar{X}$, la desviación típica muestral $S$, o la proporción muestral $P$).
* **Parámetro:** Es una característica fija o constante que describe numéricamente a una **población de observaciones** completa. Los parámetros son valores fijos y absolutos pero generalmente desconocidos para el investigador (debido a la imposibilidad fáctica de evaluar a todo el universo poblacional). Se representan de manera unívoca mediante letras griegas (por ejemplo, la media poblacional $\mu$, la desviación típica poblacional $\sigma$, o la proporción poblacional $\pi$).
* **Estimador:** Es un estadístico muestral específico cuyos valores numéricos se consideran matemáticamente próximos al parámetro poblacional homólogo. La inferencia opera utilizando el estadístico calculado empíricamente como un estimador para aproximar el verdadero parámetro desconocido.

```
       [ PROCESO DE EXTRACTO ]                  [ PROCESO DE INFERENCIA ]
 Población de Referencia (Parámetro) --------> Muestra de Estudio (Estadístico)
        (Fijo, griego: μ, σ, π)     m.a.s.       (Variable, latino: X̄, S, P)
           ^                                                |
           |____________________(Estimador)_________________|

```

### El Muestreo Aleatorio Simple (m.a.s.)

Para que un estadístico funcione legítimamente como un estimador válido, la extracción de la muestra debe regirse estrictamente bajo el protocolo de un **muestreo aleatorio simple** (m.a.s.). Este procedimiento metodológico impone dos condiciones probabilísticas esenciales:

1. Todos los elementos de la población poseen exactamente la misma probabilidad de ser seleccionados para conformar la muestra.
2. Las extracciones de los individuos son completamente independientes entre sí; la selección de un sujeto no altera ni influye en la probabilidad de selección de los restantes.

---

## 2. Distribución Muestral de un Estadístico

Dado que un estadístico varía de una muestra a otra, si un investigador extrajera de forma sistemática e infinita todas las muestras posibles de un tamaño determinado ($n$) de una población, obtendría un conjunto masivo de valores para ese estadístico. La función de probabilidad que modela el comportamiento de esos valores teóricos recibe el nombre formal de **distribución muestral de un estadístico**.

### 2.1. El Teorema Central del Límite (TCL)

El **Teorema Central del Límite** es el pilar matemático que fundamenta la estadística inferencial bivariada y paramétrica. Establece de forma rígida las propiedades de la distribución muestral de la media aritmética ($\bar{X}$).

* **Definición Formal:** Si una muestra aleatoria procede de una población con media $\mu$ y desviación típica $\sigma$, a medida que el tamaño muestral ($n$) tiende a ser lo suficientemente grande ($n \ge 30$), la distribución muestral de la media tenderá a aproximarse de manera asintótica a una **distribución normal**, independientemente de la forma o morfología que presente la variable en la población original.

### 2.2. Propiedades de la Distribución Muestral de la Media

La distribución muestral resultante del TCL cumple con tres propiedades paramétricas estrictas:

1. **Valor Esperado:** La media de todas las medias muestrales posibles (el valor esperado de la distribución muestral, $E(\bar{X})$) es exactamente igual a la media de la población original:

$$E(\bar{X}) = \mu$$


2. **Error Estándar ($\sigma_{\bar{X}}$):** La desviación típica de la distribución muestral de la media recibe el nombre específico de **error estándar**. Cuantifica el grado de variabilidad o fluctuación que sufren las medias de las muestras por efecto del azar de muestreo. Se calcula dividiendo la desviación típica poblacional por la raíz cuadrada del tamaño de la muestra:

$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$



> **Advertencia Metodológica:** No se debe confundir la desviación típica ($S$ o $\sigma$) con el error estándar ($\sigma_{\bar{X}}$). La desviación típica mide la dispersión o heterogeneidad de las puntuaciones individuales de los sujetos dentro de una muestra. El error estándar mide la variabilidad y la falta de precisión de la media calculada como estimadora del parámetro. A medida que el tamaño de la muestra ($n$) se incrementa, el error estándar decrece de forma inversamente proporcional, lo que significa que muestras más grandes garantizan estimaciones sustancialmente más precisas y estables.

---

## 3. Fundamentos del Contraste de Hipótesis

El **contraste de hipótesis** (o prueba de hipótesis) es un proceso estructurado de decisión formal en el cual una afirmación científica o teórica sobre un parámetro poblacional es puesta en relación con la evidencia empírica de los datos muestrales para dictaminar si es compatible o no con ellos.

Todo contraste metodológico exige la formulación obligatoria de dos hipótesis estadísticas rivales, las cuales deben ser exhaustivas y mutuamente excluyentes:

### 3.1. Hipótesis Nula ($H_0$)

Es la hipótesis del *status quo*, de la ausencia de efecto, de la no diferencia o de la independencia lineal. Afirma de manera rígida que cualquier variación o diferencia observada en los datos de la muestra se debe puramente al azar de muestreo o a fluctuaciones fortuitas, y no a una causa sistemática.

> **Principio de Presunción de Veracidad:** Dentro del diseño lógico de la ciencia, la **hipótesis nula se presume inicialmente como verdadera** a lo largo de todo el desarrollo del análisis matemático. El proceso de contraste está diseñado para evaluar si la evidencia empírica acumulada en los datos es lo suficientemente fuerte como para destruir dicha presunción y forzar su rechazo.

### 3.2. Hipótesis Alternativa ($H_1$)

Es la hipótesis del investigador. Afirma que existe una diferencia real, un efecto sistemático, una relación de covariación o una dependencia significativa en la población. Se postula como la contradicción directa de $H_0$, y solo se acepta como verdadera si los datos muestrales demuestran de forma probabilística que la hipótesis nula es insostenible.

---

## 4. Matriz de Decisiones y Errores en la Inferencia

Debido a que las decisiones inferenciales se toman bajo condiciones de incertidumbre basadas en distribuciones muestrales probabilísticas, el investigador nunca alcanza una certeza absoluta. Al contrastar las hipótesis, existen cuatro escenarios lógicos posibles estructurados en una matriz de contingencia:

| Decisión del Investigador | Hipótesis Nula ($H_0$) real es **VERDADERA** | Hipótesis Nula ($H_0$) real es **FALSA** |
| --- | --- | --- |
| **Mantener / Aceptar $H_0$** | **Decisión Correcta** Probabilidad: $1 - \alpha$ | **Error Tipo II ($\beta$)** Probabilidad: $\beta$ |
| **Rechazar $H_0$** | **Error Tipo I ($\alpha$)** Probabilidad: $\alpha$ (Nivel de Significancia) | **Decisión Correcta (Potencia)** Probabilidad: $1 - \beta$ |

### 4.1. Error Tipo I ($\alpha$)

Ocurre cuando el investigador toma la decisión de **rechazar la hipótesis nula siendo esta analíticamente verdadera** en la población. En términos prácticos, consiste en concluir que existe un efecto, una diferencia o una relación significativa cuando en realidad el fenómeno observado se debió meramente al azar (un falso positivo científico).

* La probabilidad máxima de cometer este error se denomina **nivel de significancia** ($\alpha$), y es fijada a priori por el investigador (convencionalmente en el $5\%$, $\alpha = 0.05$).

### 4.2. Error Tipo II ($\beta$)

Se presenta cuando el investigador toma la decisión de **mantener la hipótesis nula siendo esta analíticamente falsa** en la población. En términos prácticos, consiste en concluir que no hay diferencias o efectos significativos cuando en realidad el fenómeno sí existía pero la prueba falló en detectarlo (un falso negativo científico).

* La probabilidad de cometer este error se denota como $\beta$. El valor complementario, **$1 - \beta$**, se define formalmente como la **potencia del contraste**, y mide la capacidad real de una prueba estadística para detectar diferencias poblacionales legítimas cuando estas verdaderamente existen.

---

## 5. El P-Valor (Significancia Estadística)

El **p-valor** (o probabilidad asociada) es el indicador probabilístico cuantitativo sobre el cual se ejecuta la decisión de rechazar o mantener la hipótesis nula.

* **Definición Formal:** El p-valor es la probabilidad de obtener un resultado muestral igual o más extremo que el efectivamente observado, bajo el supuesto estricto de que la hipótesis nula ($H_0$) es perfectamente verdadera en la población de origen.

### 5.1. Regla de Decisión Estándar

El p-valor actúa como un termómetro de la compatibilidad de los datos con $H_0$:

* **Si `p <= 0.05`:** El resultado es estadísticamente significativo. La probabilidad de que el azar haya generado estos datos es tan baja ($<5\%$) que la presunción de veracidad de la hipótesis nula colapsa. Por lo tanto, **se rechaza $H_0$** y se acepta la validez de la hipótesis alternativa ($H_1$).
* **Si `p > 0.05`:** El resultado no es estadísticamente significativo. Los datos observados son perfectamente compatibles con las fluctuaciones normales del azar muestral. Por lo tanto, **se mantiene $H_0$**, concluyendo que no hay evidencia suficiente para afirmar un efecto real.

### 5.2. Factores Determinantes del P-valor

De acuerdo con las demostraciones analíticas del manual de Botella et al. (2012), la probabilidad asociada a un estadístico de contraste está regulada por tres variables independientes:

1. **Magnitud del Efecto:** A mayor distancia real entre los grupos o mayor fuerza de correlación entre las variables (efecto grande), el estadístico de contraste se inflará, provocando un p-valor consecuentemente más pequeño y significativo.
2. **Variabilidad de los Datos:** A menor dispersión o heterogeneidad interna de las puntuaciones (varianza pequeña), menor será el solapamiento entre las distribuciones de muestreo, lo que reduce el p-valor.
3. **Tamaño de la Muestra ($n$):** El tamaño muestral es el factor más sensible para alterar la significancia. Al incrementarse $n$, el error estándar decrece de manera drástica, elevando artificialmente el valor del estadístico de contraste. Muestras masivas pueden volver significativos ($p \le 0.05$) efectos clínicamente irrelevantes.

---

## 6. Supuestos Previos Obligatorios: Pruebas de Normalidad y Homocedasticidad

Antes de proceder a la aplicación de cualquier prueba estadística de contraste para comparar grupos, el diseño metodológico impone verificar si los datos de la muestra cumplen con ciertos supuestos teóricos matemáticos. De esta verificación depende la elección entre activar **técnicas paramétricas** (altamente potentes, dependientes de la distribución normal) o **técnicas no paramétricas** (libres de distribución, ideales para muestras asimétricas o con valores atípicos severos).

### 6.1. Prueba de Shapiro-Wilk para Normalidad

Esta prueba se aplica con el objetivo de evaluar formalmente si la distribución de frecuencias de una variable cuantitativa continua en la muestra se ajusta de manera óptima al modelo teórico de la curva normal.

* **Hipótesis Estadísticas:**
* $H_0$: Los datos de la muestra **SÍ** se distribuyen normalmente.
* $H_1$: Los datos de la muestra **NO** se distribuyen normalmente.


* **Criterio de Decisión en Jamovi:**
* Si el p-valor de Shapiro-Wilk es **`> 0.05`**: Se acepta e integra la hipótesis nula ($H_0$). El estadístico $W$ resultante se aproximará a la unidad, confirmando que los datos se ajustan a una **distribución normal**, habilitando el uso de pruebas paramétricas.
* Si el p-valor de Shapiro-Wilk es **`< 0.05`**: Se rechaza la hipótesis nula ($H_0$). Los datos presentan una asimetría o curtosis que viola la normalidad, obligando al uso de pruebas no paramétricas.



### 6.2. Prueba de Levene para Homogeneidad de Varianzas (Homocedasticidad)

Cuando la investigación se enfoca en comparar dos o más muestras independientes, es requisito matemático validar si los grupos proceden de poblaciones que poseen varianzas idénticas o uniformes.

* **Hipótesis Estadísticas:**
* $H_0$: Los grupos poseen varianzas **IGUALES** (Existe homocedasticidad).
* $H_1$: Los grupos poseen varianzas **DIFERENTES** (Existe heterocedasticidad).


* **Criterio de Decisión en Jamovi:**
* Si el p-valor de Levene es **`> 0.05`**: Se mantiene $H_0$, asumiendo la igualdad de varianzas entre los grupos para los cálculos.
* Si el p-valor de Levene es **`< 0.05`**: Se rechaza $H_0$, confirmando la existencia de varianzas significativamente desiguales, lo que exige aplicar correcciones matemáticas de ajuste (como la corrección de Welch).



---

## 7. Criterios Metodológicos para la Selección de Pruebas Estadísticas

La selección de la técnica de contraste adecuada para responder a una hipótesis científica no es una decisión heurística; se rige por un árbol de decisión lógica estructurado a partir de tres preguntas guía fundamentales:

1. **¿Qué tipo de variables quiero analizar y cuál es su nivel de medición?** (Cualitativas categoriales frente a cuantitativas continuas).
2. **¿Cuántos niveles, condiciones o grupos estructuran la variable independiente?** (Dos grupos independientes, medidas repetidas longitudinales o múltiples factores).
3. **¿La variable cumple rigurosamente con el supuesto de normalidad y está libre de valores atípicos severos?**

A continuación, se detalla el cuadro integrador macro que regula la adopción de técnicas paramétricas y no paramétricas de uso estándar en psicología y psicopedagogía:

| Naturaleza de las Variables en Intersección | Diseño de los Grupos / Condiciones | TÉCNICAS PARAMÉTRICAS *(Requieren normalidad: Shapiro-Wilk > 0.05)* | TÉCNICAS NO PARAMÉTRICAS *(Libres de distribución: Shapiro-Wilk < 0.05)* |
| --- | --- | --- | --- |
| 1 Cualitativa (Dicotómica) x  1 Cuantitativa Continua | **2 Grupos Independientes** *(ej. Varones vs. Mujeres)* | **Prueba T de Student** para muestras independientes | **Prueba U de Mann-Whitney** |
| 1 Cualitativa (Dicotómica) x  1 Cuantitativa Continua | **2 Medidas Relacionadas** *(ej. Antes vs. Después del tratamiento)* | **Prueba T de Student** para muestras apareadas / correlacionadas | **Prueba de Rangos con Signo de Wilcoxon** |
| 1 Cualitativa (> 2 categorías) x  1 Cuantitativa Continua | **> 2 Grupos Independientes** *(ej. Control vs. Tratamiento A vs. Tratamiento B)* | **ANOVA de una vía** *(Análisis de Varianza)* | **Prueba de Kruskal-Wallis** |
| 1 Cualitativa (> 2 categorías) x  1 Cuantitativa Continua | **> 2 Medidas Relacionadas** *(ej. Evaluación a los 1, 3 y 6 meses)* | **ANOVA de medidas repetidas** | **Prueba de Friedman** |
| Múltiples Variables Cualitativas x  1 Cuantitativa Continua | **> 2 Factores Cruzados** *(ej. Analizar Género y Tipo de Diagnóstico a la vez)* | **ANOVA de dos vías** | *No presenta alternativa no paramétrica estándar directa* |

---

## 8. Bloque Práctico Instrumental: Ejecución de Supuestos y Contrastes en Jamovi

Para operativizar la verificación de supuestos y ejecutar la selección de pruebas sobre una matriz de datos reales, se detalla la ruta analítica dentro del entorno del software **Jamovi**:

### Paso 1: Configuración de la Exploración de Descriptivos y Normalidad

1. Cargar la base de datos de trabajo en Jamovi (por ejemplo, `db_presion_sociocultural`).
2. Dirigirse a la pestaña superior de **`Analyses`**, hacer clic en el botón **`Exploration`** y seleccionar la opción **`Descriptives`**.
3. Trasladar la variable cuantitativa continua de interés (por ejemplo, `IMC`) al cuadro de **`Variables`**.
4. Para evaluar el comportamiento diferenciado de la variable según los grupos que se pretenden comparar, trasladar la variable clasificatoria categórica (por ejemplo, `Sexo`) al cuadro denominado **`Split by`**.
5. Desplegar el menú inferior de **`Plots`** y activar la casilla **`Density`** para obtener una inspección visual de la campana.
6. Desplegar el menú inferior de **`Statistics`**, localizar el apartado de distribución y activar de forma explícita la casilla **`Shapiro-Wilk normality test`**. Inspeccionar el p-valor resultante en la tabla para decidir si se avanza por la vía paramétrica o no paramétrica de acuerdo con la tabla de la Sección 7.

### Paso 2: Ejecución de una Prueba T para Muestras Independientes y Verificación de Homocedasticidad

1. Dirigirse a la barra de herramientas superior de **`Analyses`** y pulsar el botón **`T-Tests`**.
2. Dentro del listado desplegado, seleccionar el comando **`Independent Samples T-Test`**.
3. Trasladar la variable dependiente cuantitativa (`IMC`) al cuadro superior rotulado como **`Dependent Variables`**, y la variable independiente de agrupación (`Sexo`) al cuadro inferior rotulado como **`Grouping Variable`**.
4. Localizar en el panel de control izquierdo el bloque denominado **`Assumptions`** (Supuestos) y marcar activamente las casillas:
* `Homogeneity test` (para que Jamovi ejecute de forma automatizada la **Prueba de Levene**).
* `Normality test` (para obtener el reporte formal de Shapiro-Wilk integrado en el contraste).


5. *Selección Flexible de la Prueba:* En el apartado superior de **`Tests`**, activar la opción correspondiente según los supuestos verificados:
* Si Levene y Shapiro-Wilk fueron significativos ($p > 0.05$), mantener marcada la opción por defecto `Student's t`.
* Si Levene violó la igualdad de varianzas ($p < 0.05$), activar la opción `Welch's t`.
* Si Shapiro-Wilk violó la normalidad ($p < 0.05$), activar la casilla de la prueba no paramétrica alternativa: `Mann-Whitney U`.


6. Inspeccionar el p-valor (`p`) final del contraste en la tabla de resultados para determinar si se rechaza o se mantiene la hipótesis nula de igualdad entre los grupos.

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulo 13: Distribución muestral de un estadístico; Capítulo 14: El contraste de hipótesis; Capítulo 15: Introducción a la inferencia estadística). Ediciones Pirámide.
* Sarli, L. (2025). *Estadística inferencial, Teorema Central del Límite y Contraste de Hipótesis* (Material didáctico de la Clase 8). Universidad Favaloro.
* Speranza, T. B. (2026). *Probabilidad, contraste de hipótesis y verificación de supuestos en Jamovi* (Guía de Trabajo Práctico 8).