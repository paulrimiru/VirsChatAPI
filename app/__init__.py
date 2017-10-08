from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_api import FlaskAPI
from flask_restful import Api
from flask_redis import FlaskRedis
from flask_heroku import Heroku

from instance.config import app_config


configobj = 'development'
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object(app_config[configobj])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://mike:10131994@localhost/virs_db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app)
api = Api(app)
redis = FlaskRedis(app)
manager = Manager(app)
heroku = Heroku(app)

manager.add_command('db', MigrateCommand)

from app import routes