from flask import Blueprint
from app.controllers.producto_controller import (listar_productos,
                                                 crear_producto,
                                                 consultar_producto_por_id,
                                                 consultar_producto_por_nombre,
                                                 consultar_calorias_producto,
                                                 consultar_rentabilidad_producto,
                                                 consultar_costo_produccion_producto,
                                                 realizar_venta_producto,
                                                 realizar_reabastecimiento_producto, renovar_inventario)

producto_bp = Blueprint('producto_bp', __name__)


# Rutas para productos
@producto_bp.route('/productos', methods=['GET'])
def get_productos():
    return listar_productos()

@producto_bp.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto_by_id(producto_id):
    return consultar_producto_por_id(producto_id)


@producto_bp.route('/productos', methods=['POST'])
def add_producto():
    return crear_producto()

@producto_bp.route('/productos/nombre/<string:nombre>', methods=['GET'])
def get_producto_by_nombre(nombre):
    return consultar_producto_por_nombre(nombre)

@producto_bp.route('/productos/<int:producto_id>/calorias', methods=['GET'])
def get_calorias_producto(producto_id):
    return consultar_calorias_producto(producto_id)

@producto_bp.route('/productos/<int:producto_id>/rentabilidad', methods=['GET'])
def get_rentabilidad_producto(producto_id):
    return consultar_rentabilidad_producto(producto_id)

@producto_bp.route('/productos/<int:producto_id>/costo', methods=['GET'])
def get_costo_produccion_producto(producto_id):
    return consultar_costo_produccion_producto(producto_id)

@producto_bp.route('/productos/<int:producto_id>/vender', methods=['POST'])
def vender_producto(producto_id):
    return realizar_venta_producto(producto_id)

@producto_bp.route('/productos/<int:producto_id>/reabastecer', methods=['POST'])
def reabastecer_producto(producto_id):
    return realizar_reabastecimiento_producto(producto_id)

@producto_bp.route('/productos/<int:producto_id>/renovar', methods=['POST'])
def renovar_inventario_producto(producto_id):
    return renovar_inventario(producto_id)
