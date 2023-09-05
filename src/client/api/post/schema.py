from marshmallow import fields
from validate_docbr import CPF, CNPJ
from email_validator import validate_email, EmailNotValidError
from re import findall, sub

class Validation(object):
    def name(value: str) -> bool:
        if len(value.strip().split(' ')) < 2:
            return False
        return True
    def nickname(value: str) -> bool:
        if len(value.strip().split(' ')) != 1:
            return False
    def document(value: str) -> bool:
        if CPF().validate(str(value).zfill(11)):
            return True
        if CNPJ().validate(str(value).zfill(14)):
            return True
        return False
    def phone(value: str) -> bool:
        value = sub('\D', '', value)
        pat = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        if findall(pat, value):
            return True
        else:
            return False
    def email(value: str) -> bool:
        try:
            validate_email(value)
            return True
        except EmailNotValidError:
            return False
    
IN = {
    "name": fields.Str(required=True, validate=Validation.name),
    "nickname": fields.Str(required=False, validate=Validation.nickname),
    "document": fields.Str(required=True, validate=Validation.document),
    "phone": fields.Str(required=True, validate=Validation.phone),
    "email": fields.Str(required=True, validate=Validation.email)
}

