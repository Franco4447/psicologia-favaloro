# Biología del Comportamiento — Clase 02
## Introducción a la biología molecular
*Universidad Favaloro · Turno vespertino 2026 · Mariana Imperatori – Pablo Koss*

---

## 🗺️ Hoja de ruta de la clase (el "para qué" de todo esto)

Esta clase responde a una pregunta que, como futuro psicólogo, puede sonarte lejana: **¿por qué un psicólogo necesita entender moléculas?** La respuesta es el hilo que recorre todos los slides:

> El comportamiento se puede estudiar en **5 niveles** (cognitivo → conductual → sistémico → celular → **molecular**). Esta clase baja al sótano —los niveles **celular y molecular**— porque allí están las **causas materiales** de lo que después observamos como conducta.

La clase está construida como un **viaje de ida y vuelta**:

1. **Plantea el marco** → niveles de análisis + *nature/nurture*.
2. **Muestra que un mismo comportamiento se puede medir en 3 niveles** → experimento de la respuesta de fuga en roedores.
3. **Introduce un caso testigo** que reaparecerá al final → el **receptor 5-HT2A** y la memoria.
4. **Te da la "caja de herramientas" molecular** (el grueso de la clase):
   - Dogma central → estructura del ADN → replicación → cromosomas → ciclo y división celular → ARN → proteínas → transcripción → traducción → código genético → **leyes de Mendel** → genética no mendeliana → mutaciones.
5. **Cierra el círculo** → vuelve al receptor 5-HT2A y demuestra cómo **un único cambio molecular** (una base, un aminoácido) **trepa** por todos los niveles hasta modificar la **memoria** y la **ansiedad**.

🧭 **Idea-fuerza para todo el cursado:** un cambio en una letra del ADN → cambia un aminoácido → cambia una proteína (un receptor) → cambia la señalización de una neurona → cambia un circuito → **cambia la conducta**. Toda la clase es una demostración de esa cadena causal.

---

## 1. Niveles de análisis del comportamiento

El estudio del comportamiento se organiza en niveles, de lo más "molar" (global) a lo más "molecular" (microscópico):

| Nivel | ¿Qué estudia? | Ejemplo |
|---|---|---|
| **Cognitivo** | Procesos mentales: memoria, atención, lenguaje, decisión | ¿Cómo recuerdo una lista de palabras? |
| **Conductual** | Conducta observable y medible | % de tiempo que un roedor escapa |
| **Sistémico** | Sistemas y circuitos cerebrales | Activación de la amígdala |
| **Celular** | La neurona como unidad | Disparo de un electrodo, corrientes sinápticas |
| **Molecular** | ADN, ARN, proteínas, receptores | Cantidad de una proteína, una variante génica |

🎯 **Foco de la Clase 02:** los dos niveles inferiores → **celular y molecular** (los slides los enmarcan en rojo). Es el "para qué" del meme de "¿Por qué? ¿Por qué?": para *explicar* la conducta no alcanza con describirla, hay que buscar sus **mecanismos**.

### Nature & Nurture (naturaleza y crianza)
Dos explicaciones clásicas del comportamiento humano:

- **Nature (naturaleza):** la herencia biológica y la genética determinan la conducta.
- **Nurture (crianza):** la sociedad, la cultura y los procesos sociales la determinan.

> 💡 **Callout — no es "o lo uno o lo otro":** la neurociencia actual no elige un bando. Genes y ambiente **interactúan** (esto es justamente lo que adelanta el *spoiler* de epigenética del slide 18, y el tema de la clase del 22/4: "Interacción genes y ambiente"). El ADN no es un destino fijo: el ambiente puede modular **cuándo y cuánto** se expresa un gen.

---

## 2. Un mismo comportamiento, tres niveles de medición
### Experimento: respuesta de fuga en roedores según la proximidad del predador

Diseño elegante porque mide **el mismo fenómeno** (el miedo/escape ante un predador) en **tres niveles** a la vez. El estímulo: el **olor** de un gato (no hace falta el gato real; basta la señal olfatoria de amenaza).

**Grupos experimentales** (manipulan la distancia gato–roedor):

| Grupo | Distancia | Significado |
|---|---|---|
| **G1** | 8 cm | Predador muy cerca → máxima amenaza |
| **G2** | 20 cm | Amenaza intermedia |
| **G3** | 40 cm | Amenaza baja |
| **G4** | *Naïve* | **Control:** roedores **no expuestos** al olor del predador |

> ⚠️ **Callout metodológico — ¿por qué el control "Naïve" es lo más importante?**
> Sin un grupo que **nunca** vio el estímulo, no podés saber si lo que medís se debe al predador o a cualquier otra cosa (manipulación, novedad del aparato, estrés inespecífico). El control es la **línea de base** contra la cual todo lo demás cobra sentido. Es el corazón del método experimental: **comparar contra una referencia.**

**Los 3 niveles de lectura (readouts):**

```
        ESTÍMULO: olor de predador a distancia X
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  1) CONDUCTUAL      2) SISTÉMICO/      3) MOLECULAR
   Fuga (% tiempo)      CELULAR          Cantidad de
                     Activación de       "Proteína A"
                      la amígdala
   (caja 60×40×40)   (electrodo →       (muestra → tubo
                      amplificador →      → cuantificación)
                      señal cruda)
```

**Resultado clave: los tres niveles convergen y muestran una relación dosis–respuesta.**
Cuanto más cerca el predador (mayor amenaza), **mayor** la fuga, **mayor** la activación de la amígdala y **mayor** la cantidad de Proteína A. El control naïve (G4) muestra los valores más bajos.

**Lectura de la significancia estadística** (clave para interpretar gráficos en toda la materia):

| Símbolo | Qué significa en este experimento |
|---|---|
| `*` | **G1** es significativamente distinto del **resto** |
| `**` | **G2** es significativamente distinto de **G3 y G4** |
| `***` | **G3** es significativamente distinto de **G4** |

> 🧠 **Mensaje del experimento:** la **amígdala** es una región crítica para el control de la conducta de fuga, y un comportamiento de miedo se puede "leer" simultáneamente como conducta, como actividad de un circuito y como un cambio en una proteína. **Esos tres niveles son tres ventanas al mismo proceso.** La "Proteína A" es un marcador molecular de actividad —volveremos a esta idea con el gen *FosB* en la Guía 1 (Problema 4).

