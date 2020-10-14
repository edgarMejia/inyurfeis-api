from app import db
from datetime import datetime


class Account(db.Model):

    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(255), nullable=False)

    password = db.Column(db.String(500), nullable=False)

    available = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(db.DateTime)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    account_type_id = db.Column(db.Integer, db.ForeignKey('account_type.id'))

    def __init__(self, message, client_id):
        self.message = message
        self.client_id = client_id

    def __repr__(self):
        return '<Account %r>' % self.message
