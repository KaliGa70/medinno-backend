from ..models.medication_schedules import MedicationSchedules
from .. import db

def get_all_medication_schedules():
    return MedicationSchedules.query.all()

def create_medication_schedule(data):
    new_schedule = MedicationSchedules(
        fecha=data['fecha'],
        hora=data['hora'],
        recipes_recipe_id=data['recipes_recipe_id']
    )
    db.session.add(new_schedule)
    db.session.commit()
    return new_schedule