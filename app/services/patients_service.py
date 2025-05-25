from ..models.patients import Patients
from ..models.caregivers import Caregivers
from .. import db
from sqlalchemy.orm import joinedload

def get_all_patients():
    return Patients.query.all()

def get_all_patients_by_caregiver_count(caregiver_id):
    return (
        Patients.query
        .join(Patients.caregivers)
        .filter(Caregivers.caregiver_id == caregiver_id)
        .all()
    )

def get_all_patients_by_caregiver(caregiver_id: int) -> list[dict]:
    patients = (
        Patients.query
                .options(joinedload(Patients.names))
                .filter(Patients.caregivers.any(caregiver_id=caregiver_id))
                .all()
    )

    resultado = []
    for p in patients:
        n = p.names
        resultado.append({
            'patient_id':       p.patient_id,
            'cuarto':           p.cuarto,
            'fecha_nacimiento': p.fecha_nacimiento.isoformat(),
            'sexo':             p.sexo,
            'name': {
                'name_id':          n.name_id,
                'first_name':       n.first_name,
                'middle_name':      n.middle_name,
                'last_name':        n.last_name,
                'second_last_name': n.second_last_name,
                'full_name':        f"{n.first_name} {n.middle_name} {n.last_name} {n.second_last_name}".strip()
            }
        })

    return resultado

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