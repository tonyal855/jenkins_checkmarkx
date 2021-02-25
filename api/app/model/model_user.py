from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema, validate
from datetime import datetime
from app import app

db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    admin_nik = db.Column(db.String,unique=True, nullable=False)
    admin_name = db.Column(db.String, nullable=False)
    adress = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False)
    last_access = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    workspace_id = db.Column(db.String, nullable=False)

class SchemaAdminValidate(Schema):
    admin_nik = fields.String(required=True, validate=validate.Length(max=12))
    admin_name = fields.String(required=True)
    adress = fields.String(required=True)
    phone = fields.Integer(required=True, validate=validate.Length(max=13))
    created_date = fields.DateTime(required=True)
    last_access = fields.DateTime(required=True)
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    workspace_id = fields.Integer(required=True)

class Workspace(db.Model):
    __tablename__ = "workspace"
    workspace_id = db.Column(db.Integer, nullable=False, primary_key=True,)
    admin = db.Column(db.Integer, nullable=False)
    logging = db.Column(db.Integer, nullable=False)
    transaction = db.Column(db.Integer, nullable=False)
    vehicle = db.Column(db.Integer, nullable=False)
    container = db.Column(db.Integer, nullable=False)
    importer = db.Column(db.Integer, nullable=False)
    customer = db.Column(db.Integer, nullable=False)

class SchemaWorkspaceValidation(Schema):
    admin = fields.Integer(required=True)
    logging = fields.Integer(required=True)
    transaction = fields.Integer(required=True)
    vehicle = fields.Integer(required=True)
    container = fields.Integer(required=True)
    importer = fields.Integer(required=True)
    customer = fields.Integer(required=True)



