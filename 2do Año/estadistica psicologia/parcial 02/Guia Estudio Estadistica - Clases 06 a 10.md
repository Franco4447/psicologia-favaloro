# 📘 Guía de Estudio Integral
## Estadística aplicada a la Psicología y la Psicopedagogía
### Clases 6 a 10 — Universidad Favaloro · Lic. Leticia Sarli

---

## 🧭 Cómo usar esta guía

Cada módulo (= una clase) está organizado en cuatro capas que se leen en orden:

1. **🎯 Lo que entra al examen** — resumen ultra-corto, tipo flashcard.
2. **🧠 Entender la lógica** — explicación conceptual, "por qué se hace así".
3. **🔧 La herramienta técnica** — fórmulas, supuestos, interpretación.
4. **📋 Ejemplo de la clase** — el caso que aparece en la presentación.

Al final de cada módulo hay un **⚠️ Errores frecuentes** y un **✅ Checklist de repaso**.

> **Estrategia pedagógica:** primero entender el problema que la prueba viene a resolver, después la fórmula. Si en el examen olvidás la fórmula pero entendés la lógica, podés reconstruirla. Al revés no funciona.

---

## 🗺️ Mapa conceptual general del recorrido

El curso atraviesa un único hilo conductor: **cómo pasar de una muestra a conclusiones sobre la población**. Cada clase suma una pieza:

```
┌─────────────────────────────────────────────────────────────────┐
│                  ESTADÍSTICA INFERENCIAL                         │
│      "Conclusiones sobre la población a partir de una muestra,   │
│              controlando un margen de error"                     │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  ¿Las variables       ¿Cuál es la         ¿Cómo decido si lo
   están RELACIONADAS  PROBABILIDAD        que veo es REAL o
   entre sí?           de ese resultado?   producto del azar?
        │                     │                     │
   ┌────┴─────┐         ┌─────┴────┐         ┌──────┴──────┐
   ▼          ▼         ▼          ▼         ▼             ▼
  Clase 6   Clase 6   Clase 7    Clase 7   Clase 8     Clases 9-10
  Ji²       Pearson   Binomial   Normal    Contraste   Pruebas t
  (cualit.) Spearman                        de          ANOVA
            (cuant.)                        hipótesis
```

**Lectura del mapa:** las clases 6 y 7 te dan las **herramientas conceptuales** (asociación + probabilidad + distribuciones). La clase 8 te da el **método de decisión** (contraste de hipótesis). Las clases 9 y 10 son **aplicaciones concretas** de ese método para comparar grupos.

---

## 📦 MÓDULO 1 — CLASE 6: Asociación entre variables

### 🎯 Lo que entra al examen

| Pregunta | Respuesta corta |
|---|---|
| ¿Cuándo uso **Ji Cuadrado** (χ²)? | Cuando ambas variables son **cualitativas** (categóricas). |
| ¿Cuándo uso **Pearson** (*r*)? | Cuando ambas variables son **cuantitativas continuas** con relación **lineal** y distribución normal. |
| ¿Cuándo uso **Spearman** (ρ)? | Cuando hay variables **cuasi-cuantitativas/ordinales**, o cuando hay **valores extremos** (outliers) que afectarían a Pearson. |
| ¿Qué mide χ²? | La diferencia entre **frecuencias observadas y esperadas** bajo el supuesto de independencia. |
| Rango de los coeficientes *r* y ρ | Entre **−1 y +1**. |
| ¿Qué significa *r* = 0? | Que **no hay relación LINEAL** (puede haber relación curvilínea, ojo). |
| ¿Correlación implica causalidad? | **NO.** Nunca. |

---

### 🧠 Entender la lógica

En las ciencias del comportamiento casi nunca hay relaciones deterministas perfectas (como en la física). En su lugar hay **regularidades estadísticas**: tendencias a que los cambios en una variable acompañen a cambios en otra. El objetivo de este módulo es **cuantificar esa tendencia**.

El tipo de variable determina la herramienta:

```
                  ¿Qué tipo de variables tengo?
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   2 cualitativas       2 cuantitativas      1 ordinal o
   (categóricas)        continuas            con outliers
        │                     │                     │
        ▼                     ▼                     ▼
   Ji Cuadrado            Pearson r            Spearman ρ
       (χ²)
```

---

### 🔧 Herramienta 1: Prueba de Ji Cuadrado (χ²)

#### ¿Para qué sirve?
Para evaluar si **dos variables cualitativas (nominales)** están relacionadas o son independientes.

#### La lógica matemática
La prueba compara dos cosas que se organizan en una **tabla de contingencia**:

- **Frecuencias observadas** (*f_O*): lo que realmente contaste en tu muestra.
- **Frecuencias esperadas** (*f_E*): lo que *deberías* contar SI las variables fueran totalmente independientes.

$$\chi^2 = \sum \frac{(f_O - f_E)^2}{f_E}$$

#### Interpretación intuitiva
- Si **observado ≈ esperado**, el cociente da cerca de cero → las variables son **independientes**.
- Si **observado se aleja mucho de esperado**, el cociente se infla → las variables están **asociadas**.

#### Hipótesis
- **H₀:** Las variables son independientes (no hay relación).
- **H₁:** Las variables están asociadas (dependientes).

#### Ejemplo de la clase: ¿el género influye en la preferencia terapéutica?

```
        ┌──────────────────────────────────┐
        │   Tabla de contingencia          │
        ├──────────┬────────┬─────────┬────┤
        │          │  psa   │cognitiva│Tot.│
        ├──────────┼────────┼─────────┼────┤
        │ mujer    │   40   │   36    │ 76 │
        │ varón    │   33   │   41    │ 74 │
        ├──────────┼────────┼─────────┼────┤
        │ Total    │   73   │   77    │150 │
        └──────────┴────────┴─────────┴────┘
```

Resultado en Jamovi: **χ² = 0.969 ; gl = 1 ; p = 0.325**

**Interpretación:** como *p > 0.05*, **no se rechaza H₀**. Las variables son independientes: el género no influye en la preferencia terapéutica.

---

### 🔧 Herramienta 2: Coeficiente de Correlación de Pearson (*r*)

#### ¿Para qué sirve?
Para medir la **fuerza y dirección de la relación LINEAL** entre dos variables cuantitativas continuas.

#### Las cuatro propiedades clave (para el examen)

```
┌────────────────────────────────────────────────────────────┐
│ PROPIEDADES de Pearson r                                   │
├────────────────────────────────────────────────────────────┤
│ 1. RANGO:  −1  ≤  r  ≤  +1                                 │
│                                                            │
│ 2. SIGNO:                                                  │
│       r > 0  →  relación DIRECTA  (sube X, sube Y)         │
│       r < 0  →  relación INVERSA  (sube X, baja Y)         │
│       r = 0  →  no hay relación LINEAL                     │
│                                                            │
│ 3. INVARIANZA: cambiar unidades (mts→pies, kg→libras)      │
│    NO altera el valor de r.                                │
│                                                            │
│ 4. EQUIVALENCIA: r es una covarianza calculada sobre       │
│    puntuaciones típicas (media=0, DE=1).                   │
└────────────────────────────────────────────────────────────┘
```

#### Interpretación de la magnitud

| |r| | Fuerza |
|---|---|
| < 0.1 | Despreciable |
| 0.1 – 0.3 | Débil / pequeña |
| 0.3 – 0.5 | Moderada |
| > 0.5 | Fuerte / elevada |

#### Los cuatro supuestos OBLIGATORIOS

1. **Variables cuantitativas** (escala de intervalo o razón).
2. **Relación lineal** — esto se chequea **visualmente** con un gráfico de dispersión.
3. **Distribución aproximadamente normal.**
4. **Homocedasticidad** — varianza similar a lo largo de los valores.

> **⚠️ Advertencia crítica:** Pearson **solo detecta relaciones lineales**. Una relación curvilínea perfecta en "U invertida" (como la ley de Yerkes-Dodson entre activación fisiológica y rendimiento) puede dar *r ≈ 0* aunque exista una dependencia perfecta. **Siempre mirá el gráfico de dispersión antes de confiar en r.**

---

### 🔧 Herramienta 3: Coeficiente de Spearman (ρ o *r_s*)

#### ¿Cuándo se usa en lugar de Pearson?

- Una de las variables es **ordinal** (rangos, escala Likert).
- La relación es **monotónica pero no lineal** (curvilínea pero siempre creciente o siempre decreciente).
- Hay **valores extremos** que distorsionan la media.

#### Lo que hace internamente
Transforma las puntuaciones originales en **rangos posicionales** (1°, 2°, 3°...) y aplica Pearson sobre esos rangos. Esto **neutraliza el impacto de outliers**.

Su interpretación (rango, signo, fuerza) es **idéntica** a Pearson.

---

### ⚠️ Errores frecuentes (Clase 6)

