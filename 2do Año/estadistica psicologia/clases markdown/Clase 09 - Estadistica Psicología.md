# Documento de Estudio Exhaustivo: Contrastes de Hipótesis de Dos Muestras y Alternativas No Paramétricas (Clase 9)

---

## 1. Clasificación Macro de las Pruebas de Hipótesis: Paramétricas vs. No Paramétricas

Al adentrarse en la inferencia estadística bivariada, la primera gran bifurcación metodológica consiste en decidir entre el uso de técnicas paramétricas o no paramétricas. Esta elección determina la validez y la capacidad de generalización de los hallazgos en investigaciones psicológicas o psicopedagógicas.

### 1.1. Pruebas Paramétricas

Son procedimientos de contraste de hipótesis cuya validez matemática depende del cumplimiento de supuestos estrictos sobre la naturaleza de la población de origen.

* **Supuesto Central:** Asumen que los errores aleatorios que afectan a los resultados empíricos siguen de forma rigurosa una **distribución normal**. Asimismo, exigen variables dependientes de nivel cuantitativo continuo (escalas de intervalo o razón).
* **Ventaja Principal:** Poseen una elevada **potencia estadística** ($1 - \beta$), lo que significa que maximizan la probabilidad de rechazar la hipótesis nula ($H_0$) cuando esta es verdaderamente falsa en la población.

### 1.2. Pruebas No Paramétricas

También denominadas pruebas de **libre distribución** (*distribution-free*), son alternativas metodológicas que no basan sus algoritmos en ninguna suposición acerca de la forma o los parámetros de la distribución poblacional.

* **Mecanismo Operativo:** En lugar de operar con las magnitudes métricas directas (medias aritméticas), transforman los datos brutos en **rangos ordenados** o posiciones jerárquicas.
* **Condiciones de Uso:** Son la opción obligatoria cuando las muestras presentan tamaños pequeños ($n < 30$), exhiben una marcada asimetría, contienen valores atípicos severos o la variable dependiente es de nivel estrictamente **ordinal**.
* **Limitación:** Tienen menor potencia estadística para rechazar $H_0$ en comparación con sus homólogas paramétricas cuando los supuestos de estas últimas sí se cumplen.

---

## 2. Pruebas de Hipótesis para Una Muestra

El diseño de **una muestra** se aplica cuando un investigador desea contrastar si las observaciones recolectadas en un grupo específico difieren significativamente de un valor estándar, normativo o parámetro poblacional previamente conocido.

> **Caso de Estudio (Presentación de Clase):** Una profesora de Psicología desea determinar si los estudiantes de su curso presentan un nivel de ansiedad significativamente diferente del promedio nacional de estudiantes universitarios, el cual se sitúa fijado en $50\text{ puntos}$ en una escala estandarizada, con una desviación estándar poblacional ($\sigma$) desconocida.

### 2.1. Formulación de Hipótesis Estadísticas

Para este diseño de una muestra, el par de hipótesis rivales se modela formalmente de la siguiente manera:

* **Hipótesis Nula ($H_0$):** $\mu = 50$ (La media de ansiedad de la muestra es estadísticamente igual al promedio nacional; la diferencia observada se debe al azar muestral).
* **Hipótesis Alternativa ($H_1$):** $\mu \neq 50$ (La media de ansiedad de la muestra es significativamente diferente del promedio nacional; contraste bidireccional).

### 2.2. La Prueba t de Student para Una Muestra

Cuando la desviación típica de la población ($\sigma$) es desconocida (el escenario habitual en ciencias del comportamiento), se vuelve matemáticamente imposible aplicar la distribución normal unitaria ($Z$). En su lugar, la estadística recurre a la **desviación típica muestral** ($S$) como estimador, lo que exige adoptar la **distribución t de Student**.

#### Fórmula del Estadístico de Contraste:

$$t = \frac{\bar{X} - \mu_0}{\frac{S_{n-1}}{\sqrt{n}}}$$

Donde:

* $\bar{X}$ representa la media aritmética calculada en la muestra.
* $\mu_0$ es el valor de prueba o parámetro normativo bajo sospecha (en el ejemplo, $50$).
* $S_{n-1}$ representa la cuasidesviación típica muestral (estimador insesgado de $\sigma$).
* $n$ es el tamaño total de la muestra.

