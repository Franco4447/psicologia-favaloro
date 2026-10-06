"""Renderiza los diagramas Mermaid de una guía y los guarda según AGENTS.md.

Por cada bloque ```mermaid de la guía:
  - escribe 3_Guias_de_Estudio/_media/[Unidad]_[Tema]_[NN].mmd (fuente) y .png (render),
  - y deja, justo debajo del bloque, la imagen con ruta relativa:
        ![Diagrama NN](_media/[Unidad]_[Tema]_NN.png)
Es idempotente: si la imagen ya está referenciada, solo vuelve a renderizar.

Uso:
    python Scripts/estudio/diagramas.py <guia.md> [--sin-render]

Requiere mermaid-cli (mmdc). En la nube, MERMAID_PUPPETEER_CONFIG apunta al Chromium local
(lo configura .claude/hooks/session-start.sh).
"""
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter  # noqa: E402

RE_BLOQUE = re.compile(r"```mermaid\n(.*?)```\n?", re.S)


def render(mmd, png):
    exe = shutil.which("mmdc")
    if not exe:
        raise RuntimeError("falta mermaid-cli: npm install -g @mermaid-js/mermaid-cli")
    cmd = [exe, "-i", str(mmd), "-o", str(png), "-b", "white", "-s", "2"]
    cfg = os.environ.get("MERMAID_PUPPETEER_CONFIG")
    if cfg:
        cmd += ["-p", cfg]
    r = subprocess.run(cmd, capture_output=True, text=True, shell=platform.system() == "Windows")
    if r.returncode != 0 or not Path(png).exists():
        raise RuntimeError(f"mmdc falló con {Path(mmd).name}:\n{(r.stderr or r.stdout)[-800:]}")


def procesar(guia, renderizar=True):
    guia = Path(guia)
    base = guia.stem[: -len("_Guia")] if guia.stem.endswith("_Guia") else guia.stem
    media = guia.parent / "_media"
    texto = guia.read_text(encoding="utf-8-sig")
    # Si la guía no tenía ediciones manuales, se actualiza su hash al insertar las imágenes:
    # agregar referencias a diagramas no es una edición del usuario.
    sin_cambios = frontmatter.estado(guia) == "sin-cambios"
    salida, pos, n, hechos = [], 0, 0, []
    for m in RE_BLOQUE.finditer(texto):
        n += 1
        nombre = f"{base}_{n:02d}"
        salida.append(texto[pos:m.end()])
        pos = m.end()
        media.mkdir(exist_ok=True)
        mmd, png = media / f"{nombre}.mmd", media / f"{nombre}.png"
        mmd.write_text(m.group(1), encoding="utf-8")
        if renderizar:
            render(mmd, png)
        ref = f"![Diagrama {n:02d}](_media/{nombre}.png)"
        resto = texto[pos:].lstrip("\n")
        if not resto.startswith(f"![Diagrama {n:02d}]("):
            salida.append(f"\n{ref}\n\n")
        hechos.append(png)
    salida.append(texto[pos:])
    nuevo = "".join(salida)
    if nuevo != texto:
        guia.write_text(nuevo, encoding="utf-8")
        if sin_cambios:
            meta, cuerpo = frontmatter.leer(guia)
            frontmatter.escribir(guia, meta, cuerpo)
    return hechos


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    try:
        pngs = procesar(args[0], renderizar="--sin-render" not in sys.argv)
    except RuntimeError as e:
        sys.exit(f"Error: {e}")
    print(f"✓ {len(pngs)} diagrama(s)" + "".join(f"\n    {p}" for p in pngs))
