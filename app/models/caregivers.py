from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
# importa ambas tablas intermedias
from .panels   import panels_has_caregivers
from .patients import caregivers_has_patients

class Caregivers(db.Model):
    __tablename__ = 'caregivers'

    caregiver_id = db.Column(db.Integer, primary_key=True)
    password     = db.Column(db.String(300), nullable=False)
    email        = db.Column(db.String(100), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime,
                             default=datetime.utcnow,
                             onupdate=datetime.utcnow)
    is_active    = db.Column(db.Boolean, default=True)

    name_id = db.Column('names_name_id',
                        db.Integer,
                        db.ForeignKey('names.name_id'),
                        nullable=False)
    names   = db.relationship('Names', backref='caregivers')

    # 4) Relación con Panels
    panels = db.relationship(
        'Panels',
        secondary=panels_has_caregivers,
        back_populates='caregivers'
    )

    # 5) Relación con Patients (si la necesitas)
    patients = db.relationship(
        'Patients',
        secondary=caregivers_has_patients,
        back_populates='caregivers'
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Caregiver {self.email}>'
