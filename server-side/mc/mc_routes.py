from flask import Blueprint, jsonify
import requests

mc = Blueprint("mc", __name__)

@mc.route("/mc", strict_slashes=False)
def mc_home():
    """
    This function uses the get method to return all mc details
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

@mc.route("/mc/<user_id>", strict_slashes=False)
def mc_given_id(user_id):
    """
    This function returns the mc details of a specific mc
    depending on the given id
    """
    return jsonify({"message": "returns a specific mc"})
