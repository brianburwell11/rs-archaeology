from flask import Blueprint
from flask_restx import Api


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, version='2.0.0', title='RS Archaeology')

from .Artefact import *
from .Collection import *
from .Collector import *
from .Material import *
from .Reward import *

# api.add_resource(ArtefactList, '/artefacts')
# api.add_resource(ArtefactApiResource, '/artefacts/<int:id>')

# api.add_resource(CollectionList, '/collections')
# api.add_resource(CollectionApiResource, '/collections/<int:id>')

# api.add_resource(CollectorList, '/collectors')
# api.add_resource(CollectorApiResource, '/collectors/<int:id>')

# api.add_resource(MaterialList, '/materials')
# api.add_resource(MaterialApiResource, '/materials/<int:id>')

# api.add_resource(RewardList, '/rewards')
# api.add_resource(RewardApiResource, '/rewards/<int:id>')


__all__ = [
    'api_blueprint'
    'ArtefactApiResource', 'ArtefactList',
    'CollectionApiResource', 'CollectionList',
    'CollectorApiResource', 'CollectorList',
    'MaterialApiResource', 'MaterialList',
    'RewardApiResource', 'RewardList',
]