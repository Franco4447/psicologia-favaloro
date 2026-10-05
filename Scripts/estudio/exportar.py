"""Exporta una guía .md a Word (y opcionalmente PDF e impresión 2 por hoja) — skill /exportar.

Uso:
    python Scripts/estudio/exportar.py <guia.md> [--pdf] [--imprimir] [--indice] [--forzar]

  - Renderiza los diagramas Mermaid (diagramas.py) y los inserta como imágenes con un ancho que
    entra en la página (máx. 16 × 20 cm, sin agrandar imágenes chicas).
  - Convierte con pandoc usando la plantilla de estilos Scripts/estudio/plantillas/plantilla_guia.docx
    → [misma carpeta]/[Unidad]_[Tema]_Guia.docx
  - --pdf: además genera el .pdf con LibreOffice.
  - --imprimir: además genera 3_Guias_de_Estudio/_imprimir/[...]_Guia_Imprimir.pdf (A4 apaisado,
    2 páginas por hoja). Implica --pdf.
  - --indice: agrega índice al principio del Word (Word pide "actualizar campos" al abrir).
  - No sobrescribe un .docx/.pdf existente sin --forzar (puede tener retoques hechos en Word).
  - Todos los intermedios van a un directorio temporal que se borra al terminar.
"""
import argparse
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagramas  # noqa: E402
import frontmatter  # noqa: E402

PLANTILLA = Path(__file__).resolve().parent / "plantillas" / "plantilla_guia.docx"
MAX_W_CM, MAX_H_CM = 16.0, 20.0
RE_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)(\{[^}]*\})?")
RE_MERMAID = re.compile(r"```mermaid\n.*?```\n?", re.S)


def png_size(path):
    with open(path, "rb") as f:
        cab = f.read(24)
    if cab[1:4] != b"PNG":
        return None
    return struct.unpack(">II", cab[16:24])


def ancho_cm(path):
    """Ancho para que la imagen entre en MAX_W × MAX_H sin agrandarla (los PNG de mmdc están a escala 2)."""
    tam = png_size(path)
    if not tam:
        return MAX_W_CM
    w, h = tam
    natural = w / 2 / 96 * 2.54
    ancho = min(natural, MAX_W_CM)
    if ancho * h / w > MAX_H_CM:
        ancho = MAX_H_CM * w / h
    return round(ancho, 1)


def soffice():
    for c in ("soffice", "libreoffice"):
        if shutil.which(c):
            return shutil.which(c)
    for p in (r"C:\Program Files\LibreOffice\program\soffice.exe",
              r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"):
        if Path(p).exists():
            return p
    return None


def dos_por_hoja(pdf_in, pdf_out):
    """A4 apaisado con 2 páginas por hoja."""
    from pypdf import PdfReader, PdfWriter, Transformation
    r, w = PdfReader(str(pdf_in)), PdfWriter()
    W, H = 841.89, 595.28
    for i in range(0, len(r.pages), 2):
        hoja = w.add_blank_page(W, H)
        for j, pag in enumerate(r.pages[i:i + 2]):
            pw, ph = float(pag.mediabox.width), float(pag.mediabox.height)
            esc = min((W / 2) / pw, H / ph)
            dx = j * W / 2 + (W / 2 - pw * esc) / 2
            dy = (H - ph * esc) / 2
            hoja.merge_transformed_page(pag, Transformation().scale(esc).translate(dx, dy))
    Path(pdf_out).parent.mkdir(parents=True, exist_ok=True)
    with open(pdf_out, "wb") as f:
        w.write(f)


def exportar(guia, pdf=False, imprimir=False, indice=False, forzar=False):
    guia = Path(guia).resolve()
    docx = guia.with_suffix(".docx")
    pdf_path = guia.with_suffix(".pdf")
    imp_path = guia.parent / "_imprimir" / f"{guia.stem}_Imprimir.pdf"
    destinos = [docx] + ([pdf_path] if pdf or imprimir else []) + ([imp_path] if imprimir else [])
    existentes = [d for d in destinos if d.exists()]
    if existentes and not forzar:
        raise RuntimeError("ya existen (pueden tener retoques hechos a mano); usar --forzar para reemplazar:\n  "
                           + "\n  ".join(str(e) for e in existentes))
    if not shutil.which("pandoc"):
        raise RuntimeError("falta pandoc (ver Scripts/estudio/verificar_entorno.py)")

    if RE_MERMAID.search(guia.read_text(encoding="utf-8-sig")) and shutil.which("mmdc"):
        diagramas.procesar(guia)                       # .mmd + .png en _media/ y referencias en la guía
    _, cuerpo = frontmatter.leer(guia)
    if shutil.which("mmdc"):
        cuerpo = RE_MERMAID.sub("", cuerpo)            # en Word va la imagen, no el código

    def img(m):
        alt, ruta, attrs = m.groups()
        p = (guia.parent / ruta).resolve()
        if not p.exists():
            return f"*[Imagen no encontrada: {ruta}]*"
        return f"![{alt}]({p.as_posix()}){{width={ancho_cm(p)}cm}}"

    cuerpo = RE_IMG.sub(img, cuerpo)
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp, "guia.md")
        md.write_text(cuerpo, encoding="utf-8")
        cmd = ["pandoc", str(md), "-o", str(Path(tmp, "guia.docx")),
               "-f", "markdown+lists_without_preceding_blankline+pipe_tables-yaml_metadata_block-implicit_figures",
               "--resource-path", str(guia.parent), "--reference-doc", str(PLANTILLA)]
        if indice:
            cmd += ["--toc", "--toc-depth=2", "-M", "toc-title=Índice"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"pandoc falló:\n{r.stderr[-1500:]}")
        shutil.copy(Path(tmp, "guia.docx"), docx)
        hechos = [docx]
        if pdf or imprimir:
            exe = soffice()
            if not exe:
                raise RuntimeError("falta LibreOffice para el PDF (el .docx sí se generó)")
            r = subprocess.run([exe, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(docx)],
                               capture_output=True, text=True, timeout=300, shell=platform.system() == "Windows")
            generado = Path(tmp, docx.with_suffix(".pdf").name)
            if not generado.exists():
                raise RuntimeError(f"LibreOffice no generó el PDF:\n{(r.stderr or r.stdout)[-800:]}")
            shutil.copy(generado, pdf_path)
            hechos.append(pdf_path)
            if imprimir:
                dos_por_hoja(pdf_path, imp_path)
                hechos.append(imp_path)
    return hechos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guia")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--imprimir", action="store_true")
    ap.add_argument("--indice", action="store_true")
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    if not a.guia.endswith("_Guia.md"):
        sys.exit("La entrada tiene que ser una guía *_Guia.md de 3_Guias_de_Estudio/.")
    try:
        hechos = exportar(a.guia, a.pdf, a.imprimir, a.indice, a.forzar)
    except RuntimeError as e:
        sys.exit(f"Error: {e}")
    for h in hechos:
        print(f"✓ {h}")


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    main()
