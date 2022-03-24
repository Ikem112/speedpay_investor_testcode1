from datetime import datetime

from speedpay_testcode import db

# table for the Users in the app
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transactions = db.relationship('Transactions', backref='user')

    def __repr__(self):
        return f'User "{self.first_name} {self.last_name}", "{self.email}", "{self.phone_no}", "{self.date_joined}"'


# table for transactions in the app
class Transactions(db.Model):
    __tablename__ = 'Transactions'
    id = db.Column(db.Integer, primary_key=True)
    trans_name = db.Column(db.String(50), nullable=False)
    trans_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    in_app_transfer = db.relationship('In_app_transfers', backref='transaction', uselist=False)
    card_transaction = db.relationship('Card_transactions', backref='transaction', uselist=False)
    bill_payment = db.relationship('Bill_payments', backref='transaction', uselist=False)
    loan_payment = db.relationship('Loan_payments', backref='transaction', uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    def __repr__(self):
        return f'Transaction -- {self.trans_name} at -- {self.trans_time} for user {self.user_id}'

# table for in app tranfers in the app
class In_app_transfers(db.Model):
    __tablename__ = 'In App transfers'
    id = db.Column(db.Integer, primary_key=True)
    ammount_sent = db.Column(db.Float,)
    ammount_received = db.Column(db.Float,)
    in_app_transfer_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transaction_id = db.Column(db.Integer, db.ForeignKey('Transactions.id'), nullable=False)



class Card_transactions(db.Model):
    __tablename__ = 'Card Transactions'
    id = db.Column(db.Integer, primary_key=True)
    added_card = db.Column(db.Boolean, default=False, nullable=False)
    added_card_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    card_deposit_amount = db.Column(db.Float)
    card_withdrawal_amount = db.Column(db.Float)
    card_transaction_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transaction_id = db.Column(db.Integer, db.ForeignKey('Transactions.id'), nullable=False)




class Bill_payments(db.Model):
    __tablename__ = 'Bill payments'
    id = db.Column(db.Integer, primary_key=True)
    bill_payment_type = db.Column(db.String(50), nullable=False)
    bill_payment_amount = db.Column(db.Float, nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('Transactions.id'), nullable=False)



class Loan_payments(db.Model):
    __tablename__ = 'Loan Payments'
    id = db.Column(db.Integer, primary_key=True)
    loan_collected = db.Column(db.Float)
    date_of_loan_collected = db.Column(db.DateTime, default=datetime.utcnow)    
    loan_repaid = db.Column(db.Float)
    date_of_loan_repaid = db.Column(db.DateTime, default=datetime.utcnow)
    transaction_id = db.Column(db.Integer, db.ForeignKey('Transactions.id'), nullable=False)


def total_bill_transactions():
    bills = Bill_payments.query.all()
    bill_amount = []
    for bill in bills:
        bill_amount.append(bill.bill_payment_amount)

    total_bills = sum(bill_amount)
    
    return total_bills

total_bill_transactions()

def total_loan_transactions():
    loans = Loan_payments.query.all()
    loan_amount = []
    for loan in loans:
        loan_amount.append(loan.loan_collected)

    total_loans = sum(loan_amount)

    return total_loans
    

