from sys import path

from flask import request
from flask_restx import fields, marshal, Resource

from . import api
from .third_party import get_ge_value, get_image_url

path.insert(0, "..")
from auth import auth
from db import *


# material_list = api.model('MaterialList', {
#                                 'count': fields.Integer,
#                                 'materials': fields.List(DictItem(
#                                     attribute
#                                     # 'id': fields.Integer,
#                                     # 'name': fields.String
#                                 ))
#                             })


@api.route("/materials")
class MaterialList(Resource):
    """A list of all of the Materials"""

    # @api.response(200, 'Success', material_list)
    def get(self):
        alignment = request.args.get("alignment", None)
        try:
            session = Session()
            if alignment:
                materials = (
                    session.query(Material)
                    .order_by(Material.name)
                    .filter_by(alignment=alignment)
                    .all()
                )
            else:
                materials = session.query(Material).order_by(Material.name).all()
            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        return [{"id": m.id, "name": m.name} for m in materials]


material = api.model(
    "Material",
    {
        "id": fields.Integer,
        "name": fields.String,
        "alignment": fields.String(
            enum=[
                "Agnostic",
                "Armadylean",
                "Bandosian",
                "Dragonkin",
                "Saradominist",
                "Zamorakian",
                "Zarosian",
            ]
        ),
        "img": fields.Url,
        "price": fields.Integer,
    },
)


@api.route("/materials/<int:id>")
class MaterialApiResource(Resource):
    """A material used to restore Artefacts."""

    @api.response(200, "Success", material)
    def get(self, id):
        try:
            session = Session()
            material = session.query(Material).filter_by(id=id).first()
            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        if material is None:
            return {"error": f"No Material with id={id} exists."}, 404

        return {
            "id": id,
            "name": material.name,
            "alignment": material.alignment,
            "img": get_image_url(id),
            "price": get_ge_value(id),
        }, 200


__all__ = ["MaterialList", "MaterialApiResource"]
