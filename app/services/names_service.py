from ..models.names import Names
from .. import db

def get_all_names():
    return Names.query.all()

def create_name(data):
    new_name = Names(
        first_name=data['first_name'],
        middle_name=data['middle_name'],
        last_name=data['last_name'],
        second_last_name=data['second_last_name']
    )
    db.session.add(new_name)
    db.session.commit()
    return new_name