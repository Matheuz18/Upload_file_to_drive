from pathlib import Path

local_project_path= Path(__file__).parent


UPLOAD_PATH = str(local_project_path) + '\\datas\\'
CLIENT_SECRETS_PATH = str(local_project_path) + "\\control_google\\client_secrets.json"
SETTINGS_YAML = str(local_project_path) + "\\control_google\\settings.yaml"



input()