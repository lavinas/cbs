from flask_restx import Resource, Api
# tools
from ...util.settings import Settings
from ...util.mysql import MySql
from ...util.log import Log
# modules
from .new.control import NewClient


def client_api(api: Api):
    api = api.namespace('client')
    sett = Settings('client')
    db = MySql(sett)
    log = Log(sett)
    
    @api.route('/')
    @api.route('')
    class Default(Resource):
        def get(self):
            return 'Pong'
        def post(self):
            return 'Pong'

    @api.route('/new')
    class New(Resource):
        def post(self):
            return NewClient(sett, db, log).run()

