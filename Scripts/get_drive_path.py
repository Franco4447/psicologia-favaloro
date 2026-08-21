import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def get_folder_path(service, folder_id):
    path = []
    current_id = folder_id
    while current_id:
        file = service.files().get(fileId=current_id, fields="id, name, parents").execute()
        path.insert(0, file.get('name'))
        parents = file.get('parents')
        if not parents:
            break
        current_id = parents[0]
    return ' / '.join(path)

def main():
    creds = Credentials.from_authorized_user_file('gdrive_token.json', ['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=creds)
    
    folders = [
        '1Dc_QpcTJ_Ncs-B1BFPWSWHqbqLFErgum',
        '13lvYHO5i-bslvJUaeLGzIzb635Y4RSwW'
    ]
    
    for fid in folders:
        print(f"Path for {fid}:")
        print(get_folder_path(service, fid))
        print("---")

if __name__ == '__main__':
    main()
