from flask import Blueprint
from flask_restful import Api

from .Artefact import *
from .Collector import *
from .Material import *


api_blueprint = Blueprint('api_blueprint', __name__)
api = Api(api_blueprint)

api.add_resource(ArtefactList, '/artefacts')
api.add_resource(ArtefactApi, '/artefacts/<int:id>')

api.add_resource(CollectorList, '/collectors')
api.add_resource(CollectorApi, '/collectors/<int:id>')

api.add_resource(MaterialList, '/materials')
api.add_resource(MaterialApi, '/materials/<int:id>')


__all__ = [
    'api_blueprint'
]