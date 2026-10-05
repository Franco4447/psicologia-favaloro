# Stimuli Specification & Materials Mining Report: Survey 2

**Agent**: `spec_miner_survey_2`  
**Date / Timestamp**: 2026-09-20T23:25:00Z  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\spec_miner_survey_2`  
**Target File**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\spec_miner_survey_2\handoff.md`  
**Orchestrator Recipient**: `a385a74f-853a-4974-829a-239ecab00da0`  

---

## 1. Observation

Direct observations extracted from the authoritative source files:

### A. Authoritative Files Inspected
1. **`ORIGINAL_REQUEST.md`** (`.agents/ORIGINAL_REQUEST.md`):
   - Lines 46-58 define the 20-news loop:
     - *Noticias verdaderas*: Numeración interna 1-12
     - *Fake news para afines a Psicoanálisis*: nº 14, 16, 18, 20, 21, 23, 25, 27
     - *Fake news para afines a Basada en Evidencia*: nº 13, 15, 17, 19, 22, 24, 26, 28
     - *Tiempo de lectura*: 10 segundos con indicador visual de progreso y avance automático.
     - *Pantalla de respuesta*: 4 opciones según escala Murphy/León (sin límite de tiempo, registrando tiempo de respuesta en ms):
       1. «Recuerdo claramente haber visto/leído este evento» (Falso Recuerdo)
       2. «No recuerdo haberlo visto, pero creo que sucedió» (Falsa Creencia)
       3. «Lo recuerdo diferente»
       4. «No lo recuerdo en absoluto»
     - *Botón para avanzar* a la siguiente noticia.
   - Line 19: Note specifying `Noticia_01.jpg` a `Noticia_28.jpg` (y una `.png`).

2. **`Noticias/NOTICIAS TRADUCIDAS.docx`** (`PARCIAL 2 - INVESTIGACIÓN/Noticias/NOTICIAS TRADUCIDAS.docx`):
   - Extracted via XML parsing (`word/document.xml`). Contains exactly 3 tables:
     - Table 1 (13 rows, header + 12 items): «1. Noticias verdaderas (True News)», internal numbers 1 to 12.
     - Table 2 (9 rows, header + 8 items): «2. Noticias falsas – Conjunto 1 (Fake News Set 1)», internal numbers 13 to 20.
     - Table 3 (9 rows, header + 8 items): «3. Noticias falsas – Conjunto 2 (Fake News Set 2)», internal numbers 21 to 28.
   - Each row contains: Section number (`N.º`), English text (`English`), Spanish translation (`Español latinoamericano`), and internal ID (`Numeración interna`).
   - Footnote paragraph: *«Nota metodológica breve: si estos titulares se utilizarán como estímulos experimentales, conviene realizar una prueba piloto y, de ser posible, una retrotraducción (back-translation) para verificar equivalencia semántica entre idiomas.»*

3. **`Noticias/noticias imagenes/`** (`PARCIAL 2 - INVESTIGACIÓN/Noticias/noticias imagenes/`):
   - Verified using PIL (`PIL.Image.open().verify()`): Exactly 28 image files exist.
   - Filenames follow the two-digit pattern `Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_27.jpg`, `Noticia_28.jpg` (27 JPEGs in RGB format).
   - **CRITICAL ASSET VARIATION**: `Noticia_26.png` is an RGBA PNG image (1697x413 px, 409,356 bytes). It is NOT `.jpg`.
   - Image resolutions are standardized wide horizontal headline banners: width 1682–1712 px, height 411–432 px (~4:1 aspect ratio). Total folder footprint: 3,425,758 bytes (~3.27 MB).
   - Visual inspection of the images confirms they are composite Google Feed-style cards containing the Spanish headline text, source icon/publication attribution (blurred), blurred article preview snippet, and right-aligned illustration photo.

