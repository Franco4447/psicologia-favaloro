import json
import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds_file = 'gdrive_credentials.json'
    token_file = 'gdrive_token.json'
    
    # Run the flow using the client secrets file
    flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
    
    # We will use port 3000 to match the redirect_uri in the JSON
    print("Starting authentication flow... Please check the URL below.")
    creds = flow.run_local_server(port=3000, prompt='consent', open_browser=False)
    
    # Save the credentials for the next run
    with open(token_file, 'w') as token:
        token.write(creds.to_json())
    
    print(f"Token saved successfully to {token_file}!")

if __name__ == '__main__':
    main()
