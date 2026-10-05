# Documento de Estudio Exhaustivo: Análisis de Varianza (ANOVA) y Tamaño del Efecto (Clase 10)

*Este documento constituye una guía de estudio de alta calidad que integra el esqueleto conceptual y el orden temático fijados por la Dra. Leticia Sarli para la Clase 10 de la materia, enriquecido con el desarrollo teórico profundo, el rigor metodológico y las fórmulas provistas en los manuales de referencia (Botella, Suero y Ximénez), junto con las pautas instrumentales de la Lic. Trinidad B. Speranza para la ejecución práctica en el software Jamovi.*

---

## 1. De la Prueba t de Student al Análisis de Varianza (ANOVA)

En los módulos previos de inferencia estadística, se introdujo la **prueba t de Student** como la herramienta paramétrica idónea para comparar las medias de dos grupos independientes o relacionados. Sin embargo, en la práctica de la investigación psicológica y psicopedagógica, es sumamente habitual enfrentarse a diseños de investigación que involucran **tres o más grupos o condiciones experimentales** (por ejemplo, comparar el nivel de ansiedad en tres turnos de cursada: Mañana, Tarde y Noche; o evaluar el rendimiento académico bajo tres métodos de enseñanza distintos).

Cuando el investigador posee tres o más medias muestrales, surge la tentación intuitiva de aplicar múltiples pruebas t de Student emparejando los grupos de dos en dos (Grupo 1 vs. Grupo 2; Grupo 1 vs. Grupo 3; Grupo 2 vs. Grupo 3). Desde el punto de vista metodológico, esta práctica es completamente inadmisible debido al fenómeno de la **inflación del Error Tipo I**.

### 1.1. El Problema de las Comparaciones Múltiples

Cada vez que se ejecuta un contraste de hipótesis aislado bajo un nivel de significancia preestablecido (convencionalmente $\alpha = 0.05$), existe un $5\%$ de probabilidad de rechazar la hipótesis nula siendo esta verdadera (cometer un **Error Tipo I** o falso positivo). Si realizamos múltiples comparaciones independientes sobre la misma matriz de datos, la probabilidad global o familiar de cometer al menos un Error Tipo I ($\alpha_{\text{global}}$) se incrementa de manera exponencial de acuerdo con la siguiente ecuación:

$$\alpha_{\text{global}} = 1 - (1 - \alpha)^c$$

Donde $c$ representa el número de comparaciones bilaterales realizadas ($c = \frac{k(k-1)}{2}$, siendo $k$ el número de grupos).

> **Advertencia Conceptual:** Si un diseño consta de 4 grupos independientes, se requerirían 6 pruebas t de Student distintas. Al aplicar la fórmula, la probabilidad global de cometer un falso positivo científico asciende a $1 - (1 - 0.05)^6 = 1 - (0.95)^6 \approx 0.265$. Esto significa que el investigador operaría con un **$26.5\%$ de Error Tipo I**, destruyendo por completo el rigor probabilístico del estudio.

Para solucionar este impedimento metodológico, Ronald Fisher desarrolló el **Análisis de Varianza (ANOVA)**. El ANOVA es una técnica paramétrica de control omnibús que permite contrastar simultáneamente la igualdad de las medias de tres o más grupos independientes en una única operación matemática, manteniendo el Error Tipo I estrictamente confinado en el $\alpha$ elegido (ej. $5\%$).

---

## 2. Fundamentos y Lógica del ANOVA de un Factor (One-Way ANOVA)

El **ANOVA de un factor** (o de una vía) se aplica ante la presencia de una **variable independiente (VI)** de naturaleza cualitativa (nominal u ordinal) que posee tres o más niveles o grupos independientes, y una **variable dependiente (VD)** de carácter cuantitativo continuo.

### 2.1. Formulación de Hipótesis Estadísticas

El ANOVA contrasta formalmente el siguiente par de hipótesis en la población de origen:

* **Hipótesis Nula ($H_0$):** Postula que todas las medias poblacionales son idénticas. Refleja la ausencia de efecto de la variable independiente.

$$H_0: \mu_1 = \mu_2 = \mu_3 = \dots = \mu_k$$


