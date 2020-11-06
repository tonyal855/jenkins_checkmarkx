from flask import request,jsonify
from app import app, api
from app.model import errors
from app.model.model_data_source import db, SchemaCustomerValidation, Customer, SchemaImporterValidation, Importer, SchemaContainerValidation, Container, SchemaVehicleValidation, Vehicle

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

@app.route('{}/add_customer'.format(api), methods=['POST'])
def add_customer():
    req = request.form
    schem = SchemaCustomerValidation()
    err = schem.validate(req)
    if err:
        return err, 422
    check = Customer.query.filter_by(customer_name=req['customer_name']).first()
    if check is None:
        new_cust = Customer(customer_name=req['customer_name'], customer_description=req['customer_description'])
        db.session.add(new_cust)
        db.session.commit()
        return jsonify(message="success", status=200)

    else:
        return errors.ALREADY_EXIST

@app.route('{}/get_all_customer/'.format(api), methods=['GET'])
def get_all_customer():
    if 'page' in request.args:
        page = request.args['page']
    else:
        page = 1

    CusList = Customer.query.order_by(Customer.customer_id.asc()).paginate(page=int(page), per_page=10, error_out=False).items
    arrMap = []
    for x in CusList:
        temp_dict = x.__dict__
        temp_dict.pop('_sa_instance_state', None)
        arrMap.append(temp_dict)
    return jsonify(message="success", data=arrMap, status=200)


@app.route('{}/delete_customer'.format(api), methods=["POST"])
def delete_customer():
    customer_id = request.form["customer_id"]
    res = Customer.query.filter_by(customer_id=customer_id).first()
    if res:
        db.session.delete(res)
        db.session.commit()
        return jsonify(message="succes delete"), 200
    else:
        return errors.INVALID_INPUT_422

@app.route('{}/update_customer'.format(api), methods=['POST'])
def update_customer():
    req = request.form
    schem = SchemaCustomerValidation()
    err = schem.validate(req)
    if err:
        return err, 422
    res = Customer.query.filter_by(customer_id=req['customer_id']).first()
    if res:
        res.customer_name = req['customer_name']
        res.customer_description = req['customer_description']

        db.session.commit()
        return jsonify(message="success update")
    else:
        return errors.NOT_FOUND_404


@app.route('{}/add_importer'.format(api), methods=['POST'])
def add_importer():
    req = request.form
    schme = SchemaImporterValidation()
    err = schme.validate(req)
    if err:
        return err, 422
    check = Importer.query.filter_by(importer_name=req['importer_name']).first()
    if check is None:
        new_impt = Importer(importer_name=req['importer_name'], importer_description=req['importer_description'])
        db.session.add(new_impt)
        db.session.commit()
        return jsonify(message="success", status=200)

    else:
        return errors.ALREADY_EXIST

@app.route('{}/get_all_importer/'.format(api), methods=['GET'])
def get_all_importer():
    if 'page' in request.args:
        page = request.args['page']
    else:
        page = 1

    ImpList = Importer.query.order_by(Importer.importer_id.asc()).paginate(page=int(page), per_page=10, error_out=False).items
    arrMap = []
    for x in ImpList:
        temp_dict = x.__dict__
        temp_dict.pop('_sa_instance_state', None)
        arrMap.append(temp_dict)
    return jsonify(message="success", data=arrMap, status=200)

@app.route('{}/delete_importer'.format(api), methods=["POST"])
def delete_importer():
    importer_id = request.form["importer_id"]
    res = Importer.query.filter_by(importer_id=importer_id).first()
    if res:
        db.session.delete(res)
        db.session.commit()
        return jsonify(message="succes delete"), 200
    else:
        return errors.INVALID_INPUT_422

@app.route('{}/update_importer'.format(api), methods=['POST'])
def update_importer():
    req = request.form
    res = Importer.query.filter_by(importer_id=req['importer_id']).first()
    if res:
        res.importer_name = req['importer_name']
        res.importer_description = req['importer_description']

        db.session.commit()
        return jsonify(message="success update")
    else:
        return errors.NOT_FOUND_404

@app.route('{}/add_container'.format(api), methods=['POST'])
def add_container():
    req = request.form
    schme = SchemaContainerValidation()
    err = schme.validate(req)
    if err:
        return err, 422
    new_cont = Container(container_type=req['container_type'], container_size=req['container_size'], container_color=req['container_color'], container_cost=req['container_cost'],
                         importer_id=req['importer_id'], customer_id=req['customer_id'])
    db.session.add(new_cont)
    db.session.commit()
    return jsonify(message="success", status=200)

@app.route('{}/add_vehicle'.format(api), methods=['POST'])
def add_vehicle():
    req = request.form
    schme = SchemaVehicleValidation()
    err = schme.validate(req)
    if err:
        return err, 422
    new_vehicle = Vehicle(vehicle_driver=req['vehicle_driver'], vehicle_type=req['vehicle_type'], vehicle_size=req['vehicle_size'], vehicle_logistic_schema=req['vehicle_logistic_schema'],
                         vehicle_cost=req['vehicle_cost'], customer_id=req['customer_id'], importer_id=req['importer_id'], container_id=req['container_id'],)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(message="success", status=200)
