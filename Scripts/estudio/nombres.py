"""Nombres y rutas de archivos generados, según las convenciones de AGENTS.md.

Uso como módulo (desde las skills):
    from nombres import nombre, ruta, validar
    nombre("guia", "U05", tema="Duelo y melancolía")            -> "U05_DueloYMelancolia_Guia.md"
    ruta("2do Año", "Psicoanálisis", "guia", "U05", tema="...")  -> Path(".../3_Guias_de_Estudio/U05_..._Guia.md")

Uso por línea de comandos:
    python Scripts/estudio/nombres.py generar guia --unidad U05 --tema "Duelo y melancolía"
    python Scripts/estudio/nombres.py generar repaso --unidad U05 --tema "Duelo y melancolía"   # ficha de repaso
    python Scripts/estudio/nombres.py generar guia --unidad Transversal_EstructurasClinicas  # eje que cruza clases
    python Scripts/estudio/nombres.py generar crudo --unidad U04 --texto 15 --autor Freud --tema "Duelo y melancolía"
    python Scripts/estudio/nombres.py validar "2do Año/Psicoanálisis/3_Guias_de_Estudio/C01_CienciaYPsicoanalisisFreudYLasEscuelas_Guia.md" ...
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

# Etapa del pipeline y sufijo de cada tipo de archivo generado
TIPOS = {
    "crudo":      ("2_Textos_Extraidos", "Crudo", ".md"),
    "guia":       ("3_Guias_de_Estudio", "Guia", ".md"),
    "repaso":     ("3_Guias_de_Estudio", "Repaso_Guia", ".md"),   # ficha de repaso corta de una guía
    "imprimir":   ("3_Guias_de_Estudio/_imprimir", "Guia_Imprimir", ".pdf"),
    "diagrama":   ("3_Guias_de_Estudio/_media", None, ".png"),
    "flashcards": ("4_Flashcards", "Flashcards", ".csv"),
    "simulacro":  ("5_Evaluaciones", "Simulacro", ".md"),
    "resultados": ("5_Evaluaciones", "Resultados", ".md"),
    "enunciado":  ("5_Evaluaciones", "Enunciado", ".pdf"),
    "resuelto":   ("5_Evaluaciones", "Resuelto", ".pdf"),
}

# Códigos de unidad válidos (ver AGENTS.md → "Detalle de los componentes del nombre")
RE_UNIDAD = re.compile(
    r"^(U\d{2}|C\d{2}(?:_\d{2})*|Global(?:_(?:1erC|2doC))?|Transversal_[A-Za-z0-9]+|Inv)$"
)


def pascal(texto, max_palabras=0):
    """'Duelo y melancolía' -> 'DueloYMelancolia'. Nunca corta palabras por la mitad."""
    sin_acentos = "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )
    palabras = [p for p in re.split(r"[^A-Za-z0-9]+", sin_acentos) if p]
    if max_palabras:
        palabras = palabras[:max_palabras]
    return "".join(p[0].upper() + p[1:] for p in palabras)


def nombre(tipo, unidad, tema="", autor="", texto=None, nn=None, ext=None):
    """Arma el nombre de archivo para `tipo` (ver TIPOS)."""
    if tipo not in TIPOS:
        raise ValueError(f"Tipo desconocido: {tipo}. Opciones: {', '.join(TIPOS)}")
    if not RE_UNIDAD.match(unidad):
        raise ValueError(f"Código de unidad inválido: {unidad!r} (ej.: U05, C17_18, Global_1erC, Inv)")
    _, sufijo, ext_def = TIPOS[tipo]
    partes = [unidad]
    if texto is not None:
        partes.append(f"T{int(texto):02d}")
    if autor:
        partes.append(pascal(autor))
    if tema:
        partes.append(pascal(tema))
    if tipo == "crudo" and not autor:
        raise ValueError("Un texto extraído necesita autor: [Unidad]_[Autor]_[Capítulo]_Crudo.md")
    if tipo == "diagrama":
        if nn is None:
            raise ValueError("Un diagrama necesita número: [Unidad]_[Tema]_[NN].png")
        partes.append(f"{int(nn):02d}")
    else:
        partes.append(sufijo)
    return "_".join(partes) + (ext or ext_def)


def ruta(anio, materia, tipo, unidad, **kwargs):
    """Ruta completa dentro del repo: [Año]/[Materia]/[Etapa]/[nombre]."""
    etapa = TIPOS[tipo][0]
    return RAIZ / anio / materia / etapa / nombre(tipo, unidad, **kwargs)


def validar(path):
    """Devuelve la lista de problemas del nombre/ubicación de `path` (vacía si está bien)."""
    p = Path(path)
    problemas = []
    stem = p.stem
    if re.search(r"\s|\(|\)", p.name):
        problemas.append("tiene espacios o paréntesis")
    if re.match(r"^(\(\d\)|\d+ - )", p.name):
        problemas.append("tiene prefijo de copia como '(2) ' o '2 - '")
    if re.search(r"_(v\d+|FINAL)$", stem, re.I) or re.search(r"_(v\d+|FINAL)_", stem, re.I):
        problemas.append("tiene sufijo de versión (_v10, _FINAL): el historial lo guarda git")
    if ".temp." in p.name or p.name.lower().startswith("test"):
        problemas.append("es un archivo temporal: borrarlo al terminar")
    for tipo, (etapa, sufijo, _) in TIPOS.items():
        if sufijo and stem.endswith("_" + sufijo):
            if etapa.split("/")[0] not in p.parts:
                problemas.append(f"un *_{sufijo} debería estar en {etapa}/")
            unidad = stem.split("_")[0]
            cand = "_".join(stem.split("_")[:2])
            if not (RE_UNIDAD.match(unidad) or RE_UNIDAD.match(cand)):
                problemas.append(f"no empieza con un código de unidad válido (U05, C17_18, Global_1erC…): {unidad}")
            sin_sufijo = stem[: -len(sufijo) - 1]
            if RE_UNIDAD.match(sin_sufijo) and not sin_sufijo.startswith(("Global", "Transversal")):
                problemas.append(f"falta el tema: [Unidad]_[Tema]_{sufijo} (ej.: {sin_sufijo}_[Tema]_{sufijo})")
            break
    return problemas


def _cli():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generar", help="imprime el nombre para un archivo nuevo")
    g.add_argument("tipo", choices=list(TIPOS))
    g.add_argument("--unidad", required=True)
    g.add_argument("--tema", default="")
    g.add_argument("--autor", default="")
    g.add_argument("--texto", type=int)
    g.add_argument("--nn", type=int)
    g.add_argument("--ext")
    v = sub.add_parser("validar", help="revisa nombres y ubicaciones de archivos")
    v.add_argument("archivos", nargs="+")
    a = ap.parse_args()

    if a.cmd == "generar":
        try:
            print(nombre(a.tipo, a.unidad, tema=a.tema, autor=a.autor, texto=a.texto, nn=a.nn, ext=a.ext))
        except ValueError as e:
            sys.exit(f"Error: {e}")
    else:
        mal = 0
        for f in a.archivos:
            probs = validar(f)
            if probs:
                mal += 1
                print(f"✗ {f}\n    - " + "\n    - ".join(probs))
            else:
                print(f"✓ {f}")
        sys.exit(1 if mal else 0)


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    _cli()
