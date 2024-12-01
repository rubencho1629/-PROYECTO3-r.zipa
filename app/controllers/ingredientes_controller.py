from flask import jsonify, request
from app.models.Ingrediente import Ingrediente
from app.config import db

def listar_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([
        {"id": ingrediente.id, "nombre": ingrediente.nombre, "es_sano": ingrediente.es_sano}
        for ingrediente in ingredientes
    ])


def consultar_ingrediente_por_id(ingrediente_id):
    ingrediente = Ingrediente.query.get(ingrediente_id)
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    return jsonify({"id": ingrediente.id, "nombre": ingrediente.nombre})

def consultar_ingrediente_por_nombre(nombre):
    ingrediente = Ingrediente.query.filter_by(nombre=nombre).first()
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    return jsonify({"id": ingrediente.id, "nombre": ingrediente.nombre})

def consultar_si_ingrediente_es_sano(ingrediente_id):
    ingrediente = Ingrediente.query.get(ingrediente_id)
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    return jsonify({"es_sano": ingrediente.es_sano})
