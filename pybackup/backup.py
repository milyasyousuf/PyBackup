from pybackup import settings as cf
import pyodbc,datetime,shutil,os,zipfile
class BuildBackup():
    def __init__(self):
        self.filename =cf.DATABASES["NAME"]+"_"+datetime.datetime.today().strftime('%Y_%m_%d')+".bak"
        self.backup_directory = cf.DIRECTORY["BACKUP_DIRECTORY"]
        self.backup_directory_with_root = cf.DIRECTORY["MSSQL_DATA_DIRECTORY"]
        self.home_directory = cf.DIRECTORY["HOME_DIRECTORY"]
        self.compress_file_name = self.filename.split(".")[0]+cf.COMPRESSION_TYPE
        self.cnxn = pyodbc.connect(cf.DATABASES['CONNECTION'],autocommit=True)
    def get_mssql_database(self):
        cursor = self.cnxn.cursor()
        cursor.execute("BACKUP DATABASE "+cf.DATABASES['NAME']+" TO disk = '"+self.filename+"';")
        while cursor.nextset():
            pass
        print("BACKUP DATABASE "+cf.DATABASES['NAME']+" TO disk = '"+self.filename+"';")
    
    def copy_back_file(self):
        source  = self.backup_directory_with_root+self.filename
        destination = self.home_directory+self. backup_directory+self.filename
        if not os.path.exists(os.path.dirname(destination)):
            os.mkdir(self.home_directory+self.backup_directory)
        shutil.move(source, destination)
    def compress_backup_file(self):
        destination = self.home_directory+self.backup_directory+self.compress_file_name
        source = self.home_directory+self. backup_directory+self.filename
        file_zip = zipfile.ZipFile(destination, 'w')
        file_zip.write(source, compress_type=zipfile.ZIP_DEFLATED)
        file_zip.close()
        os.remove(source)