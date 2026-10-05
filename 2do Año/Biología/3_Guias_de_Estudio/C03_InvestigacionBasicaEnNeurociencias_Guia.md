# Clase 3 — Investigación Básica en Neurociencias
### Biología del Comportamiento · Universidad Favaloro · Turno vespertino 2026
*Docentes: Mariana Imperatori — Pablo Koss*

---

## 🧭 Hoja de ruta de la clase (el arco conceptual)

Esta clase **no es sobre un contenido**, sino sobre **cómo se construye el conocimiento** en neurociencias: qué se asume, cómo se descubrió lo que sabemos, y con qué herramientas se investiga hoy. El recorrido lógico de las diapositivas es:

1. **La premisa fundamental** → el cerebro es el órgano de la conducta y de la mente (Kandel). Si esto es cierto, la conducta puede *investigarse* biológicamente.
2. **¿Qué son las neurociencias?** → un abordaje multidisciplinario, con disciplinas y ramas.
3. **Historia / Doctrina de la Neurona** → cómo se descubrió la unidad del sistema nervioso (la neurona) y cómo se comunican las neuronas. Recorrido por **niveles de organización**: de la célula → al impulso eléctrico → a la transmisión química → a la sinapsis → a la plasticidad → a los microcircuitos → a los macrocircuitos.
4. **¿Cómo se investiga? Ética y modelos** → las 3 R, la normativa (CICUAL, ANMAT), y los modelos *in vivo / in vitro / in silico*.
5. **Tipos de modelos animales** → inducidos, espontáneos, genéticamente modificados; modelos de estrés/depresión.
6. **Herramientas genéticas** → knockout, knockin, condicional, CRISPR, antisentido.
7. **¿Qué modelamos y cómo lo evaluamos?** → modelado de enfermedades + pruebas conductuales + técnicas moleculares + conectómica.
8. **Ejemplos de investigación integradora** → papers reales que combinan todo el toolkit.
9. **Investigación en humanos** → registros, neuroimágenes, estimulación, muestras biológicas y multiómicas.

> **Idea-eje para el parcial:** La clase recorre una doble lógica simultánea — una **cronológica** (cómo evolucionó históricamente el saber) y una **de niveles de organización** (molécula → sinapsis → circuito → cerebro completo). Cada técnica que se presenta sirve para "ver" o "manipular" uno de esos niveles.

---

## 0. La premisa fundamental: el cerebro como órgano de la conducta

### La frase de Kandel
> *"Toda conducta es el resultado de la función cerebral. Lo que conocemos comúnmente como mente es un conjunto de operaciones que el cerebro lleva a cabo."*
> — Eric Kandel, *Principios de Neurociencia* (5.ª ed., 2013)

Esta es la **base epistemológica de toda la materia**: si la mente es lo que hace el cerebro, entonces emociones, memoria, decisiones, ansiedad o adicción pueden estudiarse con los métodos de la biología. Es la justificación de por qué un estudiante de Psicología estudia neuronas y técnicas de laboratorio.

### El espíritu del método científico (los epígrafes)
Las primeras láminas abren con citas que resumen una actitud científica:

| Autor | Idea central | Por qué importa |
|---|---|---|
| **A. Conan Doyle** (Sherlock Holmes) | No teorizar antes de tener los datos; el riesgo es "retorcer los hechos" para que encajen en la teoría. | Advierte contra el **sesgo de confirmación**. |
| **B. F. Skinner** | "Ciencia es la voluntad de aceptar los hechos aunque se opongan a los deseos." | La evidencia manda, no nuestras preferencias. |
| **John Donne** | Cuanto más crece la isla del conocimiento, más extensa es la costa de lo desconocido. | Todo descubrimiento abre nuevas preguntas. |
| **Anónimo** | "La perfección es enemiga de un buen comienzo." | Vale la pena empezar a investigar aunque no se tenga todo resuelto. |

### ¿Qué son las Neurociencias?
**Definición:** abordaje **multidisciplinario** de las **bases biológicas del comportamiento**.

```
                    NEUROCIENCIAS
        (bases biológicas del comportamiento)
                          │
        ┌─────────────────┴──────────────────┐
   DISCIPLINAS                            RAMAS
   (qué nivel/método)                  (qué pregunta)
   • Neuroanatomía                     • Molecular
   • Neuroquímica                      • Cognitiva
   • Neurofisiología                   • Clínica
   • Neuropsicología                   • Computacional
                                       • Del Desarrollo
                                       • Cultural
```

> **Truco para no confundir:** las **disciplinas** son las "lentes" o métodos clásicos (anatomía, química, fisiología, psicología); las **ramas** son los campos de aplicación o escalas de pregunta (de lo molecular a lo cultural).

---

## 1. Historia: la construcción de la Doctrina de la Neurona

> *"Bueno, vamo' a investigá'."* — (lámina de transición)

Toda esta sección responde a una pregunta: **¿cómo llegamos a saber que el cerebro está hecho de células individuales que se comunican?** El recorrido va de la estructura (la neurona) a la función (cómo dialogan las neuronas) y de ahí a los circuitos.

### 1.1. El gran debate: Reticularistas vs. Neuronistas

A fines del siglo XIX había dos teorías enfrentadas sobre la estructura del sistema nervioso:

| | **RETICULARISTAS** | **NEURONISTAS** |
|---|---|---|
| **Tesis** | El SN es una **red continua** (un retículo): todo está fusionado, sin interrupciones. | El SN está formado por **células individuales y discretas** (neuronas) que solo se **contactan**, no se fusionan. |
| **Figuras** | Camillo **Golgi**, O. Deiters, J. von Gerlach | Santiago **Ramón y Cajal**, W. His, A. Forel |
| **Resultado** | Teoría finalmente **descartada**. | Teoría **correcta** → "Doctrina de la Neurona". |

**El detalle irónico y clave:** Golgi (reticularista) inventó la **tinción de plata** (método de Golgi) que teñía neuronas completas y al azar. Cajal (neuronista) usó *esa misma técnica* para demostrar… ¡lo contrario de lo que creía Golgi! Las imágenes mostraban células **separadas**.

