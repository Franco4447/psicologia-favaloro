"""Funciones compartidas por los scripts de Google Drive (auth, list_drive, get_drive_path, fetch_pdfs).

Las credenciales viven en la raíz del repositorio y están en .gitignore:
    gdrive_credentials.json  -> cliente OAuth descargado de Google Cloud Console
    gdrive_token.json        -> token que genera auth.py
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CREDENCIALES = RAIZ / "gdrive_credentials.json"
TOKEN = RAIZ / "gdrive_token.json"

# Solo lectura: alcanza para listar y descargar, y no permite modificar ni borrar nada en Drive.
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def servicio():
    """Cliente de la API de Drive v3 a partir del token guardado por auth.py."""
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    if not TOKEN.exists():
        sys.exit(f"No existe {TOKEN.name}: corré primero  python Scripts/auth.py")
    from google.auth.exceptions import RefreshError
    from google.auth.transport.requests import Request

    # Sin forzar scopes: un token viejo (permiso 'drive' completo) sigue funcionando.
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid:
        try:
            creds.refresh(Request())
        except RefreshError:
            sys.exit("El token de Drive venció o fue revocado: corré  python Scripts/auth.py  para renovarlo")
        TOKEN.write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds)


def listar(service, consulta, campos="id, name, mimeType"):
    """Todos los archivos que cumplen la consulta, recorriendo todas las páginas."""
    archivos, pagina = [], None
    while True:
        res = service.files().list(
            q=consulta, pageSize=1000, pageToken=pagina,
            fields=f"nextPageToken, files({campos})",
        ).execute()
        archivos.extend(res.get("files", []))
        pagina = res.get("nextPageToken")
        if not pagina:
            return archivos


def utf8_consola():
    """La consola de Windows usa cp1252: sin esto, los acentos de los nombres pueden romper print()."""
    for flujo in (sys.stdout, sys.stderr):
        flujo.reconfigure(encoding="utf-8", errors="replace")
