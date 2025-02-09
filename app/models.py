from app import db
from datetime import datetime


class Secret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.utcnow())
    likes = db.Column(db.Integer, nullable=True, default=0)

    def __init__(self, secret, date_posted, likes=0):
        self.secret = secret
        self.date_posted = date_posted
        self.likes = likes

    def __repr__(self):
        return f"Secret('{self.date_posted}', '{self.secret}')"
