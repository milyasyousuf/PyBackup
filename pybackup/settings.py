import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
        'NAME': config('DB_NAME'),
        'CONNECTION':config('CONNECT_STRING_LOCAL'),
}
DIRECTORY = {
        'BACKUP_DIRECTORY':config("BACKUP_DIRECTORY"),
        'MSSQL_DATA_DIRECTORY':config("MSSQL_DATA_DIRECTORY"),
        'HOME_DIRECTORY':config("HOME_DIRECTORY"),
}
GDRIVE = {
        'CLIENT_SCERET_FILE':config("GDRIVE_CLIENT_SCERET_FILENAME"),
        'FOLDER_ID':config("GDRIVE_FOLDER_ID"),
        'CREDENTIALS_FILE':config("GDRIVE_CREDENTIALS_FILENAME"),
}
COMPRESSION_TYPE=config("COMPRESSION_TYPE")