---

## 3. El hilo conductor: el receptor 5-HT2A (parte 1)

Antes de bajar a las herramientas moleculares, la clase planta una "semilla" que germinará al final.

**El paper (de Quervain et al.):** *"A functional genetic variation of the 5-HT2a receptor affects human memory"*.

- La **serotonina (5-HT, 5-hidroxitriptamina)** y sus receptores —incluido el **5-HT2A**— son importantes para el **aprendizaje y la memoria**.
- El receptor 5-HT2A abunda en el **hipocampo** y la **corteza prefrontal**, dos estructuras clave de memoria.
- Existe un **polimorfismo frecuente** del gen que codifica el receptor (**HTR2A**): predice un **cambio de aminoácido** (Histidina → Tirosina) en la posición 452 (notación **H452Y**), con una frecuencia del alelo minoritario de ~9%.
- Los portadores **heterocigotas (His/Tyr)** tienen una **respuesta del receptor atenuada** ("blunted"): menor y más lenta movilización de calcio intracelular ante el estímulo.
- **Resultado conductual:** en el gráfico de "palabras recordadas", His/His y His/Tyr arrancan iguales en el recuerdo inmediato, pero a los **5 minutos y a las 24 h** los **His/Tyr recuerdan menos**.

> 🔑 **Por qué importa ahora:** este caso es la prueba de que **una sola letra cambiada en el ADN** puede modificar la memoria de una persona. Pero para *entender* cómo, primero necesitamos saber qué es un gen, un alelo, un codón y una proteína. Por eso la clase ahora "baja" a lo molecular. Reaparecerá en las secciones 16 y 21.

---

## 4. El dogma central de la biología molecular

La **biología molecular** estudia los mecanismos de **transmisión** y **expresión** de la información genética en las células —factor fundamental para determinar la estructura y función de todo el organismo.

**El dogma central:** la información fluye en **una sola dirección**.

```
                    REPLICACIÓN
                    (ADN → ADN)
                       ↺
                   ┌────────┐
    [ NÚCLEO ]     │  ADN   │
                   └───┬────┘
                       │  TRANSCRIPCIÓN
                       ▼
                   ┌────────┐
                   │  ARNm  │
                   └───┬────┘
   ····· membrana nuclear / poro ·····
                       │
    [ CITOPLASMA ]     ▼  TRADUCCIÓN
                   ┌──────────┐
                   │ PROTEÍNA │
                   └──────────┘
```

| Proceso | De → A | ¿Dónde? |
|---|---|---|
| **Replicación** | ADN → ADN | Núcleo |
| **Transcripción** | ADN → ARN | Núcleo |
| **Traducción** | ARN → Proteína | Citoplasma (ribosomas) |

> 💡 **Por qué el ADN se queda en el núcleo:** el ADN es el "manuscrito original" demasiado valioso para salir. Se hace una "fotocopia de trabajo" (el **ARNm**) que sí puede viajar al citoplasma a fabricar proteínas. La **compartimentalización** núcleo/citoplasma es la base de esta lógica.

---

## 5. La célula y su núcleo

El escenario físico del dogma central:

- **Núcleo:** contiene el ADN; rodeado por la **membrana nuclear**.
- **Nucleoporos:** "puertas" en la membrana por donde sale el ARNm.
- **Nucléolo:** región donde se fabrican componentes de los ribosomas.
- **Ribosomas:** "fábricas" de proteínas (en el citoplasma o sobre el retículo).
- **Citoplasma:** donde ocurre la **traducción**.

Recorrido del mensaje: el ADN se **transcribe** en el núcleo → el **ARNm** sale por el nucleoporo → en el citoplasma el **ribosoma** lo lee y **traduce** en proteína.

---

## 6. Estructura del ADN

### 6.1 Estructura primaria — el ADN como polímero

El ADN es un **polímero de nucleótidos**. Cada **nucleótido** tiene tres partes:

```
   NUCLEÓTIDO = [ GRUPO FOSFATO ] + [ AZÚCAR ] + [ BASE NITROGENADA ]
                                    (desoxirribosa en ADN)
```

- **Bases del ADN:** **A**denina, **G**uanina, **T**imina, **C**itosina.
- Los nucleótidos se unen por **enlaces covalentes fosfodiéster**: el carbono **5'** de una desoxirribosa con el carbono **3'** de la siguiente. Esto da **direccionalidad** a la cadena (extremos 5' y 3').

> 🧩 **Profundización (no está explícito en el slide, pero te ordena la cabeza) — Purinas vs. Pirimidinas:**
> - **Purinas** (anillo doble, más grandes): **A**denina y **G**uanina → mnemotecnia **"AG = Anillo Grande"**.
> - **Pirimidinas** (anillo simple, más chicas): **C**itosina, **T**imina (y **U**racilo en el ARN).
> - **Regla de oro del apareamiento:** una purina **siempre** se aparea con una pirimidina (por eso la doble hélice tiene un ancho constante).

### 6.2 La doble hélice (Watson & Crick, 1953)

En **1953**, James Watson y Francis Crick reportaron la **configuración de doble hélice** del ADN —apoyados en las **cristalografías de rayos X de Rosalind Franklin** (que aparecen en el slide).

Es posible porque las bases forman **parejas complementarias**:

```
   A ═══ T   (2 enlaces de hidrógeno)
   G ≡≡≡ C   (3 enlaces de hidrógeno)
```

- Las dos hebras son **antiparalelas** (una corre 5'→3', la otra 3'→5').
- La hélice tiene un **surco mayor** y un **surco menor**.

> 🧠 **Mnemotecnias para no equivocarte nunca:**
> - **"A**migos **T**ímidos / **G**randes **C**ompañeros" → A–T, G–C.
> - **"La G y la C son más fuertes"** (3 enlaces > 2): por eso el ADN rico en G-C es más difícil de separar.

### Tabla comparativa ADN vs. ARN (la verás de nuevo en la sección 8)

