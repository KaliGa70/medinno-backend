from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Inicializar SQLAlchemy
db = SQLAlchemy()

def create_app():
    """
    Factory function para crear y configurar la aplicación Flask.
    """
    # Crear la instancia de Flask
    app = Flask(__name__)

    # Configurar la aplicación desde la clase Config
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar blueprints (rutas)
    register_blueprints(app)

    return app

def register_blueprints(app):
    """
    Registrar todos los blueprints (rutas) de la aplicación.
    """
    from .routes.names_routes import names_bp
    from .routes.patients_routes import patients_bp
    from .routes.turns_routes import turns_bp
    from .routes.caregivers_routes import caregivers_bp
    from .routes.alerts_routes import alerts_bp
    from .routes.recipes_routes import recipes_bp
    from .routes.drugs_routes import drugs_bp
    from .routes.medication_schedules_routes import medication_schedules_bp
    from .routes.panels_routes import panels_bp

    app.register_blueprint(names_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(turns_bp)
    app.register_blueprint(caregivers_bp)
    app.register_blueprint(alerts_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(drugs_bp)
    app.register_blueprint(medication_schedules_bp)
    app.register_blueprint(panels_bp)