# 🧰 Scripts de Google Drive

Utilidades en Python para listar y descargar material de la cátedra desde Google Drive
usando la API v3.

| Script | Qué hace |
|--------|----------|
| `auth.py` | Corre el flujo OAuth (puerto `3000`) y guarda el token en `gdrive_token.json` |
| `list_drive.py` | Lista nombre, ID y tipo MIME de los archivos de una carpeta de Drive |
| `get_drive_path.py` | Muestra la ruta completa (`Carpeta / Subcarpeta / …`) de una carpeta a partir de su ID |
| `fetch_pdfs.py` | Descarga todos los PDFs de una o más carpetas de Drive a un directorio local |

## Utilidades de mantenimiento

| Script | Qué hace |
|--------|----------|
| `move_biblio.ps1` | Copia `.md` extraídos con formato `NN. Autor - Título.md` a `2_Textos_Extraidos/` como `[Unidad]_T[NN]_[Autor]_[Titulo]_Crudo.md` |
| `move_compendio.ps1` | Copia guías `clase_N.md`, `00_global*.md` y `psicosis.md` a `3_Guias_de_Estudio/` como `C[NN]_Guia.md`, `Global_[Cuatri]_Guia.md` y `Transversal_Psicosis_Guia.md` |
| `check_wide.js` | (Node) Lista los PNG de una carpeta `_media/` que quedan demasiado anchos al insertarse en Word |

Los scripts de PowerShell aceptan `-WhatIf` para ver qué harían sin copiar nada, y no
sobrescriben archivos existentes salvo que se pase `-Force`. Ayuda completa:
`Get-Help .\Scripts\move_biblio.ps1 -Full`.

```powershell
# Ver qué nombres generaría (no copia nada)
.\Scripts\move_biblio.ps1 -Origen "C:\descargas\biblio-2c" `
  -Destino ".\2do Año\Psicoanálisis\2_Textos_Extraidos" -Unidad U05 -WhatIf
#   "27. Belucci - Las intervenciones del analista.md"
#   -> U05_T27_Belucci_LasIntervencionesDelAnalista_Crudo.md

# Títulos largos: limitar a N palabras enteras
.\Scripts\move_biblio.ps1 -Origen ... -Destino ... -Unidad U05 -MaxPalabras 4

.\Scripts\move_compendio.ps1 -Origen "C:\descargas\compendio" `
  -Destino ".\2do Año\Psicoanálisis\3_Guias_de_Estudio" -Cuatrimestre 2doC
```

```bash
node Scripts/check_wide.js "2do Año/Psicoanálisis/3_Guias_de_Estudio/_media"        # límite 500 pt
node Scripts/check_wide.js "2do Año/Psicoanálisis/3_Guias_de_Estudio/_media" 400    # límite propio
```

## Utilidades de las skills de estudio (`Scripts/estudio/`)

Las usan las skills de estudio (ver [`docs/PLAN_SKILLS_ESTUDIO.md`](../docs/PLAN_SKILLS_ESTUDIO.md)),
pero también se pueden correr a mano.

| Script | Qué hace |
|--------|----------|
| `verificar_entorno.py` | Muestra qué herramientas están instaladas (Python, pandoc, LibreOffice, Tesseract, mermaid-cli) y cómo instalar las que faltan. `--probar` además renderiza un diagrama de prueba |
| `nombres.py` | Genera el nombre correcto de un archivo según `AGENTS.md` (`generar guia --unidad U05 --tema "Duelo y melancolía"` → `U05_DueloYMelancolia_Guia.md`) y revisa nombres existentes (`validar <archivos>`) |
| `frontmatter.py` | Lee y escribe la cabecera YAML de los `.md` generados. `estado <archivo>` dice si una guía fue editada a mano desde que se generó, para no pisarla |

```bash
python Scripts/estudio/verificar_entorno.py --probar
python Scripts/estudio/nombres.py validar "2do Año/Psicoanálisis/3_Guias_de_Estudio/"*.md
```

En las sesiones de Claude Code en la nube, `.claude/hooks/session-start.sh` instala todo
automáticamente al arrancar.

## Requisitos

```bash
pip install -r Scripts/requirements.txt
```

## Configuración (una sola vez)

1. En Google Cloud Console, crear un **ID de cliente OAuth** de tipo «Aplicación de
   escritorio» (o web con redirect `http://localhost:3000/`) y habilitar la **Google Drive API**.
2. Descargar el JSON del cliente como `gdrive_credentials.json` en el directorio desde el
   que vas a correr los scripts.
3. Ejecutar `python Scripts/auth.py`, abrir la URL que imprime y autorizar. Se genera
   `gdrive_token.json`.

Los dos archivos de credenciales están en `.gitignore`: **nunca** los subas al repositorio.

## Uso

Los IDs de carpeta y la ruta de destino están escritos dentro de cada script (bloque
`if __name__ == '__main__':`). Antes de correrlos:

- Reemplazá los IDs de carpeta por los de la materia que querés descargar (el ID es la
  última parte de la URL `https://drive.google.com/drive/folders/<ID>`).
- En `fetch_pdfs.py`, apuntá `dest` a `[Año]/[Materia]/1_Bibliografia_Original/` para
  respetar [`AGENTS.md`](../AGENTS.md). El valor actual apunta a una carpeta global
  `Bibliografía` que las reglas del repositorio ya no permiten.

```bash
python Scripts/list_drive.py
python Scripts/get_drive_path.py
python Scripts/fetch_pdfs.py
```

## Limitaciones conocidas

- Solo se lee la primera página de resultados (`pageSize=100`); carpetas con más de 100
  archivos quedan incompletas porque no se sigue `nextPageToken`.
- El scope pedido es `drive` (lectura y escritura). Para estos scripts alcanza con
  `drive.readonly`.
- Las rutas y los IDs no se pueden pasar por línea de comandos todavía.
