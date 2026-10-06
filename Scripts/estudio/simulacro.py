"""Valida simulacros y registra resultados (skill /simulacro).

Formato del simulacro (5_Evaluaciones/[Unidad]_[Tema]_Simulacro.md), con cabecera YAML:

    ## A) Opción múltiple
    ### A1. Enunciado...
    - a) ...
    - b) ...            (4 o 5 opciones)
    ## B) Verdadero / Falso (justificá en una línea)
    ### B1. Afirmación...
    ## C) Distinciones finas
    ### C1. ¿Qué diferencia X de Y?
    ## D) Desarrollo
    ### D1. Consigna...
    ## E) Casos y aplicación        (opcional)
    ### E1. Situación + consignas...
    ## Clave de respuestas
    ### A1 — b
    Justificación... *(Fuente: C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md, §2)*
    ### B1 — Falso
    ...
    ### D1
    Respuesta modelo + rúbrica... *(Fuente: ...)*

Uso:
    python Scripts/estudio/simulacro.py validar <simulacro.md>
    python Scripts/estudio/simulacro.py resultados <respuestas.json>
        -> escribe 5_Evaluaciones/[Unidad]_[Tema]_Resultados.md (cabecera con temas_flojos)

Formato de respuestas.json (lo arma la skill en modo interactivo):
    {"simulacro": "<ruta al simulacro.md>", "fecha": "2026-10-05",
     "respuestas": [{"id": "A1", "puntaje": 1, "max": 1, "tema": "Pseudo-objeción",
                     "fuente": "C08_PulsionDeMuerteYCompulsionDeRepeticion_Guia.md §2", "comentario": "..."}]}
    Una pregunta cuenta como floja si puntaje / max < 0.6.
"""
import collections
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter  # noqa: E402

SECCIONES = {"A": "Opción múltiple", "B": "Verdadero / Falso", "C": "Distinciones finas",
             "D": "Desarrollo", "E": "Casos y aplicación"}
RE_PREG = re.compile(r"^###\s+([A-E]\d+)\.\s+\S")
RE_OPC = re.compile(r"^\s*-\s+([a-e])\)\s+\S")
RE_CLAVE = re.compile(r"^###\s+([A-E]\d+)(?:\s+[—-]\s+(.+?))?\s*$")
UMBRAL_FLOJO = 0.6


def _partir(cuerpo):
    m = re.search(r"^##\s+Clave de respuestas\s*$", cuerpo, re.M)
    if not m:
        return cuerpo, None
    return cuerpo[: m.start()], cuerpo[m.end():]


def analizar(path):
    """Devuelve (meta, preguntas: {id: [opciones]}, clave: {id: (respuesta, texto)})."""
    meta, cuerpo = frontmatter.leer(path)
    enunciados, texto_clave = _partir(cuerpo)
    preguntas, actual = collections.OrderedDict(), None
    for linea in enunciados.splitlines():
        m = RE_PREG.match(linea)
        if m:
            actual = m.group(1)
            preguntas[actual] = []
            continue
        if linea.startswith("#"):
            actual = None
        mo = RE_OPC.match(linea)
        if actual and mo:
            preguntas[actual].append(mo.group(1))
    clave = collections.OrderedDict()
    if texto_clave:
        bloques = re.split(r"(?m)^(?=###\s)", texto_clave)
        for b in bloques:
            m = RE_CLAVE.match(b.splitlines()[0]) if b.strip() else None
            if m:
                clave[m.group(1)] = ((m.group(2) or "").strip(), b)
    return meta, preguntas, clave


def validar(path):
    errores, avisos = [], []
    meta, preguntas, clave = analizar(path)
    if not meta or meta.get("tipo") != "simulacro":
        errores.append("falta la cabecera YAML con tipo: simulacro (usar frontmatter.escribir)")
    if not preguntas:
        errores.append("no se encontraron preguntas (formato '### A1. Enunciado')")
    if not clave:
        errores.append("falta la sección '## Clave de respuestas' o está vacía")
    for pid in preguntas:
        if pid not in clave:
            errores.append(f"{pid}: no tiene respuesta en la clave")
    for pid in clave:
        if pid not in preguntas:
            errores.append(f"{pid}: está en la clave pero no en el examen")
    letras = collections.Counter()
    for pid, opciones in preguntas.items():
        sec = pid[0]
        resp, texto = clave.get(pid, ("", ""))
        if sec == "A":
            if len(opciones) not in (4, 5) or opciones != list("abcde"[: len(opciones)]):
                errores.append(f"{pid}: opción múltiple con opciones {opciones} (se esperan a–d o a–e)")
            if resp not in opciones:
                errores.append(f"{pid}: la respuesta de la clave ({resp!r}) no es una de sus opciones")
            letras[resp] += 1
        elif opciones:
            avisos.append(f"{pid}: tiene opciones pero no está en la sección A")
        if sec == "B" and pid in clave and resp not in ("Verdadero", "Falso"):
            errores.append(f"{pid}: la clave debe decir 'Verdadero' o 'Falso', no {resp!r}")
        if pid in clave and "Fuente:" not in texto:
            errores.append(f"{pid}: la respuesta no cita la fuente ('*(Fuente: ...)*')")
        if sec == "D" and pid in clave and not re.search(r"r[úu]brica|para un 10", texto, re.I):
            avisos.append(f"{pid}: pregunta de desarrollo sin rúbrica")
    total_a = sum(letras.values())
    if total_a >= 4:
        letra, n = letras.most_common(1)[0]
        if n / total_a > 0.5:
            avisos.append(f"la opción correcta es '{letra}' en {n} de {total_a} preguntas: variar la posición")
    resumen = collections.Counter(pid[0] for pid in preguntas)
    return errores, avisos, resumen


