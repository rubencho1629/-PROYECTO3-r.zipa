from app.config import db
from app import create_app

# Crear la aplicación
app = create_app()

# Crear las tablas en SQLite
with app.app_context():
    db.create_all()
    print("Tablas creadas en SQLite")
