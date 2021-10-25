from sys import path

from flask import request
from flask_restful import Resource

from .third_party import get_ge_value, get_image_url
path.insert(0, '..')
from auth import auth
from db import *


class MaterialList(Resource):
    """A list of all of the Materials"""

    def get(self):
        alignment = request.args.get('alignment', None)
        try: 
            session = Session()
            if alignment:
                materials = session.query(Material).order_by(Material.name).filter_by(alignment=alignment).all()
            else:
                materials = session.query(Material).order_by(Material.name).all()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        return {
            'count': len(materials),
            'materials': [{'id':m.id, 'name':m.name} for m in materials]
        }, 200


class MaterialApi(Resource):
    """A material used to restore Artefacts."""

    def get(self, id):
        try: 
            session = Session()
            material = session.query(Material).filter_by(id=id).first()
            session.close()
        except Exception as e:
            session.close()
            return {'error':str(e)}, 500

        if material is None:
            return {'error': f'No Material with id={id} exists.'}, 404

        return {
            'id': id,
            'name': material.name,
            'alignment': material.alignment,
            'img': get_image_url(id),
            'price': get_ge_value(id)
            }, 200

    @auth.login_required()
    def post(self):
        return 'post'


__all__ = [
    'MaterialList',
    'MaterialApi'
]