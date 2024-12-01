import jwt
from datetime import datetime, timedelta
from app.config import Config

def generar_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),  # Token expira en 1 hora
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
    return token
