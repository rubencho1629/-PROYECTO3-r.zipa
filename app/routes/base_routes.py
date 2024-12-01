from flask import Blueprint
from app.controllers.base_controller import listar_bases, crear_base, actualizar_base, eliminar_base

base_bp = Blueprint('base_bp', __name__)

@base_bp.route('/bases', methods=['GET'])
def get_bases():
    return listar_bases()
base_bp.route('/bases', methods=['POST'])(crear_base)
base_bp.route('/bases/<int:base_id>', methods=['PUT'])(actualizar_base)
base_bp.route('/bases/<int:base_id>', methods=['DELETE'])(eliminar_base)
