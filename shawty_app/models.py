from . import db


class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String, unique=True)
    created = db.Column(db.String, unique=True)
    count = db.Column(db.Integer, default=0)
