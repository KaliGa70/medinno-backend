from .. import db

class Patients(db.Model):
    __tablename__ = 'patients'
    patient_id = db.Column(db.Integer, primary_key=True)
    cuarto = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(45), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    name_id = db.Column('names_name_id', db.Integer, db.ForeignKey('names.name_id'), nullable=False)
    names = db.relationship('Names', backref='patients')