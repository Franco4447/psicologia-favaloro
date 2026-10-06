"""Descarga los PDF de una o más carpetas de Google Drive a 1_Bibliografia_Original/ de una materia.

    python Scripts/fetch_pdfs.py --materia "2do Año/Psicoanálisis" <ID_de_carpeta> [<ID> ...]
    python Scripts/fetch_pdfs.py --materia "2do Año/Psicoanálisis" <ID> --dry-run

Respeta AGENTS.md: nunca guarda en una carpeta global /Bibliografía, sino en
[Año]/[Materia]/1_Bibliografia_Original/ (se crea si no existe). Los PDF conservan el nombre
que tienen en Drive: renombralos después según la convención de AGENTS.md. Esa carpeta no se
versiona en git (.gitignore): los PDF quedan solo en la copia local.
"""
import argparse
import io
import re
import sys

from drive_comun import RAIZ, listar, servicio, utf8_consola


def nombre_seguro(nombre):
    """Quita los caracteres que Windows no admite en nombres de archivo."""
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", nombre).strip().rstrip(".")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpetas", nargs="+", metavar="ID", help="ID de la carpeta de Drive")
    ap.add_argument("--materia", required=True,
                    help='carpeta de la materia, relativa a la raíz del repo (ej.: "2do Año/Psicoanálisis")')
    ap.add_argument("--sobrescribir", action="store_true", help="vuelve a descargar los que ya existen")
    ap.add_argument("--dry-run", action="store_true", help="solo lista qué descargaría")
    args = ap.parse_args()

    materia = (RAIZ / args.materia).resolve()
    if RAIZ not in materia.parents or len(materia.relative_to(RAIZ).parts) != 2:
        sys.exit('--materia debe ser "[Año]/[Materia]", relativo a la raíz del repositorio')
    if not materia.is_dir():
        sys.exit(f"No existe la carpeta de la materia: {materia.relative_to(RAIZ)}")
    destino = materia / "1_Bibliografia_Original"

    from googleapiclient.http import MediaIoBaseDownload

    service = servicio()
    for carpeta in args.carpetas:
        pdfs = listar(service, f"'{carpeta}' in parents and mimeType='application/pdf' and trashed = false",
                      campos="id, name")
        print(f"== {carpeta}: {len(pdfs)} PDF")
        for pdf in pdfs:
            ruta = destino / nombre_seguro(pdf["name"])
            if ruta.exists() and not args.sobrescribir:
                print(f"  ya existe, se saltea: {ruta.name}")
                continue
            if args.dry_run:
                print(f"  descargaría: {ruta.relative_to(RAIZ)}")
                continue
            destino.mkdir(parents=True, exist_ok=True)
            pedido = service.files().get_media(fileId=pdf["id"])
            with io.FileIO(ruta, "wb") as fh:
                descarga = MediaIoBaseDownload(fh, pedido)
                listo = False
                while not listo:
                    _, listo = descarga.next_chunk()
            print(f"  descargado: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    utf8_consola()
    main()
