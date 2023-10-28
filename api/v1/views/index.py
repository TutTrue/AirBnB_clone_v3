#!/usr/bin/python3
"""status route"""
from api.v1.views import app_views
from flask import jsonify



#@app_views.route('/status')
#def status():
#    return jsonify({"status": "OK"})
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
