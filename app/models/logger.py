from app import db
from datetime import datetime


class Logger(db.Model):

    __tablename__ = 'logger'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    message = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, message, client_id):
        self.message = message
        self.client_id = client_id

    def __repr__(self):
        return '<Logger %r>' % self.message
