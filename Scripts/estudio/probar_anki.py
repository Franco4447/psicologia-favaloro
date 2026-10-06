"""Importa mazos CSV en una colección de Anki temporal para comprobar que funcionan.

Simula lo que pasa en tu Anki: importa cada CSV dos veces y verifica que
  1) se crean todas las tarjetas, en el mazo y con el tipo de nota correctos, y
  2) la segunda importación ACTUALIZA las mismas notas en vez de duplicarlas.

Requiere el paquete `anki` (pip install anki). Es opcional: si no está, la skill
/flashcards se queda con la validación de anki_csv.py.

Uso:
    python Scripts/estudio/probar_anki.py <archivo.csv> [...] [--idioma es|en]
"""
import shutil
import sys
import tempfile
from pathlib import Path


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    idioma = "en" if "--idioma" in sys.argv and sys.argv[sys.argv.index("--idioma") + 1] == "en" else "es"
    args = [a for a in args if a not in ("es", "en")]
    if not args:
        sys.exit(__doc__)
    try:
        from anki.collection import Collection, ImportCsvRequest
        from anki.lang import set_lang
    except ImportError:
        sys.exit("Falta el paquete 'anki' (pip install anki). La prueba de importación es opcional.")

    set_lang("es_ES" if idioma == "es" else "en_US")
    d = tempfile.mkdtemp()
    col = Collection(str(Path(d, "prueba.anki2")))
    mal = 0
    try:
        for csv_path in args:
            meta = col.get_csv_metadata(path=str(Path(csv_path).resolve()), delimiter=None)
            req = ImportCsvRequest(path=str(Path(csv_path).resolve()), metadata=meta)
            r1 = col.import_csv(req).log
            antes = col.note_count()
            r2 = col.import_csv(req).log
            despues = col.note_count()
            nuevas, actualizadas = len(r1.new), len(r2.updated) + len(r2.duplicate)
            problemas = len(r1.conflicting) + len(r1.missing_notetype) + len(r1.missing_deck) + len(r1.empty_first_field)
            ok = nuevas > 0 and problemas == 0 and antes == despues
            mal += not ok
            print(f"{'✓' if ok else '✗'} {csv_path}")
            print(f"    1ª importación: {nuevas} notas nuevas; problemas: {problemas}")
            print(f"    2ª importación: {len(r2.new)} nuevas, {actualizadas} ya existentes (sin duplicar: {antes == despues})")
            if r1.missing_notetype:
                print("    → El tipo de nota no existe en la colección: revisá --tipo-basico/--tipo-cloze en anki_csv.py")
        mazos = sorted(d.name for d in col.decks.all_names_and_ids() if d.name not in ("Default", "Predeterminado"))
        print("Mazos creados: " + ", ".join(mazos))
    finally:
        col.close()
        shutil.rmtree(d, ignore_errors=True)
    sys.exit(1 if mal else 0)


if __name__ == "__main__":
    # La consola de Windows usa cp1252 y no puede imprimir ✓/✗/acentos fuera de ese juego
    for _flujo in (sys.stdout, sys.stderr):
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    main()
