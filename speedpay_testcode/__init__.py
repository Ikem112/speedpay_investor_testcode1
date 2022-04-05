from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow

from config import Config


import psycopg2

db = SQLAlchemy()
# jwt = JWTManager()
# ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    # jwt.init_app(app)
    # app.app_context().push()
    #ma.init_app(app)

    from .blueprints import testcode as testcode_blueprint
    app.register_blueprint(testcode_blueprint )

    return app

     







# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:OmoLewa223@localhost/Speedpay_Database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False








