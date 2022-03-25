from sys import path

from flask import request
from flask_restx import Resource
from sqlalchemy.orm import joinedload

from . import api
from .third_party import get_image_url

path.insert(0, "..")
from auth import auth
from db import *
from db import Base


@api.route("/artefacts")
class ArtefactList(Resource):
    """A list of items that can be restored using Materials."""

    def get(self):
        alignment = request.args.get("alignment", None)
        sort_by = request.args.get("sort", "level").lower()
        if sort_by not in ["level", "name", "id"]:
            sort_by = "level"

        try:
            session = Session()
            artefacts = session.query(Artefact)

            if sort_by == "level":
                artefacts = artefacts.order_by(Artefact.level_required).order_by(
                    Artefact.name
                )
            elif sort_by == "name":
                artefacts = artefacts.order_by(Artefact.name)
            elif sort_by == "id":
                artefacts = artefacts.order_by(Artefact.id)

            if alignment:
                artefacts = artefacts.filter_by(alignment=alignment)

            artefacts = artefacts.all()
            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        return [{"id": a.id, "name": a.name} for a in artefacts]


@api.route("/artefacts/<int:id>")
class ArtefactApiResource(Resource):
    """An item that can be restored using Materials."""

    def get(self, id):
        try:
            session = Session()
            artefact = (
                session.query(Artefact)
                .filter_by(id=id)
                .options(joinedload("materials"))
                .first()
            )
            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        if artefact is None:
            return {"error": f"No Artefact with id={id} exists."}, 404

        materials = []
        for m in artefact.materials:
            materials.append(
                {
                    "id": m.id,
                    "name": m.name,
                    "amount": session.query(Base.metadata.tables["material_artefact"])
                    .filter_by(artefact_id=id)
                    .filter_by(material_id=m.id)
                    .first()
                    .amount,
                }
            )

        return {
            "id": id,
            "name": artefact.name,
            "alignment": artefact.alignment,
            "levelRequired": artefact.level_required,
            "xp": artefact.xp,
            "img": get_image_url(id),
            "imgDamaged": get_image_url(artefact.id - 1),
            "materials": materials,
        }


__all__ = ["ArtefactList", "ArtefactApiResource"]
