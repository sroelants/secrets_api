from app import ma
from marshmallow import fields


class SecretSchema(ma.Schema):
    secret = fields.Str(required=True)
    date_posted = fields.DateTime()


secret_schema = SecretSchema()
secrets_schema = SecretSchema(many=True)
