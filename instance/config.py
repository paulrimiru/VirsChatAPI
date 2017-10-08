# config.py

import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql+psycopg2://mike:10131994@localhost/virs_db')
    

class DevelopmentConfig(Config):
    """Configurations for Development."""
    CSRF_ENABLED = True
    SECRET = 'secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    CSRF_ENABLED = True
    SECRET = 'secret'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:10131994@localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'configobj':Config,
    'SECRET_KEY':'secret_key'
}