| | **ADN** | **ARN** |
|---|---|---|
| Azúcar | Desoxirribosa | Ribosa |
| Bases | A, G, C, **T (Timina)** | A, G, C, **U (Uracilo)** |
| Hebras | Doble (doble hélice) | Simple (en general) |
| Función | Almacén de información | Mensajero / ejecutor |

---

## 7. Replicación del ADN

**Característica central: la replicación es SEMICONSERVATIVA.**
Cada hebra de la doble hélice funciona como **molde** para sintetizar una nueva hebra complementaria. El resultado: cada molécula hija tiene **una hebra vieja y una nueva**.

```
        ADN original                 Dos copias (semiconservativas)
        ║║  (vieja)                    ║┃   ┃║
        ║║                    →        ║┃   ┃║
        ║║  (vieja)                    ║┃   ┃║
                                      vieja+nueva  nueva+vieja
```

**Reglas de la enzima ADN polimerasa:**
- Requiere un **molde** y un **cebador (primer/iniciador)**.
- Sintetiza **siempre** en dirección **5' → 3'**.

**Consecuencia de la antiparalelidad → dos hebras se sintetizan distinto:**

| Hebra | Cómo se sintetiza |
|---|---|
| **Hebra líder (adelantada)** | De forma **continua** (sigue a la horquilla) |
| **Hebra rezagada (retrasada)** | En **fragmentos cortos** = **fragmentos de Okazaki**, que luego se unen |

> 🩺 **Nota clínica/psicológica:** la fidelidad de la replicación importa. Cuando se acumulan errores → **mutaciones** (sección 17). El ADN tiene **enzimas reparadoras**; fallas en esa maquinaria se vinculan a cáncer y a algunos trastornos del neurodesarrollo.

---

## 8. Organización del ADN: cromatina y cromosomas

El ADN es larguísimo (**~2 metros por cromosoma**), así que debe estar **empaquetado** para caber en el núcleo.

```
ADN (doble hélice)
   │ se enrolla sobre proteínas
   ▼
HISTONAS → NUCLEOSOMAS ("cuentas de un collar")
   │ se compacta más
   ▼
CROMATINA
   │ máxima compactación (durante la división)
   ▼
CROMOSOMA
```

Esta estructura compacta conserva suficiente **plasticidad** para permitir las funciones esenciales del ADN:
- **Replicación** (copiarse)
- **Reparación** (corregir errores)
- **Recombinación** (intercambiar material)
- **Expresión** de la información genética (transcripción)

> 🔮 **SPOILER de la clase → EPIGENÉTICA (interacción genes–ambiente):**
> El nivel de **empaquetamiento** de la cromatina decide qué genes están "accesibles" para expresarse y cuáles están "guardados". El **ambiente** (estrés, dieta, experiencias) puede modificar químicamente histonas y ADN (sin cambiar la secuencia) y así regular la expresión génica. Es el puente entre *nature* y *nurture* (tema del 22/4).

---

## 9. El cariotipo y el genoma humano

- **Genoma humano:** el conjunto de todo el ADN localizado en los **46 cromosomas** de cada célula.
- Tenemos **23 pares**:
  - **22 pares de autosomas** (numerados 1 a 22).
  - **1 par de cromosomas sexuales** (XX o XY).
- **Cariotipo:** la "foto" ordenada de los cromosomas de una célula. Sirve para detectar **anomalías numéricas o estructurales**.

---

## 10. El ciclo celular y la división celular

### 10.1 El ciclo celular

```
        ┌──────── INTERFASE ────────┐      MITOSIS
        G1  →   S   →   G2      →    (Profase → Prometafase →
              (replicación              Metafase → Anafase →
               del ADN)                       Telofase)
```

- **Interfase** = G1 (crecimiento) + **S** (se replica el ADN) + G2 (preparación).
- **Mitosis** = división del núcleo (las 5 fases de arriba).

### 10.2 Mitosis (células somáticas)

- Durante la fase S se **duplica el ADN**; la mitosis produce **2 células hijas idénticas**, con la **misma** cantidad de ADN que la original.
- Función: **crecimiento y regeneración** celular.
- Las células somáticas son **diploides (2n)** → tienen los **23 pares** (46 cromosomas).

### 10.3 Meiosis (células gaméticas / germinales)

- Produce **gametas** (óvulos y espermatozoides).
- Dos divisiones sucesivas: **Meiosis I** y **Meiosis II** → **4 células haploides**.
- Las células germinales son **haploides (n)** → **23 cromosomas** (la mitad).
- Genera **variabilidad genética** (recombinación + segregación al azar).

### 📊 Mitosis vs. Meiosis (cuadro clave)

| | **Mitosis** | **Meiosis** |
|---|---|---|
| Células | Somáticas | Germinales (gametas) |
| N° de divisiones | 1 | 2 (I y II) |
| Células resultantes | 2 | 4 |
| Ploidía resultante | Diploide (2n) | Haploide (n) |
| Resultado genético | Hijas **idénticas** | Hijas **variables** |
| Función | Crecimiento/regeneración | Reproducción/variabilidad |

### 10.4 Cuando la división falla: el Síndrome de Down

- **Síndrome de Down = Trisomía del par 21** (tres copias del cromosoma 21 en lugar de dos).
- Se origina por una **no disyunción** (los cromosomas no se separan bien durante la meiosis).
- ⚠️ **No es hereditario** (lo aclara el slide): es un error en la formación de la gameta, no un rasgo que se transmita de generación en generación.

> 🩺 **Nota:** los resultados de la no disyunción se ven como gametas con n+1 o n-1 cromosomas. Esto conecta con la importancia de la correcta segregación en la meiosis.

---

## 11. Cromosomas homólogos, genes y alelos

- Heredamos **dos juegos** de cromosomas: uno del **padre**, otro de la **madre**.
- Cada par de **cromosomas homólogos** codifica para las **mismas proteínas** y tiene los genes en el **mismo orden/posición** (locus).
- **ALELOS:** formas **alternativas del mismo gen** que ocupan una **posición idéntica** en los cromosomas homólogos y controlan el **mismo carácter** —pero **no necesariamente llevan la misma información**.

