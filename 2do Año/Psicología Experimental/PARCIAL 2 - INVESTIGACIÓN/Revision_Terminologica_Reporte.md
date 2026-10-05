# Reporte de Revisión Terminológica: Orientaciones Terapéuticas en el Experimento

## 1. Análisis del Código y Clasificación Actual

Se analizaron los siguientes archivos del código fuente:
- `src/components/DemographicsScreen.tsx`: Muestra a los participantes tres opciones de orientación terapéutica:
  1. **Psicoanálisis**: "Enfoques psicodinámicos, teoría freudiana o lacaniana."
  2. **Basada en Evidencia Científica**: "Terapia cognitivo-conductual (TCC), terapias conductuales contextuales o de tercera ola."
  3. **Otros / Ninguna en particular**: "Sistémica, humanista, neuropsicología, o sin preferencia definida."
- `src/lib/experimentState.ts`: Determina que cualquier participante que elija la opción **"Otros"** queda **excluido** del análisis principal (`isIncluded: false`, `exclusionReason: 'orientacion_otros'`), y se le asignan estímulos de control o de relleno.
- `src/data/stimuli.ts`: Los estímulos falsos (Fake News) están diseñados específicamente para atacar o bien al **Psicoanálisis** (ej. atacando a Freud, Lacan, técnicas proyectivas) o bien a la **Terapia Cognitivo-Conductual / Conductismo** (ej. atacando a Watson, Skinner, terapia breve). 

## 2. Validación con la Bibliografía Empírica

La categorización utilizada en el experimento se fundamenta de forma directa y exclusiva en el paper:
**León et al. (2023) - "Fake news and false memory formation in the psychology debate" (emp 1)**.

### a) Psicoanálisis (PSA) y Prácticas Basadas en Evidencia (EBP)
León et al. operativizan el "gran debate de la psicología en Argentina" dividiendo a la población en dos polos ideológicos predominantes:
- **Psychoanalysis (PSA)**: Identificado en el paper como la corriente hegemónica, englobando enfoques freudianos, post-freudianos o lacanianos.
- **Evidence-Based Practices (EBP)**: Definido explícitamente en el texto como *"Evidence-Based Practices (EBP) such as cognitive and behavioral therapy (CBT)"*. 

Por lo tanto, la descripción actual en `DemographicsScreen.tsx` para ambas categorías es **perfectamente precisa y coherente** con la literatura en la que se basa el experimento.

### b) La categoría "Otros" y la Ambigüedad
En el estudio de León et al. (2023), los autores señalan: *"There were 26 participants who did not define a preferred theoretical framework or had an ambiguous orientation and were therefore excluded from the experiment"*. 

Corrientes como la **Sistémica**, **Humanista**, **Gestalt**, o la **Neuropsicología**, presentan ciertas ambigüedades teóricas:
- La Neuropsicología es una disciplina científica basada en evidencia. Un participante de esta rama podría sentirse tentado a elegir "Basada en Evidencia Científica".
- Las terapias sistémicas e integrativas pueden tener soporte empírico en ciertos contextos, aunque no pertenezcan históricamente a la TCC tradicional.

**Sin embargo, metodológicamente es correcto agruparlas en "Otros" y excluirlas del análisis**. ¿Por qué? Porque el *Efecto de Congruencia* (Frenda et al., 2013; Murphy et al., 2019) que busca medir el experimento depende de un **sesgo partidario o ideológico fuerte**. Los estímulos creados (las fake news) atacan específicamente al Conductismo/Cognitivismo y al Psicoanálisis. Si un neuropsicólogo o un terapeuta sistémico fuera incluido en el grupo "Basada en Evidencia", al leer una noticia falsa atacando a John B. Watson o a B.F. Skinner, **no experimentaría la misma disonancia cognitiva ni el "ataque a su identidad profesional"** que experimentaría un terapeuta cognitivo-conductual. 

## 3. Conclusiones y Recomendaciones

1. **La terminología actual es correcta y válida.** El diseño refleja fielmente las categorías operacionales de León et al. (2023).
2. **"Otros" está bien definido en el código:** Alistar explícitamente "Sistémica, humanista, neuropsicología" dentro de la categoría "Otros" (como ya se hace en la interfaz) es una excelente decisión de diseño. Evita que profesionales de estas ramas se autoseleccionen erróneamente en "Basada en Evidencia Científica", lo cual contaminaría la muestra del grupo EBP (quienes deben defender teóricamente la TCC ante las fake news).
3. **No se requieren modificaciones en esta iteración.** Las descripciones en la pantalla de demografía guían correctamente al usuario para lograr una muestra limpia y dicotómica, tal como lo requiere la medición del Efecto de Congruencia.
