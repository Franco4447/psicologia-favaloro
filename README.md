# 🧠 Hub de Estudio: Licenciatura en Psicología - Universidad Favaloro

Bienvenidos al repositorio central de apuntes, bibliografía y resúmenes de la carrera de Psicología. Este espacio está diseñado para trabajar en conjunto con **Antigravity** y el plugin **study-workflow** para potenciar el aprendizaje, automatizar la creación de resúmenes y facilitar el estudio activo.

## 📁 Estructura del Repositorio

El contenido está organizado por año y cuatrimestre. Dentro de cada materia (cuando se creen), la estructura ideal sugerida para que los agentes funcionen óptimamente es:

- `/Bibliografía`: Textos fuente, PDFs originales y desgrabaciones.
- `/Resúmenes`: Archivos Markdown (`.md`) generados por la skill `study-summarizer`.
- `/Flashcards`: Archivos CSV generados por `anki-flashcards` listos para importar a Anki.
- `/Entregables`: Documentos finales exportados en PDF o Word con `export-study-material`.

## 🛠️ Flujo de Estudio Recomendado (Study Workflow)

1. **Digitalización**: Si tienes textos en PDF (por ejemplo, desde tu Google Drive), podemos convertirlos usando la skill `pdf-to-markdown` para que sean procesables.
2. **Generación de Guías**: Solicita crear un resumen de un apunte específico. Se utilizará la skill `study-summarizer` para extraer la tesis central, glosarios, mapas conceptuales (Mermaid) y citas importantes.
3. **Estudio Activo (Anki)**: A partir del resumen, podemos generar tarjetas de memoria usando la skill `anki-flashcards` para repasar conceptos clave.
4. **Autoevaluación**: Antes de un parcial, puedes pedir realizar un examen de prueba utilizando la skill `interactive-evaluation`.
5. **Exportación**: Cuando necesites imprimir o compartir un resumen final, usamos `export-study-material` para obtener un `.docx` o `.pdf` prolijo.

## 🔗 Integración con Google Drive

Actualmente, existe un acceso directo (`Google Drive Acceso.url`) en la raíz. Para procesar eficientemente los archivos ubicados en Drive con estas herramientas:

1. **Google Drive para Escritorio**: Es la opción recomendada. Instala la app oficial de Google para que tu Drive aparezca como un disco local (ej. `G:\`). De esta forma, el agente puede leer y resumir los PDFs directamente desde allí y guardarlos aquí.
2. **Descarga Selectiva**: Puedes descargar los PDFs o apuntes de Google Drive que vayas a estudiar en la semana dentro de las carpetas `/Bibliografía` correspondientes en este directorio de OneDrive.

---
*Este archivo sirve como contexto base para que los agentes comprendan la estructura y el propósito de este directorio.*
