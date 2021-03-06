from sys import path

from flask_restx import fields, Resource

from . import api
from .third_party import get_ge_value, get_image_url
path.insert(0, '..')
from db import *


@api.route('/rewards')
class RewardList(Resource):
    """A list of all of the items used as Rewards for contributing to Collections"""

    def get(self):
        try: 
            session = Session()
            rewards = session.query(Reward).order_by(Reward.name).all()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        return [{'id':r.id, 'name':r.name} for r in rewards]


reward = api.model('Reward', {
                        'id': fields.Integer,
                        'name': fields.String,
                        'img': fields.Url,
                        'price': fields.Integer
                    })

@api.route('/rewards/<int:id>')
@api.doc(params={'id': 'the in-game ID for the item, which is also its ID in the database'})
class RewardApiResource(Resource):
    """A reward for contributing to a collection."""

    @api.response(200, 'Success', reward)
    def get(self, id):
        try: 
            session = Session()
            reward = session.query(Reward).filter_by(id=id).first()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        if reward is None:
            return {'error': f'No Reward with id={id} exists.'}, 404

        return {
            'id': id,
            'name': reward.name,
            'img': get_image_url(id),
            'price': get_ge_value(id)
            }


__all__ = [
    'RewardList',
    'RewardApiResource'
]