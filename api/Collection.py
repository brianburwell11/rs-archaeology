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


@api.route("/collections")
class CollectionList(Resource):
    def get(self):
        collector_id = request.args.get("collectorId", None)
        try:
            session = Session()
            if collector_id:
                collections = (
                    session.query(Collection).filter_by(collector_id=collector_id).all()
                )
            else:
                collections = session.query(Collection).all()
            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        return [{"id": c.id, "name": c.name} for c in collections]


@api.route("/collections/<int:id>")
class CollectionApiResource(Resource):
    def get(self, id):
        try:
            session = Session()
            collection = (
                session.query(Collection)
                .filter_by(id=id)
                .options(joinedload("artefacts"), joinedload("rewards"))
                .first()
            )
            if collection is None:
                session.close()
                return {"error": f"No Collection with id={id} exists."}, 404

            collector = (
                session.query(Collector).filter_by(id=collection.collector_id).first()
            )

            session.close()
        except Exception as e:
            session.close()
            return {"error": str(e)}, 500

        artefacts = []
        max_level = 1
        for a in collection.artefacts:
            artefacts.append({"id": a.id, "name": a.name})

            if a.level_required > max_level:
                max_level = a.level_required

        rewards = []
        for r in collection.rewards:
            rewards.append(
                {
                    "id": r.id,
                    "name": r.name,
                    "amount": session.query(Base.metadata.tables["reward_collection"])
                    .filter_by(collection_id=id)
                    .filter_by(reward_id=r.id)
                    .first()
                    .amount,
                }
            )

        return {
            "id": id,
            "name": collection.name,
            "collector": {"id": collector.id, "name": collector.name},
            "levelRequired": max_level,
            "artefacts": artefacts,
            "rewards": rewards,
        }


__all__ = ["CollectionList", "CollectionApiResource"]
