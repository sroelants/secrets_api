class Config(object):
    DEBUG = False 
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
     DEBUG = True

class TestingConfig(Config):
     TESTING = True
     SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

     # Enable the TESTING flag to disable the error catching during request
     # handling so that you get better error reports when performing test
     # requests against the application.
     TESTING = True