> 🏅 **Premio Nobel de Fisiología o Medicina 1906:** compartido por **Golgi y Cajal**. En la ceremonia, ambos defendieron posturas opuestas. La historia le dio la razón a Cajal.

**El dibujo de Cajal** (la neurona piramidal con sus dendritas etiquetadas a, b, c, d): es uno de los íconos de la neurociencia. Cajal era un dibujante extraordinario y sus láminas siguen usándose como material didáctico.

### 1.2. Cómo se comunican las neuronas: la señal eléctrica y la química

> *(Lámina de Frankenstein)* — guiño a la idea histórica de "animar" tejido con electricidad: la **bioelectricidad**.

A partir de acá, el recorrido sigue la pregunta **¿cómo viaja la información?** — primero la señal *dentro* de la neurona (eléctrica), después *entre* neuronas (química).

#### Línea de tiempo de descubrimientos clave

| Año | Investigador(es) | Descubrimiento | Nivel |
|---|---|---|---|
| **1771** | Luigi **Galvani** | **"Electricidad animal"**: la pata de rana se contrae con estímulo eléctrico → el tejido nervioso/muscular usa electricidad. | Bioelectricidad |
| **1860** | **Meynert** y **Wernicke** | **Macrocircuitos**: haces de asociación que conectan regiones cerebrales. | Circuito (macro) |
| **1906** | Charles **Sherrington** | Acuña el término **"sinapsis"**: el punto de contacto (no de continuidad) entre dos neuronas. | Sinapsis (concepto) |
| **1926** | Otto **Loewi** | **Vagusstoff**: prueba que la transmisión del impulso puede ser **química**, no solo eléctrica. | Transmisión química |
| **1950** | De Robertis y Couteaux | **Vesículas sinápticas**: la base estructural (microscopía electrónica) del almacenamiento de neurotransmisor. | Sinapsis (estructura) |
| **1952** | **Fatt** y **Katz** | **Neurotransmisión química cuántica**: potenciales espontáneos en la unión neuromuscular. | Transmisión química |
| **1959** | John **Eccles** | **Microcircuitos inhibitorios** (células de Renshaw, IPSP). | Circuito (micro) |
| **1963** | **Hodgkin** y **Huxley** | **Potencial de acción**: mecanismo iónico de la señal eléctrica (axón gigante de calamar). | Señal eléctrica |
| **1973** | **Bliss** y **Lomo** | **LTP** (potenciación a largo plazo): plasticidad sináptica. | Plasticidad |
| **1994** | **Nakanishi** | **Circuito asociado a una conducta** (efecto Bruce). | Circuito-conducta |

> ⚠️ **Ojo:** las diapositivas **no** presentan estos hitos en orden cronológico estricto, sino por **lógica conceptual** (de la señal eléctrica → química → estructura → plasticidad → circuitos). Esta tabla los ordena por año para que tengas el mapa temporal completo; abajo se explican en el orden de la clase.

#### Galvani (1771) — "Electricidad animal"
Observó que las patas de rana se contraían al aplicarles corriente. Fue la primera evidencia de que el tejido excitable funciona con **electricidad**: nace la **electrofisiología**.

#### Hodgkin y Huxley (1963) — El potencial de acción
Usaron el **axón gigante del calamar** (¡tan grueso que se le podían meter electrodos adentro!) para describir cómo los flujos de **Na⁺ y K⁺** a través de la membrana generan el potencial de acción. El registro clásico muestra el pico que sube hasta ~+40 mV desde un reposo de ~−70 mV.
> **Por qué el calamar:** el tamaño del axón (modelo "elegido por su conveniencia técnica") permitió mediciones imposibles en mamíferos. Es un ejemplo perfecto de cómo **la elección del modelo habilita el descubrimiento** (idea que vuelve más adelante con los modelos animales).

#### Otto Loewi (1926) — La transmisión química ("Vagusstoff")
Loewi soñó el experimento (literalmente, anotó la idea de madrugada). Estimuló el **nervio vago** de un corazón de rana en una cámara, y luego pasó ese líquido a un **segundo corazón** sin estimular: el segundo corazón **también enlenteció su ritmo**. Conclusión: la estimulación del vago liberó una **sustancia química** (luego identificada como **acetilcolina**) que transmitió la señal.
> 🔑 Este experimento demostró que la comunicación neuronal no es solo eléctrica: hay **mensajeros químicos** (neurotransmisores). Es la piedra fundacional de toda la **neuroquímica** y, más tarde, de la neuropsicofarmacología (¡tu Clase 9!).

#### Charles Sherrington (1906) — La sinapsis
Antes de verla, Sherrington **dedujo** su existencia y le puso nombre: la punta de la ramificación axónica **no es continua** con la siguiente célula, sino que está "meramente en contacto". A ese contacto especializado lo llamó **sinapsis**. (Esto da la razón a Cajal sobre el debate reticularista.)

#### Fatt y Katz (1952) — Neurotransmisión química, ahora medida
En la **unión neuromuscular** registraron fluctuaciones espontáneas de voltaje (los futuros "potenciales miniatura"). Mostraron que la liberación de neurotransmisor es **cuántica** (en paquetes) — base de la teoría de la liberación vesicular.

#### De Robertis y Couteaux (1950) — Las vesículas sinápticas
Con **microscopía electrónica** vieron por primera vez las **vesículas sinápticas** (los "sacos" que contienen el neurotransmisor) en la terminal presináptica. ¡Le pusieron estructura física a lo que Fatt y Katz medían eléctricamente!
> 🇦🇷 **Dato local:** Eduardo De Robertis fue un destacado investigador argentino. Es un buen ejemplo de ciencia hecha en la región.

