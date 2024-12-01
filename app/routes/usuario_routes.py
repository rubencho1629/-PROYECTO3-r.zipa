from flask import Blueprint, jsonify, request
from app.controllers.usuario_controller import registrar_usuario, autenticar_usuario

usuario_bp = Blueprint("usuario_bp", __name__)

@usuario_bp.route('/registro', methods=['POST'])
def registro():
    return registrar_usuario()

@usuario_bp.route('/login', methods=['POST'])
def login():
    return autenticar_usuario()
