import os

# Conexión a base de datos RDS
db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'bookstore_user')
db_password = os.environ.get('DB_PASSWORD', 'bookstore_pass')
db_name = os.environ.get('DB_NAME', 'bookstore')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:5432/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'secretkey')

# Carpeta de subida de archivos (en EFS)
UPLOAD_FOLDER = '/mnt/efs/uploads'