1. **Confundir "no significativo" con "no hay relación".** Pearson r = 0 solo significa "no hay relación LINEAL". Puede haber una relación curva muy fuerte.
2. **Inferir causalidad desde correlación.** *Aumentan helados → aumentan quemaduras solares.* La causa común es el verano. Siempre que veas una correlación, pensá en una "tercera variable" oculta.
3. **Aplicar Pearson a variables ordinales** (ej: escala Likert de 5 puntos). Corresponde Spearman.
4. **Olvidar el gráfico de dispersión.** Sin él no se puede verificar el supuesto de linealidad.

---

### ✅ Checklist de repaso — Clase 6

- [ ] Sé qué prueba elegir según el tipo de variables (Ji², Pearson o Spearman).
- [ ] Puedo explicar la diferencia entre frecuencia observada y esperada.
- [ ] Recuerdo el rango de *r* y qué significa cada signo.
- [ ] Sé los 4 supuestos de Pearson.
- [ ] Entiendo por qué **correlación ≠ causalidad**.
- [ ] Puedo nombrar una situación donde Spearman es preferible a Pearson.

---

## 📦 MÓDULO 2 — CLASE 7: Probabilidad y Distribuciones Teóricas

### 🎯 Lo que entra al examen

| Pregunta | Respuesta corta |
|---|---|
| ¿Qué es la probabilidad? | Un número entre **0 y 1** que cuantifica las opciones de verificación de un suceso. |
| ¿Qué distribución uso para variables **dicotómicas**? | **Binomial** (éxito/fracaso). |
| ¿Qué distribución uso para variables **cuantitativas continuas**? | **Normal** (campana de Gauss). |
| ¿Cuáles son los 2 parámetros que definen una curva normal? | La **media (μ)** y la **desviación típica (σ)**. |
| ¿Qué es la normal **unitaria** (estándar)? | Una normal con **μ = 0** y **σ = 1**. |
| ¿Cuántos datos caen entre μ ± 1σ? | El **68.26%**. |
| ¿Cuántos datos caen entre μ ± 2σ? | El **95.44%**. |
| ¿Cuántos datos caen entre μ ± 3σ? | El **99.73%**. |
| Fórmula del puntaje Z | $z = (X_i - μ) / σ$ |

---

### 🧠 Entender la lógica

La estadística inferencial necesita una herramienta matemática para conectar lo que observamos en la muestra con lo que ocurre en la población. Esa herramienta es la **probabilidad**.

**Concepto clave (frecuencialista):** la probabilidad NO predice qué pasa en un caso individual. Describe regularidades "a la larga" — qué porcentaje de veces ocurrirá un evento si repitiéramos el experimento infinitas veces en las mismas condiciones.

$$P(A) = \lim_{N \to \infty} \frac{n_A}{N}$$

```
        ┌──────────────────────────────┐
        │  Propiedades axiomáticas     │
        ├──────────────────────────────┤
        │  0  ≤  P(A)  ≤  1            │
        │                              │
        │  P(suceso imposible) = 0     │
        │  P(suceso seguro)    = 1     │
        └──────────────────────────────┘
```

Muchos fenómenos psicológicos siguen patrones predecibles que se ajustan a **modelos matemáticos teóricos**. Si una variable empírica se parece a un modelo conocido, podemos aplicar todas las propiedades del modelo para hacer inferencia.

---

### 🔧 Modelo 1: Distribución Binomial (para variables dicotómicas)

#### ¿Cuándo se aplica?

Cuando hay un experimento con **dos resultados posibles** (éxito/fracaso) que se repite *N* veces de forma independiente.

**Ejemplos en Psicología:**
- Cumple con criterio diagnóstico DSM-5 / No cumple.
- Presencia / Ausencia de un síntoma.
- Consumidor / No consumidor.
- Acierta una pregunta de opción múltiple / Falla.

#### Las dos condiciones obligatorias

1. La probabilidad de éxito **π** es **constante** en cada repetición e **independiente** del resultado anterior.
2. La variable X cuenta el **número de éxitos** en N ensayos.

Se simboliza: **X ~ B(N; π)**

#### Fórmula de la función de probabilidad

$$P(X = X_i) = \binom{N}{X_i} \cdot \pi^{X_i} \cdot (1-\pi)^{N-X_i}$$

Donde el coeficiente combinatorio (binomial de Newton) se desglosa como:

$$\binom{N}{X_i} = \frac{N!}{X_i! \cdot (N - X_i)!}$$

**Recordatorio matemático:** el factorial *N!* = 1 × 2 × 3 × … × N. Por convención, **0! = 1**.

#### 📋 Ejemplo trabajado

Un test tiene N = 4 reactivos de opción múltiple. Cada uno tiene 4 opciones, así que si el niño responde al azar, π = 0.25. ¿Cuál es la probabilidad de que acierte exactamente 3 reactivos por azar?

**Paso 1 — Combinatoria:**
$$\binom{4}{3} = \frac{4!}{3! \cdot 1!} = \frac{24}{6 \cdot 1} = 4$$

**Paso 2 — Sustitución:**
$$P(X=3) = 4 \cdot (0.25)^3 \cdot (0.75)^1 = 4 \cdot 0.015625 \cdot 0.75 = 0.0469$$

**Interpretación clínica:** la probabilidad de acertar 3 de 4 por puro azar es del **4.69%**. Como es muy baja, si un niño obtiene esa puntuación, tenemos evidencia para rechazar la hipótesis de azar y concluir que hay aptitud verbal real.

---

### 🔧 Modelo 2: Distribución Normal (para variables cuantitativas continuas)

#### ¿Cuándo se aplica?

Cuando la variable de interés es cuantitativa continua y su distribución empírica **se asemeja lo suficiente** a una curva normal teórica como para poder trabajar "como si" lo fuera.

**Ejemplos en Psicología:** Tiempo de reacción, cociente intelectual (CI), puntuaciones en rasgos de personalidad, niveles de ansiedad...

Se simboliza: **X ~ N(μ; σ)**

#### Las 5 propiedades que tenés que saber

```
╔═══════════════════════════════════════════════════════════════╗
║  PROPIEDADES DE LA DISTRIBUCIÓN NORMAL                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  1. SIMETRÍA respecto a μ                                     ║
║     → Media = Mediana = Moda                                  ║
║     → 50% del área a cada lado                                ║
║                                                               ║
║  2. ASINTÓTICA al eje X                                       ║
║     → Las colas se extienden hacia ±∞                         ║
║     → Nunca tocan el eje horizontal                           ║
║                                                               ║
║  3. PUNTOS DE INFLEXIÓN en μ ± 1σ                             ║
║     → Donde la curva cambia de cóncava a convexa              ║
║                                                               ║
║  4. FAMILIA DE CURVAS                                         ║
║     → Definida por solo 2 parámetros: μ y σ                   ║
║     → σ pequeña → campana esbelta (leptocúrtica)              ║
║     → σ grande  → campana achatada (platicúrtica)             ║
║                                                               ║
║  5. INVARIANZA ante combinaciones lineales                    ║
║     → Cualquier transformación lineal de una normal           ║
║       también es una normal                                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

> **Mnemotecnia:** **SAPFI** — Simétrica, Asintótica, Puntos de inflexión, Familia, Invariante.

---

### 🔧 Distribución Normal Unitaria (Estándar) y puntaje Z

Dentro de la familia infinita de curvas normales, hay una particular muy útil: aquella donde **μ = 0 y σ = 1**. Se llama **normal unitaria** o **estándar** y se simboliza **N(0;1)**.

Cualquier valor de una variable normal puede transformarse a su equivalente en la normal unitaria mediante la **fórmula de tipificación (puntaje Z)**:

$$z = \frac{X_i - \mu}{\sigma}$$

**Interpretación de Z:** te dice **cuántas desviaciones típicas** se aleja un valor de la media.
- z = +1 → un sujeto está 1 DE por encima del promedio.
- z = −2 → un sujeto está 2 DE por debajo del promedio.

---

### 📊 Red de equivalencias bajo la curva normal

Esta tabla es central y altamente probable en el examen:

| Posición | Z | Puntuación T | Rango Percentilar | Interpretación clínica |
|:---:|:---:|:---:|:---:|:---|
| μ − 3σ | −3.0 | 20 | 0.1 % | Excepcionalmente bajo |
| μ − 2σ | −2.0 | 30 | 2.3 % | Marcadamente bajo (umbral clínico) |
| μ − 1σ | −1.0 | 40 | 15.9 % | Levemente bajo |
| **μ** | **0** | **50** | **50.0 %** | **Promedio exacto** |
| μ + 1σ | +1.0 | 60 | 84.1 % | Levemente alto |
| μ + 2σ | +2.0 | 70 | 97.7 % | Marcadamente alto |
| μ + 3σ | +3.0 | 80 | 99.9 % | Excepcionalmente alto |

#### Reglas prácticas del área bajo la curva

```
                              ┌─────────────────────────┐
                              │   68.26%                │
                              │   ←─────────────────→   │
                              │                         │
                       ┌──────┴─────────────────────────┴──────┐
                       │            95.44%                     │
                       │   ←───────────────────────────────→   │
                       │                                       │
              ┌────────┴───────────────────────────────────────┴────────┐
              │                     99.73%                              │
              │   ←─────────────────────────────────────────────────→   │
              │                                                         │
   ───────────┼──────────┼──────────┼──────────┼──────────┼─────────────┼──────────
            μ−3σ       μ−2σ       μ−1σ        μ        μ+1σ           μ+2σ       μ+3σ