```
   Cromosoma paterno     Cromosoma materno
        │ Gen 1 ──────────── Gen 1 │
        │ Gen 2 ──────────── Gen 2 │   ← cada par de genes
        │ Gen 3 ──────────── Gen 3 │     enfrentados = ALELOS
        │ Gen 4 ──────────── Gen 4 │
        │ Gen 5 ──────────── Gen 5 │
```

| Término | Definición |
|---|---|
| **Homocigota** | Ambos alelos **iguales** (AA o aa) |
| **Heterocigota** | Alelos **diferentes** (Aa) |
| **Dominante** (mayúscula) | Alelo cuya característica **se expresa** |
| **Recesivo** (minúscula) | Característica con **menor probabilidad** de expresarse; necesita **2 alelos recesivos** (aa) para manifestarse |

> 🔁 **Reconectando con el 5-HT2A:** "His/His" y "His/Tyr" del paper del slide 9 **son genotipos de alelos**. His/His = homocigota; His/Tyr = heterocigota. ¡La variante de memoria es exactamente este concepto de alelos!

---

## 12. Estructura primaria del ARN

El ARN también es un **polímero de nucleótidos**, pero con dos diferencias respecto del ADN:
- Azúcar = **ribosa** (en vez de desoxirribosa).
- Base = **Uracilo (U)** en lugar de Timina (U se aparea con A).

**Tres tipos de ARN (clave para la traducción):**

| ARN | Función |
|---|---|
| **ARNm (mensajero)** | Lleva la "fotocopia" del gen del núcleo al ribosoma |
| **ARNt (de transferencia)** | **Transporta los aminoácidos** al ribosoma |
| **ARNr (ribosomal)** | Forma parte de la **estructura del ribosoma** |

---

## 13. Proteínas: polímeros de aminoácidos

Las proteínas son **polímeros de aminoácidos** y tienen **4 niveles de organización**:

| Nivel | Descripción |
|---|---|
| **Primaria** | Secuencia lineal de aminoácidos |
| **Secundaria** | Plegamientos locales: **hélice α** y **hoja β (plisada)** |
| **Terciaria** | La proteína madura se pliega **sobre sí misma** (forma 3D) |
| **Cuaternaria** | Varias cadenas polipeptídicas unidas |

**Principales funciones de las proteínas** (¡todo lo que hace la célula lo hacen proteínas!):

| Tipo | Función |
|---|---|
| **Enzimas** | Regular la transmisión de la información genética y el metabolismo |
| **Estructurales** | Mantener la forma de la célula (citoesqueleto, membrana, matriz) |
| **De transporte** | Asegurar la constancia fisicoquímica del medio intracelular |
| **Receptores** | Mediar la relación con el medio extracelular |
| **Hormonas, factores de crecimiento, anticuerpos** | Transmitir señales entre células |

> 🔑 **Conexión clave:** el receptor **5-HT2A** es una **proteína de tipo receptor**. Por eso, cuando una variante génica cambia un aminoácido (His→Tyr), cambia la **forma y función del receptor**, y con ello la señalización neuronal. Acá se entiende todo el caso.

---

## 14. Transcripción y traducción de la información genética

### Vista general (célula eucariota)

```
   [NÚCLEO]   ADN
                │ TRANSCRIPCIÓN
                ▼
              pre-ARN
                │ PROCESAMIENTO  ← (ver profundización)
                ▼
              ARNm ──── sale al ──────┐
                                      ▼
   [CITOSOL]                   RIBOSOMA
                                      │ TRADUCCIÓN
                                      ▼
                                  POLIPÉPTIDO → PROTEÍNA
```

**Hebras del ADN en la transcripción** (¡no confundir!):

| Hebra | Rol |
|---|---|
| **Cadena molde (template)** | La que **lee** la ARN polimerasa (3'→5') |
| **Cadena codificante** | La que **NO** se lee; su secuencia es **igual** al ARN (cambiando T por U) |

Ejemplo del slide: molde `TAC TAG AGC ATT` → ARN `AUG AUC UCG UAA` → polipéptido `Met–Ile–Ser`.

> 🧩 **Profundización — ¿qué es el "Procesamiento" que menciona el slide?**
> En eucariotas, el transcrito primario (pre-ARNm) se **madura** antes de salir del núcleo:
> 1. **Caperuza (cap) en el extremo 5'** → lo protege y ayuda al ribosoma a reconocerlo.
> 2. **Cola poli-A en el extremo 3'** → estabilidad.
> 3. **Splicing** → se eliminan los **intrones** (no codificantes) y se unen los **exones** (codificantes).

### 14.1 Transcripción: Iniciación

La ARN polimerasa no empieza en cualquier lado: reconoce una región reguladora llamada **promotor**.

```
   5'─[ sitios de reconocimiento ]──[ Región transcrita ]──3'
       └────── PROMOTOR ──────┘   +1 (sitio de inicio)
```

> 🧩 **Profundización importante — el slide mezcla procariotas y eucariotas; acá los separo:**
>
> **En PROCARIOTAS** (slides con TTGACG/TATAAT):
> - El promotor tiene dos secuencias conservadas: el **elemento –35** (consenso TTGACG) y el **elemento –10** (consenso TATAAT, "caja de Pribnow").
> - La propia ARN polimerasa (vía su subunidad sigma) los reconoce directamente.
>
> **En EUCARIOTAS** (slide de la "Caja TATA"):
> - La ARN polimerasa **NO** puede unirse sola: necesita proteínas auxiliares llamadas **factores de transcripción**, que se unen **primero** al promotor (sobre la **caja TATA**) y ayudan a la **ARN polimerasa II** a sujetarse del ADN.
> - El ARNm (mensajero) en eucariotas lo fabrica la **ARN polimerasa II**.

### 14.2 Transcripción: Elongación

La ARN polimerasa avanza sobre la cadena molde, abre la doble hélice y va **agregando ribonucleótidos complementarios** en dirección 5'→3', formando la hebra de ARN. Detrás, el ADN vuelve a cerrarse.

---

## 15. Traducción y código genético

### 15.1 La traducción

