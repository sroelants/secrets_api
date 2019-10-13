from app import api, ma, db
from flask_restplus import Resource
from app.models import Secret
from app.schemas import secrets_schema


@api.route('/api/secrets')
class SecretsResource(Resource):
    def get(self):
        secrets = Secret.query.all()
        return secrets.schema.dump(secrets)

    def post(self):
        pass
