from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_marshmallow import Marshmallow
import os
import psycopg2



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:OmoLewa223@localhost/Speedpay_Database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)
# ma = Marshmallow(app)

from speedpay_testcode import routes



