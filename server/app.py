from flask import Flask
from flask_cors import CORS

from .ext import configuration


def minimal_app(**config):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app
