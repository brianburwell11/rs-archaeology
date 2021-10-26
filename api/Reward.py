from sys import path

from flask_restful import Resource

from .third_party import get_ge_value, get_image_url
path.insert(0, '..')
from auth import auth
from db import *


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

        return {
            'count': len(rewards),
            'rewards': [{'id':r.id, 'name':r.name} for r in rewards]
        }, 200


class RewardApiResource(Resource):
    """A reward for contributing to a collection."""

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