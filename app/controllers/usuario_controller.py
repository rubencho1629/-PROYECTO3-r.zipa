from flask import request, jsonify
from app.models.Usuario import Usuario
from app.utils import generar_token

def registrar_usuario():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Faltan datos"}), 400

    try:
        user = Usuario.create_user(username, password)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def autenticar_usuario():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = Usuario.authenticate(username, password)
    if user:
        token = generar_token(user.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401
