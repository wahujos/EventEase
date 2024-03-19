"""importing the required modules"""

from flask import Blueprint, jsonify

#create an instance of the Blueprint
catering = Blueprint("catering", __name__)

@catering.route("/catering", strict_slashes=False)
def get_catering_services():
    """
    returns all catering services
    """
    return jsonify({"message": "returns all catering services"})

@catering.route("/catering/<user_id>", strict_slashes=False)
def get_a_catering_service(user_id):
    """
    returns catering service depending on the id passed
    """
    return jsonify({"message": "returns a catering service depending on the id passed"})
