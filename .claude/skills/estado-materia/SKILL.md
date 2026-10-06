---
name: estado-materia
description: 'Muestra en qué estado está cada materia del repositorio de Psicología: por unidad o clase, qué tiene en cada etapa (textos extraídos, guía, Word, flashcards, simulacro, último resultado) y qué falta hacer, con los temas flojos de los simulacros y los nombres que no siguen AGENTS.md. Usala siempre que el usuario pregunte qué le falta, qué tiene hecho, cómo viene una materia, por dónde seguir, qué estudiar, o pida un panorama o inventario de sus apuntes.'
---

# Estado de una materia

```bash
python Scripts/estudio/estado.py                      # todas las materias de 2do Año
python Scripts/estudio/estado.py Psicoanálisis        # una o varias materias
python Scripts/estudio/estado.py --anio "1er Año" …   # otro año (1er Año: archivo histórico, nombres sin normalizar)
```

## Cómo presentarlo

1. Corré el script para lo que pidió el usuario (si no dice materia, todas las de 2do Año).
2. No pegues la salida entera si es larga: resumí por materia —qué está completo, qué falta— y
   mostrá la tabla solo de la materia que le interesa.
3. Priorizá lo pendiente con criterio de estudio, no solo de archivos:
   - si en el Planificador (`Planificador_Parciales/`) o en lo que dijo el usuario hay un parcial
     cerca, primero las unidades que entran en ese parcial;
   - los **temas flojos** de simulacros anteriores antes que material nuevo;
   - flashcards y simulacros de guías que ya existen (rinden rápido) antes que guías nuevas.
4. Proponé el siguiente paso concreto con la skill que corresponde (`/flashcards`, `/simulacro`,
   `/guia-estudio`, `/exportar`, `/digitalizar`) o `/estudiar-unidad` para hacer todo de una unidad.

## Ojo

- Los **textos extraídos** y la **bibliografía original** no se suben a git: el conteo es el de la
  copia local (en una sesión en la nube faltan: solo están en el OneDrive del usuario).
- "Nombres fuera de AGENTS.md" incluye guías viejas sin tema en el nombre (`C01_Guia.md` en vez de `C01_[Tema]_Guia.md`) o con
  sufijos de versión (`_v10`, `_FINAL`). **No las renombres sin permiso**: proponelo.
- "Guías editadas a mano": no regenerarlas sin preguntar.
