from flask_restx import Resource, Api
# tools
from ...util.settings import Settings
from ...util.mysql import MySql
from ...util.log import Log
# modules
from .post.control import Post


def client_api(api: Api):
    domain = 'client'
    sett = Settings(domain)
    db = MySql(sett)
    log = Log(sett)
    api = api.namespace(domain)
    
    @api.route('/')
    @api.route('')
    class Client(Resource):
        def post(self):
            c = Post(sett, db, log)
            return c.run()
