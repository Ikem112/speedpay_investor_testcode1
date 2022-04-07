# # # from speedpay_testcode.models import Users, db

# # try:
# #     bob = Users(first_name='bob', last_name='stew', email='bob@mail.com', phone_no='08097565785', address='lekki')
# #     ben = Users(first_name='ben', last_name='burna', email='ben@mail.com', phone_no='08078986457', address='lekki, lagos')
# #     ikem = Users(first_name='ikem', last_name='stew', email='ikem@mail.com', phone_no='08097565785', address='lekki')
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

# from models import Users
# from speedpay_testcode import db
# from faker import Faker
# import random




# a = Users.query.get(34)
# b = Users.query.get(21)
# c = Users.query.get(56)
# d = Users.query.get(22)
# e = Users.query.get(37)
# f = Users.query.get(90)
# g = Users.query.get(200)
# h = Users.query.get(126)
# i = Users.query.get(135)
# j = Users.query.get(37)
# k = Users.query.get(10)
# l = Users.query.get(90)
# m = Users.query.get(73)
# n = Users.query.get(20)
# o = Users.query.get(100)
# p = Users.query.get(101)
# q = Users.query.get(102)
# r = Users.query.get(103)
# s = Users.query.get(104)
# t = Users.query.get(105)
# u = Users.query.get(106)
# v = Users.query.get(107)
# w = Users.query.get(108)
# x = Users.query.get(109)
# y = Users.query.get(110)
# z = Users.query.get(111)
# aa = Users.query.get(112)
# ab = Users.query.get(113)
# ac = Users.query.get(114)
# ad = Users.query.get(115)
# ae = Users.query.get(116)
# af = Users.query.get(117)
# ag = Users.query.get(118)
# ah = Users.query.get(201)
# ai = Users.query.get(202)
# aj = Users.query.get(203)
# ak = Users.query.get(208)
# al = Users.query.get(207)
# am = Users.query.get(222)
# an = Users.query.get(216)
# ao = Users.query.get(289)
# ap = Users.query.get(238)
# aq = Users.query.get(223)




# trans_type = ['bill_payment', 'loan_payment']
# users = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ag,ai,aj,ak,al,am,an,ao,ap,aq]

# for _ in range(3000):
#     random.choice(users)
#     random.choice(trans_type)