#### Bliss y Lomo (1973) — Plasticidad: la LTP
Descubrieron la **Potenciación a Largo Plazo (LTP)** en el **hipocampo**: tras una estimulación de alta frecuencia, la respuesta sináptica (el EPSP) queda **aumentada durante horas**. El gráfico clásico muestra que tras varios "tétanos" (flechas), la amplitud sube a ~200-300% y se mantiene, mientras la vía control sigue en 100%.
> 🔑 **Importancia enorme:** la LTP es el principal **modelo celular del aprendizaje y la memoria** (conecta directamente con tus Clases de Neurobiología de la memoria). Es la base fisiológica del principio de Hebb: *"neuronas que se activan juntas, se conectan más fuerte"*.

#### Eccles (1959) — Microcircuitos inhibitorios
Describió la **inhibición recurrente** mediante las **células de Renshaw** en la médula espinal. El esquema clave:
- Una **motoneurona** envía una colateral de su axón a una **célula de Renshaw**.
- Esa sinapsis es **excitatoria** (colinérgica) → se bloquea con **dihidro-β-eritroidina** (antagonista de ACh).
- La célula de Renshaw, a su vez, **inhibe** a la motoneurona liberando **glicina** → genera un **IPSP** (potencial postsináptico inhibitorio) → se bloquea con **estricnina** (antagonista de glicina).

> **Para fijar:**
> - **EPSP** = potencial **excitatorio** (despolariza, acerca al disparo).
> - **IPSP** = potencial **inhibitorio** (hiperpolariza, aleja del disparo).
> - **Renshaw + estricnina/glicina** = circuito inhibitorio recurrente (autorregulación de la motoneurona).

#### Nakanishi (1994) — Un circuito ligado a una conducta concreta
Aquí el salto conceptual es enorme: ya no es "cómo funciona una sinapsis", sino **cómo un microcircuito específico produce una conducta**.
- **El efecto Bruce:** en ratones, una hembra preñada **interrumpe el embarazo** (bloqueo de la gestación) si percibe las **feromonas de un macho extraño** (distinto al padre). Es una memoria olfativa.
- El circuito está en el **bulbo olfatorio accesorio**, en sinapsis **dendrodendríticas** entre células mitrales (MC) y granulares (GC), reguladas por **glutamato (mGluR2)**, **GABA** y **noradrenalina**.
- El experimento farmacológico (gráfico de "pregnancy block %") muestra que activar/bloquear receptores específicos **modifica la formación de esa memoria olfativa** → demuestra causalidad entre molécula, circuito y conducta.

#### Meynert y Wernicke (1860) — Macrocircuitos
Ya en el siglo XIX se intuían los **haces de asociación**: fascículos de fibras que conectan regiones cerebrales distantes.
> *"Los haces de asociación pueden compararse a un hilo conector que permite que una imagen eleve a la otra sobre el umbral de la consciencia."* — Meynert, 1865

Esta intuición es el antecedente histórico de la **conectómica** moderna (que veremos al final).

> 🧩 **Síntesis de la sección histórica (niveles de organización):**
> **Molécula/ión** (Galvani, H&H, Loewi) → **Sinapsis** (Sherrington, Fatt-Katz, De Robertis) → **Plasticidad** (Bliss-Lomo) → **Microcircuito** (Eccles) → **Circuito-conducta** (Nakanishi) → **Macrocircuito** (Meynert-Wernicke). Cada técnica posterior de la clase permite "mirar" alguno de estos niveles.

---

## 2. ¿Cómo se investiga? Ética y modelos experimentales

> *(Lámina del Dr. Nick / Simpson con la jeringa)* — transición humorística hacia la **experimentación**.

Antes de tocar un animal, hay un marco **ético y legal** que ordena toda la investigación biomédica.

### 2.1. El principio de las 3 R (Russell y Burch, 1959)

Es el corazón de la ética de experimentación con animales. Aparece tanto en la normativa argentina como en formularios internacionales.

| R | Significado | Pregunta guía |
|---|---|---|
| **Reemplazo** (Replacement) | Sustituir animales por **métodos alternativos** (experimentos *in vitro*, cultivos celulares, modelos por computadora). | ¿Es posible lograr el objetivo **sin** animales? |
| **Reducción** (Reduction) | Usar el **mínimo número** de animales necesario para resultados significativos (buen diseño experimental, estadística adecuada). | ¿Cómo uso la **menor cantidad** posible? |
| **Refinamiento** (Refinement) | Mejorar técnicas y condiciones para **minimizar el sufrimiento y el dolor**. | ¿Cómo reduzco el malestar del animal? |

> 🧠 **Mnemotecnia:** **"Las 3 R: Reemplazo, Reducción, Refinamiento"** → *no usar si se puede evitar; usar pocos; hacerlos sufrir lo menos posible.*

### 2.2. El marco legal en Argentina
- **Disposición ANMAT 9236/2023** (Boletín Oficial 03/11/2023): aprueba el **Régimen de Buenas Prácticas en Bioterios**. Establece explícitamente que solo pueden usarse animales tras aplicar **rigurosamente las 3 R**, y que **no** podrán usarse si existe un método alternativo satisfactorio.
- **CICUAL** — **Comité Institucional de Cuidado y Uso de Animales de Laboratorio**: el organismo que, en cada institución, vela por el trato humanitario, promueve el reemplazo/reducción/refinamiento y aprueba (o no) los protocolos. Es el "filtro ético" obligatorio de cualquier proyecto con animales.

> **Para el parcial:** asociá **3 R → Russell y Burch**; **CICUAL → comité institucional que aprueba protocolos**; **ANMAT 9236/2023 → la norma argentina de bioterios**.

### 2.3. Modelos *in vivo*, *in vitro* e *in silico*

| Tipo | Qué es | Ejemplos |
|---|---|---|
| **In vivo** | En un **organismo vivo** completo. | Mosca, pez cebra, ratón, rata, primate. |
| **In vitro** | En **células/tejidos** fuera del organismo ("en vidrio"). | Cultivos celulares, organoides, microscopía. |
| **In silico** | Modelos **computacionales** / simulaciones. | Modelado de proteínas, redes neuronales. |

#### Comparación de modelos animales clásicos

