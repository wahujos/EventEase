"""importing the required modules"""
from flask import Blueprint, jsonify

# Create an instance of the blueprint
music_band = Blueprint("music_band", __name__)

@music_band.route("/music_band", strict_slashes=False)
def get_all_bands():
    """
    This function gets all details of the music bands
    """
    return jsonify({"message": "Gets all details of the music bands"})

@music_band.route("/music_band/<user_id>", strict_slashes=False)
def get_given_band(user_id):
    """
    This function gets the details of a specific band
    depending on the id given
    """
    return jsonify({"message": "Gets details of a specific band"})
