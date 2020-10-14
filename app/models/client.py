from app import db
from datetime import datetime


class Client(db.Model):

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    full_name = db.Column(db.String(255))

    auth_token = db.Column(db.String(900))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    logger = db.relationship("Logger", backref='logger', lazy=True)

    account = db.relationship("Account", backref='account', lazy=True)

    def __init__(self, full_name, auth_token):
        self.full_name = full_name
        self.auth_token = auth_token

    def __repr__(self):
        return '<Client %r>' % self.full_name
