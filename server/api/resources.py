from flask import abort, jsonify
from flask_restful import Resource

from server.models import Task


class TasksResource(Resource):
    def get(self):
        tasks = Task.query.all() or abort(204)
        return jsonify({"tasks": [task.to_dict() for task in tasks]})


class TaskItemResource(Resource):
    def get(self, task_id):
        task = Task.query.filter_by(id=task_id).first() or abort(404)
        return jsonify(task.to_dict())


class PongItemResource(Resource):
    def get(self):
        return jsonify({"msg": "pong"})