| Modelo | Ventajas | Limitaciones |
|---|---|---|
| **Mosca de la fruta** (*Drosophila melanogaster*) | Fácil de trabajar, generación corta, bajo costo. | Genéticamente lejana del humano, anatomía simple, sin sistema inmune adaptativo. |
| **Pez cebra** (*Danio rerio*) | Alta tasa reproductiva, desarrollo externo (se ve el embrión), similitud genética. | Flexibilidad, predictividad y valor traslacional **moderados**. |
| **Ratón** (*Mus musculus*) | **Conducta compleja**, órganos homólogos al humano, similitud genética. | Costos de cría muy altos, ciclo experimental largo, **restricciones éticas**. |
| **Modelos in vitro** | Fáciles, bajo costo de mantenimiento, ciclo corto. | Sistema **simplificado**, muy controlado, **pobre correlación** con mecanismos *in vivo*. |

> **El gran trade-off (lámina NAM):** a medida que el modelo se acerca al humano —de cultivos 2D → organoides 3D → "brain-on-a-chip" → pez cebra → roedores → roedores xenografiados → primates no humanos— **aumenta** la relevancia fisiológica, la complejidad y la validez aparente (*face validity*), pero **disminuye** la justificación ética y el rendimiento/costo-eficiencia. Los **NAM** (*New Approach Methods*, métodos sin animales) buscan correrse hacia el extremo *in vitro* / *in silico*.

#### Tres perspectivas para elegir un modelo
- **Evolutiva:** ¿qué tan cercano filogenéticamente es al humano?
- **Biomédica:** ¿qué tan bien reproduce la enfermedad/proceso de interés?
- **Ética:** ¿es justificable el uso de ese animal?

---

## 3. Tipos de modelos animales

No todos los modelos se construyen igual. La "torta" de modelos:

| Categoría | Cómo se genera |
|---|---|
| **Inducidos** | Se provoca la condición. Subtipos: por **estrés**, por **lesión**, por **fármaco/farmacología**, **biológicos**, por **mutación**. |
| **Espontáneos** | El animal desarrolla la condición naturalmente. |
| **De resistencia a enfermedad** | Estudia por qué algunos **no** enferman. |
| **Negativos** | No desarrollan la enfermedad esperada (controles). |
| **Genéticamente modificados** | Editados con **CRISPR/Cas9, ZFNs, SCNT**. |
| **De enfermedades no humanas / huérfanas** | Patologías propias del animal o enfermedades raras. |

### 3.1. Modelos de estrés / depresión (ejemplo desarrollado)
La lámina de "Animal Models" organiza los modelos de patología afectiva en tres lógicas:

- **Causación biológica:** inyección de **LPS** (inflamación), **bulbectomía** (extirpación del bulbo olfatorio), **corticosterona** en la bebida, modelos **genéticos**, manipulación **optogenética**.
- **Adversidad temprana** (*early life adversity*): **separación materna**, **cuidado materno deficiente** (*poor mothering*).
- **Estrés adulto** (*adult stress*): **derrota social** (*social defeat*), **UCMS** (estrés crónico leve impredecible), **indefensión aprendida** (*learned helplessness*).

> 🩺 **Nota clínica/psicológica:** estos modelos son la base experimental de buena parte de lo que sabemos sobre depresión, ansiedad y trauma. La **separación materna** y el **estrés crónico** modelan, respectivamente, factores de riesgo del desarrollo y del adulto — conceptos centrales en psicopatología.

---

## 4. Herramientas genéticas

Si la conducta tiene base biológica, manipular **genes** específicos permite probar relaciones **causa-efecto** (qué hace ese gen en el comportamiento).

### 4.1. Modelos de ratón genéticamente modificados

| Modelo | Qué hace | Cuándo se usa |
|---|---|---|
| **Knockout constitutivo** (*global*) | Se **elimina** un gen **en todas las células**, desde el embrión. | Ver el efecto de la ausencia total del gen. |
| **Knockout condicional / tejido-específico** | El gen se elimina **solo en ciertos tejidos** y/o **a partir de cierto momento**. Da control de **dónde** y **cuándo**. | Evitar que el KO sea letal o afecte todo el cuerpo. |
| **Knockout inducible** | El gen se apaga **al administrar un inductor** (ej. tamoxifeno, doxiciclina). | Estudiar el gen en el adulto, "encendiéndolo/apagándolo" a voluntad. |
| **Knockin** | Se **agrega/inserta** un gen (ej. la versión humana de un gen). | Cuando el ratón no expresa el gen, o su versión difiere del humano. |
| **Reporter** (reportero) | Se insertan genes que producen **proteínas fluorescentes** en una subpoblación de células. | **Identificar/visualizar** células específicas. |

> 🧠 **Mnemotecnia knockout:**
> - **Constitutivo** = "todo y siempre" (todas las células, desde el embrión).
> - **Condicional** = "elijo **dónde**".
> - **Inducible** = "elijo **cuándo**".

### 4.2. CRISPR/Cas9 (el "editor genético")

Mecanismo en 4 pasos:
1. Se **identifica** la secuencia de ADN diana (*target*).
2. El **ARN guía** (con secuencia complementaria) se une a la diana.
3. La enzima **Cas9** usa una secuencia llamada **PAM** para ubicar el sitio correcto, se une al ARN guía y **corta ambas hebras** del ADN.
4. Según cómo se programe, hay **3 resultados posibles**:
   - **a. Mutación:** la reparación introduce un cambio en el ADN.
   - **b. Deleción:** se corta a ambos lados de la diana y se **elimina** un fragmento.
   - **c. Inserción:** se "secuestra" el sistema de reparación para **insertar** una secuencia nueva.

> **Concepto clave:** CRISPR es preciso, barato y rápido → revolucionó la generación de modelos genéticos. (Mencionado junto con **ZFNs** y **SCNT** como otras técnicas de edición.)

### 4.3. Oligonucleótidos antisentido (ASO)