def resultados(path_json):
    datos = json.loads(Path(path_json).read_text(encoding="utf-8-sig"))
    sim = Path(datos["simulacro"])
    meta_sim, preguntas, _ = analizar(sim)
    resp = datos["respuestas"]
    faltan = [pid for pid in preguntas if pid not in {r["id"] for r in resp}]
    puntaje = sum(r["puntaje"] for r in resp)
    maximo = sum(r["max"] for r in resp)
    flojos = collections.OrderedDict()
    for r in resp:
        if r["max"] and r["puntaje"] / r["max"] < UMBRAL_FLOJO:
            t = flojos.setdefault(r["tema"], {"tema": r["tema"], "fuente": r.get("fuente", ""), "preguntas": []})
            t["preguntas"].append(r["id"])
    por_sec = collections.OrderedDict()
    for r in resp:
        s = por_sec.setdefault(r["id"][0], [0, 0])
        s[0] += r["puntaje"]
        s[1] += r["max"]

    salida = sim.with_name(sim.name.replace("_Simulacro.md", "_Resultados.md"))
    fecha = datos.get("fecha", datetime.date.today().isoformat())
    pct = round(100 * puntaje / maximo) if maximo else 0
    meta = {
        "materia": meta_sim.get("materia"), "unidad": meta_sim.get("unidad"), "tipo": "resultados",
        "simulacro": sim.name, "fecha": fecha,
        "puntaje": puntaje, "maximo": maximo, "porcentaje": pct,
        "temas_flojos": list(flojos.values()), "skill": "simulacro",
    }
    intento = [f"## Intento del {fecha} — {puntaje:g} / {maximo:g} ({pct} %)", ""]
    if faltan:
        intento += [f"Preguntas no evaluadas en este intento: {', '.join(faltan)}.", ""]
    intento += ["| Sección | Puntaje |", "|---|---|"]
    intento += [f"| {SECCIONES[s]} | {p:g} / {m:g} |" for s, (p, m) in sorted(por_sec.items())]
    intento += ["", "### Detalle", "", "| Pregunta | Puntaje | Tema | Comentario |", "|---|---|---|---|"]
    intento += [f"| {r['id']} | {r['puntaje']:g} / {r['max']:g} | {r['tema']} | {r.get('comentario', '').replace('|', '/')} |"
                for r in sorted(resp, key=lambda r: (r["id"][0], int(r["id"][1:])))]
    intento += ["", "### Temas para repasar", ""]
    if flojos:
        intento += [f"- **{t['tema']}** ({', '.join(t['preguntas'])}) → repasar en {t['fuente'] or 'la guía'}" for t in flojos.values()]
    else:
        intento.append("Ninguno: todas las respuestas superaron el 60 %.")

    # Varios intentos del mismo simulacro: se conserva el historial (el más reciente primero)
    anteriores, historial = "", []
    if salida.exists():
        meta_ant, cuerpo_ant = frontmatter.leer(salida)
        historial = list((meta_ant or {}).get("intentos", []))
        if meta_ant:
            historial.append({k: meta_ant[k] for k in ("fecha", "puntaje", "maximo", "porcentaje")})
        i = cuerpo_ant.find("## Intento del ")
        anteriores = cuerpo_ant[i:].strip() if i >= 0 else ""
    if historial:
        meta["intentos"] = historial

    lineas = [f"# Resultados — {sim.stem.replace('_Simulacro', '')}", ""]
    if historial:
        lineas += ["| Fecha | Puntaje |", "|---|---|"]
        lineas += [f"| {h['fecha']} | {h['puntaje']:g} / {h['maximo']:g} ({h['porcentaje']} %) |" for h in historial]
        lineas += [f"| **{fecha}** | **{puntaje:g} / {maximo:g} ({pct} %)** |", ""]
    if flojos:
        lineas += ["Para practicar los temas flojos: pedí *flashcards de los temas flojos* con este archivo "
                   "(skill `/flashcards`).", ""]
    lineas += intento + ([ "", anteriores] if anteriores else [])
    frontmatter.escribir(salida, meta, "\n".join(lineas))
    return salida, puntaje, maximo, list(flojos)


def _cli():
    if len(sys.argv) < 3 or sys.argv[1] not in ("validar", "resultados"):
        sys.exit(__doc__)
    if sys.argv[1] == "validar":
        mal = 0
        for f in sys.argv[2:]:
            errores, avisos, resumen = validar(f)
            partes = ", ".join(f"{n} {SECCIONES[s].lower()}" for s, n in sorted(resumen.items()))
            print(("✗ " if errores else "✓ ") + f + (f"  ({partes})" if partes else ""))
            for e in errores:
                print(f"    ERROR: {e}")
            for a in avisos:
                print(f"    aviso: {a}")
            mal += bool(errores)
        sys.exit(1 if mal else 0)
    salida, p, m, flojos = resultados(sys.argv[2])
    print(f"✓ {salida}: {p:g}/{m:g}" + (f"; temas flojos: {', '.join(flojos)}" if flojos else "; sin temas flojos"))


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    _cli()
