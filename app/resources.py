from app import api, db, CORS
from flask_restplus import Resource, fields
from app.models import Secret
from app.schemas import secrets_schema, secret_schema
from flask import request, jsonify
from marshmallow import ValidationError


secret_model = api.model('Secret', {
    'secret': fields.String,
    'date_posted': fields.DateTime(),
    'likes': fields.Integer
})


@api.route('/api/secrets')
class SecretsResource(Resource):
    def get(self):
        secrets = Secret.query.all()
        return secrets_schema.dump(secrets)


    @api.expect(secret_model)
    def post(self):
        json = request.json
        secret = secret_schema.load(json)
        db.session.add(secret)
        db.session.commit()

        # CORS
        response = jsonify(json).headers.add('Access-Control-Allow-Origin', '*')


@api.route('/api/secret/<int:id>')
class SecretResource(Resource):
    @api.expect(secret_model)
    def put(self, id):
        json = request.json
        update = secret_schema.load(json)
        secret = Secret.query.get(id)
        secret.likes = update.likes

        db.session.add(secret)
        db.session.commit()



@api.route('/api/secrets/<int:page>')
class SecretsPageResource(Resource):
    def get(self, page):
        secrets = Secret.query.order_by(Secret.date_posted.desc()).paginate(page=page, per_page=1).items
        response = jsonify(secrets_schema.dump(secrets))
        response.headers.add('Access-Control-Allow-Origin', '*')  # CORS
        return response
