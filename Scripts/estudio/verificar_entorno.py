"""Verifica que estén instaladas las herramientas que usan las skills de estudio.

Uso:
    python Scripts/estudio/verificar_entorno.py            # tabla de qué hay y qué falta
    python Scripts/estudio/verificar_entorno.py --probar   # además prueba OCR y diagramas

Sale con código 1 si falta algo obligatorio para alguna skill.
"""
import importlib.util
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WIN = platform.system() == "Windows"

# nombre, cómo detectarlo, skills que lo usan, obligatorio, instalación (Windows, Linux)
PY = [
    ("pyyaml", "yaml", "todas", True),
    ("pdfplumber", "pdfplumber", "/digitalizar", True),
    ("pypdf", "pypdf", "/digitalizar", True),
    ("python-pptx", "pptx", "/digitalizar", True),
    ("openpyxl", "openpyxl", "/flashcards", False),
]

LIBREOFFICE_WIN = [r"C:\Program Files\LibreOffice\program\soffice.exe",
                   r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"]

BIN = [
    ("pandoc", ["pandoc"], "/exportar", True,
     "winget install JohnMacFarlane.Pandoc", "apt-get install pandoc"),
    ("LibreOffice", ["soffice", "libreoffice"], "/exportar (PDF)", False,
     "winget install TheDocumentFoundation.LibreOffice", "apt-get install libreoffice"),
    ("Tesseract (OCR)", ["tesseract"], "/digitalizar (PDF escaneados)", False,
     "winget install UB-Mannheim.TesseractOCR (marcar idioma Spanish)", "apt-get install tesseract-ocr tesseract-ocr-spa"),
    ("Node.js", ["node"], "/guia-estudio, /exportar (diagramas)", True,
     "winget install OpenJS.NodeJS.LTS", "apt-get install nodejs npm"),
    ("mermaid-cli (mmdc)", ["mmdc"], "/guia-estudio, /exportar (diagramas)", True,
     "npm install -g @mermaid-js/mermaid-cli", "npm install -g @mermaid-js/mermaid-cli"),
]


def buscar(cmds):
    for c in cmds:
        p = shutil.which(c)
        if p:
            return p
    if WIN and "soffice" in cmds:
        return next((p for p in LIBREOFFICE_WIN if Path(p).exists()), None)
    return None


def tesseract_spa(exe):
    try:
        out = subprocess.run([exe, "--list-langs"], capture_output=True, text=True, timeout=20)
        return "spa" in (out.stdout + out.stderr).split()
    except Exception:
        return False


def probar_mermaid(exe):
    with tempfile.TemporaryDirectory() as d:
        src, out = Path(d, "t.mmd"), Path(d, "t.png")
        src.write_text("graph TD; A-->B", encoding="utf-8")
        cmd = [exe, "-i", str(src), "-o", str(out)]
        # En la nube se usa el Chromium preinstalado (ver .claude/hooks/session-start.sh)
        cfg = os.environ.get("MERMAID_PUPPETEER_CONFIG")
        if cfg:
            cmd += ["-p", cfg]
        try:
            subprocess.run(cmd, capture_output=True, timeout=120, shell=WIN)
        except Exception:
            return False
        return out.exists()


def main():
    probar = "--probar" in sys.argv
    falta_oblig = False
    filas = []

    ok_py = sys.version_info >= (3, 9)
    filas.append(("Python ≥ 3.9", ok_py, platform.python_version(), "todas", "https://www.python.org/downloads/"))
    falta_oblig |= not ok_py

    for nombre, mod, skills, oblig in PY:
        ok = importlib.util.find_spec(mod) is not None
        filas.append((nombre, ok, "" if ok else "falta", skills, "pip install -r Scripts/requirements.txt"))
        falta_oblig |= oblig and not ok

    for nombre, cmds, skills, oblig, inst_win, inst_lin in BIN:
        p = buscar(cmds)
        det = p or "falta"
        ok = bool(p)
        if ok and nombre.startswith("Tesseract") and not tesseract_spa(p):
            ok, det = False, "falta el idioma español (spa)"
        if ok and probar and nombre.startswith("mermaid"):
            ok = probar_mermaid(p)
            det = "renderiza OK" if ok else "instalado pero no renderiza (¿falta Chromium?)"
        filas.append((nombre, ok, det, skills, inst_win if WIN else inst_lin))
        falta_oblig |= oblig and not ok

    ancho = max(len(f[0]) for f in filas)
    for nombre, ok, det, skills, inst in filas:
        print(f"{'✓' if ok else '✗'} {nombre:<{ancho}}  {skills:<38} {det}")
        if not ok:
            print(f"  {'':<{ancho}}  → instalar: {inst}")
    print("\nTodo listo." if not falta_oblig else "\nFalta algo obligatorio (ver ✗ arriba).")
    sys.exit(1 if falta_oblig else 0)


if __name__ == "__main__":
    main()
