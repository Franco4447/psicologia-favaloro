"""Extrae texto de PDFs y PowerPoint a Markdown "crudo" (skill /digitalizar).

Uso:
    python Scripts/estudio/extraer.py <entrada.pdf|.pptx> <salida_Crudo.md> [opciones]

Opciones:
    --titulo "Autor - Título"   Título del documento (por defecto, el nombre del archivo)
    --paginas 3-10              Solo ese rango de páginas/diapositivas
    --ocr auto|si|no            auto (defecto): OCR solo en páginas sin texto (escaneadas)
    --idioma spa                Idioma de Tesseract (spa, eng, spa+eng…)
    --imagenes                  Guarda las imágenes en 2_Textos_Extraidos/_media/<crudo>/ y las enlaza
    --diapositivas              Conserva los saltos de línea (automático en PPTX y PDFs apaisados)

Qué hace:
  - PDF con texto: extrae página por página; detecta páginas a DOS COLUMNAS y las lee en orden.
  - PDF escaneado: renderiza la página (pypdfium2) y aplica OCR con Tesseract, midiendo la confianza.
  - Limpieza: une palabras cortadas por guion al final de línea, rearma párrafos, quita encabezados
    y pies de página repetidos y números de página sueltos, normaliza ligaduras (ﬁ → fi).
  - PPTX: título, texto (con viñetas por nivel), tablas y notas del orador de cada diapositiva.
  - Escribe "## Página N" / "## Diapositiva N" para poder citar, una cabecera YAML y un informe de
    calidad (páginas por OCR, confianza media, páginas dudosas).
"""
import argparse
import collections
import io
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter  # noqa: E402

LIGADURAS = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "\u00ad": "", "\u00a0": " "}
FIN_ORACION = tuple('.!?:»”"')
MIN_CHARS_TEXTO = 40      # menos que esto en una página = probablemente escaneada
UMBRAL_CONF = 75          # confianza OCR media por debajo de esto = página dudosa


# ---------------------------------------------------------------------- limpieza
def normalizar(t):
    for a, b in LIGADURAS.items():
        t = t.replace(a, b)
    return t


def quitar_repetidos(paginas):
    """Quita encabezados/pies que se repiten en muchas páginas (y números de página sueltos)."""
    if len(paginas) < 3:
        return paginas
    cuenta = collections.Counter()
    for lineas in paginas:
        bordes = [l for l in lineas if l.strip()][:2] + [l for l in lineas if l.strip()][-2:]
        cuenta.update({re.sub(r"\d+", "#", l.strip()) for l in bordes})
    repetidas = {k for k, n in cuenta.items() if n >= max(3, 0.4 * len(paginas)) and len(k) < 120}
    limpias = []
    for lineas in paginas:
        nl = [l for l in lineas
              if re.sub(r"\d+", "#", l.strip()) not in repetidas and not re.fullmatch(r"\s*[-–]?\s*\d{1,4}\s*[-–]?\s*", l)]
        limpias.append(nl)
    return limpias


def armar_parrafos(lineas, diapositivas=False):
    """Une líneas cortadas por guion y rearma párrafos (salvo en diapositivas)."""
    # "pla- -" / "pla- —": basura del OCR después del guion de corte
    lineas = [re.sub(r"([a-záéíóúñü])-\s*[-–—]+\s*$", r"\1-", l.rstrip()) for l in lineas]
    if diapositivas:
        return "\n".join(l for l in lineas if l.strip())
    largos = [len(l) for l in lineas if len(l) > 20]
    mediana = statistics.median(largos) if largos else 60
    out, actual = [], ""
    for i, l in enumerate(lineas):
        s = l.strip()
        if not s:
            if actual:
                out.append(actual)
                actual = ""
            continue
        if actual.endswith("-") and re.search(r"[a-záéíóúñü]-$", actual) and s[:1].islower():
            actual = actual[:-1] + s                      # fun- / da → funda
        elif actual:
            actual += " " + s
        else:
            actual = s
        sig = next((x.strip() for x in lineas[i + 1:] if x.strip()), "")
        corta = len(s) < 0.75 * mediana
        es_titulo = re.fullmatch(r"(\d+\.|[IVX]+\.|[A-ZÁÉÍÓÚ][^.]{0,60})", s) and corta and not s.endswith(",")
        if (s.endswith(FIN_ORACION) and (corta or (sig[:1].isupper() and corta))) or es_titulo or not sig:
            out.append(actual)
            actual = ""
    if actual:
        out.append(actual)
    return "\n\n".join(out)