#### El Concepto de Grados de Libertad ($gl$):

La distribución t de Student no es una curva única, sino una familia de curvas cuya morfología depende exclusivamente de los **grados de libertad**. Los grados de libertad representan el número de observaciones independientes en una muestra que son libres de variar tras haber impuesto una restricción estadística (como el cálculo previo de la media). Para la prueba t de una muestra, se calculan de forma rígida como:


$$gl = n - 1$$

A medida que los grados de libertad se incrementan (muestras más grandes), la distribución t de Student se aproxima de manera asintótica a la distribución normal estándar ($Z$).

---

## 3. Comparación de Dos Grupos Independientes

Este diseño metodológico se presenta cuando el objetivo científico es contrastar si existen diferencias significativas entre dos poblaciones distintas e independientes (diseño entresujetos), evaluadas a partir de una variable cualitativa dicotómica (variable independiente, ej. Género: Matutino vs. Vespertino) y una variable cuantitativa continua (variable dependiente, ej. Ansiedad Final).

### 3.1. Prueba t de Student para Muestras Independientes

Es la técnica paramétrica por excelencia para este diseño. Contrasta la hipótesis nula de que ambas medias poblacionales son idénticas ($H_0: \mu_1 = \mu_2$).

#### Supuestos Teóricos Obligatorios:

Para que el resultado de la prueba t de Student sea válido, la matriz de datos debe satisfacer tres condiciones:

* **Independencia:** Las observaciones de ambos grupos deben haber sido generadas aleatoriamente y ser completamente independientes entre sí.
* **Normalidad:** La variable dependiente debe distribuirse de forma aproximadamente normal en ambos grupos de origen (verificado mediante *Shapiro-Wilk > 0.05*).
* **Homocedasticidad:** Las varianzas de ambas poblaciones deben ser estadísticamente iguales (verificado mediante la *Prueba de Levene > 0.05*).

#### Fórmula del Estadístico de Contraste (con Varianzas Iguales):

$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1 + n_2 - 2} \cdot \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$

Los grados de libertad que regulan la masa probabilística de este contraste se computan formalmente como:


$$gl = n_1 + n_2 - 2$$

### 3.2. Prueba t de Welch (Alternativa ante Heterocedasticidad)

Si al inspeccionar los datos se constata que se cumple el supuesto de normalidad pero se viola de forma flagrante el supuesto de homocedasticidad (es decir, la prueba de Levene arroja un *p-valor < 0.05*, indicando varianzas significativamente desiguales), el estadístico t de Student clásico pierde validez.

Para solucionar esta distorsión, se aplica de forma automática la **Prueba t de Welch**. Este algoritmo matemático realiza un ajuste corrector ponderando de manera independiente la varianza de cada grupo y recalculando los grados de libertad mediante una ecuación fraccionaria compleja (lo que habitualmente genera grados de libertad con valores decimales en las salidas de software). Las hipótesis y la interpretación del p-valor se mantienen idénticas.

### 3.3. Cuantificación de la Relevancia Práctica: Tamaño del Efecto ($d$ de Cohen)

Un error común en la investigación psicológica consiste en asumir que alcanzar un p-valor altamente significativo ($p \le 0.05$) implica de forma automática que la diferencia hallada entre los grupos es de gran relevancia clínica o práctica. Como se demostró en módulos teóricos previos, la significancia estadística es extremadamente sensible al tamaño muestral ($n$).

Para independizar la interpretación del impacto del tamaño de la muestra, es obligatorio calcular el **tamaño del efecto**, instrumentado en este diseño mediante la **d de Cohen**. Este índice cuantifica de forma estandarizada la magnitud de la distancia existente entre las dos medias en términos de unidades de desviación típica combinada.

#### Fórmula de la d de Cohen Muestral:

$$d = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{combinada}}}$$

#### Criterios de Interpretación de Jacob Cohen:

* $|d| \approx 0.20 \longrightarrow$ Tamaño del efecto **pequeño**.
* $|d| \approx 0.50 \longrightarrow$ Tamaño del efecto **moderado**.
* $|d| \ge 0.80 \longrightarrow$ Tamaño del efecto **grande** o clínicamente relevante.

