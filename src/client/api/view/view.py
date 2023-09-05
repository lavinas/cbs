from flask import jsonify, Response
from typing import Any
from werkzeug.exceptions import (
    BadRequest,
    Unauthorized, Forbidden, Conflict
)

def view(func):
    def inner(*args, **kwargs) -> Any:
        try:
            return success(func(*args, **kwargs))
        except BadRequest as exp:
            return error(400, 'invalid_request', str(exp.description))
        except Forbidden as exp:
            return error(401, 'invalid_client', 
                                    'Client authentication failed.')      
        except Unauthorized as exp:
            return error(401, 'invalid_credentials', 
                                    'The user credentials were incorrect.')
        except Conflict as exp:
            return error(409, 'conflict', str(exp.description))            
        except Exception as exp:
            return error(500, 'internal_error', 
                                    'contact vooo admin')
    return inner

def success(result: dict) -> Response:
    response = jsonify(result)
    response.status_code = 200
    return response

def error(code: int, name: str, description: str) -> Response:
    result = {
        'error': name,
        'error_description': description            
    }
    response = jsonify(result)
    response.status_code = code
    return response