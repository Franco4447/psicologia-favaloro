"""Muestra la ruta completa (Carpeta / Subcarpeta / ...) de una o más carpetas de Google Drive.

    python Scripts/get_drive_path.py <ID_de_carpeta> [<ID_de_carpeta> ...]
"""
import argparse

from drive_comun import servicio, utf8_consola


def ruta(service, carpeta):
    partes, actual = [], carpeta
    while actual:
        f = service.files().get(fileId=actual, fields="id, name, parents").execute()
        partes.insert(0, f["name"])
        padres = f.get("parents")
        actual = padres[0] if padres else None
    return " / ".join(partes)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpetas", nargs="+", metavar="ID", help="ID de la carpeta de Drive")
    args = ap.parse_args()

    service = servicio()
    for carpeta in args.carpetas:
        print(f"{carpeta}: {ruta(service, carpeta)}")


if __name__ == "__main__":
    utf8_consola()
    main()
