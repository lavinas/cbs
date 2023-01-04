from flask_restx import Resource, Api

def client_api(api: Api):
    api = api.namespace('client', description='client signup')

    @api.route('/')
    class Client(Resource):
        def get(self):
            return {'ok': 'ok'}
    
    