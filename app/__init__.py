# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort;
# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import User

    APP = FlaskAPI(__name__, instance_relative_config=True)
    APP.config.from_object(app_config[config_name])
    APP.config.from_pyfile('config.py')
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://mike:10131994@localhost/virs_db'
    db.init_app(APP)

    @APP.route('/users/', methods=['GET', 'POST'])
    def usercreation():
        if request.method == 'POST':
            username = str(request.data.get('username'))
            usertype = str(request.data.get('usertype'))
            email = str(request.data.get('email'))
            password = str(request.data.get('password'))

            if username:
                user = User(username=username, usertype=usertype, email=email, password=password)
                response = jsonify({'success':True, 'message':'user created '+username})
                response.status_code = 201
                return response
        else:
            userlist = User.get_all()
            result = []

            for user in userlist:
                obj = {
                    'username':user.username,
                    'email':user.email,
                    'type':user.usertype
                }
                result.append(obj)
            response = jsonify(result)
            response.status_code = 201
    @APP.route('/users/login/', methods=['GET','POST'])
    def userlogin():
        if request.method == 'POST':
            email = str(request.data.get('email'))
            password = str(request.data.get('password'))

    @APP.route('users/<str:email>', methods=['POST', 'GET', 'PUT'])
    def user_manipulation():
        if request.method == 'POST':
            
        elif request.method == 'GET':
            
        elif request.method == 'PUT':
            
    return APP