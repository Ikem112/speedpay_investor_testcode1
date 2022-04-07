from speedpay_testcode.models import db, Users, Transactions, In_app_transfers, Card_transactions, Bill_payments, Loan_payments
from datetime import datetime, date, time, timedelta
from sqlalchemy import func

def total_bill_transactions():
    bills = Bill_payments.query.all()
    bill_amount = []
    for bill in bills:
        bill_amount.append(bill.bill_payment_amount)

    total_bills = sum(bill_amount)
    
    return total_bills

def total_trans_amount():
    total_amount = total_bill_transactions() + total_loan_transactions()
    return total_amount

def total_loan_transactions():
    loans = Loan_payments.query.all()
    loan_amount = []
    for loan in loans:
        loan_amount.append(loan.loan_collected)

    total_loans = sum(loan_amount)

    return total_loans

def total_daily_reg():
    daily_reg_users = Users.query.filter(Users.date_joined == datetime.today()).count()
    return daily_reg_users

def total_weekly_reg():
    weekly_reg_users = Users.query.filter(Users.date_joined > datetime.today() - timedelta(weeks=1)).count()
    return weekly_reg_users

def total_monthly_reg():
    monthly_reg_users = Users.query.filter(Users.date_joined > datetime.today() - timedelta(days=30)).count()
    return monthly_reg_users




def avg_reg_user(duration):
    total_rec_durations = db.session.query(func.date_trunc(duration, Users.date_joined)).group_by(func.date_trunc(duration, Users.date_joined)).count()
    total_users = Users.query.count()

    average = total_users // total_rec_durations

    return average

def avg_trans(duration):
    total_trans_periods = db.session.query(func.date_trunc(duration, Transactions.trans_time)).group_by(func.date_trunc(duration, Transactions.trans_time)).count()
    
    average = total_trans_amount() // total_trans_periods

    return average

def total_trans_daily():
    daily_trans = Transactions.query.filter(Transactions.trans_time == datetime.today()).count()
    return daily_trans

def total_trans_weekly():
    weekly_trans = Transactions.query.filter(Transactions.trans_time > datetime.today() - timedelta(weeks=1)).count()
    return weekly_trans

def total_trans_monthly():

    monthly_trans = Transactions.query.filter(Transactions.trans_time > datetime.today() - timedelta(days=30)).count()
    return monthly_trans