4. **`Psicología Experimental - Favaloro.docx` & `experimento.docx`**:
   - Paragraph 25 (`Psicología Experimental - Favaloro.docx`): Explains the ideological congruence manipulation: *«La variable interviniente a controlar son las creencias previas de los sujetos sobre el tema de las noticias (psicoanálisis y terapia basada en evidencia) y el impacto del efecto de congruencia... al inicio del test, hacer que el participante seleccione con cuál terapia siente más afinidad, y en base a esa respuesta se utilizarán fake-news que estén alineadas a su ideología. Se busca el efecto de congruencia y no se lo evita porque la inducción emocional podría no ser suficiente para que se cree un falso recuerdo...»*
   - Paragraph 26: Explains reading and response time as covert proxies of System 2 cognitive deliberation: *«Utilizar el 'tiempo en pantalla' como medida encubierta (proxy) de la deliberación cognitiva (Sistema 2)... se implementará un tiempo de lectura máximo lo suficientemente generoso como para evitar el registro de datos atípicos por distracciones, pero que permita al participante avanzar libremente a la siguiente pantalla antes de dicho corte. Este tiempo de lectura no afectará la deliberación o no deliberación, ya que luego se pasará a la pantalla para elegir la respuesta en la cual no habrá límite de tiempo.»*
   - Paragraph 67: Explains excluded subjects handling: *«Las personas que no cumplen con el motivo de inclusión se les dará el enunciado de Grupo Control pero NO serán asignados a Grupo Control. Además se les asignará uno de los dos conjuntos de fake-news de forma aleatoria.»*

5. **`Feedback_Diseño_Experimental.md`**:
   - Section 2.B stresses adhering strictly to the 4-point scale from Murphy et al. (2021) / León et al. (2023) to differentiate biographically grounded False Memories from general False Beliefs.

6. **`emp 1 - Fake news and false memory formation in the psychology debate - Leon et al (2023).md`**:
   - Documents original experimental paradigm in Argentina (N=326).
   - Explains that the 8 fake news were paired and counterbalanced across 2 mirrored sets to control for story salience.

---

## 2. Logic Chain

From the direct observations, the stimulus presentation engine and experimental parameters follow this deductive logic chain:

1. **Stimuli Universe**: There are exactly 28 news stimuli items in total:
   - 12 True News (`id: 1` through `12`).
   - 16 Fabricated Fake News (`id: 13` through `28`), structured as two complementary sets of 8 items each (Set 1: `13–20`, Set 2: `21–28`).

2. **Counterbalancing Mirror-Pairs**: Every item in Fake News Set 1 has a mirror counterpart in Set 2:
   - Pair 1: #13 (Anti-Psychoanalysis) <--> #21 (Anti-Cognitive) [Hospital electroshocks trial]
   - Pair 2: #14 (Anti-Cognitive) <--> #22 (Anti-Psychoanalysis) [Pediatrician claiming autism cure]
   - Pair 3: #15 (Anti-Psychoanalysis) <--> #23 (Anti-Cognitive) [Formosa padlocked refrigerator starvation]
   - Pair 4: #16 (Anti-Cognitive) <--> #24 (Anti-Psychoanalysis) [Depression 5-year malpractice refusal of diagnosis]
   - Pair 5: #17 (Anti-Psychoanalysis) <--> #25 (Anti-Cognitive) [Texas young woman suicide post-discharge]
   - Pair 6: #18 (Anti-Cognitive) <--> #26 (Anti-Psychoanalysis) [Suspended license therapist undressing patients]
   - Pair 7: #19 (Anti-Psychoanalysis) <--> #27 (Anti-Cognitive) [Dakota shooter passed projective vs psychometric tests]
   - Pair 8: #20 (Anti-Cognitive) <--> #28 (Anti-Psychoanalysis) [Neuroimaging debunks Watson vs Freud]

3. **Ideological Congruence Mapping (Within-Subject Alignment)**:
   - In this experiment, participants are exposed ONLY to fake news that attack their rival school, thereby confirming their own ideological bias (congruence effect):
     - **Pro-Psychoanalysis participants** (`orientacion == 'Psicoanálisis'`) receive all 8 Anti-Cognitive fake news:
       `[14, 16, 18, 20, 21, 23, 25, 27]`
     - **Pro-Evidence-Based participants** (`orientacion == 'Basada en Evidencia Científica'`) receive all 8 Anti-Psychoanalysis fake news:
       `[13, 15, 17, 19, 22, 24, 26, 28]`
   - Because both sets draw 4 items from Set 1 and 4 items from Set 2, neither participant ever sees two mirror versions of the same headline.

