"""Protocolos de creación de apuntes y perfil de cada materia (ver AGENTS.md → «Protocolos de apuntes»).

Antes de crear cualquier material de estudio, la skill propone al usuario los protocolos con sus
pros y contras y recomienda uno para el caso. Este módulo es la única fuente de verdad del catálogo:
para agregar o ajustar un protocolo se edita PROTOCOLOS (y su descripción detallada en
.claude/skills/guia-estudio/references/protocolos.md); nombres.py y estado.py lo leen de acá.

Cada materia tiene un perfil en [Año]/[Materia]/Perfil_Materia.md (cabecera YAML + notas libres):
formato de cada evaluación, protocolo habitual y fuentes de la cátedra. Si no existe, se crea con la
plantilla de .claude/skills/guia-estudio/references/plantilla_perfil_materia.md, preguntando al
usuario lo que no se sepa.

Uso:
    python Scripts/estudio/protocolos.py listar
    python Scripts/estudio/protocolos.py perfil --materia "Psicología Evolutiva" [--anio "2do Año"]
    python Scripts/estudio/protocolos.py proponer --materia "Psicología Evolutiva" --unidad C21 \\
        [--evaluacion "4.º parcial"] [--final] [--pedido "texto del pedido"]
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
PERFIL = "Perfil_Materia.md"

# Formatos de evaluación que puede declarar un perfil, y el protocolo que les corresponde.
FORMATOS = {
    "respuesta_corta": ("Opción múltiple, V/F o abiertas de pocos renglones", "cursada"),
    "desarrollo":      ("Preguntas de desarrollo con extensión mínima (p. ej., 10 renglones)", "desarrollo"),
    "oral":            ("Lección oral, exposición o coloquio", "oral"),
    "problemas":       ("Ejercicios, cálculos o procedimientos a resolver", "procedimental"),
    "trabajo_escrito": ("Trabajo práctico, informe o monografía con bibliografía", "lectura"),
    "final_integral":  ("Final que abarca toda la materia", "extendido"),
    "sin_definir":     ("Todavía no se sabe", None),
}

# Catálogo. El orden es el de presentación. `sufijo` es el del nombre de archivo
# ([Unidad]_[Tema]_<sufijo>.md); el extendido conserva el sufijo histórico «Guia».
PROTOCOLOS = {
    "cursada": {
        "nombre": "A. Cursada",
        "sufijo": "Cursada_Guia",
        "palabras": "2.000–3.500 por clase",
        "para": "Exámenes de respuesta corta (opción múltiple, V/F, abiertas breves)",
        "pros": ["Se estudia rápido: solo lo que pide el programa y lo que se dio en clase",
                 "Prioriza lo que la cátedra remarca (diapositivas, apuntes)",
                 "Trae práctica en el formato real del examen"],
        "contras": ["No reemplaza al libro: un detalle fuera de clase puede faltar",
                    "Si no hay diapositivas ni apuntes, el recorte depende solo del programa (provisorio)",
                    "Respuestas modelo cortas: no alcanza para un desarrollo largo"],
        "plantilla_completa": False,
        "exportar": ["--sin-saltos"],
    },
    "desarrollo": {
        "nombre": "B. Desarrollo",
        "sufijo": "Desarrollo_Guia",
        "palabras": "5.000–8.000 por clase o bloque",
        "para": "Exámenes de desarrollo con extensión mínima; parciales por baterías de preguntas",
        "pros": ["Una respuesta modelo completa por pregunta, con la extensión pedida",
                 "Incluye las citas textuales y la articulación entre autores que se evalúan",
                 "Sigue sirviendo para el final"],
        "contras": ["Lleva más tiempo de lectura que la versión de cursada",
                    "Menos detalle de ejemplos y cifras que el extendido",
                    "Necesita conocer las preguntas o ejes de la cátedra para ordenarse bien"],
        "plantilla_completa": True,
        "exportar": ["--indice"],
    },
    "extendido": {
        "nombre": "C. Extendido",
        "sufijo": "Guia",
        "palabras": "Sin tope (≈ el largo del texto fuente)",
        "para": "Final integral, textos que la cátedra pide leer completos y no se dieron en clase, o a pedido",
        "pros": ["Reemplaza el texto: todos los ejemplos, casos, cifras y matices",
                 "Sirve para cualquier pregunta posible y para el final",
                 "Control de cobertura contra la fuente"],
        "contras": ["Muy largo: difícil de repasar antes de un parcial",
                    "Mezcla lo central con lo accesorio si no se marca el origen",
                    "Más tiempo de generación y de lectura"],
        "plantilla_completa": True,
        "exportar": ["--indice"],
    },
    "oral": {
        "nombre": "D. Oral",
        "sufijo": "Oral_Guia",
        "palabras": "1.500–3.000 por tema",
        "para": "Lecciones orales, exposiciones y coloquios",
        "pros": ["Guion por bloques de tiempo, listo para decir en voz alta",
                 "Preguntas probables del tribunal con respuesta",
                 "Apoyo visual (esquema o diapositivas) incluido"],
        "contras": ["No sirve como apunte de lectura completo",
                    "Si el formato real no es oral, hay que rehacerlo",
                    "Depende de saber el tiempo y las pautas de la exposición"],
        "plantilla_completa": False,
        "exportar": ["--sin-saltos"],
    },
    "procedimental": {
        "nombre": "E. Procedimental",
        "sufijo": "Procedimental_Guia",
        "palabras": "Según la cantidad de procedimientos",
        "para": "Materias de problemas: estadística, metodología, cálculo",
        "pros": ["Árbol de decisión («qué prueba o método uso»)",
                 "Pasos y ejemplos resueltos de punta a punta",
                 "Errores típicos de cálculo e interpretación"],
        "contras": ["Poca teoría en prosa: no sirve para preguntas conceptuales largas",
                    "Necesita ejercicios de la cátedra para calibrar",
                    "Los ejemplos hay que verificarlos uno por uno"],
        "plantilla_completa": False,
        "exportar": [],
    },
    "lectura": {
        "nombre": "F. Lectura de investigación",
        "sufijo": "Lectura_Guia",
        "palabras": "500–1.000 por artículo",
        "para": "Artículos para un TP, informe o monografía",
        "pros": ["Ficha por artículo: pregunta, hipótesis, método, resultados, limitaciones",
                 "Dice cómo citarlo y para qué sirve en el trabajo",
                 "Permite comparar muchos artículos rápido"],
        "contras": ["No sirve para rendir un examen sobre el artículo",
                    "Pierde el detalle de la discusión del autor",
                    "Hay que leer el original para citar textual"],
        "plantilla_completa": False,
        "exportar": ["--sin-saltos"],
    },
}

# Capas derivadas: se proponen igual, pero lo que se elige es la guía base y el alcance.
CAPAS = ["ficha de repaso (_Repaso_Guia)", "cuadro integrador (Transversal_)", "flashcards", "simulacro"]

RE_MATERIAL_CLASE = re.compile(r"(diapositiva|presentaci[oó]n|apunte|catedra|cátedra|ppt)", re.I)


def protocolo_de_archivo(path):
    """Clave del protocolo de una guía según su nombre (o su cabecera, si la tiene)."""
    stem = Path(path).stem
    for clave, p in PROTOCOLOS.items():
        if p["sufijo"] != "Guia" and stem.endswith("_" + p["sufijo"]):
            return clave
    if re.search(r"_(Resumen|Sintesis\w*|Repaso)_Guia$", stem):
        return None  # ficha o resumen: capa derivada, no guía principal
    if stem.endswith("_Guia") and Path(path).suffix == ".md" and Path(path).exists():
        meta, _ = frontmatter.leer(path)
        if meta and meta.get("protocolo") in PROTOCOLOS:
            return meta["protocolo"]
    return "extendido" if stem.endswith("_Guia") else None


def dir_materia(materia, anio=None):
    anios = [anio] if anio else [p.name for p in sorted(RAIZ.iterdir()) if p.is_dir() and "Año" in p.name]
    for a in anios:
        d = RAIZ / a / materia
        if d.is_dir():
            return d
    return None


def leer_perfil(d):
    p = d / PERFIL
    if not p.exists():
        return None
    meta, cuerpo = frontmatter.leer(p)
    return {"meta": meta or {}, "notas": cuerpo.strip(), "ruta": p}


def material_de_clase(d, unidad):
    """Archivos de la cátedra o del usuario (diapositivas, apuntes) que parecen de esa unidad/clase."""
    if not unidad:
        return []
    num = re.findall(r"\d+", unidad)
    pats = [re.escape(unidad)] + [rf"(clase|unidad)\s*0?{n}\b" for n in num]
    hallados = []
    for etapa in ("1_Bibliografia_Original", "2_Textos_Extraidos"):
        base = d / etapa
        if not base.is_dir():
            continue
        for f in base.rglob("*"):
            ruta = str(f.relative_to(d))
            if f.is_file() and RE_MATERIAL_CLASE.search(ruta) and any(re.search(p, ruta, re.I) for p in pats):
                hallados.append(ruta)
    return sorted(set(hallados))


def evaluacion_pertinente(meta, nombre=None):
    evs = meta.get("evaluaciones") or []
    if nombre:
        for e in evs:
            if nombre.lower() in str(e.get("nombre", "")).lower():
                return e
    proximas = [e for e in evs if str(e.get("estado", "")).lower() not in ("rendida", "aprobada")]
    return (proximas or evs or [None])[0]


def recomendar(perfil, evaluacion=None, final=False, pedido=""):
    """Devuelve (clave_recomendada, motivos: list[str], avisos: list[str])."""
    motivos, avisos = [], []
    pedido = (pedido or "").lower()
    for clave, p in PROTOCOLOS.items():
        nombre = p["nombre"].split(". ", 1)[1].lower()
        if re.search(rf"(protocolo|versi[oó]n|modo)\s+(de\s+)?({re.escape(clave)}|{re.escape(nombre)})", pedido):
            motivos.append(f"el pedido pide el protocolo «{p['nombre']}»")
            return clave, motivos, avisos
    if final or "final" in pedido:
        motivos.append("es para un final integral")
        return "extendido", motivos, avisos
    if perfil:
        ev = evaluacion_pertinente(perfil["meta"], evaluacion)
        if ev and ev.get("formato") in FORMATOS and FORMATOS[ev["formato"]][1]:
            motivos.append(f"la evaluación «{ev.get('nombre')}» es de formato «{ev['formato']}»"
                           + (f" ({ev['detalle']})" if ev.get("detalle") else ""))
            return FORMATOS[ev["formato"]][1], motivos, avisos
        hab = perfil["meta"].get("protocolo_habitual")
        if hab in PROTOCOLOS:
            motivos.append(f"es el protocolo habitual de la materia según su perfil")
            return hab, motivos, avisos
        avisos.append("el perfil no dice el formato de la evaluación: preguntalo")
    else:
        avisos.append(f"la materia no tiene {PERFIL}: crealo con el usuario (formato de sus exámenes)")
    motivos.append("sin datos del examen, se recomienda empezar acotado (se puede ampliar después)")
    return "cursada", motivos, avisos


def tabla_protocolos(recomendado=None):
    filas = ["| Protocolo | Para qué | Extensión | A favor | En contra |", "|---|---|---|---|---|"]
    for clave, p in PROTOCOLOS.items():
        marca = " **(recomendado)**" if clave == recomendado else ""
        filas.append(f"| {p['nombre']}{marca} | {p['para']} | {p['palabras']} | "
                     f"{'<br>'.join('+ ' + x for x in p['pros'])} | {'<br>'.join('− ' + x for x in p['contras'])} |")
    return "\n".join(filas)


def _cli():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("listar", help="catálogo de protocolos con pros y contras")
    pp = sub.add_parser("perfil", help="muestra el perfil de una materia")
    pr = sub.add_parser("proponer", help="propuesta de protocolos con recomendación para un pedido")
    for s in (pp, pr):
        s.add_argument("--materia", required=True)
        s.add_argument("--anio")
    pr.add_argument("--unidad", help="código de unidad o clase (U05, C17, C17_23…)")
    pr.add_argument("--evaluacion", help="nombre de la evaluación del perfil (p. ej., «4.º parcial»)")
    pr.add_argument("--final", action="store_true", help="el material es para un final integral")
    pr.add_argument("--pedido", default="", help="texto del pedido del usuario")
    a = ap.parse_args()

    if a.cmd == "listar":
        print(tabla_protocolos())
        print("\nFormatos de evaluación del perfil: " + ", ".join(f"{k} → {v[1] or '—'}" for k, v in FORMATOS.items()))
        return
    d = dir_materia(a.materia, a.anio)
    if not d:
        sys.exit(f"No encuentro la materia «{a.materia}».")
    perfil = leer_perfil(d)
    if a.cmd == "perfil":
        if not perfil:
            sys.exit(f"{d.relative_to(RAIZ)} no tiene {PERFIL}.")
        print(perfil["ruta"].read_text(encoding="utf-8"))
        return
    clave, motivos, avisos = recomendar(perfil, a.evaluacion, a.final, a.pedido)
    clase = material_de_clase(d, a.unidad)
    if a.unidad and not clase:
        avisos.append(f"no encontré diapositivas ni apuntes de {a.unidad}: el recorte se haría solo con el programa")
    print(f"# Propuesta de protocolo — {a.materia}" + (f" · {a.unidad}" if a.unidad else ""))
    print()
    print(tabla_protocolos(clave))
    print()
    print(f"**Recomendado: {PROTOCOLOS[clave]['nombre']}** — porque " + "; ".join(motivos) + ".")
    if clase:
        print("\nMaterial de clase encontrado: " + "; ".join(clase[:8]) + (" …" if len(clase) > 8 else ""))
    for x in avisos:
        print(f"\n⚠ {x}")


if __name__ == "__main__":
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    _cli()
