
from flask import Flask
from flask_restx import Api
from .client.api import client_api

endpoints = {
    client_api
}

# getting main aplication
def get_app(**kwargs):
    app = _start_flask(**kwargs)
    api = Api(app)
    for p in endpoints:
        p(api)
    return app

# starting flasking module
def _start_flask(**kwargs):
    app = Flask(__name__)
    if kwargs.get("celery"):
        _init_celery(kwargs.get("celery"), app)
    app.config["JSON_SORT_KEYS"] = False
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    @app.after_request
    def set_response_headers(response):
        response.headers["Cache-Control"] = \
            "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return app

# initiate celery if iit has celery
def _init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask