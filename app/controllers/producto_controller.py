from flask import jsonify, request
from app.models.Producto import Producto
from app.config import db

def listar_productos():
    productos = Producto.query.all()  # Obtiene todos los productos de la base de datos
    return jsonify([
        {
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "base_id": producto.base_id,
            "usuario_id": producto.usuario_id
        }
        for producto in productos
    ])
def consultar_producto_por_id(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": producto.id,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "calorias": producto.calorias,
        "rentabilidad": producto.rentabilidad,
        "costo_produccion": producto.costo_produccion
    })
def consultar_producto_por_nombre(nombre):
    producto = Producto.query.filter_by(nombre=nombre).first()
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": producto.id,
        "nombre": producto.nombre,
        "precio": producto.precio
    })

def consultar_calorias_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"calorias": producto.calorias})

def consultar_rentabilidad_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"rentabilidad": producto.rentabilidad})

def consultar_costo_produccion_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"costo_produccion": producto.costo_produccion})

def realizar_venta_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    if producto.stock <= 0:
        return jsonify({"error": "No hay suficiente stock"}), 400

    producto.stock -= 1
    db.session.commit()
    return jsonify({"message": "Producto vendido exitosamente", "stock_actual": producto.stock})

def realizar_reabastecimiento_producto(producto_id):
    data = request.get_json()
    cantidad = data.get("cantidad", 0)

    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    producto.stock += cantidad
    db.session.commit()
    return jsonify({"message": "Producto reabastecido", "stock_actual": producto.stock})

def renovar_inventario(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    producto.stock = producto.stock_maximo  # Asegúrate de que este atributo exista
    db.session.commit()

    return jsonify({
        "id": producto.id,
        "nombre": producto.nombre,
        "stock": producto.stock,
        "stock_maximo": producto.stock_maximo
    })


def crear_producto():
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = request.get_json()

        # Validar campos obligatorios
        if 'nombre' not in data or 'precio' not in data or 'base_id' not in data or 'usuario_id' not in data:
            return jsonify({"error": "Faltan campos obligatorios: 'nombre', 'precio', 'base_id', 'usuario_id'"}), 400

        # Crear un nuevo producto
        nuevo_producto = Producto(
            nombre=data['nombre'],
            precio=data['precio'],
            base_id=data['base_id'],
            usuario_id=data['usuario_id']
        )

        # Guardar en la base de datos
        db.session.add(nuevo_producto)
        db.session.commit()

        return jsonify({"message": "Producto creado exitosamente"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500