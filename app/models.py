from app import db
from datetime import datetime


class Secret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.utcnow())

    def __init__(self, secret):
        self.secret = secret

    def __repr__(self):
        return f"Secret('{self.date_posted}', '{self.secret}')"
