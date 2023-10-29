#!/usr/bin/python3
"""states route"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """get a list of cities """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = [obj.to_dict() for obj in state.cities]
    return make_response(jsonify(cities), 200)


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """get city by id"""
    city = storage.get(City, city_id)
    return make_response(jsonify(city.to_dict()),
                         200) if city else abort(404)

