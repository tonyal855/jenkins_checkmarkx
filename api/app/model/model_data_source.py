from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema, validate
from app import app

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = "customer"
    customer_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    customer_name = db.Column(db.String, unique=True, nullable=False)
    customer_description = db.Column(db.String, nullable=False)

class SchemaCustomerValidation(Schema):
    customer_name = fields.String(required=True)
    customer_description = fields.String(required=True)

class Importer(db.Model):
    __tablename__ = "importer"
    importer_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    importer_name = db.Column(db.String, unique=True, nullable=False)
    importer_description = db.Column(db.String, nullable=False)

class SchemaImporterValidation(Schema):
    importer_name = fields.String(required=True)
    importer_description = fields.String(required=True)


class Container(db.Model):
    __tablename__ = "container"
    container_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    container_type = db.Column(db.String, unique=True, nullable=False)
    container_size = db.Column(db.String, nullable=False)
    container_color = db.Column(db.String, nullable=False)
    container_cost = db.Column(db.String, nullable=False)
    importer_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)


class SchemaContainerValidation(Schema):
    container_type = fields.String(required=True)
    container_size = fields.String(required=True)
    container_color = fields.String(required=True)
    container_cost = fields.String(required=True)
    importer_id = fields.Integer(required=True)
    customer_id = fields.Integer(required=True)

class Vehicle(db.Model):
    __tablename__ = "vehicle"
    vehicle_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    vehicle_driver = db.Column(db.String, unique=True, nullable=False)
    vehicle_type = db.Column(db.String, nullable=False)
    vehicle_size = db.Column(db.String, nullable=False)
    vehicle_logistic_schema = db.Column(db.String, nullable=False)
    vehicle_cost = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    importer_id = db.Column(db.Integer, nullable=False)
    container_id = db.Column(db.Integer, nullable=False)


class SchemaVehicleValidation(Schema):
    vehicle_driver = fields.String(required=True)
    vehicle_type = fields.String(required=True)
    vehicle_size = fields.String(required=True)
    vehicle_logistic_schema = fields.String(required=True)
    vehicle_cost = fields.Integer(required=True)
    customer_id = fields.Integer(required=True)
    importer_id = fields.Integer(required=True)
    container_id = fields.Integer(required=True)