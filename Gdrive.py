from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import settings as cf


class GoogleDriveConn():
    def __init__(self):
        self.client_secret = cf.GDRIVE["CLIENT_SCERET_FILE"]
        self.credentials = cf.GDRIVE["CREDENTIALS_FILE"]
        self.drive = self.authorize_drive()
        self.drive_folder_id = cf.GDRIVE["FOLDER_ID"]

    def authorize_drive(self):
        gauth = GoogleAuth()
        gauth.DEFAULT_SETTINGS['client_config_file'] = self.client_secret
        gauth.LoadCredentialsFile(self.credentials)
        return GoogleDrive(gauth)

    def upload_file_gdrive(self,filename):
        file1 = self.drive.CreateFile({'title': filename,"mimeType":"application/zip","parents": [{"kind": "drive#fileLink","id": self.drive_folder_id}]})
        file1.SetContentFile(filename)
        file1.Upload() # Upload the file.
        print('title: %s, id: %s' % (file1['title'], file1['id']))