# importing the necessary imports
from flask import Flask
from mc.mc_routes import mc
from catering.catering_routes import catering
from equipment.equipment_routes import equipment
from music_band.band_routes import music_band


app = Flask(__name__)
app.register_blueprint(mc, url_prefix="/api")
app.register_blueprint(catering, url_prefix="/api")
app.register_blueprint(equipment, url_prefix="/api")
app.register_blueprint(music_band, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
