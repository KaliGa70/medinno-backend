from .. import db

class Names(db.Model):
    __tablename__ = 'names'
    name_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    second_last_name = db.Column(db.String(50), nullable=False)