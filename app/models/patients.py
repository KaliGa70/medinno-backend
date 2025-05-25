from .. import db
from datetime import datetime

# Si existe también una tabla paciente-caregiver
caregivers_has_patients = db.Table(
    'caregivers_has_patients',
    db.Column(
        'caregivers_caregiver_id',
        db.Integer,
        db.ForeignKey('caregivers.caregiver_id'),
        primary_key=True
    ),
    db.Column(
        'patients_patient_id',
        db.Integer,
        db.ForeignKey('patients.patient_id'),
        primary_key=True
    )
)

class Patients(db.Model):
    __tablename__ = 'patients'
    patient_id       = db.Column(db.Integer, primary_key=True)
    cuarto           = db.Column(db.String(45), nullable=False)
    sexo             = db.Column(db.String(45), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    is_active        = db.Column(db.Boolean, default=True, nullable=False)
    name_id          = db.Column('names_name_id',
                                 db.Integer,
                                 db.ForeignKey('names.name_id'),
                                 nullable=False)
    names            = db.relationship('Names', backref='patients')
    created_at       = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at       = db.Column(db.DateTime,
                                 default=datetime.utcnow,
                                 onupdate=datetime.utcnow)

    caregivers = db.relationship(
        'Caregivers',
        secondary=caregivers_has_patients,
        back_populates='patients'
    )
