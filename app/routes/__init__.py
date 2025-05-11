from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar rutas
    from app.routes import names_routes, patients_routes, turns_routes, caregivers_routes, alerts_routes, recipes_routes, drugs_routes, medication_schedules_routes, panels_routes
    app.register_blueprint(names_routes.names_bp)
    app.register_blueprint(patients_routes.patients_bp)
    app.register_blueprint(turns_routes.turns_bp)
    app.register_blueprint(caregivers_routes.caregivers_bp)
    app.register_blueprint(alerts_routes.alerts_bp)
    app.register_blueprint(recipes_routes.recipes_bp)
    app.register_blueprint(drugs_routes.drugs_bp)
    app.register_blueprint(medication_schedules_routes.medication_schedules_bp)
    app.register_blueprint(panels_routes.panels_bp)


    return app