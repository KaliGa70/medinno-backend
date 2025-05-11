from ..models.caregivers import Caregivers
from .. import db

def get_all_caregivers():
    return Caregivers.query.all()

def create_caregiver(data):
    new_caregiver = Caregivers(
        password=data['password'],
        email=data['email'],
        name_id=data['name_id']
    )
    db.session.add(new_caregiver)
    db.session.commit()
    return new_caregiver