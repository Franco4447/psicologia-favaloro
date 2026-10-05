"""Arma, valida y lee mazos CSV de flashcards para Anki (skill /flashcards).

El CSV usa los encabezados de importación de Anki (2.1.55+), así Anki reconoce solo el
separador, el mazo, el tipo de nota y las etiquetas:

    #separator:Semicolon
    #html:true
    #guid column:1        <- ID estable: al reimportar, Anki ACTUALIZA la tarjeta en vez de duplicarla
    #notetype column:2    <- "Básico" (pregunta/respuesta) o "Respuesta anidada" (cloze)
    #deck column:3        <- Materia::Unidad
    #tags column:6
    clave;tipo;mazo;frente;dorso;etiquetas

Uso:
    # 1) La skill escribe las tarjetas en un JSON temporal y lo convierte:
    python Scripts/estudio/anki_csv.py construir tarjetas.json --materia Psicoanálisis --unidad C08 \\
        --fuente C08_PulsionDeMuerte_Guia.md --salida "2do Año/Psicoanálisis/4_Flashcards/C08_PulsionDeMuerte_Flashcards.csv"
    # 2) Validar un CSV existente:
    python Scripts/estudio/anki_csv.py validar <archivo.csv>
    # 3) Leer un CSV existente como JSON de entrada (para reusar las claves al regenerar):
    python Scripts/estudio/anki_csv.py leer <archivo.csv>

Formato del JSON de entrada (lista):
    [{"clave": "pulsion-de-muerte-def", "tipo": "basica" | "cloze",
      "frente": "...", "dorso": "...", "tags": ["definicion"]}]
    - basica: frente = pregunta, dorso = respuesta.
    - cloze:  frente = texto con {{c1::...}}, dorso = contexto extra (puede ir vacío).

Los nombres de los tipos de nota dependen del idioma con que se creó la colección de Anki:
español = "Básico" / "Respuesta anidada"; inglés = "Basic" / "Cloze". Se cambian con
--tipo-basico / --tipo-cloze o con las variables ANKI_TIPO_BASICO / ANKI_TIPO_CLOZE.
"""
import argparse
import csv
import io
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nombres import pascal  # noqa: E402

CABECERA = [
    "#separator:Semicolon",
    "#html:true",
    "#guid column:1",
    "#notetype column:2",
    "#deck column:3",
    "#tags column:6",
]
COLUMNAS = ["clave", "tipo", "mazo", "frente", "dorso", "etiquetas"]
RE_CLOZE = re.compile(r"\{\{c\d+::.+?\}\}")
RE_CLAVE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_FRENTE, MAX_DORSO = 250, 600


def tipos_de_nota(args=None):
    basico = getattr(args, "tipo_basico", None) or os.environ.get("ANKI_TIPO_BASICO") or "Básico"
    cloze = getattr(args, "tipo_cloze", None) or os.environ.get("ANKI_TIPO_CLOZE") or "Respuesta anidada"
    return basico, cloze


