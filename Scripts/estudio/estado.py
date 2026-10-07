"""Estado de una materia en el pipeline (skill /estado-materia).

Uso:
    python Scripts/estudio/estado.py                       # todas las materias de 2do Año
    python Scripts/estudio/estado.py Psicoanálisis Biología
    python Scripts/estudio/estado.py --anio "1er Año" ...

Para cada unidad/clase muestra qué hay en cada etapa (textos extraídos, guía, Word, flashcards,
simulacro, último resultado) y lista lo pendiente: textos sin guía, guías sin Word, sin flashcards o
sin simulacro, temas flojos de los simulacros y nombres que no siguen AGENTS.md.
Los textos extraídos no se versionan en git: se cuentan los de la copia local.
"""
import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter  # noqa: E402
from nombres import RAIZ, validar  # noqa: E402

RE_COD = re.compile(r"^(U\d{2}|C\d{2}(?:_\d{2})*|Global_(?:1erC|2doC)|Global|Transversal_[A-Za-z0-9]+|Inv)(?=_)")
ETAPAS = {"2_Textos_Extraidos": "crudo", "3_Guias_de_Estudio": "guia", "4_Flashcards": "flash", "5_Evaluaciones": "eval"}


def codigo(nombre):
    m = RE_COD.match(nombre)
    return m.group(1) if m else None


def orden(cod):
    m = re.match(r"([A-Za-z]+)_?(\d+)?", cod)
    pref = {"U": 0, "C": 1, "Global": 2, "Transversal": 3, "Inv": 4}.get(m.group(1), 5)
    return (pref, int(m.group(2)) if m.group(2) else 0, cod)


def analizar(dir_materia):
    filas = collections.defaultdict(lambda: collections.defaultdict(list))
    malos, editadas, flojos, anteriores = [], [], [], []
    for etapa, clave in ETAPAS.items():
        d = dir_materia / etapa
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.is_dir():
                continue
            probs = validar(f)
            if probs:
                malos.append((f.relative_to(dir_materia), probs[0]))
            cod = codigo(f.name)
            if not cod:
                continue
            if clave == "guia":
                variante = "resumen" if re.search(r"_(Resumen|Sintesis\w*|Repaso)_Guia", f.name) else "guia"
                filas[cod][f"{variante}{f.suffix}"].append(f)
                if f.suffix == ".md" and frontmatter.estado(f) == "editado":
                    editadas.append(f.name)
                if f.suffix == ".md" and variante == "guia" and formato_anterior(f):
                    anteriores.append(cod)
            elif clave == "eval":
                tipo = "resultado" if f.stem.endswith("_Resultados") else "eval"
                filas[cod][tipo].append(f)
                if tipo == "resultado":
                    meta, _ = frontmatter.leer(f)
                    if meta:
                        for t in meta.get("temas_flojos", []):
                            flojos.append((cod, t["tema"], t.get("fuente", "")))
            else:
                filas[cod][clave].append(f)
    return filas, malos, editadas, flojos, anteriores


def formato_anterior(guia):
    """True si la guía no tiene las secciones del formato actual (references/plantilla_guia.md)."""
    texto = guia.read_text(encoding="utf-8-sig", errors="replace")
    return "## Hilo conductor" not in texto or "Esqueleto" not in texto


def marca(n):
    return "✓" if n == 1 else (str(n) if n else "—")


def reporte(dir_materia):
    filas, malos, editadas, flojos, anteriores = analizar(dir_materia)
    out = [f"## {dir_materia.name}", ""]
    if not filas:
        out += ["*(sin archivos en las carpetas del pipeline)*", ""]
        return out, {}
    out += ["| Unidad | Textos extraídos | Guía .md | Word | Resúmenes / fichas | Flashcards | Simulacro / evaluación | Último resultado |",
            "|---|---|---|---|---|---|---|---|"]
    pend = collections.defaultdict(list)
    for cod in sorted(filas, key=orden):
        r = filas[cod]
        guia_md, guia_doc = r.get("guia.md", []), r.get("guia.docx", [])
        res = len(r.get("resumen.md", [])) + len(r.get("resumen.docx", [])) + len(r.get("resumen.pdf", []))
        ult = ""
        if r.get("resultado"):
            meta, _ = frontmatter.leer(r["resultado"][-1])
            ult = f"{meta.get('porcentaje')} % ({meta.get('fecha')})" if meta else "✓"
        out.append(f"| {cod} | {marca(len(r.get('crudo', [])))} | {marca(len(guia_md))} | {marca(len(guia_doc))} | "
                   f"{marca(res)} | {marca(len(r.get('flash', [])))} | {marca(len(r.get('eval', [])))} | {ult or '—'} |")
        hay_guia = guia_md or guia_doc
        if r.get("crudo") and not hay_guia:
            pend["Textos extraídos sin guía (→ /guia-estudio)"].append(cod)
        if guia_md and not guia_doc:
            pend["Guías sin Word (→ /exportar)"].append(cod)
        if hay_guia and not r.get("flash"):
            pend["Guías sin flashcards (→ /flashcards)"].append(cod)
        if hay_guia and not r.get("eval"):
            pend["Guías sin simulacro (→ /simulacro)"].append(cod)
    out.append("")
    for titulo, cods in pend.items():
        out.append(f"- **{titulo}:** {', '.join(cods)}")
    if flojos:
        out.append("- **Temas flojos en simulacros:** " + "; ".join(f"{c}: {t}" for c, t, _ in flojos))
    if anteriores:
        out.append("- **Guías con formato anterior** (sin hilo conductor o sin esqueletos de respuesta; "
                   f"actualizar con /guia-estudio cuando haya tiempo): {', '.join(sorted(set(anteriores), key=orden))}")
    if editadas:
        out.append(f"- **Guías editadas a mano** (no regenerar sin preguntar): {', '.join(editadas)}")
    if malos:
        out.append(f"- **Nombres fuera de AGENTS.md ({len(malos)}):**")
        out += [f"  - `{p}`: {motivo}" for p, motivo in malos[:15]]
        if len(malos) > 15:
            out.append(f"  - … y {len(malos) - 15} más (`python Scripts/estudio/nombres.py validar …`)")
    out.append("")
    return out, pend


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("materias", nargs="*")
    ap.add_argument("--anio", default="2do Año")
    a = ap.parse_args()
    base = RAIZ / a.anio
    if not base.is_dir():
        sys.exit(f"No existe {base}")
    dirs = [base / m for m in a.materias] if a.materias else sorted(p for p in base.iterdir() if p.is_dir())
    faltan = [d for d in dirs if not d.is_dir()]
    if faltan:
        sys.exit("No existe: " + ", ".join(d.name for d in faltan) + f". Materias: {', '.join(p.name for p in base.iterdir() if p.is_dir())}")
    lineas = [f"# Estado del pipeline — {a.anio}", ""]
    for d in dirs:
        lineas += reporte(d)[0]
    print("\n".join(lineas))


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    main()
