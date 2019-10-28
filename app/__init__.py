from flask import Flask
from config import DevelopmentConfig, Config
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()
api = Api()
from app.resources import SecretsResource


def create_app(config=DeployConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    CORS(app)

    return app
