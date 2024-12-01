from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    db.create_all()
    print("Todas las tablas han sido creadas.")