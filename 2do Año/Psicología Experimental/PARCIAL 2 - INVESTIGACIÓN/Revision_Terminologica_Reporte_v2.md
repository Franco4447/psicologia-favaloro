# Reporte de Revisión Terminológica: Orientaciones Terapéuticas

Este reporte analiza la clasificación de las orientaciones terapéuticas en el experimento, contrastando la implementación en el código con la bibliografía provista y la literatura académica general.

## 1. Implementación en el Código

En el archivo `DemographicsScreen.tsx`, se presentan a los participantes tres opciones de orientación terapéutica, cada una con un texto descriptivo aclaratorio:
1. **Psicoanálisis**: "Enfoques psicodinámicos, teoría freudiana o lacaniana."
2. **Basada en Evidencia Científica**: "Terapia cognitivo-conductual (TCC), terapias conductuales contextuales o de tercera ola."
3. **Otros / Ninguna en particular**: "Sistémica, humanista, neuropsicología, o sin preferencia definida."

En la lógica del experimento (`experimentState.ts` y `stimuli.ts`), la selección de **"Otros" excluye al participante de la muestra principal** (`isIncluded: false`). A estos participantes se les muestra un set aleatorio de estímulos, pero sus datos no contaminan el análisis del Efecto de Congruencia principal.

## 2. Validación con la Bibliografía Empírica (Leon et al., 2023)

El reporte anterior acierta al señalar que esta clasificación deriva directamente del estudio original de Leon et al. (2023) (*Fake news and false memory formation in the psychology debate*). En dicho paper, los autores abordan la polarización en Argentina:
* Por un lado, la hegemonía del **Psicoanálisis** (49.8% de la currícula, enfoques freudianos, post-freudianos y lacanianos).
* Por otro lado, la búsqueda de integrar **Prácticas Basadas en Evidencia (EBP)**, representadas explícitamente en el paper por las terapias cognitivas y cognitivo-conductuales (CBT).

En la metodología de Leon et al. (2023), **26 participantes que no definieron un marco teórico preferido o tenían una orientación ambigua fueron excluidos del análisis (N=300 a N=274)**. Por lo tanto, excluir a la categoría "Otros" replica fielmente la metodología validada empíricamente.

## 3. El Problema de la Ambigüedad en la Literatura Académica General

La investigación anterior dejó un "vacío" al no abordar dónde se sitúan realmente terapias como la sistémica, la humanista o la neuropsicología en el marco de la evidencia científica global.

* **La definición amplia de "Basado en Evidencia":** En la psicología clínica internacional (ej. APA División 12), las "Prácticas Basadas en Evidencia" no son sinónimo exclusivo de TCC. Diversos abordajes sistémicos (ej. Terapia Familiar Funcional) o enfoques de raíz humanista (ej. Terapia Focalizada en las Emociones) poseen un robusto respaldo empírico. Asimismo, la **Neuropsicología** es intrínsecamente científica y basada en evidencia biológica/cognitiva.
* **El sesgo de los Estímulos:** Si un neuropsicólogo eligiera la opción "Basada en Evidencia Científica" bajo la premisa de que su práctica es científica, el sistema le asignaría el `FakeNewsSet` diseñado para atacar a la EBP (`EBP_CONGRUENT_FAKE_IDS`). Sin embargo, al revisar `stimuli.ts`, las fake news anti-EBP atacan figuras muy específicas del conductismo y cognitivismo: B.F. Skinner, John B. Watson, Abraham Low, o terapias cognitivas breves.
* **Dilución del Efecto de Congruencia:** Un terapeuta sistémico o un neuropsicólogo no experimentaría disonancia cognitiva ni amenaza a su identidad profesional al leer una noticia falsa atacando a Skinner o a la Terapia Cognitiva. Si estos profesionales se incluyeran en el grupo "EBP", no presentarían el Efecto de Congruencia esperado, diluyendo los resultados estadísticos del experimento.

## 4. Conclusión y Recomendaciones

La categorización actual es **metodológicamente necesaria y correcta** para este diseño experimental específico. 

Al incluir el texto descriptivo *"Terapia cognitivo-conductual (TCC), terapias conductuales contextuales o de tercera ola"* debajo de "Basada en Evidencia Científica", se evita la ambigüedad, guiando a los terapeutas sistémicos, humanistas o neuropsicólogos a elegir "Otros". Esto garantiza que la variable independiente (alineación ideológica TCC vs Psicoanálisis) se mantenga pura respecto a los estímulos diseñados.

**Recomendación:** No modificar el código actual. Las etiquetas en `DemographicsScreen.tsx` logran un equilibrio excelente entre el rigor metodológico del Efecto de Congruencia y la claridad para el usuario.

## Remaining Questions & Gaps

* **Escalabilidad de los Estímulos:** El set de estímulos está fuertemente atado al binomio Psicoanálisis vs TCC/Conductismo. Para futuras iteraciones que busquen medir la susceptibilidad a las *fake news* en la comunidad psicológica en general (incluyendo a neuropsicólogos o sistémicos), se deberán redactar nuevas *fake news* específicas que apunten a los dogmas y figuras de esas sub-disciplinas.
* **Validez Ecológica del Debate:** Aunque en Argentina la polarización Psicoanálisis vs TCC es predominante (Fierro, 2015), encasillar a toda la "evidencia científica" en la TCC puede alienar a profesionales de otras ramas empíricas durante el proceso de *debriefing*. Sería prudente asegurar que en el `DebriefingScreen.tsx` se aclare que la restricción metodológica fue intencional por el diseño de los estímulos, y no una declaración epistemológica de la cátedra sobre qué disciplinas carecen de evidencia.
