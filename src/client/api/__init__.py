from flask_restx import Resource, Api
from .schema import POST_OUT
from .control import Control

def client_api(api: Api):
    api = api.namespace('client', description='client signup')
    @api.route('/')
    class Client(Resource):
        # post
        @api.response(code=200, description="OK", 
                      model=api.schema_model("Auth", POST_OUT))
        def post(self):
            return Control.post()