from flask_restx import Resource, Api
from .schema import POST_OUT
from .control import Control
from ...util.settings import Settings
from ...util.mysql import MySql
from ...util.log import Log
from ...util.document import Document

def client_api(api: Api):
    domain = 'client'
    sett = Settings(domain)
    db = MySql(sett)
    log = Log(sett)
    doc = Document()
    api = api.namespace(domain)
    
    # main route
    @api.route('/')
    @api.route('')
    class Client(Resource):
        # post
        @api.response(code=200, description="OK", 
                      model=api.schema_model("Auth", POST_OUT))
        def post(self):
            c = Control(sett, db, log, doc)
            return c.post()
