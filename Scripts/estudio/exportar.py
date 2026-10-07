"""Exporta una guía .md a Word (y opcionalmente PDF e impresión 2 por hoja) — skill /exportar.

Uso:
    python Scripts/estudio/exportar.py <guia.md> [--pdf] [--imprimir] [--indice] [--sin-saltos] [--forzar]

  - Renderiza los diagramas Mermaid (diagramas.py) y los inserta como imágenes con un ancho que
    entra en la página (máx. 16 × 20 cm, sin agrandar imágenes chicas).
  - Convierte con pandoc usando la plantilla de estilos Scripts/estudio/plantillas/plantilla_guia.docx
    → [misma carpeta]/[Unidad]_[Tema]_Guia.docx
  - --pdf: además genera el .pdf con LibreOffice.
  - --imprimir: además genera 3_Guias_de_Estudio/_imprimir/[...]_Guia_Imprimir.pdf (A4 apaisado,
    2 páginas por hoja). Implica --pdf.
  - Recuadros de color y saltos de página con el filtro plantillas/recuadros.lua: las citas en bloque
    que empiezan con «Idea-fuerza», «🔑», «Para el parcial», «Esqueleto», «⚠ No confundir»,
    «▸ Complemento», «Fuente»… salen como recuadros; cada sección «## N.» empieza en página nueva.
    La plantilla trae encabezado con el título de la guía, pie con «página / total», márgenes
    estrechos (1,27 cm) con 3 cm a la derecha para anotar a mano, y texto justificado; las tablas
    se alinean a la izquierda (el script se lo pone a cada párrafo de tabla).
  - --indice: agrega índice al principio del Word (Word pide "actualizar campos" al abrir).
  - --sin-saltos: sin saltos de página entre secciones (gasta menos papel).
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
import zipfile
from xml.sax.saxutils import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagramas  # noqa: E402
import frontmatter  # noqa: E402

PLANTILLA = Path(__file__).resolve().parent / "plantillas" / "plantilla_guia.docx"
FILTRO = Path(__file__).resolve().parent / "plantillas" / "recuadros.lua"
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


RE_SALTO = re.compile(rb'<w:p>\s*<w:r>\s*<w:br w:type="page"\s*/>\s*</w:r>\s*</w:p>'
                      rb'((?:\s*<w:bookmark(?:Start|End)[^>]*/>)*\s*<w:p>\s*<w:pPr>\s*<w:pStyle w:val="Heading2"\s*/>)')


RE_TABLA = re.compile(rb"<w:tbl>.*?</w:tbl>", re.S)
RE_PPR_TABLA = re.compile(rb"<w:pPr>(?:(?!</w:pPr>).)*</w:pPr>", re.S)


def tabla_a_la_izquierda(m):
    """En la plantilla el texto es justificado; en las tablas queda feo: se alinea a la izquierda
    cada párrafo de tabla que no traiga su propia alineación."""
    def ppr(mp):
        bloque = mp.group(0)
        if b"<w:jc " in bloque:
            return bloque
        return bloque.replace(b"</w:pPr>", b'<w:jc w:val="left"/></w:pPr>')
    tabla = RE_PPR_TABLA.sub(ppr, m.group(0))
    return re.sub(rb"<w:p>(?!\s*<w:pPr>)", b'<w:p><w:pPr><w:jc w:val="left"/></w:pPr>', tabla)


def ajustar_docx(docx, titulo):
    """Retoques que pandoc no hace: título en el encabezado, saltos de página como «salto antes del
    título» (no dejan páginas en blanco si el salto cae al final de una página) y tablas alineadas
    a la izquierda."""
    tmp = docx.with_suffix(".ajuste.docx")
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            datos = zin.read(item.filename)
            if item.filename.startswith("word/header"):
                datos = datos.replace(b"TITULO_GUIA", escape(titulo).encode("utf-8"))
            elif item.filename == "word/document.xml":
                datos = RE_SALTO.sub(rb"\1<w:pageBreakBefore/>", datos)
                datos = RE_TABLA.sub(tabla_a_la_izquierda, datos)
            zout.writestr(item, datos)
    tmp.replace(docx)


def titulo_de(cuerpo, guia):
    m = re.search(r"^# (.+)$", cuerpo, re.M)
    return re.sub(r"[*_`]", "", m.group(1)).strip() if m else guia.stem


def exportar(guia, pdf=False, imprimir=False, indice=False, forzar=False, sin_saltos=False):
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
               "-f", "markdown+lists_without_preceding_blankline+pipe_tables-yaml_metadata_block-implicit_figures-tex_math_dollars",
               "--resource-path", str(guia.parent), "--reference-doc", str(PLANTILLA),
               "--lua-filter", str(FILTRO)]
        if sin_saltos:
            cmd += ["-M", "sin_saltos=true"]
        if indice:
            cmd += ["--toc", "--toc-depth=2", "-M", "toc-title=Índice"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"pandoc falló:\n{r.stderr[-1500:]}")
        ajustar_docx(Path(tmp, "guia.docx"), titulo_de(cuerpo, guia))
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
    ap.add_argument("--sin-saltos", action="store_true")
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    if not a.guia.endswith("_Guia.md"):
        sys.exit("La entrada tiene que ser una guía *_Guia.md de 3_Guias_de_Estudio/.")
    try:
        hechos = exportar(a.guia, a.pdf, a.imprimir, a.indice, a.forzar, a.sin_saltos)
    except RuntimeError as e:
        sys.exit(f"Error: {e}")
    for h in hechos:
        print(f"✓ {h}")


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    main()
