from .. import db

class MedicationSchedules(db.Model):
    __tablename__ = 'medication_schedules'
    medication_schedule_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    recipes_recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
    recipes = db.relationship('Recipes', backref='medication_schedules')