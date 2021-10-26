from sys import path

from flask_restful import Resource
from sqlalchemy.orm import joinedload

from .third_party import get_NPC_image_url
path.insert(0, '..')
from auth import auth
from db import Session, Collector, Base


class CollectorList(Resource):
    """A list of all of the Collectors"""

    def get(self):
        try: 
            session = Session()
            collectors = session.query(Collector).order_by(Collector.name).all()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        return {
            'count': len(collectors),
            'collectors': [{'id':c.id, 'name':c.name} for c in collectors]
        }, 200


class CollectorApiResource(Resource):
    """An NPC that collects Artefacts."""

    def get(self, id):
        try: 
            session = Session()
            collector = session.query(Collector).filter_by(id=id).options(joinedload('collections')).first()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        if collector is None:
            return {'error': f'No Collector with id={id} exists.'}, 404

        collections = dict()
        for c in collector.collections:
            collections[c.id] = {
                'name': c.name
            }

        return {
            'id': id,
            'name': collector.name,
            'img': get_NPC_image_url(collector.name),
            'collections': collections
            }


__all__ = [
    'CollectorList',
    'CollectorApiResource'
]