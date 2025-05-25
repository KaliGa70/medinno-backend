from .. import db
from datetime import datetime

# 1) Definición de la tabla intermedia, con el nombre real
panels_has_caregivers = db.Table(
    'panels_has_caregivers',
    db.Column(
        'panels_device_id',
        db.String(32),
        db.ForeignKey('panels.device_id'),
        primary_key=True
    ),
    db.Column(
        'caregivers_caregiver_id',
        db.Integer,
        db.ForeignKey('caregivers.caregiver_id'),
        primary_key=True
    )
)

class Panels(db.Model):
    __tablename__ = 'panels'

    device_id  = db.Column(db.String(32), primary_key=True)
    name       = db.Column(db.String(64))
    patient_id = db.Column('patients_patient_id',
                           db.Integer,
                           db.ForeignKey('patients.patient_id'))
    last_seen  = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 2) Relación muchos-a-muchos con Caregivers
    caregivers = db.relationship(
        'Caregivers',
        secondary=panels_has_caregivers,
        back_populates='panels'
    )
