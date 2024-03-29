"""importing the required modules"""
from flask import Blueprint, jsonify
import requests

# Create an instance of the blueprint
music_band = Blueprint("music_band", __name__)

@music_band.route("/music_band", strict_slashes=False)
def get_all_bands():
    """
    This function gets all details of the music bands
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

@music_band.route("/music_band/<user_id>", strict_slashes=False)
def get_given_band(user_id):
    """
    This function gets the details of a specific band
    depending on the id given
    """
    return jsonify({"message": "Gets details of a specific band"})
