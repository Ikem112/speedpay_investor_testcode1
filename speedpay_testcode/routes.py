from flask import jsonify, request


from .models import Users, total_bill_transactions, total_loan_transactions, Bill_payments
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
# from .models_schema import User_Schema

from speedpay_testcode.blueprints import testcode

@testcode.route("/")
def index():
    print("i came here")
    return  index

@testcode.route("/login_investor", methods=['POST'])
def login():
    try :
        email = request.json['email']
        password = request.json['password']

        if not email:
            return jsonify({ 'status' : 'email missing'}), 400
        if not password:
            return jsonify({ 'status' : 'password missing'}), 400
        if not email and password:
            return jsonify({ 'status' : 'email and password are missing'}), 400

        user_email = Users.query.filter_by(email=email).first()
        username = user_email.first_name
         

        if not user_email:
            return jsonify({ 'status' : 'user not found'}), 400

        if user_email and password == user_email.phone_no:
            access_token = create_access_token(identity={"email":email, "username":username.title()})

            return jsonify({
                'status' : 'login success',
                'access_token' : access_token
                
            }), 200
        else:
            print (f'failed login from {email}')
            return jsonify({
                'status' : 'login failed, please check details'
            }), 422
    except Exception as e:
        print(e)
        return jsonify({'status': 'failed', 'msg': "couldn't connect to server" }), 422

@testcode.route('/statistics', methods=['GET'])
@jwt_required()
def statistics():

    current_user = get_jwt_identity()

    try:
        total_users = Users.query.count()
        amount_total_bill_trans = total_bill_transactions()
        total_loans_dispursed = total_loan_transactions()
        no_of_bill_trans = Bill_payments.query.count()
        total_transactions = amount_total_bill_trans + total_loans_dispursed
        avg_trans_per_user = total_transactions/total_users

        
        return jsonify({
            'Current_user' : current_user,
            'Users': {
                'total_users' : total_users,
                'avg_daily_reg' : 4,
                'total_daily_reg' : 6,
                'avg_weekly_reg' : 19,
                'total_weekly_reg' : 30,    
                'avg_monthly_reg' : 70, 
                'total_monthly_reg' : 120
            },
            'Transactions' : {
                'total_transactions' : total_transactions,
                'avg_trans_per_user' : avg_trans_per_user,
                'total_revenue': total_transactions,
                'avg_trans_daily' : 3_000_000,
                'avg_trans_weekly' : 17_960_000,
                'avg_trans_monthly' : 80_790_000,
                'total_trans_daily' : 4_000_000,
                'total_trans_weekly' : 12_000_000,
                'total_trans_monthly' : 20_970_700
            },
            'Loans' : {
                'total_loan_dispursed' : total_loans_dispursed,
                'total_loan_defaulted' : 0,
                'total_users_defaulting' : 23,
                'no_loans_defaulted' : 23
            },
            'Bills' : {
                'amount_total_bill_trans' : amount_total_bill_trans,
                'no_of_trans' : no_of_bill_trans,
                'most_used_bills' : ['Dstv', 'Airtel Data', 'Bet King', 'MTN Data', 'MTN Credit', 'GOtv', 'Startimes', 'IPnx Internet', 'Sporty Bet', 'PHCN'],
                'most_used_bill_type' : 'cable'
            }
        }), 200
        
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'failed',
            'message': 'server error'
        }),
        422


