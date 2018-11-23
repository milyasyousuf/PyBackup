from gdrive import GoogleDriveConn
from backup import BuildBackup 
import settings as cf,datetime

class Driver():
    def __init__(self):
        self.filename =cf.DATABASES["NAME"]+"_"+datetime.datetime.today().strftime('%Y_%m_%d')+".bak"
        self.backup_directory = cf.DIRECTORY["BACKUP_DIRECTORY"]
        self.backup_directory_with_root = cf.DIRECTORY["MSSQL_DATA_DIRECTORY"]
        self.home_directory = cf.DIRECTORY["HOME_DIRECTORY"]
        self.compress_file_name = self.filename.split(".")[0]+cf.COMPRESSION_TYPE
        self.destination  = self.home_directory+self.backup_directory+self.compress_file_name
    def run_script(self):
        bb = BuildBackup()
        bb.get_mssql_database()
        bb.copy_back_file()
        bb.compress_backup_file()
        dr = GoogleDriveConn()
        dr.upload_file_gdrive(self.destination)



drive = Driver()
drive.run_script()