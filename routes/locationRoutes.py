from flask import Blueprint, request
from controllers.locationController import LocationController

location_blueprint = Blueprint('location', __name__, url_prefix='/location')
location_controller = LocationController()

@location_blueprint.route('/create', methods=['POST'])
def createLocation():
    return location_controller.createLocation()

@location_blueprint.route('/view', methods=['GET'])
def viewLocations():
    return location_controller.viewLocations()