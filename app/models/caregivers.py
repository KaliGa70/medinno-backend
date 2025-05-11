from .. import db

class Caregivers(db.Model):
    __tablename__ = 'caregivers'
    caregiver_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    name_id = db.Column('names_name_id',db.Integer, db.ForeignKey('names.name_id'), nullable=False)
    names = db.relationship('Names', backref='caregivers')