# ---------------------------------------------------------------------- PDF
def columnas(page):
    """Devuelve las cajas (bbox) a leer, en orden de lectura.

    Divide la página en franjas horizontales: las franjas con líneas que cruzan el centro
    (títulos, figuras, leyendas a todo el ancho) se leen enteras; las demás, en dos columnas
    (primero la izquierda, después la derecha).
    """
    words = page.extract_words(use_text_flow=False)
    x0, top, x1, bottom = page.bbox
    if len(words) < 80:
        return [page.bbox]
    mitad = (x0 + x1) / 2
    der = sum(1 for w in words if w["x0"] >= mitad)
    lineas = collections.defaultdict(list)
    for w in words:
        lineas[round(w["top"] / 3)].append(w)
    info = []
    for _, ws in sorted(lineas.items()):
        cruza = any(w["x0"] < mitad - 5 and w["x1"] > mitad + 5 for w in ws)
        info.append((min(w["top"] for w in ws), max(w["bottom"] for w in ws), cruza))
    if der / len(words) < 0.3 or sum(c for *_, c in info) > 0.5 * len(info):
        return [page.bbox]                                   # una sola columna
    franjas = []                                             # [desde, hasta, a_todo_el_ancho]
    for t, b_, cruza in info:
        if franjas and franjas[-1][2] == cruza:
            franjas[-1][1] = b_
        else:
            franjas.append([t, b_, cruza])
    cajas, desde = [], top
    for i, (t, b_, cruza) in enumerate(franjas):
        hasta = bottom if i == len(franjas) - 1 else (b_ + franjas[i + 1][0]) / 2
        if cruza:
            cajas.append((x0, desde, x1, hasta))
        else:
            cajas += [(x0, desde, mitad, hasta), (mitad, desde, x1, hasta)]
        desde = hasta
    return cajas


def tesseract():
    exe = shutil.which("tesseract")
    if not exe and sys.platform == "win32":
        candidatos = [Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
                      Path(os.environ.get("LOCALAPPDATA", ""), "Programs", "Tesseract-OCR", "tesseract.exe")]
        exe = next((str(p) for p in candidatos if p.exists()), None)
    return exe


def ocr_pagina(pdf_path, indice, idioma):
    """OCR de una página. Devuelve (texto, confianza_media)."""
    import pypdfium2 as pdfium
    exe = tesseract()
    if not exe:
        raise RuntimeError("falta Tesseract (ver Scripts/estudio/verificar_entorno.py)")
    doc = pdfium.PdfDocument(str(pdf_path))
    img = doc[indice].render(scale=300 / 72).to_pil()
    with tempfile.TemporaryDirectory() as d:
        png = Path(d, "p.png")
        img.save(png)
        r = subprocess.run([exe, str(png), str(Path(d, "out")), "-l", idioma, "--psm", "1", "tsv"],
                           capture_output=True, text=True)
        tsv = Path(d, "out.tsv")
        if not tsv.exists():
            raise RuntimeError(f"Tesseract falló: {r.stderr[-400:]}")
        filas = list(csv_tsv(tsv.read_text(encoding="utf-8")))
    lineas, confs, clave_ant = [], [], None
    for f in filas:
        # Los bloques y párrafos de Tesseract son poco fiables en escaneos de libros:
        # se arman los párrafos después, con la misma heurística que el texto de PDF.
        if f["level"] != "5" or not f["text"].strip():
            continue
        clave = (f["block_num"], f["par_num"], f["line_num"])
        if clave != clave_ant:
            lineas.append(f["text"])
            clave_ant = clave
        else:
            lineas[-1] += " " + f["text"]
        confs.append(float(f["conf"]))
    return lineas, (statistics.mean(confs) if confs else 0.0)


