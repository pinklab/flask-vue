from flask import Blueprint
from flask_restful import Api

from .resources import ProductItemResource, ProductResource, PongItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(ProductResource, "/product")
    api.add_resource(ProductItemResource, "/product/<product_id>")
    api.add_resource(PongItemResource, "/pong")
    app.register_blueprint(bp)