- Ocurre en los **ribosomas** (compuestos de proteínas + **ARNr**).
- El **ARNt** transporta los aminoácidos correctos al ribosoma.
- El ribosoma "lee" el ARNm de a **tripletes** llamados **codones** y va ensamblando la cadena de aminoácidos.

### 15.2 El código genético

Cada **codón** (3 bases del ARNm) codifica **un aminoácido**. La tabla del código genético traduce los 64 codones posibles.

**Codones especiales (memorizar):**

| Codón | Función |
|---|---|
| **AUG** | **Inicio** (codifica **Metionina**, Met) |
| **UAG / UAA / UGA** | **STOP** (terminación; no codifican aminoácido) |

> 🧠 **Mnemotecnias:**
> - **AUG** = "**A**rranca **U**n **G**en" → inicio (Met).
> - Los STOP **UAG · UAA · UGA**: todos empiezan con **U** y ninguno es UGG (ese sí codifica Triptófano). Truco: *"U-Are-Gone, U-Are-Away, U-Go-Away"*.

> 🧩 **Dato útil:** el código es **degenerado/redundante** → varios codones distintos pueden codificar el mismo aminoácido (p. ej. Leucina tiene 6 codones). Esto explica por qué algunas mutaciones son "silenciosas" (sección 17).

---

## 16. 🔬 Cerrando el círculo (parte 1): la variante del 5-HT2A a nivel de codón

Ahora que tenés el código genético, el caso del receptor 5-HT2A se entiende **letra por letra**:

```
   CAU / CAC  →  HISTIDINA  (variante "común", His)
   UAU / UAC  →  TIROSINA   (variante minoritaria, Tyr)
```

- El **gen HTR2A** (que codifica el receptor 5-HT2A) tiene un punto donde algunos individuos llevan codones para **Histidina** y otros para **Tirosina**.
- Como es una **variante alélica**, una persona puede ser **His/His** (homocigota) o **His/Tyr** (heterocigota).
- Cambiar **una base** → cambia el codón → cambia el **aminoácido** en la posición 452 → cambia la **proteína-receptor** → **respuesta atenuada** → **peor memoria diferida**.

> 🎯 **Este es el corazón conceptual de la clase:** acabás de recorrer ADN → codón → aminoácido → proteína → función → conducta, en un caso humano real. Todo el "andamiaje" molecular anterior existía para poder leer estas dos líneas.

---

## 17. Introducción a la herencia: las leyes de Mendel

La transferencia de características en una familia tiene **base genética**: depende de la **información genética** heredada de los progenitores.

### 17.1 ¿Quién fue Mendel y qué hizo?

- **Gregor Mendel (1822–1884)**, "el padre de la genética", el monje botánico.
- Modelo experimental: la **planta de guisantes (*Pisum sativum*)** → fácil de cultivar, ciclo rápido, muchas semillas y **cruza controlada** (transfiriendo polen de las **anteras** —parte masculina— al **carpelo** —parte femenina).
- Estudió **7 características** fáciles de identificar (altura, color de la flor, color/forma/textura de las semillas).
- Trabajó con **"especies puras"** (ambos alelos iguales): p. ej., semillas amarillas (A) vs. verdes (v).

### 17.2 Primera ley: Ley de la UNIFORMIDAD

> **Todos los descendientes de cruzar dos especies puras son iguales entre sí** (en genotipo y fenotipo).

Cruza: **AA (amarilla) × vv (verde)** → generación parental (P).

**Cuadro de Punnett:**

|  | **A** | **A** |
|---|---|---|
| **v** | Av | Av |
| **v** | Av | Av |

- **F1:** 100% **Av** (genotipo) → 100% **amarillas** (fenotipo).
- A: carácter **dominante** (mayúscula). v: carácter **recesivo** (minúscula).

| Concepto | Definición |
|---|---|
| **Genotipo** | La constitución genética (Av, AA, vv) |
| **Fenotipo** | Las características observables (amarillo, verde) |

### 17.3 Segunda generación: cruzar la F1 (Av × Av)

**Cuadro de Punnett:**

|  | **A** | **v** |
|---|---|---|
| **A** | AA | Av |
| **v** | Av | vv |

**Resultados de la F2:**

| Proporción | Detalle |
|---|---|
| **Fenotipo 3 : 1** | 3 amarillas : 1 verde |
| **Genotipo 1 : 2 : 1** | 1 AA (homocigota dom.) : 2 Av (heterocigota) : 1 vv (homocigota rec.) |

- **Dominante:** la característica que se expresa.
- **Recesivo:** se expresa solo con **dos alelos recesivos** (vv).
- El carácter recesivo "desaparece" en F1 y **reaparece** en F2 → prueba de que los factores hereditarios **no se mezclan ni se pierden**.

### 17.4 Segunda ley: Ley de SEGREGACIÓN INDEPENDIENTE

> **Los factores hereditarios son entidades definidas que se separan (segregan) de forma independiente durante la formación de las células sexuales (gametas).**

Se demuestra con una **cruza dihíbrida** (dos rasgos a la vez): **YyRr × YyRr** → proporción fenotípica clásica de la F2 = **9 : 3 : 3 : 1**.

### 17.5 Otro ejemplo (moscas): alas

- Alelo **B** (dominante): alas normales. Alelo **b** (recesivo): alas rugosas.
- Cruza **Bb × Bb** → genotipos **1 BB : 2 Bb : 1 bb**; fenotipos **3 alas normales : 1 alas rugosas**.

---

## 18. 🔗 INTEGRACIÓN CON LA GUÍA 1 — Problema 3: el gen *fru* (genética mendeliana aplicada a la conducta)

> Este problema de la Guía 1 es la **aplicación directa** de las secciones 11 y 17. Demuestra que las leyes de Mendel no son solo de plantas: explican **comportamientos**.

**Contexto:** el gen ***fru* (*fruitless*)** en moscas, comparando mutantes homocigotas (**fru–/–**) con individuos *wild type* (**wt**, "tipo salvaje" = sin mutación).