* **Hipótesis Alternativa ($H_1$):** Niega lo afirmado por la hipótesis nula.

$$H_1: \text{Al menos dos medias poblacionales son diferentes entre sí.}$$



> **Error Común de Formulación:** Es un error metodológico grave escribir la hipótesis alternativa como $H_1: \mu_1 \neq \mu_2 \neq \mu_3$. La hipótesis alternativa del ANOVA no exige que *todas* las medias sean distintas entre sí; se satisface plenamente con que exista **una única pareja de medias** cuyo distanciamiento métrico sea significativamente diferente, permaneciendo el resto de los grupos homogéneos.

### 2.2. La Lógica Fisheriana: Descomposición de la Varianza

La genialidad conceptual del ANOVA radica en que, para determinar si las *medias* son estadísticamente iguales o diferentes, el algoritmo analiza y descompone la *variabilidad* (varianza) total presente en la matriz de observaciones cuantitativas.

La variabilidad total de los datos se fragmenta de manera aditiva en dos fuentes de variación de naturaleza contrapuesta:

1. **Varianza Inter-grupo (Varianza Entre / Between-Group Variance):** Cuantifica la dispersión o distanciamiento existente *entre las medias* de los diferentes grupos con respecto a la gran media muestral global. Esta variabilidad refleja directamente el impacto o **efecto sistemático** inducido por la variable independiente (el tratamiento, la condición o el factor clasificatorio), sumado a una porción de error aleatorio.
2. **Varianza Intra-grupo (Varianza Dentro / Error / Within-Group Variance):** Cuantifica la dispersión interna de las puntuaciones individuales de los sujetos *dentro de sus propios grupos* con respecto a la media de su respectiva condición. Debido a que todos los sujetos clasificados dentro de un mismo grupo experimentaron exactamente el mismo nivel de la variable independiente, esta variabilidad no puede atribuirse al factor bajo estudio; responde puramente a variaciones fortuitas, diferencias individuales e inherentes al azar (denominada matemáticamente **varianza de error**).

---

## 3. El Estadístico de Contraste F de Snedecor

El procedimiento del ANOVA consiste en calcular la razón o cociente matemático entre estas dos fuentes de variación a través del **estadístico F de Snedecor**.

### 3.1. Estructura del Algoritmo Matemático

Para llegar al valor del estadístico F, se divide cada **Suma de Cuadrados** ($SS$) por sus correspondientes **grados de libertad** ($gl$), obteniendo las denominadas **Medias Cuadráticas** ($MS$ o Varianzas ponderadas):

* **Grados de Libertad Inter-grupo:** Donde $k$ es la cantidad de niveles o grupos experimentales.

$$gl_{\text{Inter}} = k - 1$$


* **Grados de Libertad Intra-grupo (Error):** Donde $N$ es el tamaño total de la muestra acumulada de todos los grupos.

$$gl_{\text{Intra}} = N - k$$


* **Cálculo de la Razón F:**

$$F = \frac{\text{Media Cuadrática Inter-grupo}}{\text{Media Cuadrática Intra-grupo}} = \frac{MS_{\text{Inter}}}{MS_{\text{Intra}}}$$



### 3.2. Criterio de Decisión Probabilístico

El estadístico F opera bajo la siguiente lógica inferencial:

* Si la hipótesis nula ($H_0$) es analíticamente verdadera, la variable independiente carece de efecto; por lo tanto, la variabilidad entre las medias será baja y aproximadamente equivalente a la variabilidad del error por azar. En consecuencia, el cociente arrojará un valor de **$F \approx 1$**, lo que se traducirá en un **p-valor $> 0.05$** (se mantiene $H_0$).
* Si la hipótesis alternativa ($H_1$) es verdadera, la VI introduce un efecto sistemático que incrementa de forma significativa la separación entre las medias de los grupos, provocando que la Media Cuadrática Inter sea sustancialmente mayor que la de Error. En este escenario, el estadístico F adoptará un valor marcadamente elevado (**$F > 1$**), arrojando un **p-valor $\le 0.05$** (se rechaza $H_0$ en favor de $H_1$).

---

## 4. Supuestos Teóricos Críticos del ANOVA Paramétrico

