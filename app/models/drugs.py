from .. import db
from datetime import datetime

class Drugs(db.Model):
    __tablename__ = 'drugs'
    drug_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    formato = db.Column(db.String(100), nullable=False)
    recipes_recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
    recipes = db.relationship('Recipes', backref='drugs')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)