# # # from speedpay_testcode.models import Users, db

# # try:
# #     bob = Users(first_name='bob', last_name='stew', email='bob@mail.com', phone_no='08097565785', address='lekki')
# #     ben = Users(first_name='ben', last_name='burna', email='ben@mail.com', phone_no='08078986457', address='lekki, lagos')
# #     ikem = Users(first_name='ikem', last_name='stew', email='bob@mail.com', phone_no='08097565785', address='lekki')
# #     john = Users(first_name='john', last_name='chisco', email='john@mail.com', phone_no='08086509345', address='ajah')
# #     fred = Users(first_name='fred', last_name='pastor', email='fred@mail.com', phone_no='08078567490', address='ikorodu')
# #     tolu = Users(first_name='tolu', last_name='tolu', email='tolu@mail.com', phone_no='08098089646', address='kano')
# #     greg = Users(first_name='greg', last_name='hardy', email='greg@mail.com', phone_no='09878568999', address='kadauna')
# #     blessing = Users(first_name='blessing', last_name='success', email='blessing@mail.com', phone_no='07098907689', address='agungi')

# #     db.session.add_all([bob, ben, ikem, john, fred, tolu, greg, blessing])
# #     db.session.commit()

# # except Exception as e:

# #     print (e)


#  ikem = Users(first_name='ikem', last_name='stew', email='ikem@mail.com', phone_no='08097565785', address='lekki')  
#  john = Users(first_name='john', last_name='chisco', email='john@mail.com', phone_no='08086509345', address='ajah')
#  trans1 = Transactions(trans_name='bill_payment', user=ikem)
#  trans2 = Transactions(trans_name='bill_payment', user=ikem)
#  trans3 = Transactions(trans_name='bill_payment', user=ikem)
#  trans4 = Transactions(trans_name='bill_payment', user=ikem)
#  trans5 = Transactions(trans_name='bill_payment', user=ikem)
#  trans6 = Transactions(trans_name='loan_payment', user=john)
#  trans7 = Transactions(trans_name='loan_payment', user=john)
#  trans8 = Transactions(trans_name='loan_payment', user=john)
#  trans9 = Transactions(trans_name='loan_payment', user=john)
#  bill1 = Bill_payments(bill_payment_type='cable & tv', bill_payment_amount=70000, transaction=trans1)
#  bill2 = Bill_payments(bill_payment_type='internet', bill_payment_amount=20000, transaction=trans2)
#  bill3 = Bill_payments(bill_payment_type='cable & tv', bill_payment_amount=100000, transaction=trans3)
#  bill4 = Bill_payments(bill_payment_type='internet', bill_payment_amount=32000, transaction=trans4)
#  bill5 = Bill_payments(bill_payment_type='data recharge', bill_payment_amount=4000, transaction=trans5)
#  loan1 = Loan_payments(loan_collected=50000, loan_repaid=50000, transaction=trans6)
#  loan2 = Loan_payments(loan_collected=230000, loan_repaid=230000, transaction=trans7)
#  loan3 = Loan_payments(loan_collected=4000, loan_repaid=4000, transaction=trans8)
#  loan4 = Loan_payments(loan_collected=45000, loan_repaid=45000, transaction=trans9)