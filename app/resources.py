from app import api
from flask_restplus import Resource, fields
from app.models import Secret
from app.schemas import secrets_schema, secret_schema
from flask import request
from marshmallow import ValidationError


secret_model = api.model('Secret', {
    'secret': fields.String,
    'date_posted': fields.DateTime()
})

@api.route('/api/secrets')
class SecretsResource(Resource):
    def get(self):
        secrets = Secret.query.all()
        return secrets_schema.dump(secrets)

    @api.expect(secret_model)
    def post(self):
        json = request.json
        try:
            secret, errors = secret_schema.load(request.json)
        except ValidationError as err:
            return {"errors": err.messages}, 422
        return json
