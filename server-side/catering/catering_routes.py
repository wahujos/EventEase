"""importing the required modules"""

from flask import Blueprint, jsonify
import requests

#create an instance of the Blueprint
catering = Blueprint("catering", __name__)

@catering.route("/catering", strict_slashes=False)
def get_catering_services():
    """
    returns all catering services
    """
    useful_data = {}
    userdata = requests.get("https://dummyjson.com/users")

    if userdata.status_code == 200:
        useful_data = userdata.json()
        users = useful_data['users']
        return jsonify({"users": users})

    return jsonify({"message": "no data found"})

@catering.route("/catering/<user_id>", strict_slashes=False)
def get_a_catering_service(user_id):
    """
    returns catering service depending on the id passed
    """
    return jsonify({"message": "returns a catering service depending on the id passed"})
