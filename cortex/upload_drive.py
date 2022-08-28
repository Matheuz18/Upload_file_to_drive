import time
import os
import time
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from const import UPLOAD_PATH, CLIENT_SECRETS_PATH, SETTINGS_YAML


def file_upload(path_folder, name):

    """
        If auth screen appear even you using credentials.json verify path in settings.yaml
    """

    # create GoogleAuth object and setting the settings.yaml path
    gauth = GoogleAuth(settings_file=SETTINGS_YAML)

    # Change default client_secrets in GoogleAuth object
    gauth.DEFAULT_SETTINGS['client_config_file'] = CLIENT_SECRETS_PATH

    # Create GoogleDrive object using client_secrets auth
    drive = GoogleDrive(gauth)

    #Verify if file path exist, for not create a empty request for google drive
    d = os.path.exists(UPLOAD_PATH + name)

    if d:
        gfile = drive.CreateFile({"title": "{}".format(name),
                                  'parents': [
                                      {
                                          'id': '{}'.format(path_folder)
                                      }]
                                  })

        # Read file and set it as the content of this instance.
        gfile.SetContentFile(UPLOAD_PATH + name)

        time.sleep(30)

        gfile.Upload()  # Upload the file.

        return {"Status": "In queue"}
    else:
        return {"Status": "In queue"}