A diferencia de CRISPR (que edita el **ADN**), los **antisentido** actúan sobre el **ARN**. Tres mecanismos:

| Mecanismo | Cómo actúa | Resultado |
|---|---|---|
| **Reclutamiento de RNasaH** | El ASO se une al ARNm diana y recluta la enzima RNasaH. | **Degradación del ARNm** (se silencia el gen). |
| **Modificación del splicing** | El ASO altera el corte y empalme del ARN. | **Inclusión / exclusión de exones**. |
| **Targeting de miRNA** | El ASO secuestra un microARN. | **Secuestro del miRNA** → se libera la traducción. |

> 🩺 **Relevancia clínica:** los ASO ya son **fármacos reales** (ej. en atrofia muscular espinal). Modular el ARN sin tocar el genoma es una estrategia terapéutica de creciente importancia.

---

## 5. ¿Qué modelamos y cómo lo evaluamos?

### 5.1. ¿Qué modelamos?
La clase plantea ejemplos de patologías que se modelan en animales:
- **a) Enfermedad de Alzheimer**
- **b) Ansiedad**
- **c) Autismo**

> El desafío es la **validez del modelo**: ¿un ratón "ansioso" representa realmente la ansiedad humana? Por eso se combinan medidas conductuales + moleculares.

### 5.2. ¿Cómo evaluamos la conducta? (Pruebas conductuales)

| Prueba | Qué mide | Lógica |
|---|---|---|
| **C. elegans con sensor de Ca²⁺** | Actividad neuronal en tiempo real. | El calcio fluorescente marca neuronas activas. |
| **Y maze** (laberinto en Y) | **Memoria de trabajo** (*working memory*). | El roedor tiende a explorar el brazo nuevo (alternancia espontánea). |
| **EPM** (*Elevated Plus Maze*, laberinto en cruz elevado) | **Conductas tipo ansiedad**. | Más tiempo en brazos **abiertos** = menos ansiedad; refugio en brazos **cerrados** = más ansiedad. |
| **MWM** (*Morris Water Maze*, laberinto acuático) | **Aprendizaje y memoria espacial**. | El animal aprende a encontrar una plataforma oculta usando pistas espaciales. |

> 🧠 **Mnemotecnia de tests:**
> - **EPM → Espacios abiertos = ansiedad** (E de "Espacios" y de "Estrés").
> - **MWM → Memoria + Water (agua) = navegación espacial**.
> - **Y maze → Y de "working memory"** (alternancia).

### 5.3. Manipular circuitos: optogenética y quimiogenética
*(Las láminas las muestran como herramienta — "optogenetic manip." en modelos de estrés — y aparecen aplicadas en los papers de ejemplo.)*

- **Optogenética:** se insertan **proteínas sensibles a la luz** (opsinas) en neuronas específicas. Con un pulso de **luz** se activan o silencian neuronas con precisión de **milisegundos**. Permite probar causalidad: "si activo *esta* población, aparece *esta* conducta".
- **Quimiogenética (DREADDs):** receptores diseñados que **solo responden a una droga sintética** inerte. El ejemplo de los papers es **hM4Di** (receptor inhibitorio) activado por **CNO** (clozapina-N-óxido): al dar CNO, se **silencia** la población neuronal marcada. La sigla **hM4Di** + **CNO** = "apagar neuronas con una droga".

> 🔑 Ambas técnicas permiten pasar de **correlación** ("esta zona se activa cuando…") a **causalidad** ("si manipulo esta zona, cambia la conducta"). Es el salto metodológico más importante de la neurociencia de circuitos moderna.

### 5.4. ¿Cómo evaluamos a nivel molecular? (Técnicas bioquímicas)

| Técnica | Para qué sirve | En una frase |
|---|---|---|
| **Western Blot** | Detectar y **cuantificar una proteína específica**. | Se extraen proteínas → electroforesis (se separan por tamaño) → *blotting* → anticuerpos las detectan. |
| **ELISA** | **Cuantificar** un antígeno/proteína por colorimetría. | Antígeno fijado en placa + anticuerpo + reacción de color medida por absorbancia. |
| **Inmunofluorescencia** | **Localizar** proteínas/células en el tejido. | Cortes de tejido + anticuerpos fluorescentes → se ven al microscopio (contratinción con DAPI para núcleos). |

> **Diferencia clave para no confundir:**
> - **Western Blot / ELISA → "cuánto hay"** (cuantificación).
> - **Inmunofluorescencia → "dónde está"** (localización espacial en el tejido).

### 5.5. Conectómica
El **conectoma** es el mapa completo de las conexiones neuronales. Herramientas como el **Allen Brain Atlas** (Mouse Connectivity) permiten visualizar, en 3D, hacia dónde proyectan distintas regiones del cerebro del ratón.
> Es la versión tecnológica moderna de la intuición de **Meynert y Wernicke** sobre los haces de asociación (¡el círculo se cierra!).

---

## 6. Ejemplos de investigación integradora

La clase muestra **papers reales** para que veas cómo todas estas herramientas se combinan en un estudio. Lo importante no es memorizar los papers, sino reconocer **el toolkit en acción**.

| Estudio (título resumido) | Técnicas que combina | Hallazgo central |
|---|---|---|
| **Inhibición de proyecciones MR → giro dentado dorsal** | Quimiogenética (hM4Di/CNO) + **EPM** + **Open Field** + tareas de aprendizaje bajo estrés. | Inhibir esa vía produce un **efecto ansiolítico** y **mejora el aprendizaje** bajo estrés. |
| **Sobreactivación de CA3 dorsal y estrés por presenciar** (ratones machos adolescentes) | Marcador **c-fos** (actividad), **Golgi-Cox** (morfología dendrítica/espinas), virus **AAV-hM4Di**, batería conductual (**NOR, SOR, Y-maze, EPM, OF, Light-Dark Box**). | El estrés "por presenciar" sobreactiva **CA3 dorsal**, reduce dendritas/espinas y causa **déficit de memoria de reconocimiento**; silenciar CA3 lo revierte. |
| **La interacción social suprime el cáncer de mama vía un circuito córtico-amigdalino** | Conducta (**EPM, Light-Dark**), medición de **noradrenalina (NE)** tumoral, imágenes de bioluminiscencia, virus + **hM4Di**, trazado de circuito **ACC → BLA → … → nervio simpático → tumor**. | La **interacción social** reduce el crecimiento tumoral; la vía corteza-amígdala modula el sistema simpático y el microambiente del tumor. |

