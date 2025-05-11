from sqlalchemy import Enum
from .. import db

alert_enum = Enum(
    "CALL_NURSE",
    "EMERGENCY",
    "MEDICATION",
    "ASSISTANCE",
    "PAIN",
    "MEAL",
    "WATER",
    name="alert_type_enum",
)

class Alerts(db.Model):
    __tablename__ = 'alerts'
    alert_id = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(alert_enum, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    state = db.Column(db.SmallInteger, nullable=False, default=1)

    device_id  = db.Column('panels_device_id', db.String(32), db.ForeignKey("panels.device_id"), nullable=False)
    patient_id = db.Column('patients_patient_id', db.Integer, db.ForeignKey("patients.patient_id"), nullable=False)
    caregiver_id = db.Column('caregivers_caregiver_id', db.Integer, db.ForeignKey("caregivers.caregiver_id"))

    panels     = db.relationship('Panels', backref='alerts')
    patient   = db.relationship('Patients', backref='alerts')
    caregiver = db.relationship('Caregivers', backref='alerts')