# Original User Request

## 2026-09-20T23:19:13Z

Construir una plataforma web profesional y pulida para un experimento de Psicología Experimental universitaria que estudia el efecto de la inducción cognitiva (emocional, racional, control) sobre la creación de falsos recuerdos y falsas creencias tras la exposición a fake news. La web debe estar alojada online gratuitamente, almacenar datos de participantes en una base de datos, y el código fuente debe estar en un repositorio de GitHub.

Working directory: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento

Integrity mode: development

## Materiales de Referencia (ya existentes en el filesystem)

Los siguientes archivos contienen el diseño completo del experimento y deben ser leídos por el equipo para entender el contexto:

- **Diseño experimental principal:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Psicología Experimental - Favaloro.docx`
- **Documento de experimento (detalle variables):** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\experimento.docx`
- **Feedback del diseño:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Feedback_Diseño_Experimental.md`
- **Noticias con textos y numeración:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\NOTICIAS TRADUCIDAS.docx`
- **28 imágenes de titulares:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Noticias\noticias imagenes\Noticia_01.jpg` a `Noticia_28.jpg` (y una .png)
- **Notas de investigación:** `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\Psicología Experimental - Favaloro.md`

### Datos clave del experimento (extraídos de los documentos anteriores)

**Diseño:**
- VI (3 niveles inter-sujeto): Inducción a pensamiento emocional / racional / control
- VD: Creación de falsos recuerdos (y falsas creencias) ante fake news
- Variable interviniente controlada: Creencias previas → efecto de congruencia. El participante elige afinidad terapéutica (Psicoanálisis vs. Basada en Evidencia) y se le muestran fake news alineadas a su ideología
- Proxy: Tiempo de lectura y tiempo de respuesta como medida encubierta de esfuerzo cognitivo

**Flujo completo del experimento:**
1. **Pantalla de bienvenida** — Presentación: "Somos estudiantes de la Universidad Favaloro..." explicación de los objetivos y qué esperar
2. **Consentimiento informado** — Checkbox obligatorio para continuar
3. **Formulario demográfico:**
   - Edad (integer)
   - Sexo (multiple choice: Femenino, Masculino, Otro)
   - ¿Estudia o estudió psicología? (Sí / No)
   - Orientación terapéutica (Psicoanálisis / Basada en Evidencia Científica / Otros)
   - Universidad (texto libre)
4. **Criterio de inclusión** (lógica interna, no visible al participante):
   - Si estudia psicología + elige Psicoanálisis o Basada en Evidencia → participante incluido, se asigna a uno de los 3 grupos de inducción
   - Si NO cumple criterio → recibe prompt de Control + set aleatorio de fake news, pero se marca como "excluido" en los datos
5. **Prompt de inducción** (según grupo asignado aleatoriamente con distribución equitativa):
   - **Racional:** "Mucha gente cree que la razón conduce a una buena toma de decisiones. Cuando usamos la lógica, en lugar de los sentimientos, tomamos decisiones racionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en la razón, en lugar de en sus emociones."
   - **Emocional:** "Mucha gente cree que la emoción conduce a una buena toma de decisiones. Cuando usamos los sentimientos, en lugar de la lógica, tomamos decisiones emocionalmente satisfactorias. Por favor, evalúe los siguientes titulares de noticias basándose en sus emociones, en lugar de en la razón."
   - **Control:** "A continuación se le presentará una serie de titulares de noticias reales de 2017-2018. Estamos interesados en su opinión sobre si los titulares son precisos o no."
6. **Loop de 20 noticias** (12 verdaderas + 8 fake news congruentes con su orientación):
   - **Clasificación de noticias:**
     - Noticias verdaderas: Numeración interna 1-12
     - Fake news para afines a Psicoanálisis: nº 14, 16, 18, 20, 21, 23, 25, 27
     - Fake news para afines a Basada en Evidencia: nº 13, 15, 17, 19, 22, 24, 26, 28
   - **Por cada noticia:**
     - Se muestra la imagen del titular con tiempo de lectura de 10 segundos (con indicador visual de progreso, avance automático)
     - Luego se muestra pantalla de respuesta con 4 opciones (escala Murphy/León), SIN límite de tiempo pero registrando el tiempo de respuesta:
       1. "Recuerdo claramente haber visto/leído este evento" (Falso Recuerdo)
       2. "No recuerdo haberlo visto, pero creo que sucedió" (Falsa Creencia)
       3. "Lo recuerdo diferente"
       4. "No lo recuerdo en absoluto"
     - Botón para avanzar a la siguiente noticia
7. **Debriefing** — Revelación ética: explicar que algunas noticias eran falsas y el propósito del estudio
8. **Agradecimiento** — Pantalla final

**Stack tecnológico elegido:**
- Frontend: Deploy en Vercel o Netlify (gratuito)
- Backend/DB: Supabase free tier (PostgreSQL)
- Repositorio: GitHub

## Requirements

### R1. Plataforma web del experimento funcional y deployada

La web debe implementar el flujo completo del experimento descrito arriba, funcionando end-to-end: desde la pantalla de bienvenida hasta el agradecimiento final. Toda la interfaz debe estar en español. El diseño debe ser profesional, limpio y con buena tipografía, como corresponde a un instrumento de investigación académica serio. Las 28 imágenes de titulares (Noticia_01.jpg a Noticia_28.jpg/.png) deben estar integradas como estímulos.

### R2. Lógica experimental correcta

La asignación a los 3 grupos de inducción debe ser equitativa (no puramente aleatoria, sino balanceada). La selección de fake news debe ser congruente con la orientación terapéutica del participante según la clasificación especificada. Los participantes que no cumplen criterios de inclusión deben recibir el prompt de Control con un set aleatorio de fake news y ser marcados como "excluidos" en los datos. El orden de presentación de las 20 noticias (12 verdaderas + 8 fake) debe ser aleatorizado para cada participante.

### R3. Recolección completa de datos

El sistema debe registrar por cada participante: datos demográficos (edad, sexo, estudia psicología, orientación terapéutica, universidad), grupo de inducción asignado, set de fake news mostrado, estado de inclusión/exclusión, y por cada una de las 20 noticias: número de noticia, respuesta elegida (1-4), tiempo de lectura, tiempo de respuesta, y orden de presentación. Además, datos del navegador/dispositivo del participante para control de calidad. Todos los datos deben almacenarse en Supabase (PostgreSQL).

### R4. Exportación y dashboard

Los datos deben ser exportables como CSV. Además, debe existir un dashboard básico (protegido con contraseña) donde el investigador pueda ver: número total de participantes, distribución por grupo, y estado general del experimento.

### R5. Código en GitHub y deploy

El código fuente debe estar en un repositorio GitHub, configurado para deploy automático en Vercel o Netlify. El README debe incluir instrucciones de setup, configuración de variables de entorno (Supabase keys), y cómo hacer deploy.

## Acceptance Criteria

### Funcionalidad end-to-end
- [ ] Un usuario puede completar todo el flujo del experimento sin errores ni pantallas rotas
- [ ] Las 20 noticias se presentan con imágenes correctas y en orden aleatorio
- [ ] El tiempo de lectura de 10 segundos se respeta con indicador visual
- [ ] Las 4 opciones de respuesta funcionan y son excluyentes
- [ ] El prompt de inducción correcto se muestra según el grupo asignado

### Lógica experimental
- [ ] La distribución de participantes entre los 3 grupos se mantiene equilibrada (diferencia máxima de 2 entre el grupo más grande y el más pequeño en cualquier momento)
- [ ] Si un participante elige "Psicoanálisis" → recibe fake news nº 14,16,18,20,21,23,25,27
- [ ] Si un participante elige "Basada en Evidencia" → recibe fake news nº 13,15,17,19,22,24,26,28
- [ ] Participantes que no cumplen criterio de inclusión reciben prompt Control + son marcados como excluidos

### Datos
- [ ] Cada sesión completada genera un registro completo en Supabase con todos los campos especificados en R3
- [ ] El CSV exportado contiene una fila por noticia por participante (20 filas por participante) con todos los campos
- [ ] Los tiempos de respuesta se registran en milisegundos con precisión razonable

### Infraestructura
- [ ] La web es accesible públicamente via HTTPS en un dominio de Vercel/Netlify
- [ ] El repositorio GitHub contiene todo el código fuente y un README funcional
- [ ] Las credenciales de Supabase NO están hardcodeadas en el código (usar variables de entorno)

### Dashboard
- [ ] Existe una ruta protegida con contraseña que muestra el conteo de participantes por grupo
- [ ] Se puede descargar el CSV de datos desde el dashboard

## Verification Plan

### Automated Tests
- Ejecutar el flujo completo del experimento al menos 3 veces (una por cada grupo de inducción) verificando que los datos se persistan correctamente en Supabase
- Verificar que la distribución de grupos se mantiene equilibrada tras N asignaciones simuladas
- Validar que el CSV exportado tenga la estructura correcta y todos los campos esperados

### Manual Verification
- Abrir la URL pública del deploy y completar el experimento como participante real
- Verificar que las imágenes de noticias se cargan correctamente
- Verificar que el dashboard muestra los datos correctos y permite exportar CSV
- Confirmar que el repo de GitHub tiene README con instrucciones claras

## 2026-09-21T18:39:02Z

# Teamwork Project Prompt — Draft

> Requested team: Full team

Implementar un plan de validación de calidad automatizado (E2E) para la plataforma de psicología experimental y corregir el bug visual que impide que la barra de tiempo cargue adecuadamente mientras se muestra la noticia.

Working directory: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento
Integrity mode: development

## Requirements

### R1. Corrección del Temporizador Visual
Corregir la lógica visual o estructural en la pantalla de estímulos (`StimulusReadingScreen.tsx`) para asegurar que la barra de progreso inferior de 15 segundos crezca visiblemente en pantalla desde que la imagen termina de cargar, y que sea visible para el usuario.

### R2. Tests Automatizados (E2E)
Configurar e implementar un suite de pruebas automatizadas (recomendado: Playwright o Cypress) que simule la navegación de un participante a través de las distintas etapas del experimento, asegurando que la máquina de estados y las transiciones de páginas funcionen correctamente.

## Acceptance Criteria

### Corrección del Bug Visual
- [ ] La barra de progreso en `StimulusReadingScreen` aumenta su porcentaje de ancho (`width`) de forma ininterrumpida y visible (no se superpone ni se esconde detrás de otros elementos) durante los 15 segundos.

### Pruebas Automatizadas E2E
- [ ] Existe un comando ejecutable vía consola (ej. `npm run test:e2e`) que levanta el entorno de pruebas.
- [ ] Las pruebas pasan exitosamente y navegan por el flujo principal sin errores de ejecución.
