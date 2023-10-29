#!/usr/bin/python3
"""flask app entery point"""

from os import getenv
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.url_map.strict_slashes = False

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """not found route"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown(exception):
    """teardown appcontext"""
    storage.close()


if __name__ == '__main__':
    """port and host"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)

    app.run(host=host, port=port, threaded=True)
