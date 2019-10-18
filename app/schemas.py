from app import ma
from marshmallow import fields
from app.models import Secret


class SecretSchema(ma.ModelSchema):
    class Meta:
        model = Secret
    # secret = fields.Str(required=True)
    # date_posted = fields.DateTime()


secret_schema = SecretSchema()
secrets_schema = SecretSchema(many=True)