> 🧩 **Mensaje pedagógico:** un solo estudio moderno integra **conducta + manipulación de circuitos (quimiogenética) + marcadores moleculares + neuroanatomía + imágenes**. Esa es la lógica multidisciplinaria de las neurociencias en la práctica.

---

## 7. Investigación en humanos

> *"¿Y los animales humanos?"* — (lámina de transición)

En humanos **no** podemos hacer knockouts ni cortar tejido vivo, así que se usan métodos **no invasivos** (o mínimamente invasivos en contextos clínicos).

### 7.1. Registros de actividad cerebral

| Categoría | Técnica | Qué registra |
|---|---|---|
| **Señales continuas** | **EEG** (electroencefalografía) | Actividad eléctrica desde el **cuero cabelludo**. |
| | **ECoG** (electrocorticografía) | Actividad desde la **superficie cortical** (subdural). |
| | **Microelectrodo intracortical / MER** | Actividad de **neuronas individuales** (en cirugía). |
| | **MEG** (magnetoencefalografía) | Campos **magnéticos** generados por la actividad neuronal. |
| | **LFP** (potencial de campo local) | Actividad de **poblaciones** locales. |
| **Basadas en imagen** | **MRI / RMN** | **Estructura** cerebral. |
| | **fMRI** (RMN funcional) | **Función** (señal BOLD = flujo sanguíneo como proxy de actividad). |
| | **PET** | Metabolismo / receptores con trazadores radiactivos. |
| | **DTI** (imagen por tensor de difusión) | **Tractografía**: los haces de sustancia blanca. |

> **Compromiso clásico resolución espacial vs temporal:**
> - **EEG/MEG** → excelente resolución **temporal** (milisegundos), pobre **espacial**.
> - **fMRI** → buena resolución **espacial**, pobre **temporal** (segundos).
> - Por eso se combinan (**EEG-MEG, EEG-LFP, MEG-LFP**).

### 7.2. Neuroimágenes (aplicación)
La **tractografía (DTI)** permite, por ejemplo, mapear los haces de fibras alrededor de un **tumor** antes de una cirugía, combinada con **fMRI** para ubicar áreas funcionales (lenguaje, etc.) y definir los **límites de resección**. Une la herencia de Meynert/Wernicke (macrocircuitos) con la medicina actual.

### 7.3. Estimulación cerebral

| Técnica | Cómo funciona | Invasividad |
|---|---|---|
| **rTMS** (estimulación magnética transcraneal repetitiva) | Bobina (figura-8 o H) genera campos magnéticos que estimulan la corteza. | **No invasiva**. |
| **tDCS** (estimulación transcraneal por corriente directa) | Electrodos (ánodo/cátodo) aplican corriente débil sobre el cuero cabelludo. | **No invasiva**. |
| **DBS** (estimulación cerebral profunda) | Electrodo implantado en estructuras profundas (ej. **núcleo accumbens**) + generador de pulsos. | **Invasiva** (quirúrgica). |

> 🩺 **Uso clínico:** rTMS y tDCS se investigan/usan en depresión; DBS se usa en Parkinson, TOC refractario, etc. Son herramientas que pasan **de la investigación a la terapéutica**.

### 7.4. Muestras biológicas *in vivo*
- **BDNF y ejercicio:** se miden diferencias arterio-venosas de **BDNF** (factor neurotrófico) entre cerebro y músculo durante el ejercicio. El BDNF está ligado a plasticidad, aprendizaje y estado de ánimo.
- **Polimorfismo COMT Val158Met:** la enzima **COMT** degrada dopamina en la corteza prefrontal. El alelo **Val** → más actividad enzimática → **menos dopamina prefrontal**; el alelo **Met** → menos actividad → **más dopamina prefrontal** (y mayor densidad de receptores D1).

> 🧠 **Súper relevante para Psicología:** el COMT Val158Met es un ejemplo emblemático de **interacción genes-conducta**: distintos genotipos se asocian con diferencias en **funciones ejecutivas y memoria de trabajo**. Es un puente directo con tu Clase 8 ("Interacción genes y ambiente").

### 7.5. Multiómicas post-mortem
En tejido cerebral humano (ej. **corteza prefrontal** de cohortes con esquizofrenia/trastorno bipolar vs. controles) se integran:
- **Cuantificación de proteínas** (proteómica, LC-MS/MS).
- **Regulación de la expresión** (eQTL, pQTL): qué variantes genéticas controlan los niveles de ARN/proteína.
- **Co-localización, mediación, causalidad, pleiotropía** → para **priorizar genes candidatos** y vincularlos a estudios de asociación (GWAS).

> Es el nivel más "ómico" e integrador: cruza genoma, transcriptoma y proteoma para entender patologías psiquiátricas.

---

## 🗺️ Síntesis integradora (mapa mental de la clase)

