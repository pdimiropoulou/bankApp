from app import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema' : 'public'}
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64),  nullable=False)
    password = db.Column(db.String(64), nullable=False)

class Customer(db.Model):
    __tablename__ = 'customers'
    __table_args__ = {'schema' : 'public'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class BankAccount(db.Model):
    __tablename__ = 'bankAccounts'
    __table_args__ = {'schema' : 'public'}
    id = db.Column(db.Integer, primary_key=True)
    accountName = db.Column(db.String(120), nullable=True) 
    customerId = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(20), nullable=False, default='EUR')

class Transaction(db.Model):
    __tablename__ = 'transactions'
    __table_args__ = {'schema' : 'public'}
    id = db.Column(db.Integer, primary_key=True)
    fromAccountId = db.Column(db.Integer, nullable=False)
    toAccountId = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
