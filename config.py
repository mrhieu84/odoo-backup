import  pytz
# Timezone cho GMT+7 (Asia/Bangkok)
LOCAL_TZ = pytz.timezone('Asia/Bangkok')


USE_POSTGRES_DOCKER = False #Set True if Porgres running in docker
IS_UPLOAD_MINIO = False #set True if also upload backup files to Minio


# === Configuration Database Odoo for ===
DB_NAME = "my_db" #database backup
DB_USER = "odoo" #user backup
DB_PASSWORD = "db_password" #password database
PG_PORT = 5432
PG_BIN = '' # or PG_DUMP_BIN='/usr/local/pgsql/bin/'
PG_CONTAINER ='postgres_db' # if USE_POSTGRES_DOCKER = True, input name of container docker postgres
DUMP_PREFIX = DB_NAME


# === Configuration Minio ===
MINIO_URL = "http://localhost:9500" # URL API Minio
ACCESS_KEY = "YOUR_ACCESS_KEY" #ACCESS_KEY created  on UI minio or ROOT_USER
SECRET_KEY = "YOUR_SECRET_KEY"# SECRET_KEY created on UI minio or ROOT_USER_PASSWORD
BUCKET_BAK = "backups"



FILESTORE_DIR = "/root/odoo15_docker/odoo-data/filestore/"  # filestore of odoo
BACKUP_DIR = "/home/ubuntu/pg_dumps" # Backup path
MAX_FILES_DUMP = 3

#login UI
PASSWORD_LOGIN_UI = 'admin' #passrd login, default admin

