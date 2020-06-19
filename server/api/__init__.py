from flask import Blueprint
from flask_restful import Api

from .resources import TaskItemResource, TasksResource, PongItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(TasksResource, "/tasks/")
    api.add_resource(TaskItemResource, "/tasks/<task_id>")
    api.add_resource(PongItemResource, "/pong")
    app.register_blueprint(bp)