Al ser una técnica estadística de alta potencia paramétrica, el ANOVA de un factor exige que la base de datos cumpla simultáneamente con tres condiciones matemáticas estrictas para garantizar que las probabilidades calculadas bajo la distribución F sean fidedignas:

* **Independencia:** Cada observación o puntuación registrada debe ser generada aleatoriamente y ser completamente independiente de las demás observaciones de la muestra. Este supuesto se controla desde el diseño metodológico de la investigación mediante el muestreo aleatorio simple (m.a.s.).
* **Normalidad:** La variable dependiente cuantitativa debe presentar una distribución aproximadamente normal en cada una de las poblaciones representadas por los $k$ grupos. Se operativiza mediante la **prueba de Shapiro-Wilk** aplicada de forma independiente a cada nivel del factor. Su cumplimiento se verifica cuando el p-valor de Shapiro-Wilk es **`> 0.05`**.
* **Homocedasticidad:** Las varianzas de la variable dependiente deben ser estadísticamente iguales o uniformes entre todos los grupos independientes que se comparan. Se evalúa formalmente a través de la **prueba de Levene**. Existe homocedasticidad legítima si el p-valor de Levene es **`> 0.05`**.

### 4.1. Ruptura de Supuestos y la Alternativa No Paramétrica

* Si los datos satisfacen la normalidad pero violan la homocedasticidad (Levene $p \le 0.05$), se debe anular la razón F tradicional y aplicar de forma obligatoria el **ANOVA de Welch** (el cual incorpora coeficientes de ponderación de ajuste para controlar la heterocedasticidad).
* Si la variable dependiente viola flagrantemente el supuesto de normalidad (Shapiro-Wilk $p \le 0.05$) o se presenta en una escala puramente ordinal, el ANOVA de medias queda invalidado. En este escenario, la alternativa no paramétrica de libre distribución obligatoria es la **prueba de Kruskal-Wallis**, la cual opera transformando las puntuaciones directas de la muestra global en rangos jerárquicos ordenados para comparar las distribuciones de las **medianas**.

---

## 5. Comparaciones Múltiples o Pruebas Post-Hoc

Cuando el valor del estadístico F del ANOVA de un factor resulta significativo y se toma la decisión de rechazar la hipótesis nula ($p \le 0.05$), el investigador alcanza una conclusión omnibús: ha verificado que las medias de los grupos evaluados no son todas iguales en la población de origen. Sin embargo, el ANOVA posee una limitación intrínseca: **no especifica de forma exacta cuáles son los grupos concretos que difieren entre sí**.

Para resolver este interrogante sin inflar el Error Tipo I, es obligatorio ejecutar **pruebas post-hoc** (o comparaciones *a posteriori*). Estas pruebas realizan comparaciones binarias de parejas de medias aplicando correcciones matemáticas estrictas para ajustar el p-valor individual de cada cruce y preservar el $\alpha_{\text{global}}$ en el $5\%$.

### Métodos Clásicos de Ajuste Post-Hoc:

* **Prueba de Tukey (HSD):** Es la prueba estándar más utilizada en las ciencias del comportamiento para comparar todas las combinaciones posibles de parejas de medias. Posee un excelente equilibrio entre potencia y control del Error Tipo I, siempre y cuando los tamaños muestrales de los grupos sean relativamente homogéneos y se satisfaga la homocedasticidad.
* **Corrección de Bonferroni:** Es un método altamente conservador y estricto. Consiste en dividir el nivel de significancia original $\alpha$ por el número total de comparaciones binarias que se van a realizar ($\alpha_{\text{ajustado}} = \alpha / c$). Es ideal cuando se planifica realizar únicamente un subconjunto restringido de comparaciones.
* **Prueba de Scheffé:** Es la prueba más segura y conservadora disponible, diseñada específicamente para proteger al investigador contra falsos positivos ante cualquier tipo de comparación lineal compleja imaginable entre las medias, a costa de una pérdida de potencia estadística.

---

## 6. Variantes Avanzadas del Análisis de Varianza

El marco del ANOVA es altamente flexible y se extiende hacia diseños factoriales complejos para capturar la multicausalidad de los fenómenos psicológicos.

