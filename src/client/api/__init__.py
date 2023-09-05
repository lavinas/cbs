from flask_restx import Resource, Api
from .schema.schema import POST_OUT
from .control.control import Control
from ...util.settings import Settings
from ...util.mysql import MySql
from ...util.log import Log

def client_api(api: Api):
    domain = 'client'
    sett = Settings(domain)
    db = MySql(sett)
    log = Log(sett)
    api = api.namespace(domain)
    
    # main route
    @api.route('/')
    @api.route('')
    class Client(Resource):
        # post
        @api.response(code=200, description="OK", 
                      model=api.schema_model("Auth", POST_OUT))
        def post(self):
            c = Control(sett, db, log)
            return c.post()
