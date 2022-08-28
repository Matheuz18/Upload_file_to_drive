from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

'''
    : Create project in https://console.cloud.google.com/welcome?project=sheetsystem
    : Activate Google Drive API for project
    : Go to Manage in Google Drive API -> Credentials -> Create Credentials (OAth Client ID)
    : Application Type (Desktop app), Insert a Name for credential
    : Click in Download JSON
    : Rename client_secret_XXXXXXXXXXXX.json to client_secrets.json
    : Move client_secrets.json for project in /control_google
    : Rename settings_template.yaml to settings.yaml
        : (If necessary) How To create settings.yaml -> https://pythonhosted.org/PyDrive/oauth.html
    : Change settings.yaml for information in client_secrets.json     
    : Run create_credentials.py
    : Allow the terms using your account
    : Check if credential.json was created
    : IMPORTANT -> Run again create_credentials.py, if the auth screen appear again (and the credential.json exist), 
      you need change "save_credentials_file" path in settings.yaml to absolute path.
    
    : IMPORTANT -> Pay attention for const.py, in there have the main paths used in all project
    
    : Any problem you can contact me  matheuzcoelho18@gmail.com, use tag [Project Problem] in summary
    : Pls write you doubt in Brazilian Portuguese or English.
'''

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