| Pregunta de la guía | Respuesta razonada |
|---|---|
| Diferencias de comportamiento mutantes vs. wt | Los **fru–/– aparecen agrupados** y los **wt dispersos** |
| ¿Cómo se expresa *fru*? ¿Diferencias machos/hembras? | Se expresa **más fuertemente en machos** |
| ¿Cuántos alelos? ¿Cómo serían las gametas? | Existen **2 alelos**. Homocigota fru–/– → todas las gametas **"–"**. Heterocigota → **mitad "+" / mitad "–"**. Homocigota wt → todas **"+"** |
| ¿Cómo se comportaría un macho fru–/– vs. macho wt? | Esperaría **alteraciones en el comportamiento de apareo** |
| ¿Y una hembra fru–/– vs. hembra wt? | **Sin grandes cambios** (el gen se expresa poco en hembras) |

**Conclusión sobre el tipo de herencia:**
Los **machos mutantes homocigotas (–/–) prefieren machos** (no hembras, como sí hacen los wt). Los **heterocigotas (–/+) se comportan como wt** (normales) → por lo tanto el **alelo fru(–) es RECESIVO** y la **herencia es mendeliana simple**.

**Heredabilidad:**
> La **heredabilidad** es la importancia relativa de la **varianza genética** como determinante de la **varianza fenotípica**. Va de **0 a 1**. Acá es **alta (cercana a 1)** porque prácticamente **todos** los machos –/– muestran la preferencia → el rasgo tiene un **fuerte componente genético** en moscas.

**Cuadro de Punnett — cruza macho fru–/– × hembra fru–/+:**

|  | **fru –** | **fru –** |
|---|---|---|
| **fru –** | –/– | –/– |
| **fru +** | –/+ | –/+ |

- **50% –/+** → comportamiento **normal**.
- **50% –/–** → **preferencia por otros machos**.

> 🎯 **Lo que demuestra:** el alelo recesivo (sección 11), las gametas y la segregación (Mendel, sección 17) y el cuadro de Punnett (sección 17.2) son **exactamente las herramientas** que necesitás para predecir un **comportamiento**. La conducta de apareo es, en este caso, un **fenotipo mendeliano**.

---

## 19. Genética no mendeliana

No todos los rasgos siguen el patrón dominante/recesivo simple:

| Tipo | Definición | Ejemplo del slide |
|---|---|---|
| **Dominancia incompleta** | El heterocigota tiene un **fenotipo intermedio** entre los padres | Boca de dragón (*Antirrhinum*): roja (CRCR) × blanca (CWCW) → **rosa** (CRCW) |
| **Codominancia** | **Ambos** alelos se expresan **simultáneamente** en el heterocigota | Grupos sanguíneos **ABO** (genotipo IAIB → tipo **AB**) |
| **Alelos múltiples** | Existen **más de 2 alelos** de un gen a nivel de población (cada individuo lleva solo 2) | Color del pelaje en conejos (gen **C**: 4 alelos → negro, chinchilla, himalaya, albino) |

> 💡 **Sobre alelos múltiples:** aunque un individuo diploide solo puede tener **2 alelos**, la **población** puede tener **muchos** (en conejos: C > c^ch > c^h > c, con jerarquías de dominancia mixtas). El sistema ABO también es de alelos múltiples (I^A, I^B, i).

---

## 20. Mutaciones

**¿Qué son?** Errores de copiado que ocurren ocasionalmente al **replicarse el ADN**.

**Causas:**
- Errores en la **replicación** durante la división celular.
- Exposición a **mutágenos**.
- **Infección viral**.

Son **poco frecuentes** y suelen tener **efectos adversos** → por eso existen **enzimas reparadoras** del ADN.

**Distinción crucial (¡pregunta típica de examen!):**

| Tipo de mutación | ¿Dónde ocurre? | ¿Se transmite a la descendencia? |
|---|---|---|
| **En línea germinal** | Óvulos y espermatozoides | **SÍ** |
| **Somática** | Células del cuerpo | **NO** |

**Mutaciones cromosómicas (estructurales):** Borrado (deleción), Duplicación, Inversión, Inserción, Translocación.

**Mutaciones puntuales (a nivel de una base) — clasificación por efecto:**

| Tipo | ¿Qué pasa? | Ejemplo (Nivel proteína) |
|---|---|---|
| **Silenciosa** | Cambia la base pero el aminoácido **NO** cambia (gracias a la redundancia del código) | Lys → **Lys** |
| **Sin sentido (nonsense)** | El codón se convierte en un **STOP** prematuro → proteína truncada | → **STOP** |
| **Sentido erróneo (missense)** | Cambia a un aminoácido **diferente** | Lys → **Arg** o **Thr** |

> 🔑 **Reconectando:** la variante **H452Y** del receptor 5-HT2A (His → Tyr) es una **mutación de sentido erróneo (missense)**: cambia un aminoácido por otro y por eso altera la función del receptor.

---

## 21. 🔬 Cerrando el círculo (parte 2): del gen a la conducta

### 21.1 El 5-HT2A y la ansiedad (segundo paper)

El slide final presenta otro estudio: *"Cortical 5-HT2A Receptor Signaling Modulates Anxiety-Like Behaviors in Mice"* (Weisstaub et al.).

- Usaron ratones **knockout** del receptor (**htr2a–/–**, sin el gen) y comparados con **htr2a+/+** (normales).
- Midieron —otra vez— **los 3 niveles**:
  - **Comportamiento:** % de *freezing* (congelamiento por miedo), conducta tipo-ansiosa.
  - **Actividad cerebral/celular:** corrientes sinápticas (registros tipo el panel D/E).
  - **Molecular:** expresión de ARNm de *htr2a* en distintas regiones (corteza somatosensorial, estriado, tálamo) y niveles de **corticosterona** (hormona de estrés).
- **Mensaje:** la **señalización del receptor 5-HT2A cortical modula** los comportamientos tipo-ansiosos. Sacar/modificar el receptor (un cambio **molecular**) cambia la **conducta** y la fisiología del estrés.

> 🎯 **El viaje se completa:** la clase empezó diciendo que el comportamiento se estudia en niveles (cognitivo→molecular) y termina probándolo con un receptor concreto. **Memoria** (de Quervain) y **ansiedad** (Weisstaub), dos funciones psicológicas centrales, dependen —en parte— de **una sola proteína-receptor codificada por un gen.**