```

**Regla 68-95-99.7:**
- Entre **μ ± 1σ** se concentra el **68.26%** de los datos.
- Entre **μ ± 2σ** se concentra el **95.44%** de los datos.
- Entre **μ ± 3σ** se concentra el **99.73%** de los datos.

---

### ⚠️ Errores frecuentes (Clase 7)

1. **Confundir DE con σ.** En estadística descriptiva DE es muestral (S), σ es poblacional. En las fórmulas teóricas siempre aparece σ.
2. **Pensar que la probabilidad describe un caso individual.** No: describe el comportamiento *a la larga*.
3. **Olvidar que la curva normal es asintótica.** Las colas no llegan a 0 en ningún punto finito.
4. **Confundir Z con T.** Z tiene media 0 y DE 1. T tiene media 50 y DE 10 (escala derivada).

---

### ✅ Checklist de repaso — Clase 7

- [ ] Puedo definir probabilidad y sus límites (entre 0 y 1).
- [ ] Identifico cuándo usar binomial vs normal.
- [ ] Conozco las 5 propiedades de la curva normal.
- [ ] Sé qué define a la normal unitaria.
- [ ] Memorizo la regla 68-95-99.7.
- [ ] Puedo calcular un puntaje Z.
- [ ] Puedo traducir entre Z, T y rango percentilar usando la tabla.

---

## 📦 MÓDULO 3 — CLASE 8: Contraste de Hipótesis

### 🎯 Lo que entra al examen

| Pregunta | Respuesta corta |
|---|---|
| ¿Qué es un **estadístico**? | Característica **variable** de una **muestra**. Letras latinas (X̄, S, P). |
| ¿Qué es un **parámetro**? | Característica **fija** de una **población**. Letras griegas (μ, σ, π). |
| ¿Qué es un **estimador**? | Un estadístico cuyo valor se considera próximo al parámetro. |
| ¿Qué dice el **Teorema Central del Límite**? | Si *n* es grande, la distribución de las medias muestrales tiende a una **normal**. |
| ¿Qué es **H₀** (hipótesis nula)? | La afirmación de **ausencia** de efecto, diferencia o relación. |
| ¿Qué es **H₁** (hipótesis alternativa)? | La afirmación de que **sí existe** un efecto, diferencia o relación. |
| ¿Qué es el **Error Tipo I (α)**? | Rechazar H₀ siendo verdadera (**falso positivo**). |
| ¿Qué es el **Error Tipo II (β)**? | Mantener H₀ siendo falsa (**falso negativo**). |
| ¿Qué α se usa por convención en psicología? | **α = 0.05** |
| ¿Qué es la **potencia**? | 1 − β: probabilidad de detectar un efecto real cuando existe. |
| Regla de decisión con p-valor | Si **p ≤ 0.05** → se rechaza H₀. Si **p > 0.05** → se mantiene H₀. |

---

### 🧠 Entender la lógica

La estadística inferencial necesita un **proceso formal de decisión** para responder preguntas como *"¿es real esta diferencia entre grupos, o producto del azar?"*. Ese proceso es el **contraste de hipótesis**.

**Idea central:** asumimos por defecto que **no hay efecto** (eso es H₀). Después miramos los datos: si el resultado observado es muy improbable bajo el supuesto de que H₀ es verdadera, entonces rechazamos H₀ y aceptamos H₁.

```
           ┌─────────────────────────────────────────────┐
           │   POBLACIÓN (parámetros desconocidos: μ, σ) │
           └─────────────────────┬───────────────────────┘
                                 │
                          Muestreo aleatorio
                                 │
                                 ▼
           ┌─────────────────────────────────────────────┐
           │   MUESTRA (estadísticos calculados: X̄, S)   │
           └─────────────────────┬───────────────────────┘
                                 │
                          Inferencia con
                          margen de error
                                 │
                                 ▼
           ┌─────────────────────────────────────────────┐
           │   CONCLUSIÓN POBLACIONAL (parámetro estimado)│
           └─────────────────────────────────────────────┘
```

---

### 🔧 Conceptos clave: estadístico, parámetro, estimador

```
┌────────────────────────┬────────────────────────┬────────────────────────┐
│      ESTADÍSTICO       │       ESTIMADOR        │       PARÁMETRO        │
├────────────────────────┼────────────────────────┼────────────────────────┤
│ • Variable             │ • Es un estadístico    │ • Constante (fijo)     │
│ • Describe una         │   cuyos valores se     │ • Describe una         │
│   MUESTRA              │   consideran próximos  │   POBLACIÓN            │
│ • Letras LATINAS       │   al parámetro         │ • Letras GRIEGAS       │
│   X̄, S, P              │                        │   μ, σ, π              │
└────────────────────────┴────────────────────────┴────────────────────────┘
```

---

### 🔧 El Teorema Central del Límite (TCL)

Este teorema es **el pilar matemático** que justifica toda la estadística inferencial paramétrica.

#### Enunciado
Si una muestra aleatoria procede de una población con media μ y desviación típica σ, cuando el tamaño muestral *n* es lo suficientemente grande (convencionalmente **n ≥ 30**), la distribución de las medias muestrales tiende a una **distribución normal**, **sin importar la forma original de la variable en la población**.

#### Propiedades de la distribución muestral de la media

1. **Su media** es igual a la media poblacional:
$$E(\bar{X}) = \mu$$

2. **Su desviación típica** se llama **error estándar** y se calcula:
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

> **No confundir:** la **desviación típica (S o σ)** mide dispersión de los sujetos individuales. El **error estándar (σ_X̄)** mide la imprecisión de la media muestral como estimadora del parámetro. **A mayor n, menor error estándar.** Por eso muestras más grandes dan estimaciones más precisas.

---

### 🔧 La estructura del contraste de hipótesis

#### Las dos hipótesis (rivales, exhaustivas, mutuamente excluyentes)

**H₀ — Hipótesis nula:** afirma que NO hay efecto, diferencia o relación. Refleja el "estado por defecto" del fenómeno. **Se presume verdadera** al inicio del análisis.

**H₁ — Hipótesis alternativa:** afirma que SÍ hay efecto, diferencia o relación. Es la hipótesis del investigador. **Solo se acepta si los datos demuestran que H₀ es insostenible.**

#### Ejemplos de formulación de la presentación

| Pregunta de investigación | H₀ | H₁ |
|---|:---:|:---:|
| ¿Escuchar música relajante cambia el estado de ánimo? | μ_mr = μ_silencio | μ_mr ≠ μ_silencio |
| ¿La privación del sueño cambia la memoria? | μ_priv = μ_no_priv | μ_priv ≠ μ_no_priv |

---

### 🔧 Los cuatro elementos del contraste

1. **Supuestos:** condiciones de partida (independencia de observaciones, varianza poblacional, tamaño muestral suficiente — TCL).

2. **Estadístico de contraste:** transformación matemática del resultado muestral. Se calcula con una fórmula que depende del tipo de prueba (*t*, *F*, *r*, χ², etc.). Tiene una distribución muestral conocida.

3. **Regla de decisión:** consiste en rechazar H₀ si el estadístico cae en la **zona de rechazo (zona crítica)**, o mantenerla si cae en la **zona de aceptación**. Esa regla se basa en el **nivel de significación α** (convencionalmente 0.05) y su complementario **(1−α) = nivel de confianza** (95%).

```
                Zona de aceptación (1−α = 0.95)
                         ┌──────────┐
                       ┌─┘          └─┐
                     ┌─┘              └─┐
                   ┌─┘                  └─┐
                 ┌─┘                      └─┐
   Zona crítica│                            │ Zona crítica
   (α/2 = 0.025)│                           │ (α/2 = 0.025)
        ┌──────┘                            └──────┐
        │                                          │
   ─────┴──────────────────────────────────────────┴─────
       Rechazar H₀         Mantener H₀         Rechazar H₀
