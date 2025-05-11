from ..models.patients import Patients
from .. import db

def get_all_patients():
    return Patients.query.all()

def create_patient(data):
    new_patient = Patients(
        cuarto=data['cuarto'],
        sexo=data['sexo'],
        fecha_nacimiento=data['fecha_nacimiento'],
        name_id=data['name_id']
        )
    db.session.add(new_patient)
    db.session.commit()
    return new_patient