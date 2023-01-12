from marshmallow import fields
from ...util.document import Document
from ...util.email import Email


POST_IN = {
    "surname": fields.Str(required=False),
    "name": fields.Str(required=True),
    "document": fields.Decimal(required=True, validate=Document().validate),
    "phone": fields.Decimal(required=True),
    "email": fields.Str(required=True, validate=Email().validate)
}

POST_OUT = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "surname": {"type": "string"}
    }
}
