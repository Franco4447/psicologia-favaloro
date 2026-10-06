"""Autoriza el acceso de solo lectura a Google Drive y guarda el token en gdrive_token.json.

Requiere gdrive_credentials.json (cliente OAuth) en la raíz del repositorio.

    python Scripts/auth.py
"""
import argparse
import sys

from drive_comun import CREDENCIALES, SCOPES, TOKEN, utf8_consola


def main():
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    if not CREDENCIALES.exists():
        sys.exit(f"No existe {CREDENCIALES.name} en la raíz del repositorio (cliente OAuth de Google Cloud Console)")
    from google_auth_oauthlib.flow import InstalledAppFlow

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENCIALES), SCOPES)
    # Puerto 3000: coincide con el redirect_uri configurado en el cliente OAuth
    print("Iniciando la autorización: abrí la URL que aparece abajo.")
    creds = flow.run_local_server(port=3000, prompt="consent", open_browser=False)
    TOKEN.write_text(creds.to_json(), encoding="utf-8")
    print(f"Token guardado en {TOKEN.name}")


if __name__ == "__main__":
    utf8_consola()
    main()
