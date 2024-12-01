from flask import jsonify, request
from app.models.Base import Base
from app.config import db

def listar_bases():
    bases = Base.query.all()
    return jsonify([{"id": b.id, "nombre": b.nombre, "precio": b.precio} for b in bases])

def crear_base():
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')

    if not nombre or precio is None:
        return jsonify({"error": "Faltan datos"}), 400

    nueva_base = Base(nombre=nombre, precio=precio)
    db.session.add(nueva_base)
    db.session.commit()

    return jsonify({"message": f"Base {nueva_base.nombre} creada exitosamente"}), 201

def actualizar_base(base_id):
    data = request.get_json()
    base = Base.query.get(base_id)

    if not base:
        return jsonify({"error": "Base no encontrada"}), 404

    base.nombre = data.get('nombre', base.nombre)
    base.precio = data.get('precio', base.precio)
    db.session.commit()

    return jsonify({"message": f"Base {base.nombre} actualizada exitosamente"})

def eliminar_base(base_id):
    base = Base.query.get(base_id)

    if not base:
        return jsonify({"error": "Base no encontrada"}), 404

    db.session.delete(base)
    db.session.commit()

    return jsonify({"message": f"Base eliminada exitosamente"})
