import os

from app import create_app

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
APP = create_app(config_name)

if __name__ == '__main__':
    APP.run(host='0.0.0.0')