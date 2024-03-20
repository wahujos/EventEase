"""importing the required modules"""

from flask import Blueprint, jsonify
import requests

#create an instance of the Blueprint
catering = Blueprint("catering", __name__)

@catering.route("/catering", strict_slashes=False)
def get_catering_services():
    """
    Returns all catering services
    """
    try:
        userdata = requests.get("https://dummyjson.com/users")
        userdata.raise_for_status()  # Raise exception for HTTP errors (4xx, 5xx)

        useful_data = userdata.json()
        users = useful_data.get('users', [])
        return jsonify({"users": users})
    except requests.RequestException as e:
        # Log the error
        print("Error fetching catering data:", e)
        return jsonify({"message": "Failed to fetch catering data"}), 500  # Internal Server Error

@catering.route("/catering/<user_id>", strict_slashes=False)
def get_a_catering_service(user_id):
    """
    returns catering service depending on the id passed
    """
    return jsonify({"message": "returns a catering service depending on the id passed"})
