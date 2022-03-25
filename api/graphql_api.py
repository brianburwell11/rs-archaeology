from os.path import dirname, join, realpath

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import Blueprint, request, jsonify

from .queries import *


graphql_blueprint = Blueprint("graphql", __name__)

type_defs = load_schema_from_path(join(dirname(realpath(__file__)), "schema.graphql"))
schema = make_executable_schema(type_defs, *BINDABLES, snake_case_fallback_resolvers)

# ---------- #


@graphql_blueprint.route("/", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@graphql_blueprint.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request)
    status_code = 200 if success else 400
    return jsonify(result), status_code
