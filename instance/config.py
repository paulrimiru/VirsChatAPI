# config.py

import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:10131994@localhost/virs_db'
    DATABASE_URL = 'postgres://agjlhnyhexnjjp:71aaff89c40cf61f2fd6f2773a0235b296cf1dd862a5a8abcbe7cfb1a00195c6@ec2-50-17-217-166.compute-1.amazonaws.com:5432/daktgc3ebm2uj2'

class DevelopmentConfig(Config):
    """Configurations for Development."""
    CSRF_ENABLED = True
    SECRET = 'secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:10131994@localhost/virs_db'
    DATABASE_URL = 'postgres://agjlhnyhexnjjp:71aaff89c40cf61f2fd6f2773a0235b296cf1dd862a5a8abcbe7cfb1a00195c6@ec2-50-17-217-166.compute-1.amazonaws.com:5432/daktgc3ebm2uj2'

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