### 6.1. ANOVA de Dos Factores (Two-Way ANOVA)

Se activa ante diseños de investigación que involucran de forma simultánea **dos variables independientes cualitativas (Factores A y B)** y una variable dependiente cuantitativa continua, permitiendo evaluar tres efectos inferenciales diferenciados en una misma operación:

* **Efecto Principal del Factor A:** Evalúa de forma independiente si existen diferencias significativas entre los niveles del primer factor, ignorando la presencia del segundo.
* **Efecto Principal del Factor B:** Evalúa si existen diferencias significativas entre los niveles del segundo factor, haciendo abstracción del primero.
* **Efecto de Interacción (A x B):** Es el aporte analítico más valioso de los diseños factoriales. Evalúa si el impacto o efecto que ejerce el Factor A sobre la variable dependiente se modifica, cambia o depende de los niveles específicos en los que se encuentre posicionado el Factor B.

### 6.2. ANOVA de un Factor con Medidas Repetidas (Repeated Measures ANOVA)

Constituye la extensión paramétrica de la prueba t para muestras apareadas aplicada a diseños de investigación de carácter longitudinal o intrasujeto. Se implementa cuando **un único grupo homogéneo de sujetos es evaluado bajo tres o más momentos temporales sucesivos** (por ejemplo, registrar los niveles de depresión en fases de Pretest, Postest y Seguimiento a los 6 meses) o expuesto consecutivamente a tres o más condiciones experimentales distintas.

Al evaluar repetidamente a las mismas entidades humanas, este modelo matemático posee la ventaja metodológica de extraer y aislar de la varianza de error la variabilidad intersujeto (las diferencias individuales estables de las personas), incrementando drásticamente la potencia estadística de la prueba.

---

## 7. Cuantificación de la Relevancia Práctica: Tamaño del Efecto

Como se ha subrayado a lo largo del trayecto epistemológico de la materia, alcanzar la significancia estadística ($p \le 0.05$) es un requisito necesario pero insuficiente en la ciencia moderna. Un p-valor pequeño simplemente certifica que la diferencia hallada entre las medias de los grupos es real y que es altamente improbable que haya sido generada por el azar de muestreo. No obstante, no aporta ninguna información sobre la **magnitud, fuerza o relevancia práctica** de dicho fenómeno.

Para medir de forma fidedigna e independiente del tamaño de la muestra la fuerza de la relación existente entre las variables, el investigador debe reportar de forma obligatoria los índices de **tamaño del efecto**.

### 7.1. El Coeficiente Eta cuadrado ($\eta^2$) y Eta cuadrado parcial ($\eta_p^2$)

En el marco del ANOVA, el tamaño del efecto se operativiza mediante el coeficiente **Eta cuadrado** ($\eta^2$). Este índice se define formalmente como la proporción de la varianza total de la variable dependiente que es explicada de forma sistemática por la variable independiente o factor bajo estudio. Su fórmula matemática base estructural se define como:

$$\eta^2 = \frac{\text{Suma de Cuadrados Inter-grupo (Efecto)}}{\text{Suma de Cuadrados Total}}$$

En distribuciones complejas o factoriales (como el ANOVA de dos factores o de medidas repetidas), se prefiere el reporte de **Eta cuadrado parcial** ($\eta_p^2$), el cual calcula la porción de varianza explicada tras haber excluido del denominador otras fuentes de variación o efectos principales controlados en el diseño. Ambos coeficientes adoptan valores continuos confinados en el intervalo de cero a uno ($0 \le \eta^2 \le 1$).

### 7.2. Criterios de Interpretación de Jacob Cohen

Para dotar de significado clínico y científico a la magnitud calculada de Eta cuadrado, se adoptan universalmente los puntos de corte estandarizados propuestos por Jacob Cohen (1992) en su obra fundacional:

