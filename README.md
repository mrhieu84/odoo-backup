Daily Backup odoo

## Create a Python Virtual Environment

In `/root/backup/`, run the following commands:

```bash
sudo apt update
pip install virtualenv
virtualenv venv
```

---

## Activate the Virtual Environment

```bash
source venv/bin/activate
```

---

## Install Required Python Libraries

```bash
pip install requests filetype schedule flask flask-cors minio boto3 pytz
```
## Make the Restart Script Executable

```bash
chmod +x ./restart_flask.sh
```

## Start the Flask Backup Server

```bash
./restart_flask.sh
```


### Option 1: PostgreSQL Running in Docker

```python
import pytz
LOCAL_TZ = pytz.timezone('Asia/Bangkok')

USE_POSTGRES_DOCKER = True
IS_UPLOAD_MINIO = False

DB_NAME = "test1"
DB_USER = "odoo"
DB_PASSWORD = "password_db"
PG_PORT = 5432
PG_BIN = ''
PG_CONTAINER = 'postgres_db' #Docker container
DUMP_PREFIX = DB_NAME

MINIO_URL = "http://localhost:9000"
ACCESS_KEY = "YOUR_ACCESS_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"
BUCKET_BAK = "backups"

FILESTORE_DIR = "/root/odoo15_docker/odoo-data/filestore/"
BACKUP_DIR = "/home/ubuntu/pg_dumps"
MAX_FILES_DUMP = 3

PASSWORD_LOGIN_UI = 'your password login'
```

