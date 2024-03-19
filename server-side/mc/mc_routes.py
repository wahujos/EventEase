from flask import Blueprint, jsonify

mc = Blueprint("mc", __name__)

@mc.route("/mc", strict_slashes=False)
def mc_home():
    """
    This function uses the get method to return all mc details
    """
    data = {
            "id": 1,
            "mc_name": "John",
            "Rate in dollars": 10000,
            "contact": "Abuja"
            }
    return jsonify(data)

@mc.route("/mc/<user_id>", strict_slashes=False)
def mc_given_id(user_id):
    """
    This function returns the mc details of a specific mc
    depending on the given id
    """
    return jsonify({"message": "returns a specific mc"})