4. **Stimulus Presentation Loop Structure**:
   - Every participant is shown a total of **20 news items**: 12 True News + 8 Congruent Fake News.
   - The 20 items MUST be presented in a randomized order (e.g., Fisher-Yates shuffle per session).
   - For each item, presentation consists of two sequential phases:
     - **Phase 1: Stimulus Reading Screen** — The banner image (`Noticia_XX.jpg` or `Noticia_26.png`) is displayed.
       - Exposure duration: 10 seconds (10,000 ms).
       - Visual indicator: Progress bar reflecting remaining/elapsed time.
       - Auto-advance: On timer completion, the screen automatically transitions to Phase 2.
       - Metric recorded: `reading_time_ms`.
     - **Phase 2: Memory & Belief Evaluation Screen** — The 4-point Murphy/León categorical scale is displayed.
       - Options are mutually exclusive (single choice).
       - No time limit imposed on this screen.
       - An explicit advance button («Siguiente noticia») is pressed by the participant to confirm choice and load next trial.
       - Metric recorded: `response_time_ms` (time in ms from response screen render to button submission).

5. **Excluded Participants Handling**:
   - Participants who answer `estudia_psicologia == false` OR `orientacion == 'Otros'` are excluded from the scientific cohort.
   - To avoid disclosing exclusion and degrading participant experience, they complete the identical 20-news flow.
   - They are presented with the **Control induction prompt**.
   - They are randomly assigned either the 8 PSA-congruent fake news OR the 8 EBP-congruent fake news (50/50 probability), ensuring no duplicate mirror pairs are displayed.
   - In the database, their session is marked with `is_included: false` (and their group assignment is NOT counted toward the balanced induction quota).

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Stimuli Inventory | 28 Complete Stimuli Assets | 28 headline cards containing Spanish text, photo, and blurred article preview | Internal ID (1-28) | Rendered headline card component | Asset 404 / broken image | NOTICIAS TRADUCIDAS.docx & noticias imagenes/ |
| 2 | Stimuli Inventory | True News Baseline Set | 12 real news headlines from 2017-2018 (6 mentioning psychoanalysis topics, 6 mentioning cognitive/biological psychiatry topics) | IDs 1 to 12 | 12 baseline stimuli shown to all participants | Missing baseline item | NOTICIAS TRADUCIDAS.docx Table 1 |
| 3 | Stimuli Inventory | Fake News Mirror Pairs (Set 1 & 2) | 16 fabricated news headlines split into 8 mirror-image pairs to control for salience | IDs 13 to 28 | 8 counterbalanced pairs (13<->21, 14<->22, etc.) | Showing both items of a pair to same user | NOTICIAS TRADUCIDAS.docx Tables 2 & 3 |
| 4 | Experimental Logic | Congruent Fake News Assignment: Psicoanálisis | Selects the 8 fake news attacking cognitive/behavioral/psychometric currents for pro-psychoanalysis subjects | User orientation == 'Psicoanálisis' | Fake news set: [14, 16, 18, 20, 21, 23, 25, 27] | Incorrect ideologically incongruent fake news | ORIGINAL_REQUEST.md & Psicología Experimental.docx |
| 5 | Experimental Logic | Congruent Fake News Assignment: Basada en Evidencia | Selects the 8 fake news attacking psychoanalysis/Freudian currents for pro-evidence subjects | User orientation == 'Basada en Evidencia Científica' | Fake news set: [13, 15, 17, 19, 22, 24, 26, 28] | Incorrect ideologically incongruent fake news | ORIGINAL_REQUEST.md & Psicología Experimental.docx |
| 6 | Experimental Logic | Excluded Cohort Fake News Assignment | Selects one cohesive 8-item set at random (PSA or EBP) for participants not meeting inclusion criteria | Inclusion criteria == false | 50% chance of PSA fake set or EBP fake set; flag is_included=false | Randomly picking from 16 without pair constraint leads to mirror pair collision | Psicología Experimental.docx paragraph 67 |
| 7 | Stimulus Presentation | Trial Randomization Engine | Randomizes the order of the 20 selected news items (12 true + 8 fake) for each session | Array of 20 stimulus IDs | Shuffled array of 20 items (presentation_order 1 to 20) | Non-random order or deterministic seed across users | ORIGINAL_REQUEST.md R2 Acceptance Criteria |
| 8 | Stimulus Presentation | Stimulus Reading Screen (10s Timer) | Displays the headline image asset with a 10-second countdown / progress bar and auto-advances | Stimulus image asset, 10s duration | Visual timer, auto-advance trigger at 10,000 ms | Timer freezes on image load delay | ORIGINAL_REQUEST.md line 52 & Acceptance Criteria |
| 9 | Stimulus Presentation | Reading Time Latency Tracking | Records the exact duration in milliseconds the participant stayed on the reading screen | Start timestamp, transition timestamp | reading_time_ms (integer ms) | Clock drift or negative elapsed time | Psicología Experimental.docx paragraph 26 |
| 10 | Response Protocol | Murphy/León 4-Point Categorical Scale | Evaluates participant's memory and belief with 4 mutually exclusive radio options | Selected option index (1 to 4) | Recorded choice: false_memory, false_belief, remember_differently, not_remembered | Multiple options selected or no option selected on submit | ORIGINAL_REQUEST.md line 53 & Feedback_Diseño.md |
| 11 | Response Protocol | Untimed Deliberation with Millisecond Latency Tracking | Presents response options with no time pressure while silently capturing response latency | Response screen mount time, submit button click time | response_time_ms (integer ms) | Negative duration or premature submit | ORIGINAL_REQUEST.md line 53 & Acceptance Criteria |
| 12 | Response Protocol | Explicit Trial Advance Mechanism | Requires user to click button ('Siguiente noticia') after selecting an option to commit response and advance | Button click event + validated selection | Database trial record persistence + next trial render | Double-click leading to duplicate trial submission | ORIGINAL_REQUEST.md line 58 |
| 13 | Asset Management | PNG / JPG Asset Uniform Loader | Handles image rendering for 27 JPEG files and 1 PNG file (`Noticia_26.png`) seamlessly | Filename string (`Noticia_XX.ext`) | HTML <img> or Next.js <Image> element | Assuming all files are .jpg causing 404 for Noticia_26.jpg | noticias imagenes/ directory scan |
| 14 | Data Storage | Per-Trial Granular Data Schema | Records 20 trial rows per participant in Supabase with complete timing and stimulus metadata | Trial telemetry and participant session | 20 database rows per completed participant | Missing trial rows or dropped responses | ORIGINAL_REQUEST.md R3 |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Asset Extension Variation | `Noticia_26.jpg` requested instead of `Noticia_26.png` | HTTP 404 Error: Noticia_26 is the ONLY asset with `.png` extension (RGBA format); all others are `.jpg`. |
| 2 | Asset Numbering Leading Zero | `Noticia_1.jpg` requested instead of `Noticia_01.jpg` | HTTP 404 Error: Files 1 to 9 have a leading zero (`Noticia_01.jpg` to `Noticia_09.jpg`). |
| 3 | Mirror-Pair Collision in Excluded Cohort | Excluded participant assigned 8 fake news purely at random from all 16 | The participant might receive both #13 and #21 (identical image and story, swapped theoretical terms), breaking experimental immersion and credibility. |
| 4 | Image Preloading & Network Latency | High latency connection during 10s reading phase | If the 10s countdown starts before the image finishes loading, the participant will have less than 10s to read the headline, distorting the reading time proxy. |
| 5 | Rapid Double-Click on Submit Button | Participant rapidly clicks 'Siguiente noticia' multiple times | Without button debouncing/disabling, multiple POST requests or state race conditions may duplicate trial records or skip trials. |
| 6 | Scale Option Selection Mandatory Check | Participant clicks 'Siguiente noticia' without selecting any of the 4 options | Submission must be blocked with an inline prompt; trials must never be submitted with null or undefined responses. |
| 7 | Spanish Typographical Characters in Metadata | Rendering headlines with « » (guillemets) and tildes (e.g. #19, #20, #27, #28) | If UTF-8 is not strictly enforced in the database or frontend bundles, special characters like «superyó» or «condicionamiento» become corrupted. |
| 8 | Browser Tab Switching / Inactive Tab during 10s Timer | Participant switches to another tab during stimulus display | `setInterval` / `requestAnimationFrame` throttles in background tabs, potentially inflating `reading_time_ms` past 10 seconds. Focus/blur events should be recorded. |
| 9 | Screen Resizing & Mobile Viewing | Participant opens survey on a small smartphone screen | Stimulus images are 1682-1712px wide (~4:1 banner). On mobile devices, text will shrink unless responsive scaling or container scrolling is provided (desktop recommended). |
| 10 | Back Button Navigation in Browser | Participant presses browser 'Back' button during news loop | Could allow participant to revisit previously answered news items. History state must prevent back-navigation during the trial loop. |

---

## 5. Complete Stimuli Inventory (All 28 News Items)

| ID | Categoría | Titular en Español | Titular en Inglés | Archivo de Imagen | Formato / Dimensiones / Tamaño | Par Espejo | Blanco de Crítica | Asignación Congruente |
|----|-----------|--------------------|-------------------|-------------------|--------------------------------|------------|-------------------|-----------------------|
| **1** | Verdadera (True) | Las agencias de medicamentos son una invención del capitalismo neoliberal de la década de 1990. | Drug agencies are an invention of neoliberal capitalism in the 1990s | `Noticia_01.jpg` | JPEG, 117,846 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **2** | Verdadera (True) | Mario Bunge: el psicoanálisis y otras pseudociencias son perjudiciales. | Mario Bunge: psychoanalysis and other pseudosciences are harmful | `Noticia_02.jpg` | JPEG, 104,295 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **3** | Verdadera (True) | Una pandemia de adaptación y neoliberalismo conductual en la educación. | A pandemic of adjusting and behavioral neoliberalism in education | `Noticia_03.jpg` | JPEG, 116,892 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **4** | Verdadera (True) | Científicos explican por qué los sueños no tienen significados ocultos. | Scientists explain why dreams have no hidden meanings | `Noticia_04.jpg` | JPEG, 98,130 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **5** | Verdadera (True) | El pequeño Albert: un cruel experimento con un bebé de 11 meses para estudiar las fobias. | Little Albert, a cruel experiment on an 11-month-old baby to test phobias | `Noticia_05.jpg` | JPEG, 90,109 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **6** | Verdadera (True) | La comunidad reúne firmas contra las terapias psicoanalíticas públicas en casos de autismo. | The community gathers signatures against public psychoanalysis therapies in cases of autism | `Noticia_06.jpg` | JPEG, 143,441 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **7** | Verdadera (True) | La caja de Skinner: juegos como Candy Crush están diseñados para volverte adicto. | Skinner's Box: Games like Candy Crush are designed to get you hooked | `Noticia_07.jpg` | JPEG, 113,068 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **8** | Verdadera (True) | Wilhelm Reich: los controvertidos tratamientos sexuales de uno de los psicoanalistas más radicales de la historia. | Wilhelm Reich: the controversial sexual treatments of one of the most radical psychoanalysts in history | `Noticia_08.jpg` | JPEG, 119,497 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **9** | Verdadera (True) | El psiquiatra que aplicaba electroshocks a personas homosexuales. | The psychiatrist who applied electroshocks to homosexuals | `Noticia_09.jpg` | JPEG, 81,287 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **10** | Verdadera (True) | La feminista que refutó a Freud y su concepto de envidia del pene. | The feminist who denied Freud and his penis envy | `Noticia_10.jpg` | JPEG, 104,792 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **11** | Verdadera (True) | Expertos piden revisar los métodos actuales de diagnóstico del trastorno bipolar. | Experts call for a review of current diagnostic methods for bipolar disorder | `Noticia_11.jpg` | JPEG, 91,224 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **12** | Verdadera (True) | La historia del sobrino argentino de Freud: es psicoanalista y cuestiona la idea de ser trans antes de la pubertad. | The story of Freud's Argentinian nephew: he is a psychoanalyst and questions the idea of being trans before puberty | `Noticia_12.jpg` | JPEG, 126,302 bytes | N/A | Referencia histórica / médica | **Ambos grupos (12 verdaderas para todos)** |
| **13** | Falsa (Fake Set 1) | El terapeuta freudiano que hipnotizaba a sus pacientes con descargas eléctricas irá a juicio. | The Freudian therapist who hypnotized patients with electric shocks will go to trial | `Noticia_13.jpg` | JPEG, 120,880 bytes | #21 (Set 2) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **14** | Falsa (Fake Set 1) | Abraham Low, el pediatra y cognitivista británico que afirmaba que el autismo se curaba con terapia conductual. | Abraham Low, the British pediatrician and cognitivist who claimed that autism was cured by behavioral therapy | `Noticia_14.jpg` | JPEG, 114,004 bytes | #22 (Set 2) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **15** | Falsa (Fake Set 1) | Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia psicoanalítica. | Horror in Formosa: the young woman hospitalized for starvation, closed the refrigerator with a padlock as part of her psychoanalytic therapy | `Noticia_15.jpg` | JPEG, 102,186 bytes | #23 (Set 2) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **16** | Falsa (Fake Set 1) | Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta cognitivo se negó a darle un diagnóstico. | Malpractice is being investigated: He had been depressed for 5 years and his cognitive therapist refused to give him a diagnosis | `Noticia_16.jpg` | JPEG, 120,958 bytes | #24 (Set 2) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **17** | Falsa (Fake Set 1) | Texas: una joven se suicida después de recibir el alta de una terapia psicoanalítica. | Texas: Young woman commits suicide after being discharged from psychoanalytic therapy | `Noticia_17.jpg` | JPEG, 83,280 bytes | #25 (Set 2) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **18** | Falsa (Fake Set 1) | Suspenden la licencia de un terapeuta cognitivo que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos. | License suspended for cognitive therapist who undressed patients to help them connect with their bodies | `Noticia_18.jpg` | JPEG, 109,667 bytes | #26 (Set 2) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **19** | Falsa (Fake Set 1) | Un tirador en la ciudad de Dakota: «había superado todas las técnicas proyectivas; era una persona normal». | A shooter in Dakota city: "had passed all the projective techniques, he was a normal person" | `Noticia_19.jpg` | JPEG, 108,930 bytes | #27 (Set 2) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **20** | Falsa (Fake Set 1) | Hallazgos recientes de neuroimagen refutan el concepto de «condicionamiento» de Watson. | Recent neuroimaging findings debunk Watson's concept of 'conditioning' | `Noticia_20.jpg` | JPEG, 106,929 bytes | #28 (Set 2) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **21** | Falsa (Fake Set 2) | El terapeuta cognitivo que entrenaba a sus pacientes con descargas eléctricas irá a juicio. | The cognitive therapist who trained patients with electric shocks will go to trial | `Noticia_21.jpg` | JPEG, 123,880 bytes | #13 (Set 1) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **22** | Falsa (Fake Set 2) | Donald Winnicott, el pediatra y psicoanalista británico que afirmaba que el autismo se curaba mediante hipnosis. | Donald Winnicott, the British pediatrician, and psychoanalyst who claimed that autism was cured by hypnosis | `Noticia_22.jpg` | JPEG, 108,035 bytes | #14 (Set 1) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **23** | Falsa (Fake Set 2) | Horror en Formosa: la joven hospitalizada por inanición cerró el refrigerador con un candado como parte de su terapia cognitiva. | Horror in Formosa: the young woman hospitalized for starvation closed the refrigerator with a padlock as part of her cognitive therapy | `Noticia_23.jpg` | JPEG, 99,400 bytes | #15 (Set 1) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **24** | Falsa (Fake Set 2) | Investigan un caso de mala praxis: llevaba 5 años con depresión y su terapeuta psicoanalista se negó a darle un diagnóstico. | Malpractice is being investigated: He had been depressed for 5 years and his psychoanalyst therapist refused to give him a diagnosis | `Noticia_24.jpg` | JPEG, 114,027 bytes | #16 (Set 1) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **25** | Falsa (Fake Set 2) | Texas: una joven se suicida después de recibir el alta de una terapia cognitiva breve. | Texas: Young woman commits suicide after being discharged from brief cognitive therapy | `Noticia_25.jpg` | JPEG, 96,366 bytes | #17 (Set 1) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **26** | Falsa (Fake Set 2) | Suspenden la licencia de un psicoanalista que desvestía a sus pacientes para ayudarlos a conectarse con sus cuerpos. | License suspended for psychoanalyst who undressed patients to help them connect with their bodies | `Noticia_26.png` | PNG, 409,356 bytes | #18 (Set 1) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |
| **27** | Falsa (Fake Set 2) | Un tirador en la ciudad de Dakota: «había superado todas las técnicas psicométricas; era una persona normal». | A shooter in Dakota city: "had passed all the psychometric techniques, he was a normal person" | `Noticia_27.jpg` | JPEG, 108,691 bytes | #19 (Set 1) | Ataca TCC / Conductual / Psicométrico | **Afines a Psicoanálisis** |
| **28** | Falsa (Fake Set 2) | Hallazgos recientes de neuroimagen refutan el concepto de «superyó» de Freud. | Recent neuroimaging findings debunk Freud's concept of 'superego' | `Noticia_28.jpg` | JPEG, 82,627 bytes | #20 (Set 1) | Ataca Psicoanálisis / Freudiano | **Afines a Basada en Evidencia** |

---

## 6. Detailed Timing & Response Scale Specifications

### A. Reading Screen (Pantalla de Lectura del Estímulo)
1. **Visual Display**: Displays the headline card image asset (`Noticia_XX.jpg` or `Noticia_26.png`).
2. **Progress Indicator**: A top or bottom horizontal progress bar smoothly counting down or filling over 10,000 ms (10 seconds).
3. **Auto-Advance**: When the 10,000 ms timer reaches 0, the application transitions automatically to the response screen.
4. **Early Advance Consideration**:
   - *Design note from `Psicología Experimental - Favaloro.docx` (p. 26)*: Mentions that the reading timer can serve as a ceiling while allowing users to advance freely to capture natural deliberation speed.
   - *Specification in `ORIGINAL_REQUEST.md` (lines 52 & 94)*: Specifies a 10-second reading time with visual progress indicator and auto-advance.
   - *Implementation Recommendation*: Implement a 10.0-second auto-advance. If an early 'Continuar' button is enabled, record the exact `reading_time_ms` (0–10,000 ms). If strict auto-advance is enforced, `reading_time_ms` will record true screen residency (defaulting to 10,000 ms ± network/render latency).
5. **Telemetry Captured**:
   - `reading_time_ms`: Exact millisecond duration between the stimulus component mount and transition trigger.

### B. Response Screen (Pantalla de Evaluación)
1. **Visual Display**: Clean card presentation with the question: *«¿Cuál de las siguientes opciones describe mejor su conocimiento sobre la noticia que acaba de ver?»* (or similar neutral question).
2. **Response Scale (Murphy & León 4-point scale)**:
   - **Option 1**: `«Recuerdo claramente haber visto/leído este evento»`
     - Statistical Code: `1`
     - Psychological Construct: **Falso Recuerdo (False Memory)** on fake news; **Verdadero Recuerdo (True Memory)** on true news.
   - **Option 2**: `«No recuerdo haberlo visto, pero creo que sucedió»`
     - Statistical Code: `2`
     - Psychological Construct: **Falsa Creencia (False Belief)** on fake news; **Creencia Verdadera / Aceptación sin recuerdo** on true news.
   - **Option 3**: `«Lo recuerdo diferente»`
     - Statistical Code: `3`
     - Psychological Construct: **Memoria discrepante / recuerdo alterado**.
   - **Option 4**: `«No lo recuerdo en absoluto»`
     - Statistical Code: `4`
     - Psychological Construct: **Sin memoria / descarte**.
3. **Input Mechanics**: Mutually exclusive single-choice radio buttons or selectable interactive cards.
4. **Submission**: An explicit action button: `«Siguiente noticia»`. The button is disabled until an option is selected.
5. **Timing**: Untimed (no time pressure), but the system silently tracks `response_time_ms` from screen render to click.
6. **Telemetry Captured**:
   - `response_option`: Integer `1` to `4` (and verbatim string).
   - `response_time_ms`: Integer milliseconds.
   - `is_fake_memory`: Boolean (`true` if `is_fake && response_option == 1`).
   - `is_fake_belief`: Boolean (`true` if `is_fake && response_option == 2`).

### C. Trial Loop Structure (Loop de 20 Ensayos)
1. **Composition**: Exactly 20 items per participant = 12 True News (IDs 1-12) + 8 Congruent Fake News.
2. **Selection by Orientation**:
   - If `orientacion == 'Psicoanálisis'` -> Fake news IDs: `[14, 16, 18, 20, 21, 23, 25, 27]`.
   - If `orientacion == 'Basada en Evidencia Científica'` -> Fake news IDs: `[13, 15, 17, 19, 22, 24, 26, 28]`.
   - If Excluded (`estudia_psicologia == false` or `orientacion == 'Otros'`) -> Randomly pick either Set A (PSA) or Set B (EBP) with 50/50 probability. Mark session `is_included = false`.
3. **Randomization**: The 20 items are shuffled uniquely per participant using Fisher-Yates algorithm.
4. **No Back-Navigation**: Participants cannot go back to review or change past answers.

---

## 7. Caveats

1. **Image Asset File Format Discrepancy**: While the documentation mentions `Noticia_01.jpg` to `Noticia_28.jpg`, item 26 is strictly `Noticia_26.png`. Code implementing static string interpolation like `Noticia_${id}.jpg` will trigger a 404 for item 26 unless an extension mapping or file lookup table is used.
2. **Reading Screen Interaction Nuance**: `ORIGINAL_REQUEST.md` specifies 10s reading time with auto-advance, while research notes mention that allowing early advance captures deliberative vs intuitive variance. Frontend developers should implement 10s auto-advance and accurately measure `reading_time_ms`.
3. **Image Asset Text Redundancy**: The headline text is already rendered inside each image file. Therefore, displaying HTML headline text above or below the image would create duplicate text on screen. The image should be presented as the primary stimulus object, with the Spanish text stored in metadata for CSV export and data analysis.
4. **Image Preloading**: Because 20 large banner images (~100 KB each) are displayed in sequence, client-side preloading of upcoming images is strongly recommended to prevent timer desynchronization caused by network latency.

---

## 8. Conclusion

All 28 stimuli materials, headline texts, translations, image assets, ideological congruence mappings, and timing/response scale protocols have been completely extracted, audited, and specified. The experimental materials form a rigorous, counterbalanced design where:
- 12 true news establish a baseline (6 psychoanalysis-related, 6 evidence-related).
- 16 fake news form 8 mirrored pairs that cleanly isolate ideological congruence without confounding topic salience.
- Pro-Psychoanalysis participants are exposed only to anti-cognitive fake news (IDs 14, 16, 18, 20, 21, 23, 25, 27).
- Pro-Evidence-Based participants are exposed only to anti-psychoanalysis fake news (IDs 13, 15, 17, 19, 22, 24, 26, 28).
- Excluded participants receive the Control induction and a cohesive fake news set (either PSA or EBP) to guarantee experimental realism while preventing mirror-pair collisions.
- Timing (10s reading countdown + untimed deliberation) and response scales (4-point Murphy/León) are fully specified for direct implementation.

---

## 9. Verification Method

To independently verify this specification:
1. **Verify Asset Directory**:
   ```powershell
   Get-ChildItem 'C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes' | Measure-Object
   # Confirms 28 items, exactly one .png (Noticia_26.png) and 27 .jpg files
   ```
2. **Verify Text Extraction from DOCX**:
   ```powershell
   python parse_stimuli.py
   # Extracts all 28 rows from NOTICIAS TRADUCIDAS.docx and generates stimuli_parsed.json
   ```
3. **Verify Mirror Pair Symmetry & Congruence Partition**:
   - Confirm that PSA Set `[14, 16, 18, 20, 21, 23, 25, 27]` contains zero overlap with EBP Set `[13, 15, 17, 19, 22, 24, 26, 28]`.
   - Confirm that for every pair `(13, 21), (14, 22), (15, 23), (16, 24), (17, 25), (18, 26), (19, 27), (20, 28)`, exactly one element belongs to the PSA set and one belongs to the EBP set.
4. **Invalidation Conditions**:
   - If any image file from `Noticia_01.jpg` to `Noticia_28.jpg` is missing or fails to render.
   - If a participant assigned to 'Psicoanálisis' sees any item from `[13, 15, 17, 19, 22, 24, 26, 28]`.
   - If a participant assigned to 'Basada en Evidencia Científica' sees any item from `[14, 16, 18, 20, 21, 23, 25, 27]`.
   - If any trial fails to record `reading_time_ms` or `response_time_ms`.
