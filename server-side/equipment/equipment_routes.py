"""required imports"""
from flask import Blueprint, jsonify

# create an instance of the blueprint
equipment = Blueprint("equipment", __name__)

@equipment.route("/equipment", strict_slashes=False)
def get_all_equipment():
    """function returns all equipments"""
    return jsonify({"message": "returns all details of equipments"})


@equipment.route("/equipment/<user_id>", strict_slashes=False)
def get_given_equipment(user_id):
    """
    This function returns particular equipment
    linked to a particular user
    """
    return jsonify({"message": "returns equipment linked to the given id"})
