"""Trabajo con textos extraídos (*_Crudo.md) para la skill /guia-estudio.

Comandos:
    python Scripts/estudio/fuente.py partes <crudo.md> [--palabras 4000]
        Divide el texto en partes de ~N palabras, cortando en límites de página
        ("## Página N") o, si no hay páginas, en títulos/párrafos. Muestra el plan.
    python Scripts/estudio/fuente.py texto <crudo.md> --parte N [--palabras 4000]
        Imprime el texto de la parte N (mismo corte que `partes`), con sus marcas de página.
    python Scripts/estudio/fuente.py cobertura <crudo.md> [<crudo2.md> ...] --guia <guia.md>
        Control de omisiones: busca en la guía los términos destacados, autores con año,
        cifras y años del texto fuente, y lista los que no aparecen (agrupados por página).
        También revisa que las citas "p. N" de la guía existan en la fuente.
        Es una heurística: cada faltante hay que mirarlo y decidir si importa.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

RE_PAGINA = re.compile(r"^##\s+P[áa]gina\s+(\d+)\s*$", re.M)


def _norm(t):
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^\w%.,]+", " ", t.lower())).strip()


def bloques(texto):
    """Lista de (pagina | None, texto). Si no hay marcas de página, corta por títulos y párrafos."""
    marcas = list(RE_PAGINA.finditer(texto))
    if marcas:
        out = []
        for i, m in enumerate(marcas):
            fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
            out.append((int(m.group(1)), texto[m.start():fin]))
        return out
    trozos = re.split(r"(?m)(?=^#{1,3}\s)|\n\s*\n", texto)
    return [(None, t) for t in trozos if t.strip()]


def partes(texto, palabras=4000):
    """Agrupa bloques en partes de ~`palabras`. Devuelve [{n, pag_desde, pag_hasta, palabras, texto, titulo}]."""
    res, actual = [], []

    def cerrar():
        if not actual:
            return
        txt = "\n".join(b for _, b in actual)
        pags = [p for p, _ in actual if p is not None]
        tit = next((l.strip("# ").strip() for l in txt.splitlines()
                    if l.startswith("#") and not RE_PAGINA.match(l)), "")
        if not tit:
            tit = next((l.strip() for l in txt.splitlines() if len(l.strip()) > 20 and not RE_PAGINA.match(l)), "")
        res.append({"n": len(res) + 1, "pag_desde": min(pags) if pags else None,
                    "pag_hasta": max(pags) if pags else None, "palabras": len(txt.split()),
                    "texto": txt, "titulo": tit[:70]})
        actual.clear()

    cuenta = 0
    for pag, b in bloques(texto):
        n = len(b.split())
        if actual and cuenta + n > palabras:
            cerrar()
            cuenta = 0
        actual.append((pag, b))
        cuenta += n
    cerrar()
    return res


# --- cobertura -------------------------------------------------------------------------
STOP = {"el", "la", "los", "las", "un", "una", "de", "del", "y", "o", "en", "que", "a", "por", "para",
        "con", "su", "se", "lo", "es", "no", "al", "como", "más", "mas", "the", "of", "and", "in", "to"}


RE_BIBLIO = re.compile(r"(?mi)^\s*(?:#+\s*)?(bibliograf[ií]a|referencias(?: bibliogr[áa]ficas)?|notas)\s*:?\s*$")
LUGARES = {"Aires", "Madrid", "Barcelona", "Paris", "París", "York", "Londres", "Amorrortu", "Paidós", "Paidos", "Manantial"}


def sin_bibliografia(texto):
    """Corta la bibliografía o notas finales (último 30 % del texto) para no contar sus citas."""
    for m in RE_BIBLIO.finditer(texto):
        if m.start() > len(texto) * 0.7:
            return texto[: m.start()]
    return texto


def items_clave(texto):
    """Devuelve {item: [páginas]} con lo que una guía extendida no debería omitir."""
    encontrados = {}
    texto = sin_bibliografia(texto)

    def add(item, pag):
        item = item.strip(" .,;:()«»\"'“”")
        if len(item) < 3 or _norm(item) in STOP:
            return
        encontrados.setdefault(item, set())
        if pag is not None:
            encontrados[item].add(pag)

    propios = {}
    for pag, b in bloques(texto):
        # Términos destacados en negrita o cursiva (si el texto los conserva)
        for m in re.finditer(r"\*\*([^*\n]{3,60})\*\*|(?<![*\w])\*([^*\n]{3,60})\*(?![*\w])", b):
            add(next(g for g in m.groups() if g), pag)
        # Términos entre comillas (conceptos y fórmulas citadas): hasta 6 palabras
        for m in re.finditer(r"[«“\"]([^»”\"\n]{3,60})[»”\"]", b):
            if len(m.group(1).split()) <= 6:
                add(m.group(1), pag)
        # Autor (año) / (Autor, año); se descartan lugares de edición ("Buenos Aires, 1996")
        for m in re.finditer(r"\b([A-ZÁÉÍÓÚ][a-záéíóúñ]+(?:\s+(?:y|e|&)\s+[A-ZÁÉÍÓÚ][a-záéíóúñ]+)?)\s*,?\s*\(?((?:18|19|20)\d{2})\)?", b):
            if m.group(1) not in LUGARES:
                add(f"{m.group(1)} {m.group(2)}", pag)
        # Porcentajes
        for m in re.finditer(r"\b\d+(?:[.,]\d+)?\s?%", b):
            add(m.group(0), pag)
        # Nombres propios (mayúscula que no inicia oración): autores, casos, instituciones
        for m in re.finditer(r"(?<=[a-záéíóúñ,;] )([A-ZÁÉÍÓÚ][a-záéíóúñ]{3,}(?:\s[A-ZÁÉÍÓÚ][a-záéíóúñ]{3,})?)", b):
            if m.group(1) not in LUGARES:
                propios.setdefault(m.group(1), set()).add(pag)
    for nombre, pags in propios.items():
        if len(pags) >= 2 or None in pags:
            for pg in pags:
                add(nombre, pg)
    return {k: sorted(p for p in v if p is not None) for k, v in encontrados.items()}


def presente(item, guia_norm):
    n = _norm(item)
    if n in guia_norm:
        return True
    # Autor + año: alcanza con que aparezcan ambos cerca (formatos distintos de cita)
    m = re.match(r"(.+) ((?:18|19|20)\d{2})$", n)
    if m:
        return re.search(re.escape(m.group(1)) + r".{0,40}" + m.group(2), guia_norm) is not None or (
            m.group(1) in guia_norm and m.group(2) in guia_norm)
    return False


def cobertura(crudos, guia):
    guia_txt = Path(guia).read_text(encoding="utf-8-sig")
    guia_norm = _norm(guia_txt)
    faltan, total, pags_fuente = {}, 0, set()
    for c in crudos:
        texto = Path(c).read_text(encoding="utf-8-sig")
        pags_fuente |= {p for p, _ in bloques(texto) if p is not None}
        for item, pags in items_clave(texto).items():
            total += 1
            if not presente(item, guia_norm):
                faltan[item] = pags
    citas = {int(p) for p in re.findall(r"\bpp?\.\s?(\d+)", guia_txt)}
    citas_invalidas = sorted(citas - pags_fuente) if pags_fuente else []
    return total, faltan, sorted(citas), citas_invalidas, sorted(pags_fuente)


def _cli():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("partes")
    p.add_argument("crudo")
    p.add_argument("--palabras", type=int, default=4000)
    t = sub.add_parser("texto")
    t.add_argument("crudo")
    t.add_argument("--parte", type=int, required=True)
    t.add_argument("--palabras", type=int, default=4000)
    c = sub.add_parser("cobertura")
    c.add_argument("crudos", nargs="+")
    c.add_argument("--guia", required=True)
    a = ap.parse_args()

    if a.cmd in ("partes", "texto"):
        ps = partes(Path(a.crudo).read_text(encoding="utf-8-sig"), a.palabras)
        if a.cmd == "texto":
            if not 1 <= a.parte <= len(ps):
                sys.exit(f"La fuente tiene {len(ps)} partes.")
            print(ps[a.parte - 1]["texto"])
            return
        total = sum(x["palabras"] for x in ps)
        print(f"{Path(a.crudo).name}: {total} palabras → {len(ps)} parte(s) de ~{a.palabras}")
        for x in ps:
            pags = f"págs. {x['pag_desde']}–{x['pag_hasta']}" if x["pag_desde"] else "sin páginas"
            print(f"  Parte {x['n']}: {pags:<14} {x['palabras']:>6} palabras  {x['titulo']}")
        return

    total, faltan, citas, invalidas, pags = cobertura(a.crudos, a.guia)
    cubiertos = total - len(faltan)
    print(f"Cobertura de ítems clave: {cubiertos}/{total} ({round(100 * cubiertos / total) if total else 100} %)")
    if pags:
        print(f"Citas de página en la guía: {len(citas)} distintas" + (f"; INEXISTENTES en la fuente: {invalidas}" if invalidas else " (todas existen en la fuente)"))
        sin_citar = sorted(set(pags) - set(citas))
        if sin_citar:
            print(f"Páginas de la fuente nunca citadas: {sin_citar}")
    if faltan:
        print("\nNo aparecen en la guía (revisar si son importantes):")
        for item, ps in sorted(faltan.items(), key=lambda kv: (kv[1] or [0])[0]):
            print(f"  - {item}" + (f"  (p. {', '.join(map(str, ps))})" if ps else ""))
    sys.exit(1 if invalidas else 0)


if __name__ == "__main__":
    _cli()
