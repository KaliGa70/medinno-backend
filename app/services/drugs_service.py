from ..models.drugs import Drugs
from .. import db

def get_all_drugs():
    return Drugs.query.all()

def create_drug(data):
    new_drug = Drugs(
        name=data['name'],
        formato=data['formato'],
        recipes_recipe_id=data['recipes_recipe_id']
    )
    db.session.add(new_drug)
    db.session.commit()
    return new_drug