```

4. **Conclusión:** se decide rechazar o mantener H₀ y se interpreta en términos del problema original.

---

### 🔧 La matriz de errores posibles

```
┌─────────────────────┬─────────────────────────┬─────────────────────────┐
│                     │   H₀ es VERDADERA       │   H₀ es FALSA           │
├─────────────────────┼─────────────────────────┼─────────────────────────┤
│   MANTENER H₀       │   ✅ Decisión correcta  │   ❌ ERROR TIPO II      │
│                     │     Probabilidad: 1−α   │      β  (Falso negativo)│
├─────────────────────┼─────────────────────────┼─────────────────────────┤
│   RECHAZAR H₀       │   ❌ ERROR TIPO I       │   ✅ Decisión correcta  │
│                     │      α (Falso positivo) │     POTENCIA = 1−β      │
└─────────────────────┴─────────────────────────┴─────────────────────────┘
```

#### Analogía clínica (de la presentación)

| Realidad | Decisión | Resultado |
|---|---|---|
| Está embarazada | Test dice "embarazada" | ✅ Acierto |
| Está embarazada | Test dice "no embarazada" | ❌ **Falso negativo** (β) |
| No está embarazado | Test dice "no embarazado" | ✅ Acierto |
| No está embarazado | Test dice "embarazado" | ❌ **Falso positivo** (α) |

> **Trade-off importante:** bajar α (ser más exigente para evitar falsos positivos) **aumenta β** (más falsos negativos). No se pueden minimizar ambos errores a la vez.

---

### 🔧 El p-valor (nivel crítico)

#### Definición
El **p-valor** es la probabilidad de obtener un resultado igual o más extremo que el observado, **suponiendo que H₀ es verdadera**.

> En la presentación: *"El nivel crítico (p) de un contraste es el menor valor de α con el que se hubiera rechazado H₀."*

#### Regla de decisión

```
┌─────────────────────────────────────────────────────────┐
│   p  ≤  0.05    →    RECHAZAR H₀                        │
│                       (resultado significativo)         │
├─────────────────────────────────────────────────────────┤
│   p  >  0.05    →    MANTENER H₀                        │
│                       (resultado no significativo)      │
└─────────────────────────────────────────────────────────┘
```

#### ¿Qué hace que el p-valor sea pequeño?

El p-valor disminuye (= resultado más significativo) cuando:

1. **El efecto es grande** (las medias están muy separadas).
2. **La variabilidad es pequeña** (los datos están poco dispersos).
3. **El tamaño muestral es grande** (más datos = más precisión).

> **⚠️ Cuidado:** muestras enormes pueden volver significativos efectos triviales. Por eso siempre hay que reportar también el **tamaño del efecto**.

---

### 🔧 Tamaño del efecto

Es la magnitud de la discrepancia entre H₀ y los datos, **independiente del tamaño muestral**. Una diferencia puede ser estadísticamente significativa (p pequeño) pero poco relevante en la práctica si el tamaño del efecto es chico.

(El detalle de los coeficientes — *d* de Cohen, η² — se desarrolla en clases 9 y 10).

---

### 🔧 Pruebas paramétricas vs no paramétricas

```
┌───────────────────────────────────────────────────────────┐
│   PRUEBAS PARAMÉTRICAS                                    │
│   • Asumen distribución normal de los errores             │
│   • Requieren variables cuantitativas continuas           │
│   • TIENEN MAYOR POTENCIA estadística                     │
│   • Ej: t de Student, ANOVA, Pearson                      │
└───────────────────────────────────────────────────────────┘
                              ↕
┌───────────────────────────────────────────────────────────┐
│   PRUEBAS NO PARAMÉTRICAS                                 │
│   • NO asumen ninguna distribución de los errores         │
│   • Pueden trabajar con datos ordinales o con outliers    │
│   • TIENEN MENOR POTENCIA para rechazar H₀                │
│   • Operan transformando datos en RANGOS                  │
│   • Ej: U de Mann-Whitney, Wilcoxon, Kruskal-Wallis       │
│        Spearman, Friedman                                 │
└───────────────────────────────────────────────────────────┘
```

---

### 🔧 Tabla de selección de prueba (Cuadro integrador)

Este cuadro aparece en las presentaciones de las clases 8, 9 y 10. **Es prácticamente seguro que aparece en el examen.**

| Naturaleza de variables | Diseño | TÉCNICA PARAMÉTRICA | TÉCNICA NO PARAMÉTRICA |
|---|---|---|---|
| Cualitativa × Continua | 2 grupos independientes | **t de Student independ.** | U de Mann-Whitney |
| Cualitativa × Continua | 2 medidas relacionadas | **t de Student apareadas** | Rangos con signo de Wilcoxon |
| Cualitativa × Continua | > 2 grupos independientes | **ANOVA de una vía** | Kruskal-Wallis |
| Cualitativa × Continua | > 2 medidas relacionadas | **ANOVA medidas repetidas** | Friedman |
| Cualitativa × Continua | > 2 factores | **ANOVA de dos vías** | No hay alternativa |
| Continua × Continua | — | **Correlación de Pearson** | Correlación de Spearman |

---

### ⚠️ Errores frecuentes (Clase 8)

1. **Decir que H₀ "se acepta".** Técnicamente solo "se mantiene" o "no se rechaza" (porque la evidencia no fue suficiente para rechazarla, no porque hayamos probado que es verdadera).
2. **Interpretar p como "probabilidad de que H₀ sea verdadera".** Falso. Es la probabilidad de los datos observados *bajo el supuesto* de que H₀ es verdadera.
3. **Confundir significación estadística con relevancia práctica.** Por eso existe el tamaño del efecto.
4. **Olvidar el TCL.** Es la razón por la que podemos aplicar pruebas paramétricas aunque la población no sea normal, siempre que n sea grande.

---

### ✅ Checklist de repaso — Clase 8

- [ ] Distingo estadístico, estimador y parámetro.
- [ ] Sé qué dice el Teorema Central del Límite.
- [ ] Puedo formular H₀ y H₁ para un problema dado.
- [ ] Identifico Error Tipo I y II, y su analogía con el embarazo.
- [ ] Sé interpretar un p-valor.
- [ ] Conozco los 3 factores que hacen p más pequeño.
- [ ] Distingo pruebas paramétricas de no paramétricas.
- [ ] Puedo elegir la prueba correcta usando el cuadro integrador.

---

## 📦 MÓDULO 4 — CLASE 9: Pruebas t de Student

### 🎯 Lo que entra al examen

| Pregunta | Respuesta corta |
|---|---|
| ¿Cuándo uso **t de una muestra**? | Para comparar la media de **un grupo** con un valor de referencia conocido. |
| ¿Cuándo uso **t para muestras apareadas**? | Para comparar **dos medidas del MISMO grupo** (antes/después). |
| ¿Cuándo uso **t para muestras independientes**? | Para comparar las medias de **DOS grupos distintos** (entre sujetos). |
| ¿Por qué *t* y no *Z*? | Porque la desviación poblacional σ es **desconocida** y la estimamos con S muestral. |
| ¿Qué son los **grados de libertad**? | El número de valores que pueden variar libremente. Para t de una muestra: **gl = n − 1**. |
| Alternativa no paramétrica a t de **una muestra** | Prueba de los **Signos** / Wilcoxon |
| Alternativa no paramétrica a t **apareadas** | **Wilcoxon** (rangos con signo) |
| Alternativa no paramétrica a t **independientes** | **U de Mann-Whitney** |

---

### 🧠 Entender la lógica

La clase 9 aplica el marco de **contraste de hipótesis** al problema concreto de comparar medias. Hay tres situaciones posibles según el diseño:

```
                  ¿Qué estoy comparando?
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   1 grupo vs un       1 grupo medido       2 grupos
   valor fijo          en 2 momentos        diferentes
   (norma nacional)    (antes/después)      (turno A vs B)
        │                     │                     │
        ▼                     ▼                     ▼
   t de UNA            t para MUESTRAS      t para MUESTRAS
   MUESTRA             APAREADAS            INDEPENDIENTES
```

**¿Por qué se llama "t de Student"?** Porque la fórmula del estadístico de contraste sigue una **distribución t de Student** (no la normal Z). La diferencia clave: cuando NO conocemos la varianza poblacional σ y la tenemos que estimar con la varianza muestral S, eso introduce un poco más de incertidumbre — y la distribución t es ligeramente más "ancha" (con colas más pesadas) que la normal Z, sobre todo con muestras pequeñas.

A medida que n crece, t → Z.

---

### 🔧 Variante 1: Prueba t de una muestra

#### ¿Para qué sirve?
Comparar el promedio de una muestra con un **valor conocido o esperado** (típicamente una norma poblacional).

#### Ejemplo de la presentación
> Una profesora quiere saber si los estudiantes de su curso tienen un nivel de ansiedad **significativamente diferente** del promedio nacional de **50 puntos** en una escala estandarizada (σ poblacional desconocida).

#### Hipótesis
- **H₀:** μ = 50  *(la media del grupo es igual a la media nacional)*
- **H₁:** μ ≠ 50  *(la media del grupo es diferente)*

#### Los 4 supuestos
1. La variable dependiente está en **escala continua** (intervalo o razón).
2. **Independencia** de las observaciones.
3. **Distribución normal.**
4. **Desconocimiento de σ poblacional** → por eso usamos la S muestral.

#### Fórmula del estadístico

$$t = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}$$

Donde X̄ es la media muestral, μ₀ es el valor de prueba (50), S la desviación típica muestral y n el tamaño muestral.

#### Grados de libertad
$$gl = n - 1$$

> **¿Qué son los grados de libertad?** Son la cantidad de valores que pueden variar libremente en el cálculo, después de imponer una restricción. Si calculamos la media de n datos, una vez fijada esa media, los primeros (n−1) datos pueden tomar cualquier valor, pero el último queda determinado. Por eso "se pierde" un grado de libertad.

#### Resultado de la presentación

```
Prueba T en Una Muestra
                  Estadístico   gl     p      Tamaño del Efecto (d de Cohen)
Ansiedad           −2.70       17.0   0.015            −0.636
```

**Interpretación:** como p = 0.015 < 0.05, **se rechaza H₀**. La media de ansiedad del curso (X̄ = 36.5) es significativamente diferente de la media nacional (50). El tamaño del efecto es **moderado-grande** (d = −0.636).

#### Alternativa no paramétrica
**Wilcoxon** (prueba de los rangos con signo, versión para una muestra).

---

### 🔧 Variante 2: Prueba t para muestras apareadas

#### ¿Para qué sirve?
Para comparar **dos puntuaciones de los mismos sujetos** (diseño intra-sujetos):
- Mediciones antes vs después de un tratamiento.
- Dos condiciones experimentales aplicadas al mismo grupo.
- Pares de hermanos, parejas, etc.

#### Ejemplo de la presentación
> La profesora quiere saber si el nivel de ansiedad del grupo **al inicio del cuatrimestre** es significativamente diferente al **final del cuatrimestre**.

#### Hipótesis
- **H₀:** μ_inicio = μ_final
- **H₁:** μ_inicio ≠ μ_final

#### Los 4 supuestos
1. Variable dependiente en escala continua.
2. **Independencia de los pares** (no entre los miembros de cada par).
3. Homogeneidad de varianzas.
4. **Distribución normal de las diferencias**.

#### Lógica matemática
Internamente, la prueba calcula la **diferencia entre las dos medidas** para cada sujeto (D = X_inicio − X_final) y trata esas diferencias como una variable nueva. Después hace una prueba t sobre esa variable de diferencias.

$$t = \frac{\bar{D}}{S_D/\sqrt{n}}$$

#### Resultado de la presentación

```
Prueba T para Muestras Apareadas
                                Estadístico  gl    p     d de Cohen
Ansiedad_inicio − Ansiedad_final   −2.84    17.0  0.011    −0.669
```

**Interpretación:** p = 0.011 < 0.05 → **se rechaza H₀**. La ansiedad aumentó significativamente del inicio (X̄ = 36.5) al final del cuatrimestre (X̄ = 45.6).

#### Alternativa no paramétrica
**Prueba de Wilcoxon (rangos con signo).** Se usa cuando hay valores extremos que afectan la media, o cuando los datos violan la normalidad. Ordena todas las diferencias en valor absoluto y trabaja con los rangos.

---

### 🔧 Variante 3: Prueba t para muestras independientes

#### ¿Para qué sirve?
Para comparar **dos grupos diferentes de sujetos** (diseño entre-sujetos):
- Turno mañana vs turno tarde.
- Grupo control vs grupo experimental.
- Varones vs mujeres.

#### Ejemplo de la presentación
> La profesora quiere saber si los estudiantes del **turno vespertino** tienen un nivel de ansiedad significativamente diferente a los del **turno mañana** al final del cuatrimestre.

#### Hipótesis
- **H₀:** μ_vespertino = μ_mañana
- **H₁:** μ_vespertino ≠ μ_mañana

#### Los 4 supuestos
1. Variable dependiente en escala continua.
2. **Independencia de las observaciones** (los grupos son independientes).
3. **Homogeneidad de varianzas** (Prueba de Levene > 0.05).
4. **Distribución normal** en ambos grupos (Shapiro-Wilk > 0.05).

#### Resultado de la presentación

```
Prueba T para Muestras Independientes
              Estadístico   gl     p     d de Cohen
Ansiedad        2.50       34.0   0.017     0.835

Descriptivas
              Grupo        N    Media  Mediana   DE    EE
Ansiedad_final vespertino  18   45.6   37.0     21.2  5.00
               matutino    18   28.1   20.5     20.7  4.88
```

**Interpretación:** p = 0.017 < 0.05 → **se rechaza H₀**. Los estudiantes del turno vespertino tienen niveles de ansiedad significativamente más altos (X̄ = 45.6) que los del turno matutino (X̄ = 28.1). El tamaño del efecto es **grande** (d = 0.835).

#### Alternativa no paramétrica
**Prueba U de Mann-Whitney.** Compara dos grupos independientes en base al **orden o rango** de los valores (no a las medias). Más sensible a la mediana.

#### Si no se cumple homocedasticidad
Se usa la **corrección de Welch** (no asume varianzas iguales). Las hipótesis y la interpretación son idénticas; solo cambia internamente el cálculo de gl (que sale con decimales).

---

### 🔧 Tamaño del efecto: d de Cohen

Como la t de Student compara medias, el tamaño del efecto se mide con la **d de Cohen**:

$$d = \frac{\bar{X}_1 - \bar{X}_2}{S_{combinada}}$$

#### Criterios de interpretación (Cohen, 1992)

| |d| | Interpretación |
|---|---|
| ≈ 0.20 | Tamaño del efecto **pequeño** |
| ≈ 0.50 | Tamaño del efecto **moderado** |
| ≥ 0.80 | Tamaño del efecto **grande** |

> En el ejemplo del turno: *d = 0.835* → efecto grande (la diferencia no solo es estadísticamente significativa, sino también clínicamente relevante).

---

### 🔧 Cuadro integrador (de la presentación de Clase 9)

| Tipo de variable | Grupos/Medidas | Técnica paramétrica | Técnica no paramétrica |
|---|---|---|---|
| Cualitativa × Continua | 2 grupos independientes | t indep. | U de Mann-Whitney |
| Cualitativa × Continua | 2 medidas relacionadas | t apareadas | Wilcoxon (rangos con signo) |
| Cualitativa × Continua | > 2 grupos independientes | ANOVA de una vía | Kruskal-Wallis |
| Cualitativa × Continua | > 2 medidas relacionadas | ANOVA medidas repetidas | Friedman |
| Cualitativa × Continua | > 2 factores | ANOVA de dos vías | (no hay) |
| Continua × Continua | — | Correlación de Pearson | Correlación de Spearman |

---

### ⚠️ Errores frecuentes (Clase 9)

1. **Aplicar t independientes cuando los datos son del mismo grupo (apareados).** El diseño determina la prueba.
2. **Usar Mann-Whitney para comparar 2 medidas del mismo grupo.** Eso correspondería a Wilcoxon.
3. **Reportar la media (X̄) cuando se usa una prueba no paramétrica.** En no paramétricas se reporta la **mediana**.
4. **Olvidar reportar el tamaño del efecto.** El p-valor solo no alcanza para describir el resultado.
5. **Confundir homocedasticidad con normalidad.** Son dos supuestos diferentes con dos pruebas diferentes (Levene vs Shapiro-Wilk).

---

### ✅ Checklist de repaso — Clase 9

- [ ] Distingo las tres variantes de t (una muestra, apareadas, independientes).
- [ ] Sé cuándo usar cada una según el diseño.
- [ ] Recuerdo la fórmula básica de t y los grados de libertad.
- [ ] Sé identificar la alternativa no paramétrica de cada t.
- [ ] Puedo interpretar el d de Cohen.
- [ ] Sé cuándo usar Welch en vez de Student.
- [ ] Sé leer una salida típica de Jamovi.

---

## 📦 MÓDULO 5 — CLASE 10: ANOVA (Análisis de Varianza)

### 🎯 Lo que entra al examen

| Pregunta | Respuesta corta |
|---|---|
| ¿Cuándo uso **ANOVA** en lugar de t? | Cuando tengo **3 o más grupos/medidas** para comparar. |
| ¿Por qué no aplico varias t en lugar de una ANOVA? | Porque eso **infla el Error Tipo I** (más comparaciones = más probabilidad de falso positivo). |
| ¿Qué compara la ANOVA? | La **varianza entre grupos** vs la **varianza dentro de grupos**. |
| ¿Cuál es el estadístico de la ANOVA? | El **F de Snedecor** = MS_entre / MS_intra. |
| ¿Para qué sirven las **pruebas post-hoc**? | Para identificar **entre qué grupos específicos** hay diferencias, después de una ANOVA significativa. |
| Alternativa no paramétrica a ANOVA de una vía | **Kruskal-Wallis** |
| Alternativa no paramétrica a ANOVA de medidas repetidas | **Friedman** |
| Alternativa cuando no hay homocedasticidad | **ANOVA de Welch** (con post-hoc de Games-Howell) |
| Tamaño del efecto en ANOVA | **η² (Eta cuadrado)** |
| Umbrales de η² (Cohen) | 0.01 = pequeño · 0.06 = mediano · 0.14 = grande |
| ¿Qué evalúa la **ANOVA de dos vías**? | Dos efectos principales + el efecto de **interacción**. |

---

### 🧠 Entender la lógica

#### El problema que viene a resolver

Imaginá que querés comparar la ansiedad entre **3 turnos** (mañana, tarde, noche). Tu primera idea podría ser hacer 3 pruebas t:
- Mañana vs Tarde
- Mañana vs Noche
- Tarde vs Noche

**¿Por qué eso está mal?** Porque cada prueba t tiene un 5% de probabilidad de cometer un falso positivo. Si hacés 3 pruebas, esa probabilidad se acumula:

$$\alpha_{global} = 1 - (1 - 0.05)^3 = 1 - 0.857 = 0.143$$

¡Pasaste del 5% al **14.3%** de error tipo I sin darte cuenta! Con 4 grupos serían 6 comparaciones y el α global subiría al **26.5%**.

#### La solución: ANOVA

La ANOVA hace una **sola comparación global** que mantiene el α en el 5%. Compara si **al menos un grupo difiere de los demás**, pero sin decirte cuál (eso lo hacen los post-hoc después).

```
        TRES GRUPOS DE ANSIEDAD
                  │
                  ▼
       Una sola prueba ANOVA
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   F significativo    F no significativo
   (p ≤ 0.05)         (p > 0.05)
        │                   │
        ▼                   ▼
   Hacer pruebas        Parar acá. 
   post-hoc para        Las medias son
   ver entre qué        estadísticamente
   pares hay            iguales.
   diferencias.