* **$\eta^2 \approx 0.01$ $\longrightarrow$ Tamaño del efecto PEQUEÑO.** La variable independiente solo logra dar cuenta del $1\%$ de la variabilidad interna que presenta la variable dependiente. Su relevancia práctica es marginal.
* **$\eta^2 \approx 0.06$ $\longrightarrow$ Tamaño del efecto MEDIANO (Moderado).** El factor explica aproximadamente el $6\%$ de la varianza del constructo, reflejando un impacto observable y de relevancia intermedia en contextos de intervención comunitaria o educativa.
* **$\eta^2 \ge 0.14$ $\longrightarrow$ Tamaño del efecto GRANDE.** La variable independiente logra explicar el $14\%$ o más de la totalidad de las variaciones de la variable dependiente. Denota un fenómeno contundente con alta capacidad predictiva y máxima relevancia clínico-diagnóstica.

---

## 8. Bloque Práctico Instrumental: Interpretación de Reportes en Jamovi

Para operativizar y consolidar de manera holística la aplicación teórica del ANOVA y la interpretación del tamaño del efecto, se exponen a continuación dos casos analíticos resueltos extraídos rigurosamente de las matrices de datos de los trabajos prácticos ejecutados en el entorno de **Jamovi**.

### 8.1. Caso 1: ANOVA de un Factor Independiente (Métodos de Enseñanza)

* **Diseño:** Un equipo de psicopedagogía evalúa el rendimiento académico de tres muestras independientes de estudiantes universitarios sometidos a tres modalidades pedagógicas distintas: Sincrónico Total ($n=7$), Asincrónico Total ($n=7$) y Combinado / Híbrido ($n=7$).
* **Variables:** VI = *Método de Enseñanza* (3 niveles nominales). VD = *Rendimiento Académico* (Variable cuantitativa continua).
* **Verificación previa de supuestos en Jamovi:** Las pruebas de Shapiro-Wilk aplicadas intra-grupo arrojaron p-valores superiores a $0.05$, validando el ajuste normal. La prueba de Levene para homogeneidad de varianzas arrojó un $p = 0.341$, confirmando la homocedasticidad. Se procede por la vía paramétrica estándar de Fisher.

#### Salida del Reporte Estadístico generado en Jamovi:

```text
ANOVA de un factor - Rendimiento Académico
-----------------------------------------------------------------------
                  Suma de Cuadrados    gl    Media Cuadrática     F        p
-----------------------------------------------------------------------
Entre Grupos          145.20            2         72.60        5.42    0.015
Error (Intra)         241.20           18         13.40
-----------------------------------------------------------------------
Total                 386.40           20

```

#### Secuencia de Interpretación de Resultados:

1. **Evaluación de la Significancia:** Al inspeccionar la fila `Entre Grupos`, localizamos un estadístico $F = 5.42$ asociado a un p-valor de `p = 0.015`. Siguiendo la regla de decisión estandarizada, dado que `p <= 0.05`, **se rechaza la hipótesis nula ($H_0$)** de igualdad de medias, concluyendo con un $95\%$ de confianza que el método de enseñanza genera diferencias estadísticamente significativas en el rendimiento.
2. **Cálculo e Interpretación del Tamaño del Efecto ($\eta^2$):** Aplicando la fórmula estructural sobre la tabla:

$$\eta^2 = \frac{SS_{\text{Entre}}}{SS_{\text{Total}}} = \frac{145.20}{386.40} = 0.375$$



*Interpretación:* El valor obtenido ($\eta^2 = 0.375$) supera ampliamente el umbral crítico de Cohen para efectos elevados ($0.375 > 0.14$). Indica que el método de enseñanza explica de manera directa el **$37.5\%$ de la varianza total** del rendimiento académico, denotando un impacto de gran magnitud práctica.
3. **Inspección Descriptiva Post-Hoc (Tukey):** Tras la significancia, el software desglosa que el grupo Sincrónico Total alcanzó el rendimiento promedio más elevado ($\bar{X} = 27.33$), distanciándose significativamente ($p_{\text{Tukey}} < 0.05$) de la modalidad Combinada ($\bar{X} = 20.14$) y del grupo Asincrónico Total ($\bar{X} = 15.20$).

#### Redacción Formal del Resultado bajo Normas APA:

