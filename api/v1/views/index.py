#!/usr/bin/python3
"""status route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """return ok if api is running"""
    return jsonify({"status": "OK"})