```

---

### 🔧 La lógica fisheriana: descomposición de la varianza

La genialidad de Ronald Fisher: para saber si las **medias** son diferentes, mirá las **varianzas**. La variabilidad total de los datos se descompone en dos fuentes:

```
┌─────────────────────────────────────────────────────────────┐
│            VARIANZA TOTAL DE LOS DATOS                      │
├──────────────────────────────┬──────────────────────────────┤
│   VARIANZA ENTRE GRUPOS      │   VARIANZA DENTRO GRUPOS     │
│   (Inter-grupo / Between)    │   (Intra-grupo / Within)     │
│                              │                              │
│   Refleja el EFECTO de la    │   Refleja la variabilidad    │
│   variable independiente     │   por azar / error / dif.    │
│   + un poco de error         │   individuales              │
└──────────────────────────────┴──────────────────────────────┘
```

Visualmente:

```
   Caso A: VARIANZA ENTRE muy alta       Caso B: VARIANZA ENTRE muy baja
   (los grupos son MUY distintos)        (los grupos están mezclados)
   
          Grupo 1   Grupo 2   Grupo 3       Grupo 1   Grupo 2   Grupo 3
            ▲          ▲                    ▲          ▲          ▲
            │          ●                    │  ●       │          │  ●
            │  ●       │                    │ ●●       │  ●       │ ●●
            │  ●●      │  ●                 │  ●       │ ●●●      │  ●
            │ ●●●      │  ●●                │ ●●       │  ●●      │ ●●●
            │  ●       │ ●●●     ●          │  ●       │  ●       │  ●
            │          │  ●     ●●●         │          │          │
            │          │       ●●●●●        │          │          │
            ↓          ↓        ●           ↓          ↓          ↓
            
   F GRANDE → rechazo H₀                F ≈ 1 → mantengo H₀
```

#### El estadístico F

$$F = \frac{MS_{entre}}{MS_{intra}} = \frac{\text{Varianza explicada por el factor}}{\text{Varianza no explicada (error)}}$$

- **Si F ≈ 1:** la variabilidad entre grupos es similar a la variabilidad por azar → **mantengo H₀**.
- **Si F > 1 (y p ≤ 0.05):** la variabilidad entre grupos es mucho mayor que la del azar → **rechazo H₀**.

---

### 🔧 ANOVA de una vía / un factor

#### Diseño
- **Variable independiente (VI):** cualitativa con **≥ 3 niveles** (ej: turno → mañana/tarde/noche).
- **Variable dependiente (VD):** cuantitativa continua (ej: ansiedad).

#### Hipótesis
- **H₀:** μ_mañana = μ_tarde = μ_noche (todas las medias son iguales).
- **H₁:** Al menos dos medias son diferentes entre sí.

> **⚠️ Error frecuente:** la H₁ NO se escribe μ₁ ≠ μ₂ ≠ μ₃. Basta con que UNA pareja sea diferente para que H₁ sea verdadera.

#### Supuestos obligatorios (5 puntos)
1. La VI es nominal/ordinal con **al menos 3 niveles**.
2. La VD es de intervalo o razón.
3. **Independencia** de observaciones.
4. **Homogeneidad de varianzas** (Levene > 0.05).
5. **Distribución normal** en cada grupo (Shapiro-Wilk > 0.05).

#### Grados de libertad

Hay DOS grados de libertad en una ANOVA (por eso F siempre se reporta como F(gl1, gl2)):

```
gl_entre  =  k − 1          (k = número de niveles del factor)
gl_intra  =  N − k          (N = suma de todos los sujetos)
```

#### 📋 Ejemplo de la presentación: ansiedad por turno

```
ANOVA de Un Factor (Fisher)
                F      gl1   gl2     p
Ansiedad      16.8     2     39    < .001

Descriptivas de Grupo
        Turno     N    Media   DE     EE
Ansiedad Mañana   14   46.8   5.54   1.48
         Tarde    14   34.1   9.48   2.53
         Noche    14   30.5   7.88   2.11
```

**Interpretación:**
- F(2, 39) = 16.8, p < .001 → **se rechaza H₀**.
- Hay diferencias significativas entre los turnos.
- **Pero NO sabemos aún cuáles turnos difieren.** Para eso → pruebas post-hoc.

---

### 🔧 Pruebas Post-hoc

#### ¿Para qué sirven?
Una ANOVA significativa solo te dice "al menos un grupo es diferente". Las pruebas post-hoc identifican **entre qué pares específicos** existen las diferencias, **controlando el error tipo I global**.

```
       H₀:  μ_mañana = μ_tarde = μ_noche
                       │
            (Rechazada por ANOVA)
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
   Escenario A:                  Escenario B:
   Los TRES son                  Solo UNO difiere
   diferentes entre sí           (los otros dos iguales)
        │                             │
        ▼                             ▼
   μ_m ≠ μ_t ≠ μ_n               μ_m ≠ μ_t = μ_n
```

#### Las cuatro pruebas post-hoc más usadas

| Prueba | Cuándo se usa | Característica |
|---|---|---|
| **Tukey HSD** | Estándar para comparar todas las parejas | Buen balance potencia/control |
| **Bonferroni** | Cuando hacés un subconjunto restringido | Conservador (divide α por número de comparaciones) |
| **Dunnett** | Cuando comparás todos los grupos contra UN grupo control | Específica para diseños control vs múltiples tratamientos |
| **Games-Howell** | Cuando NO se cumple homocedasticidad | No asume igualdad de varianzas |

#### 📋 Resultado del ejemplo (de la presentación)

```
Tukey Post-Hoc Test - Ansiedad
                              Mañana   Tarde    Noche
Mañana   Diferencia medias     —      12.7     16.29
         valor p              —      < .001    < .001
Tarde    Diferencia medias                     3.57
         valor p                                0.454
Noche    Diferencia medias                      —
         valor p                                —
```

**Interpretación:**
- Mañana vs Tarde: diferencia 12.7, p < .001 → **significativa**.
- Mañana vs Noche: diferencia 16.29, p < .001 → **significativa**.
- Tarde vs Noche: diferencia 3.57, p = 0.454 → **NO significativa**.

**Conclusión:** los estudiantes del turno mañana tienen ansiedad significativamente más alta que los de tarde y noche, pero tarde y noche son estadísticamente iguales entre sí.

---

### 🔧 Alternativas a la ANOVA estándar

#### Si NO se cumple homogeneidad de varianzas → ANOVA de Welch

- Aplica si tenés > 2 grupos independientes.
- Cumple normalidad pero NO homocedasticidad.
- Post-hoc compatible: **Games-Howell**.

#### Si NO se cumple normalidad → Prueba de Kruskal-Wallis

- Alternativa **no paramétrica**.
- Opera transformando los datos en **rangos**.
- Compara distribuciones (especialmente medianas).
- Post-hoc compatible: **comparaciones de Dunn**.

---

### 🔧 ANOVA de dos vías / dos factores

#### ¿Cuándo se usa?
Cuando hay **DOS variables independientes cualitativas** simultáneas (ej: turno × tipo de universidad).

#### Tres efectos a evaluar
1. **Efecto principal del Factor A** (turno): ¿hay diferencias entre turnos independientemente del tipo de universidad?
2. **Efecto principal del Factor B** (universidad): ¿hay diferencias entre tipos de universidad independientemente del turno?
3. **Efecto de interacción (A × B):** ¿el efecto del turno depende del tipo de universidad?

> **El efecto de interacción es el aporte más valioso del diseño factorial.** Permite descubrir que el impacto de un factor cambia según el nivel del otro.

#### 📋 Ejemplo de la presentación (Turno × Universidad)

```
ANOVA - Ansiedad
                       Suma Cuad.  gl   MS      F      p      η²p