def slug(texto):
    """'Psicoanálisis' -> 'psicoanalisis'; 'Procesos Básicos II' -> 'procesos-basicos-ii'."""
    t = "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def construir(tarjetas, materia, unidad, fuente, tipo_basico, tipo_cloze):
    """Devuelve el texto del CSV. Lanza ValueError si alguna tarjeta es inválida."""
    pref = f"{slug(materia)}-{unidad.lower().replace('_', '-')}"
    mazo = f"{materia}::{unidad}"
    tag_materia = pascal(materia)
    tag_fuente = "fuente::" + Path(fuente).stem if fuente else None
    buf = io.StringIO()
    buf.write("\n".join(CABECERA) + "\n")
    w = csv.writer(buf, delimiter=";", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    errores, vistas = [], set()
    for i, t in enumerate(tarjetas, 1):
        clave = (t.get("clave") or "").strip()
        if clave.startswith(pref + "-"):  # clave copiada de `leer` con el prefijo incluido
            clave = clave[len(pref) + 1:]
        tipo = t.get("tipo")
        # El CSV declara #html:true: los saltos de línea se escriben como <br>
        frente = (t.get("frente") or "").strip().replace("\r\n", "\n").replace("\n", "<br>")
        dorso = (t.get("dorso") or "").strip().replace("\r\n", "\n").replace("\n", "<br>")
        if not RE_CLAVE.match(clave):
            errores.append(f"tarjeta {i}: clave inválida {clave!r} (usar minúsculas y guiones, ej. 'pulsion-de-muerte-def')")
        if clave in vistas:
            errores.append(f"tarjeta {i}: clave repetida {clave!r}")
        vistas.add(clave)
        if tipo not in ("basica", "cloze"):
            errores.append(f"tarjeta {i}: tipo debe ser 'basica' o 'cloze', no {tipo!r}")
            continue
        if not frente:
            errores.append(f"tarjeta {i} ({clave}): frente vacío")
        if tipo == "basica" and not dorso:
            errores.append(f"tarjeta {i} ({clave}): una tarjeta básica necesita respuesta")
        if tipo == "cloze" and not RE_CLOZE.search(frente):
            errores.append(f"tarjeta {i} ({clave}): cloze sin hueco {{{{c1::...}}}}")
        if tipo == "basica" and RE_CLOZE.search(frente):
            errores.append(f"tarjeta {i} ({clave}): tiene {{{{c1::...}}}} pero es básica")
        tags = [tag_materia, f"{tag_materia}::{unidad}"] + ([tag_fuente] if tag_fuente else [])
        tags += [re.sub(r"\s+", "_", x.strip()) for x in t.get("tags", []) if x.strip()]
        w.writerow([f"{pref}-{clave}", tipo_basico if tipo == "basica" else tipo_cloze,
                    mazo, frente, dorso, " ".join(dict.fromkeys(tags))])
    if errores:
        raise ValueError("\n".join(errores))
    return buf.getvalue()


def leer(path):
    """Devuelve (cabecera: list[str], filas: list[dict])."""
    texto = Path(path).read_bytes()
    if texto.startswith(b"\xef\xbb\xbf"):
        raise ValueError("el archivo tiene BOM UTF-8: Anki no reconoce el primer encabezado")
    lineas = texto.decode("utf-8").splitlines(keepends=True)
    cab = [l.rstrip("\n") for l in lineas if l.startswith("#")]
    cuerpo = "".join(l for l in lineas if not l.startswith("#"))
    filas = [dict(zip(COLUMNAS, r)) for r in csv.reader(io.StringIO(cuerpo), delimiter=";") if r]
    return cab, filas


def validar(path, tipo_basico, tipo_cloze):
    """Devuelve (errores, avisos)."""
    errores, avisos = [], []
    try:
        cab, filas = leer(path)
    except (ValueError, UnicodeDecodeError) as e:
        return [str(e)], []
    if cab != CABECERA:
        errores.append("encabezados de Anki distintos a los esperados:\n      " + "\n      ".join(CABECERA))
    if not filas:
        errores.append("el mazo no tiene tarjetas")
    claves, frentes = {}, {}
    for n, f in enumerate(filas, 1):
        if len(f) != len(COLUMNAS) or None in f.values():
            errores.append(f"fila {n}: tiene {len(f)} columnas, se esperaban {len(COLUMNAS)}")
            continue
        if f["clave"] in claves:
            errores.append(f"fila {n}: clave repetida con la fila {claves[f['clave']]} ({f['clave']})")
        claves[f["clave"]] = n
        key = re.sub(r"\W+", " ", f["frente"].lower()).strip()
        if key in frentes:
            avisos.append(f"fila {n}: mismo frente que la fila {frentes[key]} (posible duplicado)")
        frentes[key] = n
        if f["tipo"] not in (tipo_basico, tipo_cloze):
            errores.append(f"fila {n}: tipo de nota {f['tipo']!r} (se esperaba {tipo_basico!r} o {tipo_cloze!r})")
        if f["tipo"] == tipo_cloze and not RE_CLOZE.search(f["frente"]):
            errores.append(f"fila {n}: cloze sin hueco {{{{c1::...}}}}")
        if f["tipo"] == tipo_basico and not f["dorso"].strip():
            errores.append(f"fila {n}: tarjeta básica sin respuesta")
        if not f["frente"].strip():
            errores.append(f"fila {n}: frente vacío")
        if len(f["frente"]) > MAX_FRENTE:
            avisos.append(f"fila {n}: frente largo ({len(f['frente'])} caracteres): ¿se puede dividir?")
        if len(f["dorso"]) > MAX_DORSO:
            avisos.append(f"fila {n}: respuesta larga ({len(f['dorso'])} caracteres): ¿se puede dividir?")
        if "  " in f["etiquetas"] or f["etiquetas"] != f["etiquetas"].strip():
            avisos.append(f"fila {n}: etiquetas con espacios de más")
    return errores, avisos


def _cli():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tipo-basico")
    ap.add_argument("--tipo-cloze")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("construir")
    c.add_argument("json")
    c.add_argument("--materia", required=True)
    c.add_argument("--unidad", required=True)
    c.add_argument("--fuente", default="")
    c.add_argument("--salida", required=True)
    v = sub.add_parser("validar")
    v.add_argument("csv", nargs="+")
    r = sub.add_parser("leer")
    r.add_argument("csv")
    a = ap.parse_args()
    basico, cloze = tipos_de_nota(a)

    if a.cmd == "construir":
        tarjetas = json.loads(Path(a.json).read_text(encoding="utf-8-sig"))
        try:
            texto = construir(tarjetas, a.materia, a.unidad, a.fuente, basico, cloze)
        except ValueError as e:
            sys.exit(f"No se generó el CSV:\n{e}")
        Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
        Path(a.salida).write_text(texto, encoding="utf-8", newline="")
        n_cloze = sum(1 for t in tarjetas if t["tipo"] == "cloze")
        print(f"✓ {a.salida}: {len(tarjetas)} tarjetas ({len(tarjetas) - n_cloze} básicas, {n_cloze} cloze)")
    elif a.cmd == "validar":
        mal = 0
        for f in a.csv:
            errores, avisos = validar(f, basico, cloze)
            print(("✗ " if errores else "✓ ") + f)
            for e in errores:
                print(f"    ERROR: {e}")
            for x in avisos:
                print(f"    aviso: {x}")
            mal += bool(errores)
        sys.exit(1 if mal else 0)
    else:
        # Devuelve las tarjetas en el mismo formato que espera `construir`, para reusar las claves
        _, filas = leer(a.csv)
        tarjetas = []
        for f in filas:
            materia, _, unidad = f["mazo"].partition("::")
            pref = f"{slug(materia)}-{unidad.lower().replace('_', '-')}-"
            fijas = {pascal(materia), f"{pascal(materia)}::{unidad}"}
            tarjetas.append({
                "clave": f["clave"][len(pref):] if f["clave"].startswith(pref) else f["clave"],
                "tipo": "cloze" if RE_CLOZE.search(f["frente"]) else "basica",
                "frente": f["frente"], "dorso": f["dorso"],
                "tags": [t for t in f["etiquetas"].split() if t not in fijas and not t.startswith("fuente::")],
            })
        print(json.dumps(tarjetas, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    _cli()
