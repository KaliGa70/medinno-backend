from .. import db

class Panels(db.Model):
    __tablename__ = "panels"
    device_id    = db.Column(db.String(32), primary_key=True)
    name         = db.Column(db.String(64))           # opcional (“Box A-101”)
    patient_id   = db.Column('patients_patient_id', db.Integer, db.ForeignKey("patients.patient_id"))
    caregiver_id = db.Column('caregivers_caregiver_id', db.Integer, db.ForeignKey("caregivers.caregiver_id"))
    last_seen    = db.Column(db.DateTime)

    patient   = db.relationship('Patients', backref="panels")
    caregiver = db.relationship('Caregivers', backref="panels")