def csv_tsv(texto):
    lineas = texto.splitlines()
    cab = lineas[0].split("\t")
    for l in lineas[1:]:
        partes = l.split("\t")
        if len(partes) == len(cab):
            yield dict(zip(cab, partes))


def extraer_pdf(path, rango, modo_ocr, idioma, imagenes_dir):
    import pdfplumber
    from pypdf import PdfReader
    paginas, info = [], []
    lector = PdfReader(str(path)) if imagenes_dir else None
    with pdfplumber.open(str(path)) as pdf:
        n_total = len(pdf.pages)
        indices = range(*rango) if rango else range(n_total)
        apaisado = sum(p.width > p.height for p in pdf.pages[:5]) >= min(3, n_total)
        proporcion = pdf.pages[0].width / pdf.pages[0].height
        programa = " ".join(str(pdf.metadata.get(k, "")) for k in ("Creator", "Producer"))
        # 16:9 / 16:10 (los libros escaneados apaisados son ~1,41) o exportado por un programa de presentaciones
        formato_diapo = proporcion >= 1.55 or bool(re.search(r"PowerPoint|Keynote|Impress|Google|Slides", programa))
        for i in indices:
            if i >= n_total:
                break
            page = pdf.pages[i]
            texto = ""
            cajas = columnas(page)
            for caja in cajas:
                texto += (page.crop(caja).extract_text(x_tolerance=1.5) or "") + "\n"
            texto = normalizar(texto)
            metodo, conf = "texto", None
            if modo_ocr == "si" or (modo_ocr == "auto" and len(texto.strip()) < MIN_CHARS_TEXTO):
                lineas, conf = ocr_pagina(path, i, idioma)
                lineas = [normalizar(l) for l in lineas]
                metodo = "ocr"
            else:
                lineas = texto.splitlines()
            figuras = []
            if imagenes_dir:
                for k, im in enumerate(lector.pages[i].images, 1):
                    if len(im.data) < 8000:                  # íconos y adornos
                        continue
                    destino = imagenes_dir / f"p{i + 1:03d}_{k}{Path(im.name).suffix or '.png'}"
                    destino.parent.mkdir(parents=True, exist_ok=True)
                    destino.write_bytes(im.data)
                    figuras.append(destino)
            paginas.append(lineas)
            info.append({"n": i + 1, "metodo": metodo, "conf": conf, "columnas": 2 if len(cajas) > 1 else 1, "figuras": figuras})
    return paginas, info, apaisado and formato_diapo


# ---------------------------------------------------------------------- PPTX
def ocr_imagen(blob, idioma):
    """OCR de una imagen suelta (p. ej., de una diapositiva). Devuelve (líneas, confianza)."""
    exe = tesseract()
    if not exe:
        return [], None
    with tempfile.TemporaryDirectory() as d:
        img = Path(d, "img")
        img.write_bytes(blob)
        subprocess.run([exe, str(img), str(Path(d, "out")), "-l", idioma, "--psm", "3", "tsv"],
                       capture_output=True, text=True)
        tsv = Path(d, "out.tsv")
        if not tsv.exists():
            return [], None
        filas = [f for f in csv_tsv(tsv.read_text(encoding="utf-8")) if f["level"] == "5" and f["text"].strip()]
    lineas, ant = [], None
    for f in filas:
        if float(f["conf"]) < 40:                    # palabras muy dudosas (dibujos leídos como letras)
            continue
        clave = (f["block_num"], f["par_num"])         # en imágenes, un recuadro/párrafo = una línea
        if clave != ant:
            lineas.append(f["text"])
            ant = clave
        else:
            lineas[-1] += " " + f["text"]
    confs = [float(f["conf"]) for f in filas if float(f["conf"]) >= 40]
    return [l for l in lineas if len(l) > 2], (statistics.mean(confs) if confs else None)


