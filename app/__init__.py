from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config, db
from app.routes.ingrediente import ingrediente_bp
from app.routes.usuario_routes import usuario_bp
from app.routes.base_routes import base_bp
from app.routes.producto_routes import producto_bp


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    app.register_blueprint(usuario_bp, url_prefix='/api')
    app.register_blueprint(base_bp, url_prefix='/api')
    app.register_blueprint(producto_bp, url_prefix='/api')
    app.register_blueprint(ingrediente_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return "Bienvenido a HeladerAPI"

    return app

