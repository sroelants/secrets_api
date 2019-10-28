import os
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'secrets_db',
    'host': 'localhost',
    'port': '5432',
}

class Config(object):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_DATABASE_URI = \
        'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    # Enable the TESTING flag to disable the error catching during request
    # handling so that you get better error reports when performing test
    # requests against the application.
    TESTING = True

class DeployConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
