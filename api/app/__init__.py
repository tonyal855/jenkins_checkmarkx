from flask import Flask
from flask_jwt_extended import JWTManager,create_access_token, create_refresh_token, jwt_required,fresh_jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:''@localhost/isl_db'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:''@127.0.0.1/isl_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
jwt = JWTManager(app)
JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
app.config['SECRET_KEY'] = 'NoSecret'
app.config['JWT_SECRET'] = 'RahasiaIsNotSecret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600 # 1 hour this is in second
api = '/api/v1/'

from app.controller.controller_user import *
from app.controller.controller_data_source import *
