from flask import request,jsonify
from app import app, api, create_access_token, create_refresh_token
from app.model.model_user import  db, Admin, Workspace, SchemaWorkspaceValidation
from app.model import errors
import hashlib
from datetime import datetime



@app.route('/', methods=['GET'])
def index():
    return "ISL"

@app.route('{}/login'.format(api), methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    pswhash = hashlib.sha512(password.encode()).hexdigest()
    res = Admin.query.filter_by(username=username, password=pswhash).first()
    if res is None:
        return jsonify(message="failed", data="user not found", status=200)
    else:
        res.last_access = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.commit()
        access_token = create_access_token(identity=res.username, fresh=True)
        refresh_token = create_refresh_token(identity=res.username)
        return jsonify(message="success", access_token=access_token, refresh_token=refresh_token, workspace=res.workspace_id,status=200)


@app.route('{}/get_all_user'.format(api), methods=['GET'])
def get_all_user():
    adm = Admin.query.all()
    arrMap = []
    for x in adm:
        temp_dict = x.__dict__
        temp_dict.pop('_sa_instance_state',None)
        temp_dict.pop('password',None)
        arrMap.append(temp_dict)
    result = jsonify(message="success", data=arrMap, status=200)
    return result

@app.route('{}/get_user'.format(api), methods=['GET'])
def get_user():
    if 'username' in request.args:
        username = request.args['username']
        res = Admin.query.filter_by(username=username).first()
        if res:
            temp_dict = res.__dict__
            temp_dict.pop('_sa_instance_state', None)
            temp_dict.pop('password', None)
            return jsonify(message="success", data=temp_dict, status=200)
        else:
            return jsonify(message="success", data=[], status=200)
    else:
        return errors.NO_INPUT_400

@app.route('{}/add_user'.format(api), methods=['POST'])
def add_user():
    admin_nik = request.form['admin_nik']
    admin_name = request.form['admin_name']
    adress = request.form['adress']
    phone = request.form['phone']
    created_date = request.form['created_date']
    last_access = request.form['last_access']
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    workspace_id = request.form["workspace_id"]

    check = Admin.query.filter_by(username=username).first()
    if check is None:
        pswhash = hashlib.sha512(password.encode()).hexdigest()
        new_admin = Admin(admin_nik=admin_nik, admin_name=admin_name, adress=adress, phone=phone, created_date=created_date,
                          last_access=last_access, email=email, username=username,password=pswhash,workspace_id=workspace_id)
        db.session.add(new_admin)
        db.session.commit()
        return jsonify(message="success", status=200)
    else:
        return errors.ALREADY_EXIST


@app.route('{}/update_user'.format(api), methods=['POST'])
def update_user():
    admin_nik = request.form["admin_nik"]
    admin_name = request.form["admin_name"]
    adress = request.form["adress"]
    phone = request.form["phone"]
    created_date = request.form["created_date"]
    last_access = request.form["last_access"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    workspace_id = request.form["workspace_id"]

    res = Admin.query.filter_by(username=username).first()
    if res:
        pswhash = hashlib.sha512(password.encode()).hexdigest()

        res.admin_nik = admin_nik
        res.admin_name = admin_name
        res.adress = adress
        res.phone = phone
        res.created_date = created_date
        res.last_access = last_access
        res.email = email
        res.username = username
        res.password = pswhash
        res.workspace_id = workspace_id

        db.session.commit()
        return jsonify(message="success update")
    else:
        return jsonify(message="user not found")


@app.route('{}/delete_user'.format(api), methods=["POST"])
def delete_user():
    username = request.form["username"]
    res = Admin.query.filter_by(username=username).first()
    if res:
        db.session.delete(res)
        db.session.commit()
        return jsonify(message="succes delete")
    else:
        return jsonify(message="user not found")

@app.route('{}/get_all_workspace'.format(api), methods=['GET'])
def get_all_workspace():
    res = Workspace.query.all()
    arrMap = []
    for x in res:
        temp_dict = x.__dict__
        temp_dict.pop('_sa_instance_state', None)
        arrMap.append(temp_dict)

    return jsonify(message="success", data=arrMap, status=200)

@app.route('{}/add_workspace'.format(api), methods=['POST'])
def add_workspace():
    req = request.form
    schme = SchemaWorkspaceValidation()
    err = schme.validate(req)
    if err:
        return err, 422
    new_workspace = Workspace(admin=req['admin'], logging=req['logging'], transaction=req['transaction'], vehicle=req['vehicle'],
                              container=req['container'],importer=req['importer'], customer=req['customer'] )
    db.session.add(new_workspace)
    db.session.commit()
    return jsonify(message="success", status=200)




