from .. import db

class Turns(db.Model):
    __tablename__ = 'turns'
    turn_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)