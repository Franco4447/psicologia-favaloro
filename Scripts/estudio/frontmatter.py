"""Cabecera YAML de los .md generados por las skills de estudio.

Cada guía, simulacro o resultado generado empieza con:

    ---
    materia: Psicoanálisis
    unidad: U05
    tipo: guia
    fuentes:
      - archivo: 2_Textos_Extraidos/U05_T27_Belucci_LasIntervencionesDelAnalista_Crudo.md
        paginas: 1-14
    generado: 2026-10-05
    skill: guia-estudio
    hash_generado: 3f9a1c0b7e2d
    ---

`hash_generado` es el hash del cuerpo al momento de generarlo. Si después alguien edita
el archivo a mano, el hash deja de coincidir: así las skills saben que no deben
sobrescribirlo sin preguntar.

Uso por línea de comandos:
    python Scripts/estudio/frontmatter.py estado <archivo.md>
        -> "nuevo" (no existe), "sin-cambios" (se puede regenerar), "editado" o "sin-cabecera"
    python Scripts/estudio/frontmatter.py ver <archivo.md>
"""
import datetime
import hashlib
import sys
from pathlib import Path

import yaml

DELIM = "---"


def _hash(cuerpo):
    # Normaliza fin de línea para que Windows (CRLF) y Linux (LF) den el mismo hash
    return hashlib.sha256(cuerpo.replace("\r\n", "\n").strip().encode("utf-8")).hexdigest()[:12]


def leer(path):
    """Devuelve (meta: dict | None, cuerpo: str)."""
    texto = Path(path).read_text(encoding="utf-8-sig")
    lineas = texto.splitlines(keepends=True)
    if lineas and lineas[0].strip() == DELIM:
        for i in range(1, len(lineas)):
            if lineas[i].strip() == DELIM:
                meta = yaml.safe_load("".join(lineas[1:i])) or {}
                return meta, "".join(lineas[i + 1:]).lstrip("\n")
    return None, texto


def escribir(path, meta, cuerpo):
    """Escribe el .md con cabecera; completa `generado` y `hash_generado`."""
    meta = dict(meta)
    meta.setdefault("generado", datetime.date.today().isoformat())
    meta["hash_generado"] = _hash(cuerpo)
    cabecera = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(f"{DELIM}\n{cabecera}\n{DELIM}\n\n{cuerpo.strip()}\n", encoding="utf-8")


def estado(path):
    """'nuevo' | 'sin-cabecera' | 'sin-cambios' | 'editado'."""
    p = Path(path)
    if not p.exists():
        return "nuevo"
    meta, cuerpo = leer(p)
    if not meta or "hash_generado" not in meta:
        return "sin-cabecera"
    return "sin-cambios" if meta["hash_generado"] == _hash(cuerpo) else "editado"


EXPLICACION = {
    "nuevo": "no existe: se puede crear",
    "sin-cambios": "no fue editado a mano desde que se generó: se puede regenerar",
    "editado": "fue editado a mano: mostrar diferencias y preguntar antes de sobrescribir",
    "sin-cabecera": "no tiene cabecera (hecho a mano o con otra herramienta): preguntar antes de sobrescribir",
}

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("estado", "ver"):
        sys.exit(__doc__)
    cmd, archivo = sys.argv[1:]
    if cmd == "estado":
        e = estado(archivo)
        print(f"{e}: {EXPLICACION[e]}")
        sys.exit(0 if e in ("nuevo", "sin-cambios") else 2)
    meta, _ = leer(archivo)
    print(yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) if meta else "(sin cabecera)")