> "Se realizó un Análisis de Varianza (ANOVA) de un factor independiente con el propósito de evaluar si existían diferencias significativas en el rendimiento académico de los estudiantes en función de tres métodos de enseñanza aplicados (Sincrónico total, Asincrónico total y Combinado). La verificación de supuestos mediante las pruebas de Shapiro-Wilk y Levene permitieron asumir la normalidad y la homocedasticidad de las distribuciones ($p > 0.05$). Los resultados revelaron un efecto estadísticamente significativo del factor método de enseñanza sobre las calificaciones, $F(2, 18) = 5.42$, $p = 0.015$. La magnitud del efecto calculada mediante el coeficiente Eta cuadrado demostró ser de gran relevancia práctica, $\eta^2 = 0.375$, indicando que el método implementado explica el $37.5\%$ de la variabilidad del rendimiento. Las comparaciones múltiples post-hoc de Tukey confirmaron de forma complementaria que los alumnos bajo la modalidad sincrónica total manifestaron un rendimiento significativamente superior ($\bar{X} = 27.33$; $DE = 3.66$) con respecto a la modalidad combinada ($\bar{X} = 20.14$; $DE = 3.55$) y a la modalidad asincrónica total, la cual registró la puntuación promedio más deficiente del estudio ($\bar{X} = 15.20$; $DE = 3.71$)."

---

### 8.2. Caso 2: ANOVA de Medidas Repetidas Factorial (Precisión Motora)

* **Diseño e Hipótesis:** Un experimento de psicología cognitiva evalúa de forma longitudinal la precisión de un grupo de sujetos ($n = 23$) expuestos a un diseño factorial intrasujeto compuesto por dos factores: la *Condición de Ejecución* (Improvisación en Solitario versus Improvisación en Conjunto) y el *Tempo Musical* de metrónomo configurado en tres velocidades (120, 155 y 85 bpm).
* **Salida de Resultados en Jamovi:** El análisis multivariado arroja un efecto principal altamente significativo exclusivamente para el factor condicional, registrando un estadístico $F(1, 22) = 15.46$, un p-valor de `p < 0.001`, y un coeficiente de tamaño del efecto **Eta cuadrado parcial** muy elevado, $\eta_p^2 = 0.41$. Por el contrario, el factor temporal de la velocidad del tempo no arrojó efectos principales significativos ($p > 0.05$), demostrando la ausencia de influencia del metrónomo sobre la precisión motora.

#### Redacción Formal del Resultado bajo Normas APA:

> "La precisión psicomotora alcanzada por los participantes de la muestra fue sometida a un Análisis de Varianza (ANOVA) de medidas repetidas de dos factores, tomando como condiciones intrasujeto a la Condición de Ejecución (Improvisación en solitario vs. Improvisación en conjunto) y al Tempo configurado (120, 155 y 85 bpm). Los resultados estadísticos revelaron un efecto principal significativamente estadístico para el factor Condición de Ejecución, $F(1, 22) = 15.46$, $p < 0.001$, manifestando un tamaño del efecto grande, $\eta_p^2 = 0.41$. La inspección de las medias marginales detalló que los participantes exhibieron niveles de precisión sustancialmente superiores al ejecutar la tarea bajo la condición de improvisación en conjunto ($\bar{X} = 0.79$; $DE = 0.18$) en comparación con el desempeño registrado en la condición de improvisación en solitario ($\bar{X} = 0.67$; $DE = 0.13$). Finalmente, no se constató ningún efecto principal estadísticamente significativo para el factor Tempo, $F(2, 44) = 1.12$, $p = 0.335$, indicando que las variaciones en la velocidad del metrónomo no alteraron de forma sistemática la precisión de los sujetos."

---

### Referencias Bibliográficas de este Módulo

* Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I* (Módulos de inferencia y análisis de varianza). Ediciones Pirámide.
* Cohen, J. (1992). *A power primer*. Psychological Bulletin, 112, 155-159.
* Sarli, L. (2025). *Prueba de Hipótesis III: Análisis de Varianza (ANOVA) y Criterios de Tamaño del Efecto* (Material didáctico de la Clase 10). Universidad Favaloro.
* Speranza, T. B. (2026). *Análisis de varianza (ANOVA) de un factor y medidas repetidas en Jamovi* (Guía de Trabajo Práctico 10).