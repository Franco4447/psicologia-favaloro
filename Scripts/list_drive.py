"""Lista nombre, ID y tipo de los archivos de una o más carpetas de Google Drive.

    python Scripts/list_drive.py <ID_de_carpeta> [<ID_de_carpeta> ...]

El ID es la parte final de la URL de la carpeta: drive.google.com/drive/folders/<ID>
"""
import argparse

from drive_comun import listar, servicio, utf8_consola


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpetas", nargs="+", metavar="ID", help="ID de la carpeta de Drive")
    args = ap.parse_args()

    service = servicio()
    for carpeta in args.carpetas:
        archivos = listar(service, f"'{carpeta}' in parents and trashed = false")
        print(f"== {carpeta}: {len(archivos)} archivo(s)")
        for a in sorted(archivos, key=lambda a: a["name"].lower()):
            print(f"  {a['name']}  (ID: {a['id']})  [{a['mimeType']}]")


if __name__ == "__main__":
    utf8_consola()
    main()
