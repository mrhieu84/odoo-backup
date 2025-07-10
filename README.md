NHBackupManaer
Daily Backup odoo

## Create a Python Virtual Environment

In `/root/backup/` or `/home/user/backup`, run the following commands:

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
pip install requests filetype schedule flask flask-cors minio boto3 pytz psutil
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



## systemctl server
Note make service name: nhodoobackup, The service name is used in restart_flask.sh for checking service exists

sudo nano /etc/systemd/system/nhodoobackup.service

[Unit]
Description=Flask Server Odoo backup Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/sy_backup #replace with your folder
ExecStart=nohup /home/ubuntu/sy_backup/venv/bin/python -u flask_server.py > flask.log 2>&1 & 
Restart=always
RestartSec=5
Environment=PATH=/usr/bin:/usr/local/bin
StandardOutput=file:/home/ubuntu/sy_backup/flask.log #replace with your path flask.log
StandardError=file:/home/ubuntu/sy_backup/flask.log


[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl enable nhodoobackup.service
sudo systemctl start nhodoobackup.service


sudo journalctl -f  -u  nhodoobackup

When you change the code server, you can restart the server by using: sudo ./restart_flask or sudo systemctl restart nhodoobackup.service.



check: https://tech.nhdesign.app/article/detail/2510800017039360



