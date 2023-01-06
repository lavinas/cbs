from webargs.flaskparser import parser
from werkzeug.exceptions import BadRequest
from flask import request
from .schema import POST_IN
from .view import view
from .model import Model

class Control(object):
    
    @parser.error_handler
    def handle_error(error, req, schema, *, error_status_code, error_headers):
        raise BadRequest(error)
        
    @view
    def post():
        args = parser.parse(POST_IN, request)
        args['surname'] = 'xxxx'
        Model.post(args)
        return {'ok': 'ok'}