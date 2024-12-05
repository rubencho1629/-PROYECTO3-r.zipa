from app.config import db

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    base_id = db.Column(db.Integer, db.ForeignKey('bases.id'), nullable=False)
    calorias = db.Column(db.Float, nullable=True)
    rentabilidad = db.Column(db.Float, nullable=True)
    costo_produccion = db.Column(db.Float, nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    stock_maximo = db.Column(db.Integer, nullable=False, default=100)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)  # Relación con Usuario

    base = db.relationship('Base', backref='productos')
    usuario = db.relationship('Usuario', backref='productos')  # Relación con Usuario
