"""required imports"""
import requests
from flask import Blueprint, jsonify

# create an instance of the blueprint
equipment = Blueprint("equipment", __name__)

@equipment.route("/equipment", strict_slashes=False)
def get_all_equipment():
    """function returns all equipments"""

    try:
        productdata = requests.get("https://fakestoreapi.com/products")
        productdata.raise_for_status()  # Raise exception for HTTP errors (4xx, 5xx)

        products = productdata.json()
        return jsonify({"products": products})
    except requests.RequestException as e:
        # Log the error
        print("Error fetching equipment data:", e)
        return jsonify({"message": "Failed to fetch equipment data"}), 500
    


@equipment.route("/equipment/<user_id>", strict_slashes=False)
def get_given_equipment(user_id):
    """
    This function returns particular equipment
    linked to a particular user
    """
    return jsonify({"message": "returns equipment linked to the given id"})
