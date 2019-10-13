from flask import Flask
from config import DevelopmentConfig
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource

db = SQLAlchemy()
ma = Marshmallow()
api = Api()


@api.route('/api/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    return app
