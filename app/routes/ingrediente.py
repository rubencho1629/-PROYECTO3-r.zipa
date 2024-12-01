from flask import Blueprint
from app.controllers.ingredientes_controller import (listar_ingredientes, consultar_ingrediente_por_id, consultar_ingrediente_por_nombre, consultar_si_ingrediente_es_sano   )

ingrediente_bp = Blueprint('ingrediente_bp', __name__)


@ingrediente_bp.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    return listar_ingredientes()

@ingrediente_bp.route('/ingredientes/<int:ingrediente_id>', methods=['GET'])
def get_ingrediente_by_id(ingrediente_id):
    return consultar_ingrediente_por_id(ingrediente_id)

@ingrediente_bp.route('/ingredientes/nombre/<string:nombre>', methods=['GET'])
def get_ingrediente_by_nombre(nombre):
    return consultar_ingrediente_por_nombre(nombre)

@ingrediente_bp.route('/ingredientes/<int:ingrediente_id>/sano', methods=['GET'])
def get_ingrediente_es_sano(ingrediente_id):
    return consultar_si_ingrediente_es_sano(ingrediente_id)
