from typing import Any
from webargs.flaskparser import parser
from werkzeug.exceptions import BadRequest
from flask import request
from .schema import POST_IN
from .view import view
from .model import Model

class Control(object):
    def __init__(self, sett: Any, db: Any, log: Any):
        self.sett = sett
        self.db = db
        self.log = log
                  
    @view
    def post(self):
        args = parser.parse(POST_IN, request)
        args['surname'] = 'xxxx'
        model = Model(self.db)
        model.post(args)
        model.close()
        return {'ok': 'ok'}
    
@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error)
