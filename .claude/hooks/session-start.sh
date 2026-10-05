#!/bin/bash
# Instala las herramientas de las skills de estudio en sesiones de Claude Code en la nube.
# En la PC local no hace nada: ahí se usa Scripts/estudio/verificar_entorno.py.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Python: PDFs, PPTX, YAML, Excel, Google Drive
pip install -q --root-user-action=ignore -r Scripts/requirements.txt

# pandoc (/exportar) y OCR en español (/digitalizar)
if ! command -v pandoc >/dev/null || ! tesseract --list-langs 2>/dev/null | grep -qx spa; then
  apt-get install -y -q pandoc tesseract-ocr tesseract-ocr-spa >/dev/null 2>&1 \
    || { apt-get update -q >/dev/null 2>&1 && apt-get install -y -q pandoc tesseract-ocr tesseract-ocr-spa >/dev/null; }
fi

# LibreOffice Writer (/exportar a PDF); el contenedor trae solo el núcleo, que no abre documentos
if ! dpkg -s libreoffice-writer >/dev/null 2>&1; then
  apt-get install -y -q libreoffice-writer >/dev/null 2>&1 \
    || { apt-get update -q >/dev/null 2>&1 && apt-get install -y -q libreoffice-writer >/dev/null; }
fi

# mermaid-cli (diagramas), usando el Chromium preinstalado en vez de descargar otro
if ! command -v mmdc >/dev/null; then
  PUPPETEER_SKIP_DOWNLOAD=1 npm install -g @mermaid-js/mermaid-cli >/dev/null 2>&1
fi
CHROME="$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | sort -V | tail -1 || true)"
if [ -n "$CHROME" ]; then
  CFG="$HOME/.config/mermaid/puppeteer.json"
  mkdir -p "$(dirname "$CFG")"
  printf '{"executablePath":"%s","args":["--no-sandbox"]}\n' "$CHROME" > "$CFG"
  if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    echo "export MERMAID_PUPPETEER_CONFIG=\"$CFG\"" >> "$CLAUDE_ENV_FILE"
  fi
fi

python3 Scripts/estudio/verificar_entorno.py >/dev/null