Turno                    2052      2   1025.8  18.66  < .001  0.509
Universidad               215      1    214.9   3.91  0.056   0.098
Turno × Universidad       181      2     90.4   1.64  0.207   0.084
Residuos                 1979     36     55.0
```

**Interpretación:**
- **Turno:** p < .001 → efecto principal **significativo** (η²p = 0.509 → muy grande).
- **Universidad:** p = 0.056 → al borde de la significancia (no se rechaza H₀ con α=0.05).
- **Interacción:** p = 0.207 → no hay efecto de interacción.

---

### 🔧 ANOVA de medidas repetidas

#### ¿Cuándo se usa?
Es la **extensión de la t para muestras apareadas** cuando hay **3 o más medidas del mismo grupo**.

Ejemplos:
- Evaluar ansiedad en pretest, postest y seguimiento a 6 meses.
- Comparar el rendimiento bajo 3 condiciones experimentales aplicadas al mismo grupo.

#### Ventaja metodológica
Al evaluar repetidamente a los mismos sujetos, **se aísla la variabilidad inter-sujeto** de la varianza de error, aumentando drásticamente la potencia de la prueba.

#### Alternativa no paramétrica: **Test de Friedman**.

---

### 🔧 Tamaño del efecto: η² (Eta cuadrado)

En ANOVA, el tamaño del efecto se mide con **Eta cuadrado**:

$$\eta^2 = \frac{SS_{entre}}{SS_{total}}$$

Indica la **proporción de varianza explicada** por el factor.

#### Umbrales de interpretación (Cohen, 1992)

| Tipo de efecto | Pequeño | Mediano | Grande |
|---|---|---|---|
| r (correlación) | 0.10 | 0.30 | 0.50 |
| d (diferencia de medias) | 0.20 | 0.50 | 0.80 |
| **η²p (ANOVA)** | **0.01** | **0.06** | **0.14** |
| f² (regresión) | 0.02 | 0.15 | 0.35 |

#### ¿Cómo interpretar concretamente?

| η² | Lectura clínica |
|:---:|---|
| 0.01 | El factor explica solo el **1%** de la varianza. Relevancia práctica marginal. |
| 0.06 | El factor explica el **6%** de la varianza. Impacto observable, relevancia intermedia. |
| ≥ 0.14 | El factor explica el **14% o más** de la varianza. Fenómeno contundente y de gran relevancia. |

> **Recordá los 3 criterios para interpretar el tamaño del efecto** (de la presentación de Clase 10):
> 1. **Contexto** — un efecto pequeño puede ser muy relevante si tiene grandes consecuencias.
> 2. **Contribución al conocimiento** — ¿se compara con efectos reportados en otros estudios? (meta-análisis).
> 3. **Criterio de Cohen** — los puntos de corte estandarizados (la tabla de arriba).

---

### ⚠️ Errores frecuentes (Clase 10)

1. **Hacer múltiples t en lugar de ANOVA** → inflación del Error Tipo I.
2. **Reportar la ANOVA sin pruebas post-hoc** cuando F es significativo → no se identifica entre qué grupos hay diferencias.
3. **Hacer post-hoc cuando F no es significativo** → no tiene sentido.
4. **Escribir H₁ como "todas las medias son diferentes"** → es "al menos una es diferente".
5. **Reportar solo el p-valor sin tamaño del efecto (η²)** → la significancia estadística no informa relevancia práctica.
6. **Aplicar ANOVA estándar cuando no se cumplen los supuestos** → ignorar Welch o Kruskal-Wallis es un error metodológico grave.

---

### ✅ Checklist de repaso — Clase 10

- [ ] Sé por qué no se pueden hacer múltiples t en lugar de una ANOVA.
- [ ] Entiendo la lógica de descomposición de varianza (entre vs intra).
- [ ] Sé qué es el estadístico F y cómo se interpreta.
- [ ] Recuerdo gl_entre = k − 1 y gl_intra = N − k.
- [ ] Identifico los 5 supuestos de la ANOVA.
- [ ] Sé cuándo aplicar Welch, Kruskal-Wallis o Friedman.
- [ ] Sé para qué sirven las pruebas post-hoc y cuáles son las principales.
- [ ] Entiendo qué evalúa una ANOVA de dos vías (efecto principal × interacción).
- [ ] Puedo interpretar η² con los umbrales de Cohen.

---

## 🎯 SECCIÓN INTEGRADORA — Tablas y resúmenes finales

### 📊 Tabla maestra: ¿Qué prueba uso?

Esta tabla resume **todo el curso en un solo lugar**. Tenela impresa al lado al estudiar.

| Tipo de variables | Diseño del estudio | Prueba paramétrica | Prueba no paramétrica | Tamaño del efecto |
|---|---|---|---|---|
| 1 cuantitativa | 1 grupo vs valor conocido | **t una muestra** | Wilcoxon una muestra | d de Cohen |
| Cualitativa × Cuantitativa | 2 grupos independientes | **t independ.** | **U de Mann-Whitney** | d de Cohen |
| Cualitativa × Cuantitativa | 2 medidas relacionadas | **t apareadas** | **Wilcoxon** | d de Cohen |
| Cualitativa × Cuantitativa | > 2 grupos independientes | **ANOVA una vía** | **Kruskal-Wallis** | η² |
| Cualitativa × Cuantitativa | > 2 medidas relacionadas | **ANOVA medidas repetidas** | **Friedman** | η²p |
| Múltiples cualitativas × Cuantitativa | > 2 factores | **ANOVA dos vías** | (no hay) | η²p |
| 2 cuantitativas | — | **Pearson** | **Spearman** | r² |
| 2 cualitativas | — | (no aplica) | **Ji Cuadrado (χ²)** | V de Cramer |

---

### 🧭 Algoritmo de decisión paso a paso

```
                  ¿QUÉ PRUEBA APLICO?
                          │
                          ▼
        ┌─────────────────────────────────┐
        │  Paso 1: ¿Qué tipo de variables │
        │           tengo?                │
        └─────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   2 Cualitativas   1 Cualit + 1 Cuant   2 Cuantitativas
        │                 │                 │
        ▼                 │                 ▼
   χ² (Ji²)              │            ¿Lineal y normal?
                          │            SÍ → Pearson
                          │            NO → Spearman
                          ▼
        ┌─────────────────────────────────┐
        │  Paso 2: ¿Cuántos grupos/       │
        │           medidas tengo?        │
        └─────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
      1 grupo          2 grupos          > 2 grupos
        │                 │                 │
        ▼                 ▼                 ▼
   t una muestra    ┌────┴────┐         ┌───┴───┐
                    ▼         ▼         ▼       ▼
              Independ.   Apareadas  Indep.  Repetidas
                    │         │         │       │
                    ▼         ▼         ▼       ▼
              t indep.   t apareadas  ANOVA  ANOVA m.r.
                                                  ↓
                                              ¿>1 factor?
                                              SÍ → ANOVA 2 vías
                          │
        ┌─────────────────▼─────────────────┐
        │  Paso 3: ¿Se cumplen supuestos?   │
        │  - Normalidad (Shapiro-Wilk)      │
        │  - Homocedasticidad (Levene)      │
        │  - Sin outliers severos           │
        └───────────────────────────────────┘
                          │
              SÍ → técnica paramétrica
              NO → técnica no paramétrica equivalente
```

---

### 📐 Fórmulas clave (cheatsheet)

```
═══════════════════════════════════════════════════════════════
  PROBABILIDAD                                                  
═══════════════════════════════════════════════════════════════

  Probabilidad frecuentista:  P(A) = lim (n_A / N)
                                    N→∞

  Binomial:   P(X = X_i) = C(N, X_i) · π^X_i · (1−π)^(N−X_i)

  Combinatoria:  C(N, X_i) = N! / [X_i! · (N − X_i)!]

═══════════════════════════════════════════════════════════════
  DISTRIBUCIÓN NORMAL                                          
═══════════════════════════════════════════════════════════════

  Puntaje Z:     z = (X_i − μ) / σ

  Áreas:         μ ± 1σ → 68.26%
                 μ ± 2σ → 95.44%
                 μ ± 3σ → 99.73%

═══════════════════════════════════════════════════════════════
  CORRELACIÓN                                                  
═══════════════════════════════════════════════════════════════

  Pearson:       r_xy = S_xy / (S_x · S_y)

  Rango:         −1 ≤ r ≤ +1

  Ji Cuadrado:   χ² = Σ [(f_O − f_E)² / f_E]

═══════════════════════════════════════════════════════════════
  INFERENCIA                                                   