### 3.4. Alternativa No Paramétrica: Prueba U de Mann-Whitney

Cuando la variable dependiente viola el supuesto de normalidad (Shapiro-Wilk $< 0.05$) o se trata de una escala ordinal, la estadística paramétrica queda inhabilitada. La alternativa no paramétrica rigurosa es la **Prueba U de Mann-Whitney**.

* **Mecanismo Lógico:** La prueba ordena la totalidad de las puntuaciones de la muestra conjunta de menor a mayor, asignándoles un rango posicional numérico (1 para el menor, 2 para el siguiente, etc.). Posteriormente, suma los rangos correspondientes a cada grupo. Si la hipótesis nula es verdadera, los rangos deberían distribuirse de forma equitativa entre ambas condiciones. Si un grupo concentra rangos significativamente más altos que el otro, la prueba U registrará dicha discrepancia.
* **Hipótesis:** Contrasta la igualdad de las **medianas** o de las distribuciones de rangos entre las dos poblaciones.

---

## 4. Comparación de Dos Medidas Relacionadas (Muestras Apareadas / Intrasujeto)

Este diseño (también denominado longitudinal o de medidas repetidas) se aplica cuando un mismo grupo de sujetos es evaluado en dos momentos temporales distintos (diseño antes-después o pretest-postest) o bajo dos condiciones experimentales consecutivas. Dado que los datos proceden de las mismas entidades humanas, se elimina la variabilidad intersujeto, lo que exige un tratamiento estadístico diferenciado.

### 4.1. Prueba t de Student para Muestras Apareadas

Esta técnica paramétrica opera reduciendo las dos puntuaciones de cada sujeto a una única variable intermedio denominada **variable de diferencias** ($D_i = X_{1i} - X_{2i}$).

#### Fórmula del Estadístico de Contraste:

$$t = \frac{\bar{D}}{\frac{S_D}{\sqrt{n}}}$$

Donde $\bar{D}$ es la media aritmética de las diferencias calculadas, $S_D$ es la desviación típica de dichas diferencias y $n$ es el número total de pares de observaciones. Los grados de libertad se definen como:


$$gl = n - 1$$

* **Supuesto Crítico:** Exige que la nueva variable construida de diferencias ($D$) se distribuya de forma normal en la población.

### 4.2. Alternativa No Paramétrica: Prueba de los Rangos con Signo de Wilcoxon

Si las puntuaciones de diferencia violan de forma severa el supuesto de normalidad, se activa la **Prueba de Wilcoxon**.

* **Mecanismo Lógico:** El algoritmo calcula la diferencia directa para cada par de datos, descarta las diferencias iguales a cero, y ordena los valores absolutos de las diferencias de menor a mayor asignándoles rangos. Posteriormente, restituye a cada rango el signo (+ o -) de la diferencia original y calcula de forma separada la suma de los rangos positivos ($W^+$) y la suma de los rangos negativos ($W^-$). Si no hay efecto del tratamiento ($H_0$), ambas sumas deberían aproximarse al equilibrio numérico.

---

## 5. Cuadro de Toma de Decisiones Metodológicas

Para guiar la selección de la prueba estadística correcta según el diseño de investigación, se consolida el siguiente algoritmo de decisión:

