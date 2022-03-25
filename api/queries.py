from sys import path

from ariadne import ObjectType

# from sqlalchemy.orm import joinedload

from .third_party import *

path.insert(0, "..")
from db import Base
from db import *


query_type = ObjectType("Query")
material_type = ObjectType("Material")
artefact_type = ObjectType("Artefact")
material_amount_type = ObjectType("MaterialAmount")
collection_type

BINDABLES = [query_type, material_type, artefact_type, material_amount_type]

# ---------- #


@material_type.field("price")
def resolve_price(obj, info):
    return get_ge_value(obj.id)


@material_amount_type.field("img")
@artefact_type.field("img")
@material_type.field("img")
def resolve_img(obj, info):
    return get_image_url(obj.id)


@artefact_type.field("imgDamaged")
def resolve_imgDamaged(obj, info):
    return get_image_url(obj.id - 1)


# --- #


@query_type.field("MaterialList")
def material_list_resolver(obj, info, alignment=None):
    session = Session()
    try:
        materials = session.query(Material)
        if alignment is not None:
            materials = materials.filter_by(alignment=alignment.title())
        materials = materials.all()
    except:
        session.close()
        return []
    session.close()
    return materials


@query_type.field("Material")
def material_resolver(obj, info, id):
    session = Session()
    try:
        material = session.query(Material).filter_by(id=id).first()
    except:
        session.close()
    session.close()

    return {"id": material.id, "name": material.name, "alignment": material.alignment}


@query_type.field("Artefact")
def artefact_resolver(obj, info, id):
    artefact_materials = []

    session = Session()
    try:
        artefact = session.query(Artefact).filter_by(id=id).first()
        for material in artefact.materials:
            artefact_materials.append(
                {
                    "amount": session.query(Base.metadata.tables["material_artefact"])
                    .filter_by(artefact_id=artefact.id)
                    .filter_by(material_id=material.id)
                    .first()
                    .amount,
                    "id": material.id,
                    "name": material.name,
                    "alignment": material.alignment,
                    "price": get_ge_value(material.id),
                }
            )
    except:
        session.close()
    session.close()

    print(artefact_materials)
    return {
        "id": id,
        "name": artefact.name,
        "alignment": artefact.alignment,
        "levelRequired": artefact.level_required,
        "xp": artefact.xp,
        "materials": artefact_materials,
    }
