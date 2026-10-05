import json
import os

with open('stimuli_parsed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

img_dir = r"C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes"

pairs = {
    13: 21, 14: 22, 15: 23, 16: 24,
    17: 25, 18: 26, 19: 27, 20: 28,
    21: 13, 22: 14, 23: 15, 24: 16,
    25: 17, 26: 18, 27: 19, 28: 20
}

psycho_fake = [14, 16, 18, 20, 21, 23, 25, 27]
evid_fake = [13, 15, 17, 19, 22, 24, 26, 28]

report_lines = []

report_lines.append("# Stimuli Specification & Materials Mining Report: Survey 2")
report_lines.append("")
report_lines.append("**Agent**: `spec_miner_survey_2`  ")
report_lines.append("**Date / Timestamp**: 2026-09-20T23:25:00Z  ")
report_lines.append("**Working Directory**: `C:\\Users\\Fmendezcasariego\\OneDrive\\Carpetas\\Educación\\Universidad\\Favaloro\\Psicología\\.agents\\spec_miner_survey_2`  ")
report_lines.append("**Target File**: `C:\\Users\\Fmendezcasariego\\OneDrive\\Carpetas\\Educación\\Universidad\\Favaloro\\Psicología\\.agents\\spec_miner_survey_2\\handoff.md`  ")
report_lines.append("**Orchestrator Recipient**: `a385a74f-853a-4974-829a-239ecab00da0`  ")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# 1. Observation
report_lines.append("## 1. Observation")
report_lines.append("")
report_lines.append("Direct observations extracted from the authoritative source files:")
report_lines.append("")
report_lines.append("### A. Authoritative Files Inspected")
report_lines.append("1. **`ORIGINAL_REQUEST.md`** (`.agents/ORIGINAL_REQUEST.md`):")
report_lines.append("   - Lines 46-58 define the 20-news loop:")
report_lines.append("     - *Noticias verdaderas*: Numeración interna 1-12")
report_lines.append("     - *Fake news para afines a Psicoanálisis*: nº 14, 16, 18, 20, 21, 23, 25, 27")
report_lines.append("     - *Fake news para afines a Basada en Evidencia*: nº 13, 15, 17, 19, 22, 24, 26, 28")
report_lines.append("     - *Tiempo de lectura*: 10 segundos con indicador visual de progreso y avance automático.")
report_lines.append("     - *Pantalla de respuesta*: 4 opciones según escala Murphy/León (sin límite de tiempo, registrando tiempo de respuesta en ms):")
report_lines.append("       1. «Recuerdo claramente haber visto/leído este evento» (Falso Recuerdo)")
report_lines.append("       2. «No recuerdo haberlo visto, pero creo que sucedió» (Falsa Creencia)")
report_lines.append("       3. «Lo recuerdo diferente»")
report_lines.append("       4. «No lo recuerdo en absoluto»")
report_lines.append("     - *Botón para avanzar* a la siguiente noticia.")
report_lines.append("   - Line 19: Note specifying `Noticia_01.jpg` a `Noticia_28.jpg` (y una `.png`).")
report_lines.append("")
report_lines.append("2. **`Noticias/NOTICIAS TRADUCIDAS.docx`** (`PARCIAL 2 - INVESTIGACIÓN/Noticias/NOTICIAS TRADUCIDAS.docx`):")
report_lines.append("   - Extracted via XML parsing (`word/document.xml`). Contains exactly 3 tables:")
report_lines.append("     - Table 1 (13 rows, header + 12 items): «1. Noticias verdaderas (True News)», internal numbers 1 to 12.")
report_lines.append("     - Table 2 (9 rows, header + 8 items): «2. Noticias falsas – Conjunto 1 (Fake News Set 1)», internal numbers 13 to 20.")
report_lines.append("     - Table 3 (9 rows, header + 8 items): «3. Noticias falsas – Conjunto 2 (Fake News Set 2)», internal numbers 21 to 28.")
report_lines.append("   - Each row contains: Section number (`N.º`), English text (`English`), Spanish translation (`Español latinoamericano`), and internal ID (`Numeración interna`).")
report_lines.append("   - Footnote paragraph: *«Nota metodológica breve: si estos titulares se utilizarán como estímulos experimentales, conviene realizar una prueba piloto y, de ser posible, una retrotraducción (back-translation) para verificar equivalencia semántica entre idiomas.»*")
report_lines.append("")
report_lines.append("3. **`Noticias/noticias imagenes/`** (`PARCIAL 2 - INVESTIGACIÓN/Noticias/noticias imagenes/`):")
report_lines.append("   - Verified using PIL (`PIL.Image.open().verify()`): Exactly 28 image files exist.")
report_lines.append("   - Filenames follow the two-digit pattern `Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_27.jpg`, `Noticia_28.jpg` (27 JPEGs in RGB format).")
report_lines.append("   - **CRITICAL ASSET VARIATION**: `Noticia_26.png` is an RGBA PNG image (1697x413 px, 409,356 bytes). It is NOT `.jpg`.")
report_lines.append("   - Image resolutions are standardized wide horizontal headline banners: width 1682–1712 px, height 411–432 px (~4:1 aspect ratio). Total folder footprint: 3,425,758 bytes (~3.27 MB).")
report_lines.append("   - Visual inspection of the images confirms they are composite Google Feed-style cards containing the Spanish headline text, source icon/publication attribution (blurred), blurred article preview snippet, and right-aligned illustration photo.")
report_lines.append("")
report_lines.append("4. **`Psicología Experimental - Favaloro.docx` & `experimento.docx`**:")
report_lines.append("   - Paragraph 25 (`Psicología Experimental - Favaloro.docx`): Explains the ideological congruence manipulation: *«La variable interviniente a controlar son las creencias previas de los sujetos sobre el tema de las noticias (psicoanálisis y terapia basada en evidencia) y el impacto del efecto de congruencia... al inicio del test, hacer que el participante seleccione con cuál terapia siente más afinidad, y en base a esa respuesta se utilizarán fake-news que estén alineadas a su ideología. Se busca el efecto de congruencia y no se lo evita porque la inducción emocional podría no ser suficiente para que se cree un falso recuerdo...»*")
report_lines.append("   - Paragraph 26: Explains reading and response time as covert proxies of System 2 cognitive deliberation: *«Utilizar el 'tiempo en pantalla' como medida encubierta (proxy) de la deliberación cognitiva (Sistema 2)... se implementará un tiempo de lectura máximo lo suficientemente generoso como para evitar el registro de datos atípicos por distracciones, pero que permita al participante avanzar libremente a la siguiente pantalla antes de dicho corte. Este tiempo de lectura no afectará la deliberación o no deliberación, ya que luego se pasará a la pantalla para elegir la respuesta en la cual no habrá límite de tiempo.»*")
report_lines.append("   - Paragraph 67: Explains excluded subjects handling: *«Las personas que no cumplen con el motivo de inclusión se les dará el enunciado de Grupo Control pero NO serán asignados a Grupo Control. Además se les asignará uno de los dos conjuntos de fake-news de forma aleatoria.»*")
report_lines.append("")
report_lines.append("5. **`Feedback_Diseño_Experimental.md`**:")
report_lines.append("   - Section 2.B stresses adhering strictly to the 4-point scale from Murphy et al. (2021) / León et al. (2023) to differentiate biographically grounded False Memories from general False Beliefs.")
report_lines.append("")
report_lines.append("6. **`emp 1 - Fake news and false memory formation in the psychology debate - Leon et al (2023).md`**:")
report_lines.append("   - Documents original experimental paradigm in Argentina (N=326).")
report_lines.append("   - Explains that the 8 fake news were paired and counterbalanced across 2 mirrored sets to control for story salience.")
report_lines.append("")

# 2. Logic Chain
report_lines.append("---")
report_lines.append("")
report_lines.append("## 2. Logic Chain")
report_lines.append("")
report_lines.append("From the direct observations, the stimulus presentation engine and experimental parameters follow this deductive logic chain:")
report_lines.append("")
report_lines.append("1. **Stimuli Universe**: There are exactly 28 news stimuli items in total:")
report_lines.append("   - 12 True News (`id: 1` through `12`).")
report_lines.append("   - 16 Fabricated Fake News (`id: 13` through `28`), structured as two complementary sets of 8 items each (Set 1: `13–20`, Set 2: `21–28`).")
report_lines.append("")
report_lines.append("2. **Counterbalancing Mirror-Pairs**: Every item in Fake News Set 1 has a mirror counterpart in Set 2:")
report_lines.append("   - Pair 1: #13 (Anti-Psychoanalysis) <--> #21 (Anti-Cognitive) [Hospital electroshocks trial]")
report_lines.append("   - Pair 2: #14 (Anti-Cognitive) <--> #22 (Anti-Psychoanalysis) [Pediatrician claiming autism cure]")
report_lines.append("   - Pair 3: #15 (Anti-Psychoanalysis) <--> #23 (Anti-Cognitive) [Formosa padlocked refrigerator starvation]")
report_lines.append("   - Pair 4: #16 (Anti-Cognitive) <--> #24 (Anti-Psychoanalysis) [Depression 5-year malpractice refusal of diagnosis]")
report_lines.append("   - Pair 5: #17 (Anti-Psychoanalysis) <--> #25 (Anti-Cognitive) [Texas young woman suicide post-discharge]")
report_lines.append("   - Pair 6: #18 (Anti-Cognitive) <--> #26 (Anti-Psychoanalysis) [Suspended license therapist undressing patients]")
report_lines.append("   - Pair 7: #19 (Anti-Psychoanalysis) <--> #27 (Anti-Cognitive) [Dakota shooter passed projective vs psychometric tests]")
report_lines.append("   - Pair 8: #20 (Anti-Cognitive) <--> #28 (Anti-Psychoanalysis) [Neuroimaging debunks Watson vs Freud]")
report_lines.append("")
report_lines.append("3. **Ideological Congruence Mapping (Within-Subject Alignment)**:")
report_lines.append("   - In this experiment, participants are exposed ONLY to fake news that attack their rival school, thereby confirming their own ideological bias (congruence effect):")
report_lines.append("     - **Pro-Psychoanalysis participants** (`orientacion == 'Psicoanálisis'`) receive all 8 Anti-Cognitive fake news:")
report_lines.append("       `[14, 16, 18, 20, 21, 23, 25, 27]`")
report_lines.append("     - **Pro-Evidence-Based participants** (`orientacion == 'Basada en Evidencia Científica'`) receive all 8 Anti-Psychoanalysis fake news:")
report_lines.append("       `[13, 15, 17, 19, 22, 24, 26, 28]`")
report_lines.append("   - Because both sets draw 4 items from Set 1 and 4 items from Set 2, neither participant ever sees two mirror versions of the same headline.")
report_lines.append("")
report_lines.append("4. **Stimulus Presentation Loop Structure**:")
report_lines.append("   - Every participant is shown a total of **20 news items**: 12 True News + 8 Congruent Fake News.")
report_lines.append("   - The 20 items MUST be presented in a randomized order (e.g., Fisher-Yates shuffle per session).")
report_lines.append("   - For each item, presentation consists of two sequential phases:")
report_lines.append("     - **Phase 1: Stimulus Reading Screen** — The banner image (`Noticia_XX.jpg` or `Noticia_26.png`) is displayed.")
report_lines.append("       - Exposure duration: 10 seconds (10,000 ms).")
report_lines.append("       - Visual indicator: Progress bar reflecting remaining/elapsed time.")
report_lines.append("       - Auto-advance: On timer completion, the screen automatically transitions to Phase 2.")
report_lines.append("       - Metric recorded: `reading_time_ms`.")
report_lines.append("     - **Phase 2: Memory & Belief Evaluation Screen** — The 4-point Murphy/León categorical scale is displayed.")
report_lines.append("       - Options are mutually exclusive (single choice).")
report_lines.append("       - No time limit imposed on this screen.")
report_lines.append("       - An explicit advance button («Siguiente noticia») is pressed by the participant to confirm choice and load next trial.")
report_lines.append("       - Metric recorded: `response_time_ms` (time in ms from response screen render to button submission).")
report_lines.append("")
report_lines.append("5. **Excluded Participants Handling**:")
report_lines.append("   - Participants who answer `estudia_psicologia == false` OR `orientacion == 'Otros'` are excluded from the scientific cohort.")
report_lines.append("   - To avoid disclosing exclusion and degrading participant experience, they complete the identical 20-news flow.")
report_lines.append("   - They are presented with the **Control induction prompt**.")
report_lines.append("   - They are randomly assigned either the 8 PSA-congruent fake news OR the 8 EBP-congruent fake news (50/50 probability), ensuring no duplicate mirror pairs are displayed.")
report_lines.append("   - In the database, their session is marked with `is_included: false` (and their group assignment is NOT counted toward the balanced induction quota).")
report_lines.append("")

# 3. Features Discovered
report_lines.append("---")
report_lines.append("")
report_lines.append("## Features Discovered")
report_lines.append("")
report_lines.append("| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |")
report_lines.append("|---|----------|---------|-------------|--------|---------|----------------|----------------|")

features = [
    (1, "Stimuli Inventory", "28 Complete Stimuli Assets", "28 headline cards containing Spanish text, photo, and blurred article preview", "Internal ID (1-28)", "Rendered headline card component", "Asset 404 / broken image", "NOTICIAS TRADUCIDAS.docx & noticias imagenes/"),
    (2, "Stimuli Inventory", "True News Baseline Set", "12 real news headlines from 2017-2018 (6 mentioning psychoanalysis topics, 6 mentioning cognitive/biological psychiatry topics)", "IDs 1 to 12", "12 baseline stimuli shown to all participants", "Missing baseline item", "NOTICIAS TRADUCIDAS.docx Table 1"),
    (3, "Stimuli Inventory", "Fake News Mirror Pairs (Set 1 & 2)", "16 fabricated news headlines split into 8 mirror-image pairs to control for salience", "IDs 13 to 28", "8 counterbalanced pairs (13<->21, 14<->22, etc.)", "Showing both items of a pair to same user", "NOTICIAS TRADUCIDAS.docx Tables 2 & 3"),
    (4, "Experimental Logic", "Congruent Fake News Assignment: Psicoanálisis", "Selects the 8 fake news attacking cognitive/behavioral/psychometric currents for pro-psychoanalysis subjects", "User orientation == 'Psicoanálisis'", "Fake news set: [14, 16, 18, 20, 21, 23, 25, 27]", "Incorrect ideologically incongruent fake news", "ORIGINAL_REQUEST.md & Psicología Experimental.docx"),
    (5, "Experimental Logic", "Congruent Fake News Assignment: Basada en Evidencia", "Selects the 8 fake news attacking psychoanalysis/Freudian currents for pro-evidence subjects", "User orientation == 'Basada en Evidencia Científica'", "Fake news set: [13, 15, 17, 19, 22, 24, 26, 28]", "Incorrect ideologically incongruent fake news", "ORIGINAL_REQUEST.md & Psicología Experimental.docx"),
    (6, "Experimental Logic", "Excluded Cohort Fake News Assignment", "Selects one cohesive 8-item set at random (PSA or EBP) for participants not meeting inclusion criteria", "Inclusion criteria == false", "50% chance of PSA fake set or EBP fake set; flag is_included=false", "Randomly picking from 16 without pair constraint leads to mirror pair collision", "Psicología Experimental.docx paragraph 67"),
    (7, "Stimulus Presentation", "Trial Randomization Engine", "Randomizes the order of the 20 selected news items (12 true + 8 fake) for each session", "Array of 20 stimulus IDs", "Shuffled array of 20 items (presentation_order 1 to 20)", "Non-random order or deterministic seed across users", "ORIGINAL_REQUEST.md R2 Acceptance Criteria"),
    (8, "Stimulus Presentation", "Stimulus Reading Screen (10s Timer)", "Displays the headline image asset with a 10-second countdown / progress bar and auto-advances", "Stimulus image asset, 10s duration", "Visual timer, auto-advance trigger at 10,000 ms", "Timer freezes on image load delay", "ORIGINAL_REQUEST.md line 52 & Acceptance Criteria"),
    (9, "Stimulus Presentation", "Reading Time Latency Tracking", "Records the exact duration in milliseconds the participant stayed on the reading screen", "Start timestamp, transition timestamp", "reading_time_ms (integer ms)", "Clock drift or negative elapsed time", "Psicología Experimental.docx paragraph 26"),
    (10, "Response Protocol", "Murphy/León 4-Point Categorical Scale", "Evaluates participant's memory and belief with 4 mutually exclusive radio options", "Selected option index (1 to 4)", "Recorded choice: false_memory, false_belief, remember_differently, not_remembered", "Multiple options selected or no option selected on submit", "ORIGINAL_REQUEST.md line 53 & Feedback_Diseño.md"),
    (11, "Response Protocol", "Untimed Deliberation with Millisecond Latency Tracking", "Presents response options with no time pressure while silently capturing response latency", "Response screen mount time, submit button click time", "response_time_ms (integer ms)", "Negative duration or premature submit", "ORIGINAL_REQUEST.md line 53 & Acceptance Criteria"),
    (12, "Response Protocol", "Explicit Trial Advance Mechanism", "Requires user to click button ('Siguiente noticia') after selecting an option to commit response and advance", "Button click event + validated selection", "Database trial record persistence + next trial render", "Double-click leading to duplicate trial submission", "ORIGINAL_REQUEST.md line 58"),
    (13, "Asset Management", "PNG / JPG Asset Uniform Loader", "Handles image rendering for 27 JPEG files and 1 PNG file (`Noticia_26.png`) seamlessly", "Filename string (`Noticia_XX.ext`)", "HTML <img> or Next.js <Image> element", "Assuming all files are .jpg causing 404 for Noticia_26.jpg", "noticias imagenes/ directory scan"),
    (14, "Data Storage", "Per-Trial Granular Data Schema", "Records 20 trial rows per participant in Supabase with complete timing and stimulus metadata", "Trial telemetry and participant session", "20 database rows per completed participant", "Missing trial rows or dropped responses", "ORIGINAL_REQUEST.md R3")
]

for f in features:
    report_lines.append(f"| {f[0]} | {f[1]} | {f[2]} | {f[3]} | {f[4]} | {f[5]} | {f[6]} | {f[7]} |")

report_lines.append("")

# 4. Edge Cases
report_lines.append("---")
report_lines.append("")
report_lines.append("## Edge Cases")
report_lines.append("")
report_lines.append("| # | Feature | Input | Observed Behavior |")
report_lines.append("|---|---------|-------|-------------------|")

edge_cases = [
    (1, "Asset Extension Variation", "`Noticia_26.jpg` requested instead of `Noticia_26.png`", "HTTP 404 Error: Noticia_26 is the ONLY asset with `.png` extension (RGBA format); all others are `.jpg`."),
    (2, "Asset Numbering Leading Zero", "`Noticia_1.jpg` requested instead of `Noticia_01.jpg`", "HTTP 404 Error: Files 1 to 9 have a leading zero (`Noticia_01.jpg` to `Noticia_09.jpg`)."),
    (3, "Mirror-Pair Collision in Excluded Cohort", "Excluded participant assigned 8 fake news purely at random from all 16", "The participant might receive both #13 and #21 (identical image and story, swapped theoretical terms), breaking experimental immersion and credibility."),
    (4, "Image Preloading & Network Latency", "High latency connection during 10s reading phase", "If the 10s countdown starts before the image finishes loading, the participant will have less than 10s to read the headline, distorting the reading time proxy."),
    (5, "Rapid Double-Click on Submit Button", "Participant rapidly clicks 'Siguiente noticia' multiple times", "Without button debouncing/disabling, multiple POST requests or state race conditions may duplicate trial records or skip trials."),
    (6, "Scale Option Selection Mandatory Check", "Participant clicks 'Siguiente noticia' without selecting any of the 4 options", "Submission must be blocked with an inline prompt; trials must never be submitted with null or undefined responses."),
    (7, "Spanish Typographical Characters in Metadata", "Rendering headlines with « » (guillemets) and tildes (e.g. #19, #20, #27, #28)", "If UTF-8 is not strictly enforced in the database or frontend bundles, special characters like «superyó» or «condicionamiento» become corrupted."),
    (8, "Browser Tab Switching / Inactive Tab during 10s Timer", "Participant switches to another tab during stimulus display", "`setInterval` / `requestAnimationFrame` throttles in background tabs, potentially inflating `reading_time_ms` past 10 seconds. Focus/blur events should be recorded."),
    (9, "Screen Resizing & Mobile Viewing", "Participant opens survey on a small smartphone screen", "Stimulus images are 1682-1712px wide (~4:1 banner). On mobile devices, text will shrink unless responsive scaling or container scrolling is provided (desktop recommended)."),
    (10, "Back Button Navigation in Browser", "Participant presses browser 'Back' button during news loop", "Could allow participant to revisit previously answered news items. History state must prevent back-navigation during the trial loop.")
]

for ec in edge_cases:
    report_lines.append(f"| {ec[0]} | {ec[1]} | {ec[2]} | {ec[3]} |")

report_lines.append("")

# 5. Full Inventory Table
report_lines.append("---")
report_lines.append("")
report_lines.append("## 5. Complete Stimuli Inventory (All 28 News Items)")
report_lines.append("")
report_lines.append("| ID | Categoría | Titular en Español | Titular en Inglés | Archivo de Imagen | Formato / Dimensiones / Tamaño | Par Espejo | Blanco de Crítica | Asignación Congruente |")
report_lines.append("|----|-----------|--------------------|-------------------|-------------------|--------------------------------|------------|-------------------|-----------------------|")

for it in items:
    iid = it['id']
    sec = it['section'].split('(')[0].strip()
    esp = it['spanish'].replace('|', '\\|')
    eng = it['english'].replace('|', '\\|')
    img_name = it['image_file']
    
    # Check image stats
    img_path = os.path.join(img_dir, img_name)
    if os.path.exists(img_path):
        sz = os.path.getsize(img_path)
        ext = 'PNG' if img_name.endswith('.png') else 'JPEG'
    else:
        sz = 0
        ext = 'UNKNOWN'
        
    if iid <= 12:
        cat = "Verdadera (True)"
        counterpart = "N/A"
        target = "Referencia histórica / médica"
        congruence = "Ambos grupos (12 verdaderas para todos)"
    else:
        cat = "Falsa (Fake Set " + ("1" if iid <= 20 else "2") + ")"
        c_id = pairs[iid]
        counterpart = f"#{c_id} ({'Set 2' if iid <= 20 else 'Set 1'})"
        if iid in psycho_fake:
            target = "Ataca TCC / Conductual / Psicométrico"
            congruence = "Afines a Psicoanálisis"
        else:
            target = "Ataca Psicoanálisis / Freudiano"
            congruence = "Afines a Basada en Evidencia"
            
    report_lines.append(f"| **{iid}** | {cat} | {esp} | {eng} | `{img_name}` | {ext}, {sz:,} bytes | {counterpart} | {target} | **{congruence}** |")

report_lines.append("")

# 6. Detailed Stimulus & Timing Specifications
report_lines.append("---")
report_lines.append("")
report_lines.append("## 6. Detailed Timing & Response Scale Specifications")
report_lines.append("")
report_lines.append("### A. Reading Screen (Pantalla de Lectura del Estímulo)")
report_lines.append("1. **Visual Display**: Displays the headline card image asset (`Noticia_XX.jpg` or `Noticia_26.png`).")
report_lines.append("2. **Progress Indicator**: A top or bottom horizontal progress bar smoothly counting down or filling over 10,000 ms (10 seconds).")
report_lines.append("3. **Auto-Advance**: When the 10,000 ms timer reaches 0, the application transitions automatically to the response screen.")
report_lines.append("4. **Early Advance Consideration**:")
report_lines.append("   - *Design note from `Psicología Experimental - Favaloro.docx` (p. 26)*: Mentions that the reading timer can serve as a ceiling while allowing users to advance freely to capture natural deliberation speed.")
report_lines.append("   - *Specification in `ORIGINAL_REQUEST.md` (lines 52 & 94)*: Specifies a 10-second reading time with visual progress indicator and auto-advance.")
report_lines.append("   - *Implementation Recommendation*: Implement a 10.0-second auto-advance. If an early 'Continuar' button is enabled, record the exact `reading_time_ms` (0–10,000 ms). If strict auto-advance is enforced, `reading_time_ms` will record true screen residency (defaulting to 10,000 ms ± network/render latency).")
report_lines.append("5. **Telemetry Captured**:")
report_lines.append("   - `reading_time_ms`: Exact millisecond duration between the stimulus component mount and transition trigger.")
report_lines.append("")
report_lines.append("### B. Response Screen (Pantalla de Evaluación)")
report_lines.append("1. **Visual Display**: Clean card presentation with the question: *«¿Cuál de las siguientes opciones describe mejor su conocimiento sobre la noticia que acaba de ver?»* (or similar neutral question).")
report_lines.append("2. **Response Scale (Murphy & León 4-point scale)**:")
report_lines.append("   - **Option 1**: `«Recuerdo claramente haber visto/leído este evento»`")
report_lines.append("     - Statistical Code: `1`")
report_lines.append("     - Psychological Construct: **Falso Recuerdo (False Memory)** on fake news; **Verdadero Recuerdo (True Memory)** on true news.")
report_lines.append("   - **Option 2**: `«No recuerdo haberlo visto, pero creo que sucedió»`")
report_lines.append("     - Statistical Code: `2`")
report_lines.append("     - Psychological Construct: **Falsa Creencia (False Belief)** on fake news; **Creencia Verdadera / Aceptación sin recuerdo** on true news.")
report_lines.append("   - **Option 3**: `«Lo recuerdo diferente»`")
report_lines.append("     - Statistical Code: `3`")
report_lines.append("     - Psychological Construct: **Memoria discrepante / recuerdo alterado**.")
report_lines.append("   - **Option 4**: `«No lo recuerdo en absoluto»`")
report_lines.append("     - Statistical Code: `4`")
report_lines.append("     - Psychological Construct: **Sin memoria / descarte**.")
report_lines.append("3. **Input Mechanics**: Mutually exclusive single-choice radio buttons or selectable interactive cards.")
report_lines.append("4. **Submission**: An explicit action button: `«Siguiente noticia»`. The button is disabled until an option is selected.")
report_lines.append("5. **Timing**: Untimed (no time pressure), but the system silently tracks `response_time_ms` from screen render to click.")
report_lines.append("6. **Telemetry Captured**:")
report_lines.append("   - `response_option`: Integer `1` to `4` (and verbatim string).")
report_lines.append("   - `response_time_ms`: Integer milliseconds.")
report_lines.append("   - `is_fake_memory`: Boolean (`true` if `is_fake && response_option == 1`).")
report_lines.append("   - `is_fake_belief`: Boolean (`true` if `is_fake && response_option == 2`).")
report_lines.append("")
report_lines.append("### C. Trial Loop Structure (Loop de 20 Ensayos)")
report_lines.append("1. **Composition**: Exactly 20 items per participant = 12 True News (IDs 1-12) + 8 Congruent Fake News.")
report_lines.append("2. **Selection by Orientation**:")
report_lines.append("   - If `orientacion == 'Psicoanálisis'` -> Fake news IDs: `[14, 16, 18, 20, 21, 23, 25, 27]`.")
report_lines.append("   - If `orientacion == 'Basada en Evidencia Científica'` -> Fake news IDs: `[13, 15, 17, 19, 22, 24, 26, 28]`.")
report_lines.append("   - If Excluded (`estudia_psicologia == false` or `orientacion == 'Otros'`) -> Randomly pick either Set A (PSA) or Set B (EBP) with 50/50 probability. Mark session `is_included = false`.")
report_lines.append("3. **Randomization**: The 20 items are shuffled uniquely per participant using Fisher-Yates algorithm.")
report_lines.append("4. **No Back-Navigation**: Participants cannot go back to review or change past answers.")
report_lines.append("")

# 7. Caveats
report_lines.append("---")
report_lines.append("")
report_lines.append("## 7. Caveats")
report_lines.append("")
report_lines.append("1. **Image Asset File Format Discrepancy**: While the documentation mentions `Noticia_01.jpg` to `Noticia_28.jpg`, item 26 is strictly `Noticia_26.png`. Code implementing static string interpolation like `Noticia_${id}.jpg` will trigger a 404 for item 26 unless an extension mapping or file lookup table is used.")
report_lines.append("2. **Reading Screen Interaction Nuance**: `ORIGINAL_REQUEST.md` specifies 10s reading time with auto-advance, while research notes mention that allowing early advance captures deliberative vs intuitive variance. Frontend developers should implement 10s auto-advance and accurately measure `reading_time_ms`.")
report_lines.append("3. **Image Asset Text Redundancy**: The headline text is already rendered inside each image file. Therefore, displaying HTML headline text above or below the image would create duplicate text on screen. The image should be presented as the primary stimulus object, with the Spanish text stored in metadata for CSV export and data analysis.")
report_lines.append("4. **Image Preloading**: Because 20 large banner images (~100 KB each) are displayed in sequence, client-side preloading of upcoming images is strongly recommended to prevent timer desynchronization caused by network latency.")
report_lines.append("")

# 8. Conclusion
report_lines.append("---")
report_lines.append("")
report_lines.append("## 8. Conclusion")
report_lines.append("")
report_lines.append("All 28 stimuli materials, headline texts, translations, image assets, ideological congruence mappings, and timing/response scale protocols have been completely extracted, audited, and specified. The experimental materials form a rigorous, counterbalanced design where:")
report_lines.append("- 12 true news establish a baseline (6 psychoanalysis-related, 6 evidence-related).")
report_lines.append("- 16 fake news form 8 mirrored pairs that cleanly isolate ideological congruence without confounding topic salience.")
report_lines.append("- Pro-Psychoanalysis participants are exposed only to anti-cognitive fake news (IDs 14, 16, 18, 20, 21, 23, 25, 27).")
report_lines.append("- Pro-Evidence-Based participants are exposed only to anti-psychoanalysis fake news (IDs 13, 15, 17, 19, 22, 24, 26, 28).")
report_lines.append("- Excluded participants receive the Control induction and a cohesive fake news set (either PSA or EBP) to guarantee experimental realism while preventing mirror-pair collisions.")
report_lines.append("- Timing (10s reading countdown + untimed deliberation) and response scales (4-point Murphy/León) are fully specified for direct implementation.")
report_lines.append("")

# 9. Verification Method
report_lines.append("---")
report_lines.append("")
report_lines.append("## 9. Verification Method")
report_lines.append("")
report_lines.append("To independently verify this specification:")
report_lines.append("1. **Verify Asset Directory**:")
report_lines.append("   ```powershell")
report_lines.append("   Get-ChildItem 'C:\\Users\\Fmendezcasariego\\OneDrive\\Carpetas\\Educación\\Universidad\\Favaloro\\Psicología\\2do Año\\Psicología Experimental\\PARCIAL 2 - INVESTIGACIÓN\\Noticias\\noticias imagenes' | Measure-Object")
report_lines.append("   # Confirms 28 items, exactly one .png (Noticia_26.png) and 27 .jpg files")
report_lines.append("   ```")
report_lines.append("2. **Verify Text Extraction from DOCX**:")
report_lines.append("   ```powershell")
report_lines.append("   python parse_stimuli.py")
report_lines.append("   # Extracts all 28 rows from NOTICIAS TRADUCIDAS.docx and generates stimuli_parsed.json")
report_lines.append("   ```")
report_lines.append("3. **Verify Mirror Pair Symmetry & Congruence Partition**:")
report_lines.append("   - Confirm that PSA Set `[14, 16, 18, 20, 21, 23, 25, 27]` contains zero overlap with EBP Set `[13, 15, 17, 19, 22, 24, 26, 28]`.")
report_lines.append("   - Confirm that for every pair `(13, 21), (14, 22), (15, 23), (16, 24), (17, 25), (18, 26), (19, 27), (20, 28)`, exactly one element belongs to the PSA set and one belongs to the EBP set.")
report_lines.append("4. **Invalidation Conditions**:")
report_lines.append("   - If any image file from `Noticia_01.jpg` to `Noticia_28.jpg` is missing or fails to render.")
report_lines.append("   - If a participant assigned to 'Psicoanálisis' sees any item from `[13, 15, 17, 19, 22, 24, 26, 28]`.")
report_lines.append("   - If a participant assigned to 'Basada en Evidencia Científica' sees any item from `[14, 16, 18, 20, 21, 23, 25, 27]`.")
report_lines.append("   - If any trial fails to record `reading_time_ms` or `response_time_ms`.")
report_lines.append("")

output_path = r"C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\spec_miner_survey_2\handoff.md"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"Handoff report written to {output_path} successfully. Total lines: {len(report_lines)}")