═══════════════════════════════════════════════════════════════

  Error estándar:    σ_X̄ = σ / √n

  t una muestra:     t = (X̄ − μ₀) / (S / √n)        gl = n − 1

  t apareadas:       t = D̄ / (S_D / √n)             gl = n − 1

  t indep.:          t = (X̄₁ − X̄₂) / S_combinada    gl = n₁ + n₂ − 2

  ANOVA:             F = MS_entre / MS_intra
                     gl_entre = k − 1
                     gl_intra = N − k

═══════════════════════════════════════════════════════════════
  TAMAÑO DEL EFECTO                                            
═══════════════════════════════════════════════════════════════

  d de Cohen:       d = (X̄₁ − X̄₂) / S_combinada
                    0.20 = pequeño, 0.50 = moderado, 0.80 = grande

  Eta cuadrado:     η² = SS_entre / SS_total
                    0.01 = pequeño, 0.06 = mediano, 0.14 = grande
```

---

### 🔍 Glosario de términos clave

| Término | Definición |
|---|---|
| **α (alfa)** | Nivel de significación. Probabilidad máxima de cometer Error Tipo I. Convencional: 0.05. |
| **ANOVA** | Análisis de Varianza. Técnica para comparar medias de ≥ 3 grupos. |
| **β (beta)** | Probabilidad de cometer Error Tipo II (falso negativo). |
| **Contraste de hipótesis** | Proceso de decisión que pone una hipótesis estadística en relación con los datos empíricos. |
| **Covarianza** | Medida no estandarizada de co-variación entre dos variables (depende de las unidades). |
| **d de Cohen** | Tamaño del efecto estandarizado para diferencias de medias. |
| **Desviación típica (S, σ)** | Medida de dispersión de las puntuaciones individuales. |
| **Distribución muestral** | Distribución teórica de los valores de un estadístico si se tomaran infinitas muestras. |
| **Error estándar (σ_X̄)** | Desviación típica de la distribución muestral de la media. Mide la imprecisión del estimador. |
| **Error Tipo I** | Rechazar H₀ siendo verdadera. Falso positivo. Probabilidad = α. |
| **Error Tipo II** | Mantener H₀ siendo falsa. Falso negativo. Probabilidad = β. |
| **Estadístico** | Característica calculada en una muestra (X̄, S, P). Es variable. |
| **Estimador** | Estadístico que se considera próximo al parámetro poblacional. |
| **F de Snedecor** | Estadístico de contraste de la ANOVA = MS_entre / MS_intra. |
| **Frecuencia esperada** | En χ², lo que se observaría si las variables fueran independientes. |
| **Frecuencia observada** | En χ², lo que realmente se contó en la muestra. |
| **Grados de libertad (gl)** | Cantidad de valores que pueden variar libremente tras imponer restricciones. |
| **H₀ (hipótesis nula)** | Afirma ausencia de efecto, diferencia o relación. |
| **H₁ (hipótesis alternativa)** | Afirma que sí existe efecto, diferencia o relación. |
| **Homocedasticidad** | Igualdad de varianzas entre grupos. Se evalúa con Levene. |
| **Inferencia estadística** | Generalización de conclusiones desde una muestra a la población. |
| **Mediana** | Valor que divide la distribución en dos mitades iguales. Se usa en pruebas no paramétricas. |
| **μ (mu)** | Media poblacional. |
| **Nivel de confianza** | Complemento de α. Convencional: 95%. |
| **Normal unitaria** | Distribución normal con μ=0 y σ=1. |
| **Parámetro** | Característica fija de una población (μ, σ, π). |
| **Paramétrica (prueba)** | Asume distribución normal de los errores. Mayor potencia. |
| **No paramétrica (prueba)** | Libre de distribución. Trabaja con rangos. Menor potencia. |
| **p-valor** | Probabilidad de obtener el resultado observado (o más extremo) si H₀ es verdadera. |
| **π (pi)** | Probabilidad de éxito en un ensayo de Bernoulli. |
| **Potencia (1−β)** | Capacidad de detectar un efecto real cuando existe. |
| **Post-hoc** | Comparaciones por pares después de una ANOVA significativa. |
| **Probabilidad** | Número entre 0 y 1 que cuantifica opciones de verificación de un suceso. |
| **Puntaje T** | Escala derivada con media=50 y DE=10. |
| **Puntaje Z** | Puntuación tipificada con media=0 y DE=1. |
| **r de Pearson** | Coeficiente de correlación lineal entre dos variables cuantitativas. |
| **Rango percentilar** | Porcentaje de casos por debajo de un valor dado. |
| **ρ (rho) / r_s** | Coeficiente de correlación de Spearman (basado en rangos). |
| **σ (sigma)** | Desviación típica poblacional. |
| **Tamaño del efecto** | Magnitud del fenómeno, independiente del tamaño muestral. |
| **Teorema Central del Límite (TCL)** | Si n es suficientemente grande, la distribución de medias muestrales tiende a una normal. |
| **Welch (corrección)** | Variante de t o ANOVA cuando no se cumple homocedasticidad. |
| **η² (eta cuadrado)** | Tamaño del efecto para ANOVA: proporción de varianza explicada. |
| **χ² (chi/ji cuadrado)** | Prueba para asociación entre variables cualitativas. |

---

### 🎓 Estrategia general para el examen

#### Si te dan un caso/problema y te piden elegir la prueba:

1. **Identificá las variables.** ¿Cualitativas o cuantitativas? ¿Cuántas?
2. **Identificá el diseño.** ¿Comparás grupos independientes? ¿Medidas del mismo grupo? ¿Asociación?
3. **Contá los grupos o medidas.** 1, 2, o más de 2.
4. **Evaluá los supuestos.** ¿Normalidad? ¿Homocedasticidad? ¿Outliers?
5. **Aplicá la tabla maestra.**

#### Si te dan una salida de Jamovi:

1. **Identificá el estadístico** (t, F, χ², r, etc.).
2. **Mirá los grados de libertad** (te dicen el tipo de prueba).
3. **Mirá el p-valor.** ¿p ≤ 0.05?
4. **Mirá el tamaño del efecto** (d, η², r²).
5. **Redactá la conclusión** combinando significación + magnitud + dirección.

#### Si te piden formular hipótesis:

1. **H₀ siempre afirma igualdad / no relación / no efecto.**
2. **H₁ siempre afirma diferencia / relación / efecto.**
3. **Usá símbolos griegos** (μ, σ, π) porque hablamos de parámetros poblacionales, no muestrales.
4. **En ANOVA, H₁ es "al menos una μ diferente"**, no "todas diferentes".

---

### 🔥 Las 10 ideas clave del curso

1. La **inferencia estadística** generaliza desde la muestra a la población, con un margen de error controlado.
2. La **probabilidad** es un concepto ideal: describe regularidades a la larga, no eventos individuales.
3. La **distribución normal** modela la mayoría de las variables psicológicas cuantitativas continuas. Sus 2 parámetros: μ y σ.
4. El **Teorema Central del Límite** justifica el uso de pruebas paramétricas: si n es grande, la media muestral se distribuye normalmente.
5. El **contraste de hipótesis** decide si rechazar H₀ usando un p-valor: si p ≤ 0.05, rechazo.
6. **Error Tipo I = falso positivo (α)**; **Error Tipo II = falso negativo (β)**. Bajar uno sube el otro.
7. La **significación estadística no es lo mismo que relevancia práctica**. Siempre reportar tamaño del efecto.
8. **Correlación NO implica causalidad.** Una tercera variable oculta puede explicar la asociación.
9. **Hacer múltiples pruebas t infla el Error Tipo I.** Por eso existen ANOVA y correcciones post-hoc.
10. La elección de prueba paramétrica vs no paramétrica depende de los **supuestos** (normalidad, homocedasticidad, escala de medición).

---

### 📚 Referencias bibliográficas integradas

- Botella, J.; Suero Suñe, M.; Ximénez Gómez, C. (2012). *Análisis de Datos en Psicología I*. Ediciones Pirámide.
  - Capítulo V — Correlación lineal
  - Capítulos IX, XI, XII — Probabilidad y distribuciones
  - Capítulo XIII — Distribución muestral
  - Capítulo XIV — Contraste de hipótesis
- Bautista-Díaz et al. (2020). *Pruebas estadísticas paramétricas y no paramétricas: su clasificación, objetivos y características*. Educación y Salud. Boletín Científico Instituto de Ciencias de la Salud, 9(17), 78-81.
- Cohen, J. (1992). *A power primer*. Psychological Bulletin, 112, 155–159.
- Sarli, L. (2025). Materiales didácticos de las Clases 6 a 10. Universidad Favaloro.

---

> **Mensaje final:** la estadística no es solo fórmulas. Es una forma de razonar bajo incertidumbre. Si entendés *por qué* cada prueba existe (qué problema vino a resolver), las fórmulas y los nombres se ordenan solos. Cuando dudes, volvé al mapa conceptual general: ¿estoy midiendo asociación, calculando probabilidad, o decidiendo si algo es real?
>
> ¡Éxitos en el examen! 🎯

---

*Documento de estudio compilado para Franco · IT Patagonia · Primer cuatrimestre 2025-2026*