```
                    EL CEREBRO ES EL ÓRGANO DE LA CONDUCTA (Kandel)
                                      │
                ┌─────────────────────┼─────────────────────┐
                ▼                     ▼                     ▼
        ¿QUÉ SABEMOS?          ¿CÓMO INVESTIGAR?       ¿EN QUÉ NIVEL?
     (Doctrina de la Neurona)   (ética + modelos)     (molécula→cerebro)
                │                     │                     │
   ┌────────────┴───────┐      ┌──────┴───────┐    ┌────────┴────────┐
   Reticularistas vs.    Galvani→H&H→Loewi    3 R (Russell-Burch)   ANIMALES:
   Neuronistas           →Sherrington→Fatt-Katz  CICUAL / ANMAT      in vivo
   (Golgi vs Cajal)      →De Robertis→Bliss-Lomo  in vivo/vitro/silico  • conducta (EPM,
   Nobel 1906            →Eccles→Nakanishi                              MWM, Y-maze)
                         →Meynert-Wernicke      HERRAMIENTAS:          • circuitos (opto/
                                                • KO/KI/condicional      quimiogenética)
                                                • CRISPR / antisentido • molecular (WB,
                                                                         ELISA, IF)
                                                                       • conectoma
                                      │
                                      ▼
                              ¿Y EN HUMANOS?
                ┌──────────────┬──────────────┬──────────────┐
            Registros      Neuroimagen     Estimulación    Muestras
            (EEG, MEG,     (MRI, fMRI,      (rTMS, tDCS,    (BDNF, COMT,
             LFP, MER)      PET, DTI)        DBS)            multiómicas)
```

**La gran idea:** toda la clase muestra cómo se pasa de **observar** (correlación) a **manipular** (causalidad), y cómo cada técnica abre una "ventana" a un nivel distinto de organización — desde el ion hasta el cerebro humano completo.

---

## ✅ Autoevaluación

Respondé sin mirar (las respuestas están justo debajo):

1. ¿Cuál es la premisa de Kandel y por qué justifica que la conducta se estudie biológicamente?
2. Explicá el debate reticularistas vs. neuronistas: ¿qué sostenía cada postura, quiénes los lideraban y cómo terminó?
3. ¿Por qué es irónico que Cajal usara la técnica de Golgi?
4. ¿Qué demostró el experimento del doble corazón de rana de Otto Loewi?
5. ¿Qué diferencia hay entre un EPSP y un IPSP? ¿Qué neurotransmisor y qué antagonista intervienen en el circuito de Renshaw descrito por Eccles?
6. ¿Qué es la LTP, en qué estructura se describió y por qué es importante para la memoria?
7. Enumerá y explicá las **3 R**. ¿Quiénes las propusieron?
8. ¿Qué es el CICUAL y qué función cumple? ¿Cómo se relaciona con la Disposición ANMAT 9236/2023?
9. Compará ventajas y limitaciones de la mosca, el pez cebra y el ratón como modelos.
10. ¿Cuál es el *trade-off* entre justificación ética y relevancia fisiológica en la elección de un modelo (idea de los NAM)?
11. Diferenciá knockout **constitutivo**, **condicional** e **inducible**. ¿Qué es un ratón **reporter**?
12. Describí los 4 pasos del mecanismo CRISPR/Cas9 y sus 3 resultados posibles. ¿Sobre qué molécula actúa CRISPR vs. los antisentido?
13. ¿Qué mide cada prueba: Y-maze, EPM y MWM?
14. ¿Qué permiten la optogenética y la quimiogenética que no permiten las técnicas de mera observación? Explicá hM4Di/CNO.
15. Diferenciá Western Blot, ELISA e inmunofluorescencia (cuantificar vs. localizar).
16. ¿Qué es el conectoma y con qué intuición histórica del siglo XIX se conecta?
17. Ordená estas técnicas humanas según resolución temporal vs. espacial: EEG, fMRI, MEG. ¿Por qué se combinan?
18. Diferenciá rTMS, tDCS y DBS por mecanismo e invasividad.
19. Explicá el polimorfismo COMT Val158Met y por qué es relevante para la cognición/psicología.
20. ¿Qué tipo de información integran las multiómicas post-mortem?

<details>
<summary><b>👉 Respuestas (clic para desplegar)</b></summary>

1. "Toda conducta es resultado de la función cerebral; la mente es un conjunto de operaciones del cerebro." Si la mente es lo que hace el cerebro, puede estudiarse con métodos biológicos.
2. **Reticularistas** (Golgi, Deiters, von Gerlach): el SN es una red continua. **Neuronistas** (Cajal, His, Forel): son células discretas que solo se contactan. Ganaron los neuronistas (Doctrina de la Neurona); Nobel 1906 compartido Golgi-Cajal.
3. Golgi inventó la tinción de plata creyendo en el retículo, pero Cajal la usó para probar **lo contrario** (neuronas separadas).
4. Que la transmisión del impulso nervioso puede ser **química**: estimular el vago liberó una sustancia (Vagusstoff = acetilcolina) que enlenteció un segundo corazón.
5. EPSP = excitatorio (despolariza); IPSP = inhibitorio (hiperpolariza). Renshaw: recibe input colinérgico (ACh, bloqueado por dihidro-β-eritroidina) e inhibe a la motoneurona con **glicina** (bloqueada por **estricnina**), generando un IPSP.
6. LTP = aumento duradero de la eficacia sináptica tras estimulación de alta frecuencia; descrita por Bliss y Lomo en el **hipocampo**; es el modelo celular del aprendizaje/memoria (principio de Hebb).
7. **Reemplazo** (usar alternativas), **Reducción** (mínimo número de animales), **Refinamiento** (minimizar sufrimiento). Russell y Burch.
8. Comité Institucional de Cuidado y Uso de Animales de Laboratorio; aprueba protocolos y vela por el trato ético. La Disposición ANMAT 9236/2023 (Buenas Prácticas en Bioterios) exige aplicar las 3 R y recomienda el CICUAL.
9. Mosca: barata/rápida pero lejana genéticamente y sin inmunidad adaptativa. Pez cebra: prolífico, desarrollo externo, similitud genética, pero valor traslacional moderado. Ratón: conducta compleja y órganos homólogos, pero caro, ciclo largo y con restricciones éticas.
10. A más cercanía al humano → más relevancia fisiológica/complejidad/validez aparente, pero menor justificación ética y costo-eficiencia. Los NAM buscan reemplazar animales por métodos in vitro/in silico.
11. Constitutivo = gen eliminado en todas las células desde el embrión. Condicional = solo en ciertos tejidos/momentos (controla "dónde"). Inducible = se apaga con un inductor (controla "cuándo"). Reporter = inserta proteínas fluorescentes para visualizar células.
12. (1) Identificar diana, (2) ARN guía se une, (3) Cas9 + PAM corta ambas hebras, (4) mutación / deleción / inserción. CRISPR edita el **ADN**; los antisentido actúan sobre el **ARN**.
13. Y-maze = memoria de trabajo; EPM = ansiedad (brazos abiertos/cerrados); MWM = aprendizaje y memoria espacial.
14. Permiten establecer **causalidad** (manipular y ver el efecto en la conducta), no solo correlación. hM4Di es un DREADD inhibitorio que, al recibir la droga CNO, silencia las neuronas marcadas.
15. WB y ELISA cuantifican ("cuánto hay" de una proteína); inmunofluorescencia localiza ("dónde está" en el tejido).
16. Mapa completo de conexiones neuronales (ej. Allen Brain Atlas); se conecta con los haces de asociación de Meynert y Wernicke (macrocircuitos).
17. Resolución temporal: EEG/MEG (ms) > fMRI (s). Resolución espacial: fMRI > EEG/MEG. Se combinan para tener buena resolución espacial **y** temporal.
18. rTMS = campos magnéticos, no invasiva. tDCS = corriente directa débil por electrodos, no invasiva. DBS = electrodo implantado en estructuras profundas, invasiva/quirúrgica.
19. COMT degrada dopamina prefrontal. Val → más degradación → menos dopamina; Met → menos degradación → más dopamina (y más D1). Se asocia a diferencias en funciones ejecutivas y memoria de trabajo (interacción genes-conducta).
20. Integran genoma/expresión (eQTL, pQTL), proteómica y datos de GWAS para priorizar genes candidatos en patologías psiquiátricas.