def extraer_pptx(path, rango, imagenes_dir, modo_ocr="auto", idioma="spa"):
    from pptx import Presentation
    from pptx.util import Emu  # noqa: F401
    prs = Presentation(str(path))
    paginas, info = [], []
    for i, slide in enumerate(prs.slides):
        if rango and not (rango[0] <= i < rango[1]):
            continue
        lineas, figuras, blobs = [], [], []
        titulo = slide.shapes.title.text.strip() if slide.shapes.title is not None and slide.shapes.title.has_text_frame else ""
        if titulo:
            lineas.append(f"### {normalizar(titulo)}")

        def recorrer(shapes):
            for sh in shapes:
                if sh.shape_type == 6 and hasattr(sh, "shapes"):          # grupo
                    recorrer(sh.shapes)
                    continue
                if slide.shapes.title is not None and sh.shape_id == slide.shapes.title.shape_id:
                    continue
                if getattr(sh, "has_table", False) and sh.has_table:
                    filas = [[normalizar(c.text).replace("\n", " ").strip() for c in r.cells] for r in sh.table.rows]
                    if filas:
                        lineas.append("| " + " | ".join(filas[0]) + " |")
                        lineas.append("|" + "---|" * len(filas[0]))
                        lineas.extend("| " + " | ".join(f) + " |" for f in filas[1:])
                elif getattr(sh, "has_text_frame", False) and sh.has_text_frame:
                    for p in sh.text_frame.paragraphs:
                        t = normalizar("".join(r.text for r in p.runs)).strip()
                        if t:
                            lineas.append("  " * p.level + "- " + t)
                elif sh.shape_type == 13:                                   # imagen
                    blob = sh.image.blob
                    if len(blob) >= 8000:
                        blobs.append(blob)
                        if imagenes_dir:
                            destino = imagenes_dir / f"d{i + 1:03d}_{len(figuras) + 1}.{sh.image.ext}"
                            destino.parent.mkdir(parents=True, exist_ok=True)
                            destino.write_bytes(blob)
                            figuras.append(destino)

        recorrer(slide.shapes)
        metodo, conf = "pptx", None
        texto_propio = [l for l in lineas if not l.startswith("###")]
        if blobs and (modo_ocr == "si" or (modo_ocr == "auto" and not texto_propio)):
            ocr_lineas, confs = [], []
            for b in blobs:
                ls, c = ocr_imagen(b, idioma)
                ocr_lineas += ls
                if c is not None:
                    confs.append(c)
            if ocr_lineas:
                lineas += ["", "**Texto en imagen (OCR):**"] + [f"- {normalizar(l)}" for l in ocr_lineas]
                metodo, conf = "ocr", (statistics.mean(confs) if confs else None)
        if slide.has_notes_slide:
            notas = normalizar(slide.notes_slide.notes_text_frame.text).strip()
            if notas:
                lineas += ["", "**Notas del orador:**", notas]
        paginas.append(lineas)
        info.append({"n": i + 1, "metodo": metodo, "conf": conf, "columnas": 1, "figuras": figuras})
    return paginas, info


