from app.config import db

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    es_sano = db.Column(db.Boolean, nullable=False)  # Define si el ingrediente es sano

    def __repr__(self):
        return f"<Ingrediente {self.nombre}>"
