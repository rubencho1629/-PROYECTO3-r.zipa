from app.config import db

class Base(db.Model):
    __tablename__ = 'bases'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Base {self.nombre}>"
