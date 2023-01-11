from validate_docbr import CPF, CNPJ

class Document(object):
    def type(value: str) -> str:
        if CPF.validate(value):
            return 'CPF'
        if CNPJ.validate(value):
            return 'CNPJ'
        return None