</details>

---

## 📚 Glosario rápido

| Término | Definición breve |
|---|---|
| **Doctrina de la Neurona** | El SN está formado por células individuales (neuronas) que se contactan, no se fusionan. |
| **Sinapsis** | Punto de contacto funcional entre dos neuronas (término de Sherrington). |
| **Potencial de acción** | Señal eléctrica que recorre el axón (flujos de Na⁺/K⁺); descrito por Hodgkin y Huxley. |
| **Vagusstoff / ACh** | Sustancia química (acetilcolina) que demostró la transmisión química (Loewi). |
| **Vesícula sináptica** | "Saco" que almacena neurotransmisor en la terminal presináptica. |
| **EPSP / IPSP** | Potencial postsináptico **excitatorio** (despolariza) / **inhibitorio** (hiperpolariza). |
| **LTP** | Potenciación a largo plazo; fortalecimiento sináptico duradero; base celular de la memoria. |
| **Célula de Renshaw** | Interneurona inhibitoria (glicina) de la médula; inhibición recurrente de motoneuronas. |
| **Conectoma** | Mapa completo de las conexiones del sistema nervioso. |
| **3 R** | Reemplazo, Reducción, Refinamiento (ética de uso de animales; Russell y Burch). |
| **CICUAL** | Comité que aprueba y supervisa el uso ético de animales de laboratorio. |
| **In vivo / in vitro / in silico** | En organismo vivo / en células fuera del organismo / en simulación computacional. |
| **NAM** | *New Approach Methods*: métodos alternativos al uso de animales. |
| **Knockout (KO)** | Animal al que se le elimina un gen (constitutivo, condicional o inducible). |
| **Knockin (KI)** | Animal al que se le inserta/agrega un gen. |
| **Ratón reporter** | Expresa proteínas fluorescentes para visualizar células específicas. |
| **CRISPR/Cas9** | Sistema de edición del **ADN** (corta con Cas9 guiada por ARN; usa PAM). |
| **Antisentido (ASO)** | Oligonucleótidos que actúan sobre el **ARN** (degradación, splicing, miRNA). |
| **Optogenética** | Control de neuronas con **luz** (opsinas), precisión de milisegundos. |
| **Quimiogenética (DREADDs)** | Control de neuronas con una **droga** sintética (ej. hM4Di + CNO = silenciar). |
| **Western Blot** | Cuantificación de una proteína (separación por electroforesis + anticuerpos). |
| **ELISA** | Cuantificación colorimétrica de un antígeno. |
| **Inmunofluorescencia** | Localización de proteínas/células en tejido con anticuerpos fluorescentes. |
| **EEG / ECoG / MEG / LFP / MER** | Registros de actividad eléctrica/magnética a distinta escala/invasividad. |
| **fMRI (BOLD)** | RMN funcional: usa el flujo sanguíneo como proxy de actividad. |
| **DTI / Tractografía** | Imagen de los haces de sustancia blanca. |
| **PET** | Imagen metabólica/de receptores con trazadores radiactivos. |
| **rTMS / tDCS / DBS** | Estimulación magnética / por corriente / profunda (las dos primeras no invasivas; DBS invasiva). |
| **BDNF** | Factor neurotrófico ligado a plasticidad, aprendizaje y estado de ánimo. |
| **COMT Val158Met** | Polimorfismo que regula la dopamina prefrontal (Val = menos DA; Met = más DA). |
| **eQTL / pQTL** | Variantes genéticas que regulan los niveles de ARN (e) o proteína (p). |

---

### 🔗 Puentes con otras clases
- **Loewi (transmisión química) →** Clase 9 (Neuropsicofarmacología) y Clase 13 (Psicodélicos).
- **LTP / Bliss-Lomo →** Clases de Neurobiología de la memoria.
- **COMT Val158Met / modelos genéticos →** Clase 8 (Interacción genes y ambiente).
- **DBS en núcleo accumbens / modelos de estrés →** Clases de Adicción (10 y 11).

> **Cómo estudiar esta clase:** es **metodológica**. No te pierdas memorizando cada paper; entendé **qué herramienta sirve para qué nivel** (molécula, sinapsis, circuito, conducta, cerebro humano) y **la diferencia observar vs. manipular**. Si podés explicar la tabla de la línea de tiempo y la de técnicas humanas, tenés el núcleo del parcial.
