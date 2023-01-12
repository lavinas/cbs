from email_validator import validate_email, EmailNotValidError

class Email(object):
    def validate(self, email: str) -> bool:
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False

    