import os
import io
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def download_pdfs_from_folders(folder_ids, dest_dir):
    creds = Credentials.from_authorized_user_file('gdrive_token.json', ['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=creds)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    for folder_id in folder_ids:
        print(f"Scanning folder {folder_id}...")
        query = f"'{folder_id}' in parents and mimeType='application/pdf' and trashed = false"
        results = service.files().list(q=query, pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        
        if not items:
            print(f"No PDFs found in folder {folder_id}.")
            continue
            
        for item in items:
            file_id = item['id']
            file_name = item['name']
            file_path = os.path.join(dest_dir, file_name)
            
            print(f"Downloading {file_name}...")
            request = service.files().get_media(fileId=file_id)
            with io.FileIO(file_path, 'wb') as fh:
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
            print(f"Saved to {file_path}")

if __name__ == '__main__':
    folders = [
        '1Dc_QpcTJ_Ncs-B1BFPWSWHqbqLFErgum',
        '13lvYHO5i-bslvJUaeLGzIzb635Y4RSwW'
    ]
    # Guardaremos los PDFs originales en /Bibliografía
    dest = r'c:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\Bibliografía'
    download_pdfs_from_folders(folders, dest)