# ---------------------------------------------------------------------- salida
def informe(info, paginas_md):
    ocr = [x for x in info if x["metodo"] == "ocr"]
    vacias = [x["n"] for x, md in zip(info, paginas_md) if len(md.strip()) < MIN_CHARS_TEXTO]
    dudosas = [x["n"] for x in ocr if x["conf"] is not None and x["conf"] < UMBRAL_CONF]
    raras = []
    for x, md in zip(info, paginas_md):
        letras = sum(c.isalpha() for c in md)
        if md.strip() and letras / max(len(md.strip()), 1) < 0.55:
            raras.append(x["n"])
    return {
        "paginas": len(info),
        "por_ocr": [x["n"] for x in ocr],
        "confianza_ocr_media": round(statistics.mean(x["conf"] for x in ocr), 1) if ocr else None,
        "paginas_dudosas": sorted(set(dudosas + raras)),
        "paginas_vacias": vacias,
        "paginas_dos_columnas": [x["n"] for x in info if x["columnas"] == 2],
        "figuras": sum(len(x["figuras"]) for x in info),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada")
    ap.add_argument("salida")
    ap.add_argument("--titulo")
    ap.add_argument("--paginas")
    ap.add_argument("--ocr", choices=["auto", "si", "no"], default="auto")
    ap.add_argument("--idioma", default="spa")
    ap.add_argument("--imagenes", action="store_true")
    ap.add_argument("--diapositivas", action="store_true")
    a = ap.parse_args()

    ent, sal = Path(a.entrada), Path(a.salida)
    if not sal.name.endswith("_Crudo.md"):
        sys.exit("La salida tiene que llamarse [Unidad]_[Autor]_[Capítulo]_Crudo.md (ver nombres.py).")
    rango = None
    if a.paginas:
        d, _, h = a.paginas.partition("-")
        rango = (int(d) - 1, int(h or d))
    img_dir = sal.parent / "_media" / sal.stem if a.imagenes else None
    try:
        if ent.suffix.lower() == ".pptx":
            paginas, info = extraer_pptx(ent, rango, img_dir, a.ocr, a.idioma)
            diapos, rotulo = True, "Diapositiva"
        elif ent.suffix.lower() == ".pdf":
            paginas, info, apaisado = extraer_pdf(ent, rango, a.ocr, a.idioma, img_dir)
            # Diapositivas = apaisado con proporción de pantalla o exportado por un programa de presentaciones.
            # Los escaneos de libros también son apaisados (dos páginas por imagen, ~1,41): esos son prosa.
            diapos = a.diapositivas or apaisado
            rotulo = "Diapositiva" if diapos else "Página"
        else:
            sys.exit("Formato no soportado: usar .pdf o .pptx (los .ppt viejos, guardarlos antes como .pptx).")
    except RuntimeError as e:
        sys.exit(f"Error: {e}")

    if ent.suffix.lower() == ".pdf":
        paginas = quitar_repetidos(paginas)
    md_paginas = [armar_parrafos(p, diapositivas=diapos) for p in paginas]
    rep = informe(info, md_paginas)
    titulo = a.titulo or ent.stem
    cuerpo = [f"# {titulo}", ""]
    for x, md in zip(info, md_paginas):
        cuerpo += [f"## {rotulo} {x['n']}", "", md.strip() or "*(sin texto)*", ""]
        for fig in x["figuras"]:
            cuerpo += [f"![Figura {rotulo.lower()} {x['n']}](_media/{sal.stem}/{fig.name})", ""]
    partes = sal.resolve().parts
    materia = partes[-3] if len(partes) >= 3 else ""
    meta = {"materia": materia, "unidad": sal.name.split("_")[0], "tipo": "crudo",
            "fuentes": [{"archivo": f"1_Bibliografia_Original/{ent.name}"}], "skill": "digitalizar",
            "metodo": sorted({x["metodo"] for x in info}), "calidad": rep}
    frontmatter.escribir(sal, meta, "\n".join(cuerpo))

    print(f"✓ {sal}  ({rep['paginas']} {rotulo.lower()}s, {len(' '.join(md_paginas).split())} palabras)")
    if rep["por_ocr"]:
        print(f"  OCR en {len(rep['por_ocr'])} página(s); confianza media {rep['confianza_ocr_media']} %")
    if rep["paginas_dos_columnas"]:
        print(f"  Dos columnas detectadas en: {rep['paginas_dos_columnas']}")
    if rep["paginas_dudosas"]:
        print(f"  ⚠ Revisar a mano (OCR bajo o texto raro): {rep['paginas_dudosas']}")
    if rep["paginas_vacias"]:
        print(f"  ⚠ Sin texto: {rep['paginas_vacias']}")
    if rep["figuras"]:
        print(f"  {rep['figuras']} imagen(es) en {img_dir}")


if __name__ == "__main__":
    main()
