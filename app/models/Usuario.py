from app.config import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Cambié la longitud aquí

    @classmethod
    def create_user(cls, username, password):
        hashed_password = generate_password_hash(password)
        user = cls(username=username, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