### 21.2 🔗 INTEGRACIÓN CON LA GUÍA 1 — Problema 4: el gen *FosB* (expresión génica ↔ conducta de crianza)

> Este problema es el **broche perfecto**: conecta el **dogma central** (expresión génica), la **herencia recesiva** (Mendel) y el tema central de la clase (gen → conducta). Además, *FosB* es un **gen de expresión temprana** (su producto es un factor de transcripción que **aumenta con la actividad/experiencia**) → es exactamente lo que representaba la "**Proteína A**" del experimento de la fuga (sección 2).

**Contexto:** el gen ***FosB*** y el **comportamiento maternal/de crianza** en ratonas.

| Pregunta de la guía | Respuesta razonada |
|---|---|
| ¿Por qué comparar supervivencia de crías de madres –/– vs. +/–? | Para ver la **función de *FosB* sobre el comportamiento de crianza** |
| ¿Por qué comparar cruzas con machos –/– vs. +/–? | Para **controlar** si el efecto depende del **genotipo de la madre** o del **padre** (ej.: estrés del macho que altere la crianza) |
| ¿Qué esperaban con ese análisis? | Descartar que *FosB* afecte el **desarrollo de la glándula mamaria** o la **nutrición de la leche** (y así poder atribuirlo al **comportamiento**) |
| ¿Por qué las madres heterocigotas no tienen déficit? | Porque el **alelo FosB(–) es RECESIVO** (igual lógica que *fru* en el Problema 3) |
| ¿Qué se ve en el gráfico? | El **tiempo en devolver las crías al nido**: las madres **FosB –/– tardan más** (déficit de crianza) |

**El control olfativo (¡y acá aparece el aprendizaje!):**
Quisieron descartar que el déficit fuera por **mala olfación** (que la madre no encuentre a las crías). Diseñaron una tarea de **discriminación de olores** usando **condicionamiento clásico**:

| Elemento del condicionamiento | En este experimento |
|---|---|
| **Estímulo condicionado (EC)** | El **odorante** |
| **Estímulo incondicionado (EI)** | El **dolor de panza** |
| **Respuesta condicionada (RC)** | La **evitación** del odorante |

- **Resultado:** a mayor concentración de odorante, **menos** eligen la solución con odorante (la asocian al estímulo aversivo y la evitan). **No hay diferencias** entre FosB(+/+) y FosB(–/–) → **la olfación está intacta**.
- **Conclusión:** el déficit de las madres –/– es **del comportamiento de crianza**, no sensorial.

**El experimento final (expresión génica):**
- Como el déficit es **específico de la crianza**, *FosB* debe actuar en **regiones cerebrales** que controlan esa conducta.
- Probaron si **exponer a la madre a las crías aumenta la expresión de *FosB***.
- **Resultado:** la exposición a la cría **aumenta la expresión de *FosB*** → *FosB* podría **mediar** los cambios cerebrales que la presencia de la cría genera.

> 🧠 **La gran síntesis de la Guía 1 + Clase 02:**
> - *fru* (Problema 3) muestra el lado **"genético/mendeliano"**: un **alelo** define un fenotipo conductual (apareo).
> - *FosB* (Problema 4) muestra el lado **"expresión génica"**: un gen se **enciende por la experiencia** (la cría) y permite la conducta (crianza).
> - Juntos demuestran las **dos caras** del dogma central aplicadas a la conducta: **qué heredás** (la secuencia) y **cómo se expresa** (la regulación, modulada por el ambiente → puente con la epigenética).

---

## 🧠 Mapa mental integrador (síntesis de toda la clase)

```
                    ¿POR QUÉ EL COMPORTAMIENTO?
                    (5 niveles: cognitivo→molecular)
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        NATURE/NURTURE   EXPERIMENTO       CASO TESTIGO
        (genes+ambiente)  fuga roedor      5-HT2A + memoria
                          (3 niveles)      (His/His vs His/Tyr)
                              │
              ═══════ CAJA DE HERRAMIENTAS MOLECULAR ═══════
                              │
   DOGMA CENTRAL:  ADN ──transcripción──► ARN ──traducción──► PROTEÍNA
        │              │                    │                    │
        ▼              ▼                    ▼                    ▼
   Estructura      Replicación          3 tipos ARN          4 niveles +
   (nucleótidos,   (semiconserv.,       (m, t, r)            funciones
   doble hélice,   Okazaki)             Código genético      (¡receptor!)
   A-T / G-C)          │                (AUG, STOP)
        │              ▼
        ▼         Cromosomas → Cariotipo (46, 23 pares)
   Purinas/            │
   Pirimidinas    Ciclo celular → MITOSIS (2n) / MEIOSIS (n)
                       │              └─ error: Down (trisomía 21)
                       ▼
                  Homólogos + ALELOS (homo/heterocigota, dom/rec)
                       │
                       ▼
                  HERENCIA: Mendel (1ª uniformidad, 2ª segregación)
                       │         Punnett · 3:1 · 9:3:3:1
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   No mendeliana   MUTACIONES      🔗 GUÍA 1:
   (dom.incompleta, (silenciosa,    Problema 3 (fru, recesivo)
   codominancia,    nonsense,       Problema 4 (FosB, expresión)
   alelos múltiples) missense)
                       │
              ═══════ VUELTA AL CASO TESTIGO ═══════
                       │
        H452Y = mutación missense (His→Tyr) en el receptor 5-HT2A
                       │
        ▼ UN CAMBIO MOLECULAR TREPA HASTA LA CONDUCTA ▼
        ADN → codón → aminoácido → proteína → neurona →
        circuito → MEMORIA (de Quervain) + ANSIEDAD (Weisstaub)
```

**La frase para llevarte:** *toda la Clase 02 es la demostración de una sola cadena causal —de la letra del ADN a la conducta— y de que esa cadena se puede medir, predecir (Mendel) y modular (expresión génica / ambiente).*

---

## ✅ Autoevaluación (poné a prueba lo que entendiste)

