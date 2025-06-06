from .. import db
from datetime import datetime

class Recipes(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    patients_patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'), nullable=False)
    patients = db.relationship('Patients', backref='recipes')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)