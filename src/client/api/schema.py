from marshmallow import fields
from validate_docbr import CPF, CNPJ
from email_validator import validate_email, EmailNotValidError
from decimal import Decimal

class Validation(object):
    def name(value: str) -> bool:
        if len(value.strip().split(' ')) < 2:
            return False
        return True
    def document(value: Decimal) -> bool:
        if CPF().validate(str(value).zfill(11)):
            return True
        if CNPJ().validate(str(value).zfill(14)):
            return True
        return False
    def email(value: str) -> bool:
        try:
            validate_email(value)
            return True
        except EmailNotValidError:
            return False
    
POST_IN = {
    "surname": fields.Str(required=False),
    "name": fields.Str(required=True, validate=Validation.name),
    "document": fields.Decimal(required=True, validate=Validation.document),
    "phone": fields.Decimal(required=True),
    "email": fields.Str(required=True, validate=Validation.email)
}

POST_OUT = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "surname": {"type": "string"}
    }
}