import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './credentials.json'  # Update with your service account file path
SERVICE_ACCOUNT_FILE_2 = './utils/gsheet/credentials.json'
def get_credentials():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                creds = Credentials.from_service_account_file(
                    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            except:
                # print(f"Error loading service account credentials: {e}")
                # return None
                try:
                    creds = Credentials.from_service_account_file(
                        SERVICE_ACCOUNT_FILE_2, scopes=SCOPES)
                except Exception as e:
                    print(f"Error loading service account credentials from second file: {e}")
                    return None
        # Save the credentials for the next run
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())
    print("Google Sheets credentials loaded successfully.")
    return creds