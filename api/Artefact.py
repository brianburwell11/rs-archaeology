from sys import path

from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload

from .third_party import get_image_url
path.insert(0, '..')
from auth import auth
from db import *
from db import Base


class ArtefactList(Resource):

    def get(self):
        alignment = request.args.get('alignment', None)
        sort_by = request.args.get('sort', 'level').lower()
        if sort_by not in ['level', 'name', 'id']:
            sort_by = 'level'

        try: 
            session = Session()
            artefacts = session.query(Artefact)

            if sort_by == 'level':
                artefacts = artefacts.order_by(Artefact.level_required).order_by(Artefact.name)
            elif sort_by == 'name':
                artefacts = artefacts.order_by(Artefact.name)
            elif sort_by == 'id':
                artefacts = artefacts.order_by(Artefact.id)

            if alignment:
                artefacts = artefacts.filter_by(alignment=alignment)
            
            artefacts = artefacts.all()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        return {
            'count': len(artefacts),
            'artefacts': [{'id':a.id, 'name':a.name} for a in artefacts]
        }


class ArtefactApiResource(Resource):

    def get(self, id):
        try: 
            session = Session()
            artefact = session.query(Artefact).filter_by(id=id).options(joinedload('materials')).first()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        if artefact is None:
            return {'error': f'No Artefact with id={id} exists.'}, 404

        materials = dict()
        for m in artefact.materials:
            materials[m.id] = {
                'name': m.name,
                'amount': session.query(Base.metadata.tables['material_artefact']).filter_by(artefact_id=id).filter_by(material_id=m.id).first().amount,
                'img': get_image_url(m.id)
            }

        return {
            'id': id,
            'name': artefact.name,
            'alignment': artefact.alignment,
            'levelRequired': artefact.level_required,
            'xp': artefact.xp,
            'img': get_image_url(id),
            'imgDamaged': get_image_url(artefact.id - 1),
            'materials': materials
            # 'materials': {m.id:session.query(Base.metadata.tables['material_artefact']).filter_by(artefact_id=id).filter_by(material_id=m.id).first().amount for m in artefact.materials}
            }


__all__ = [
    'ArtefactList',
    'ArtefactApiResource'
]