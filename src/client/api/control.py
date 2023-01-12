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
        args = dict(parser.parse(POST_IN, request))
        self.db.connect()
        model = Model(self.db)
        args['nickname'] = nickname(model, args['name'])
        model.post(args)
        self.db.close()
        return {'nickname': args['nickname']}
    
@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error)
        
def nickname(model: Model, name: str) -> str:
    r = nickname_filled(model, name)
    if r is not None:
        return r
    r = nickname_surnames(model, name)
    if r is not None:
        return r
    return nickname_numbers(model, name)
 
def nickname_filled(model: Model, name: str) -> str:
    r = name.lower().replace(' ', '_')
    if model.nick_count(r) == 0:
        return r
    return None
    
def nickname_surnames(model: Model, name: str) -> str:
    names = name.split(' ')
    f = names[0].lower()
    r = None
    for i in range(len(names) - 1, 1, -1):
        s = names[i].lower()
        n = '{}_{}'.format(f, s)
        if model.nick_count(n) == 0:
            r = n
            break
    return r
 
def nickname_numbers(model: Model, name: str) -> str:
    names = name.split(name)
    f = names[0].lower()
    s = names[len(names)-1].lower()
    i = 1
    r = '{}_{}_{}'.format(f, s, i)
    while model.nick_count(r) == 0:
        i += 1
        r = '{}_{}_{}'.format(f, s, i)
    return r
