import os

# Conexión a base de datos RDS (Aurora PostgreSQL)
db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'bookstore_user')
db_password = os.environ.get('DB_PASSWORD', 'bookstore_pass')
db_name = os.environ.get('DB_NAME', 'bookstore')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Clave secreta para sesiones Flask
SECRET_KEY = os.environ.get('SECRET_KEY', 'secretkey')

# Carpeta de subida de archivos (debe estar montada con EFS)
UPLOAD_FOLDER = '/mnt/efs/uploads'
