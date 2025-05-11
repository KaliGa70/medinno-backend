from ..models.turns import Turns
from .. import db

def get_all_turns():
    return Turns.query.all()

def create_turn(data):
    new_turn = Turns(description=data['description'])
    db.session.add(new_turn)
    db.session.commit()
    return new_turn