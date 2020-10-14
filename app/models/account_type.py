from app import db


class AccountType(db.Model):

    __tablename__ = 'account_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    account_type = db.Column(db.String(100), nullable=False)

    account = db.relationship("Account")

    def __init__(self, account_type):
        self.account_type = account_type

    def __repr__(self):
        return '<AccountType %r>' % self.account_type
