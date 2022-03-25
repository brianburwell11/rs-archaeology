from flask import Blueprint, render_template


db_blueprint = Blueprint("db_blueprint", __name__, template_folder="templates")

# ------------------------------ #


@db_blueprint.route("/artefact")
def view_artefact_table():
    return render_template("artefact.html")


@db_blueprint.route("/artefact_collection_reward")
def view_artefact_collection_reward_table():
    return render_template("artefact_collection_reward.html")


@db_blueprint.route("/artefact_mystery")
def view_artefact_mystery_table():
    return render_template("artefact.html")


@db_blueprint.route("/collection")
def view_collection_table():
    return render_template("collection.html")


@db_blueprint.route("/collector")
def view_collector_table():
    return render_template("collector.html")


@db_blueprint.route("/material")
def view_material_table():
    return render_template("material.html")


@db_blueprint.route("/material_artefact")
def view_material_artefact_table():
    return render_template("material_artefact.html")


@db_blueprint.route("/reward")
def view_reward_table():
    return render_template("reward.html")


@db_blueprint.route("/reward_collection")
def view_reward_collection_table():
    return render_template("reward_collection.html")
