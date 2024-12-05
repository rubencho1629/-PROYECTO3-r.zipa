"""
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PASS_DB')}@{os.getenv('URL_DB')}/{os.getenv('NAME_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para JWT
    SECRET_KEY = os.getenv('SECRET_KEY')

class TestConfig(Config):
    # Configuración para pruebas, puedes usar una base de datos en memoria
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
"""

import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Cargar variables de entorno desde .env
load_dotenv()

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

class Config:
    # Configuración para SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Cambia la URI para usar SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para JWT
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
    TESTING = True
