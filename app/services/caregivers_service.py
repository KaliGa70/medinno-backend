from ..models.caregivers import Caregivers
from datetime import datetime
from flask_jwt_extended import create_access_token
from .. import db
from sqlalchemy.orm import joinedload


def get_all_caregivers():
    return Caregivers.query.all()

def get_caregiver_profile(user_id: int) -> dict | None:
    caregiver = (
        Caregivers.query
                  .options(joinedload(Caregivers.names))
                  .filter_by(caregiver_id=user_id)
                  .first()
    )
    if not caregiver:
        return None

    name = caregiver.names
    full_name = " ".join(filter(None, [
        name.first_name,
        name.middle_name,
        name.last_name,
        name.second_last_name
    ]))

    return {
        'caregiver_id': caregiver.caregiver_id,
        'email':        caregiver.email,
        'is_active':    caregiver.is_active,
        'created_at':   caregiver.created_at.isoformat(),
        'updated_at':   caregiver.updated_at.isoformat(),
        'name': {
            'name_id':          name.name_id,
            'first_name':       name.first_name,
            'middle_name':      name.middle_name,
            'last_name':        name.last_name,
            'second_last_name': name.second_last_name,
            'full_name':        full_name
        }
    }

class CaregiverAuthService:
    @staticmethod
    def register_caregiver(email: str, password: str, name_id: int) -> Caregivers:
        # Verifica que no exista otro caregiver con el mismo email
        if Caregivers.query.filter_by(email=email).first():
            raise ValueError("El correo electrónico ya está registrado.")
        
        caregiver = Caregivers(
            email=email,
            name_id=name_id,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        caregiver.set_password(password)
        
        db.session.add(caregiver)
        db.session.commit()
        return caregiver

    @staticmethod
    def authenticate(email: str, password: str) -> Caregivers | None:
        caregiver = Caregivers.query.filter_by(email=email, is_active=True).first()
        if caregiver and caregiver.check_password(password):
            return caregiver
        return None

    @staticmethod
    def generate_token(caregiver: Caregivers) -> str:
        # Emite un JWT con el ID del caregiver como identidad
        return create_access_token(identity=str(caregiver.caregiver_id))

    @staticmethod
    def get_caregiver_by_id(caregiver_id: int) -> Caregivers | None:
        """
        Recupera el caregiver de la base de datos dado su ID,
        o devuelve None si no existe.
        """
        return Caregivers.query.get(caregiver_id)