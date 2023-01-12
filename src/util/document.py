from validate_docbr import CPF, CNPJ

class Document(object):
    def type(self, value: str) -> str:
        if CPF.validate(value):
            return 'CPF'
        if CNPJ.validate(value):
            return 'CNPJ'
        return None
    def validate(self, value: str) -> bool:
        return self.type(value) is not None

