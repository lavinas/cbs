from string import capwords
from typing import Any
from webargs.flaskparser import parser
from werkzeug.exceptions import BadRequest, Conflict
from flask import request
from .schema import IN
from .view import view
from .model import Model
from re import sub
from decimal import Decimal

class NewClient(object):
    def __init__(self, sett: Any, db: Any, log: Any):
        self.sett = sett
        self.db = db
        self.log = log
        
    @view
    def run(self):
        args = dict(parser.parse(IN, request))
        try:
            self.db.connect()
            model = Model(self.db)
            args = format(args)
            duplicity(model, args)
            args['nickname'] = nickname(model, args)
            model.insert(args)
            self.db.close()
            self.log.info('OK', str(args))
            return args
        except Exception as exp:
            self.log.error('Error', '{}: {}'.format(exp, str(args)))
            raise exp
        
@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error)
    
        
def nickname(model: Model, args: dict) -> str:
    if 'nickname' in args:
        r = nickname_filled(model, args['nickname'])
        if r is not None:
            return r
    r = nickname_names(model, args['name'])
    if r is not None:
        return r
    return nickname_numbers(model, args['name'])
 
def nickname_filled(model: Model, name: str) -> str:
    if name is None:
        return None
    r = name.lower().replace(' ', '_')
    if model.nick_count(r) == 0:
        return r
    return None
    
def nickname_names(model: Model, name: str) -> str:
    names = name.split(' ')
    f = names[0].lower()
    r = None
    for i in range(len(names) - 1, 0, -1):
        s = names[i].lower()
        n = '{}_{}'.format(f, s)
        if model.nick_count(n) == 0:
            r = n
            break
    return r
 
def nickname_numbers(model: Model, name: str) -> str:
    names = name.split(' ')
    f = names[0].lower()
    s = names[len(names)-1].lower()
    i = 1
    r = '{f}_{s}_{i}'.format(f=f, s=s, i=i)
    while model.nick_count(r) != 0:
        i += 1
        r = '{f}_{s}_{i}'.format(f=f, s=s, i=i)
    return r

def duplicity(model: Model, args: dict) -> bool:
    if model.document_count(args['document']) != 0:
        e = Conflict()
        e.description = 'Document {} is already registered'.\
            format(args['document'])
        raise e
    
def format(args: dict) -> dict:
    args['name'] = capwords(args['name'])
    args['document'] = Decimal(sub('\D', '', args['document']))
    args['phone'] = Decimal(sub('\D', '', args['phone']))
    return args