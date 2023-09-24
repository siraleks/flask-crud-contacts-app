from app import app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Lädt die Umgebungsvariablen aus der .env-Datei

# Konstruiert die SQLAlchemy URI basierend auf den Umgebungsvariablen
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', '')
host = os.getenv('MYSQL_HOST', '127.0.0.1')
database = os.getenv('MYSQL_DB', 'flask-crud-contacts-app')
sqlalchemy_database_uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy-Instanz
db = SQLAlchemy()

