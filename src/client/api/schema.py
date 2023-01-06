from marshmallow import fields

POST_IN = {
    "surname": fields.Str(required=False),
    "name": fields.Str(required=True),
    "document": fields.Decimal(required=True),
    "phone": fields.Decimal(required=True),
    "email": fields.Str(required=True),
}

POST_OUT = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "surname": {"type": "string"}
    }
}
