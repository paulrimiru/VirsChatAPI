from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_api import FlaskAPI
from instance.config import app_config

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
manager = Manager()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://mike:10131994@localhost/virs_db'

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    manager.__call__(app=app)
    manager.add_command('db', MigrateCommand)

    return app