1. Enumerá los 5 niveles de análisis del comportamiento, de lo más global a lo más microscópico. ¿En cuáles dos se centra esta clase?
2. En el experimento de la respuesta de fuga, ¿para qué sirve el grupo "Naïve" (G4)? ¿Por qué es metodológicamente imprescindible?
3. ¿Qué relación encontraron entre los tres niveles de medición (conducta, amígdala, Proteína A) a medida que el predador se acercaba?
4. Escribí el dogma central indicando qué proceso ocurre en cada flecha y en qué compartimento celular sucede cada uno.
5. ¿Cuáles son las tres partes de un nucleótido? Diferenciá un nucleótido de ADN de uno de ARN.
6. ¿Por qué la unión A-T es más débil que la G-C? Clasificá las cuatro bases del ADN en purinas y pirimidinas.
7. Explicá por qué la replicación se llama "semiconservativa" y qué son los fragmentos de Okazaki.
8. ¿Cuántos cromosomas tiene una célula somática humana? ¿Y una gameta? Definí 2n y n.
9. Completá el cuadro: mitosis vs. meiosis (n° de divisiones, células resultantes, ploidía, variabilidad).
10. ¿Por qué el Síndrome de Down **no** es hereditario? ¿Qué error lo origina?
11. Definí: alelo, homocigota, heterocigota, dominante, recesivo.
12. Diferenciá cadena molde de cadena codificante en la transcripción. Si la cadena molde es `TAC GGA TT`, ¿cuál es la secuencia del ARNm?
13. ¿Qué diferencia hay entre la iniciación de la transcripción en procariotas (elementos –10 y –35) y en eucariotas (caja TATA + factores de transcripción)?
14. ¿Qué codón inicia la traducción y qué aminoácido codifica? Nombrá los tres codones STOP.
15. Enunciá la 1ª y la 2ª ley de Mendel. ¿Qué proporción fenotípica da una cruza Aa × Aa? ¿Y una dihíbrida AaBb × AaBb?
16. Resolvé con un cuadro de Punnett la cruza del **Problema 3**: macho fru–/– × hembra fru–/+. ¿Qué proporción de fenotipos esperás y qué significa cada uno?
17. ¿Por qué se concluye que el alelo *fru(–)* es recesivo y la herencia mendeliana simple? ¿Qué significa que la heredabilidad sea "cercana a 1"?
18. Diferenciá dominancia incompleta de codominancia, con un ejemplo de cada una.
19. Diferenciá mutación germinal de somática. ¿Cuál se transmite a la descendencia?
20. Clasificá las mutaciones puntuales (silenciosa, sin sentido, sentido erróneo). ¿De qué tipo es la variante H452Y del receptor 5-HT2A y por qué?
21. **(Problema 4)** ¿Por qué los investigadores hicieron el control de discriminación olfativa con condicionamiento clásico? Identificá el EC, el EI y la RC.
22. **(Integración)** Explicá, usando *fru* y *FosB*, las "dos caras" de la relación gen–conducta: lo que se hereda vs. cómo se expresa.

---

## 📖 Glosario rápido

| Término | Definición breve |
|---|---|
| **Alelo** | Forma alternativa de un gen, en el mismo locus de cromosomas homólogos |
| **Amígdala** | Región cerebral crítica para el miedo y la conducta de fuga |
| **Anticodón** | Triplete del ARNt complementario al codón del ARNm |
| **Cariotipo** | Foto ordenada de los cromosomas de una célula |
| **Codominancia** | Ambos alelos se expresan a la vez en el heterocigota (ej. AB) |
| **Codón** | Triplete de bases del ARNm que codifica un aminoácido |
| **Cromatina** | ADN + histonas empaquetados en el núcleo |
| **Cromosomas homólogos** | Par de cromosomas (uno materno, uno paterno) con los mismos genes |
| **Diploide (2n)** | Célula con dos juegos de cromosomas (somáticas: 46) |
| **Dogma central** | ADN → ARN → Proteína (flujo de la información) |
| **Dominancia incompleta** | El heterocigota tiene fenotipo intermedio (ej. flor rosa) |
| **Dominante / Recesivo** | Alelo que se expresa / que necesita dos copias para expresarse |
| **Enlace fosfodiéster** | Une nucleótidos (5'→3') en el esqueleto de ADN/ARN |
| **Epigenética** | Cambios en la expresión génica sin cambiar la secuencia (gen × ambiente) |
| **Exón / Intrón** | Región codificante / no codificante del pre-ARNm |
| **Fenotipo** | Características observables |
| **FosB** | Gen de expresión temprana; su expresión aumenta con la experiencia (crianza) |
| **fru (fruitless)** | Gen del comportamiento de apareo en moscas (herencia mendeliana) |
| **Gameta** | Célula sexual haploide (óvulo, espermatozoide) |
| **Genotipo** | Constitución genética |
| **Haploide (n)** | Célula con un solo juego de cromosomas (gametas: 23) |
| **Heredabilidad** | Proporción de la varianza fenotípica explicada por varianza genética (0–1) |
| **Heterocigota / Homocigota** | Alelos diferentes (Aa) / iguales (AA o aa) |
| **Histonas** | Proteínas sobre las que se enrolla el ADN (nucleosomas) |
| **Meiosis** | División que forma gametas haploides (4 células, variabilidad) |
| **Mitosis** | División que produce 2 células somáticas idénticas (2n) |
| **Missense (sentido erróneo)** | Mutación que cambia un aminoácido por otro |
| **Nonsense (sin sentido)** | Mutación que crea un codón STOP prematuro |
| **No disyunción** | Falla en la separación de cromosomas (origen del Down) |
| **Nucleótido** | Fosfato + azúcar + base nitrogenada |
| **Polimorfismo** | Variante génica frecuente en la población |
| **Replicación semiconservativa** | Cada hebra nueva se forma sobre una hebra molde vieja |
| **Splicing** | Eliminación de intrones y unión de exones |
| **Transcripción / Traducción** | ADN → ARN / ARN → Proteína |
| **5-HT2A (HTR2A)** | Receptor de serotonina; su variante H452Y afecta memoria y ansiedad |

---

*Fuentes: Slides de la Clase 02 (Imperatori & Koss, 2026) + Guía 1, Problemas 3 (fru) y 4 (FosB) resueltos. Las profundizaciones señaladas con 🧩 amplían puntos que los slides solo mencionan.*