| Tipo de Relación / Diseño | Cantidad de Grupos o Medidas | Cumplimiento de Supuestos *(Normalidad / Homocedasticidad)* | TÉCNICA PARAMÉTRICA *(Basada en Medias)* | TÉCNICA NO PARAMÉTRICA *(Basada en Rangos/Medianas)* | Indicador de Tamaño del Efecto |
| --- | --- | --- | --- | --- | --- |
| **Una Muestra vs. Valor Fijo** | 1 Grupo | SÍ (Normalidad) NO (Asimétrico/Ordinal) | **t de Student una muestra** *No aplica* | *No aplica* **Prueba de Signos** | *No aplica* |
| **Grupos Independientes** *(Entresujetos)* | 2 Niveles | SÍ (Normalidad + Homocedasticidad) SÍ (Normalidad) / NO (Homocedasticidad) NO (Violación de Normalidad u Ordinal) | **t de Student muestras indep.** **t de Welch** *No aplica* | *No aplica* *No aplica* **U de Mann-Whitney** | d de Cohen d de Cohen Rangos alternativos |
| **Medidas Relacionadas** *(Intrasujeto)* | 2 Momentos | SÍ (Normalidad de las diferencias) NO (Violación de Normalidad u Ordinal) | **t de Student muestras apareadas** *No aplica* | *No aplica* **Rangos con Signo de Wilcoxon** | d de Cohen Rangos alternativos |
| **Adelanto Diseños Complejos** | $> 2$ Niveles | SÍ (Normalidad + Homocedasticidad) NO (Violación de Supuestos) | **ANOVA de una vía** *No aplica* | *No aplica* **Prueba de Kruskal-Wallis** | $\eta^2$ (Eta cuadrado) |

---

## 6. Bloque Práctico Instrumental: Interpretación de Reportes Científicos en Jamovi

Para garantizar la correcta lectura de las salidas analíticas de Jamovi y estructurar los informes de resultados bajo normas estándar de publicación científica (APA), se exponen a continuación las pautas de redacción basadas en los módulos de trabajos prácticos.

### 6.1. Protocolo de Redacción para la Vía Paramétrica (t de Student / Welch)

Al reportar un contraste paramétrico, es un requisito obligatorio incluir de forma explícita el valor del estadístico $t$, los grados de libertad ($gl$), el p-valor (`p`) y el estimador del tamaño del efecto ($d$ de Cohen), acompañados de los estadísticos descriptivos del grupo.

> **Formato de Reporte Estándar:** "Se realizó una prueba t de Student para muestras independientes con el objetivo de evaluar si existían diferencias significativas en los niveles de ansiedad en función del turno de cursada de los estudiantes universitarios. La prueba de normalidad de Shapiro-Wilk y el test de homocedasticidad de Levene permitieron asumir el cumplimiento de los supuestos paramétricos básicos ($p > 0.05$). Los resultados revelaron una diferencia estadísticamente significativa entre las condiciones, $t(34) = 2.50$, $p = 0.017$, con un tamaño del efecto grande, $d = 0.835$. Específicamente, los estudiantes del turno vespertino registraron una media de ansiedad significativamente más elevada ($\bar{X} = 45.60$; $DE = 21.20$) en comparación con aquellos pertenecientes al turno matutino ($\bar{X} = 28.10$; $DE = 20.70$)."

### 6.2. Protocolo de Redacción para la Vía No Paramétrica (Mann-Whitney / Wilcoxon)

Al reportar un contraste no paramétrico, se deben omitir las referencias a medias y desviaciones típicas en la conclusión central, basando el reporte descriptivo estrictamente en las **medianas** ($M_d$) y reportando los estadísticos de rangos ($U$ o $W$).

> **Formato de Reporte Estándar:** "Se ejecutó una prueba U de Mann-Whitney con el propósito de determinar si existían diferencias significativas en el rendimiento académico entre los dos exámenes parciales programados para el primer cuatrimestre, ante la violación del supuesto de normalidad en las puntuaciones brutas. El análisis reflejó una diferencia estadísticamente significativa en el desempeño, $U = 2.732$, $p < 0.05$. La inspección de las medianas de los grupos de observaciones detalló que los alumnos manifestaron un mejor rendimiento en el primer parcial ($M_d = 27.33$) con respecto a las puntuaciones alcanzadas en el segundo examen parcial ($M_d = 20.14$)."

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Capítulos 13, 14 y 15). Ediciones Pirámide.
* Bautista-Díaz, M. L. et al. (2020). *Pruebas estadísticas paramétricas y no paramétricas: su clasificación, objetivos y características*. Educación y Salud Boletín Científico, Vol. 9, No. 17.
* Sarli, L. (2025). *Contraste de hipótesis y pruebas paramétricas/no paramétricas de dos muestras* (Material didáctico de la Clase 9). Universidad Favaloro.
* Speranza, T. B. (2026). *Prueba t de Student, Welch, U de Mann-Whitney y Wilcoxon en Jamovi* (Guías de Trabajos Prácticos 9).