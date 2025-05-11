from ..models.recipes import Recipes
from .. import db

def get_all_recipes():
    return Recipes.query.all()

def create_recipe(data):
    new_recipe = Recipes(
        description=data['description'],
        patients_patient_id=data['patients_patient_id']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe