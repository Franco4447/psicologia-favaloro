import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def list_drive_folder(folder_id):
    # Load credentials from the token file
    creds = Credentials.from_authorized_user_file('gdrive_token.json', ['https://www.googleapis.com/auth/drive'])
    
    # Build the Drive API client
    service = build('drive', 'v3', credentials=creds)
    
    # Call the Drive v3 API to list files in the specific folder
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(q=query, pageSize=100, fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found in the folder.')
    else:
        print('Files:')
        for item in items:
            print(f"{item['name']} (ID: {item['id']}) - Type: {item['mimeType']}")

if __name__ == '__main__':
    folder_id = '1ktEVSeHLJRo_AGXi0vS9Eff8IpMPrC1o'
    list_drive_folder(folder_id)
