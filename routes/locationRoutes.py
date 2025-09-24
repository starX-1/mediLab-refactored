from flask import Blueprint, request
from controllers.locatinController import LocationController

location_blueprint = Blueprint('location', __name__, url_prefix='/location')
location_controller = LocationController()

@location_blueprint.route('/add', methods=['POST'])
def addLocation():
    return location_controller.addLocation(request)

@location_blueprint.route('/view', methods=['GET'])
def viewLocations():
    return location_controller.viewLocations()

@location_blueprint.route('/update', methods=['PUT'])
def updateLocation():
    return location_controller.updateLocation(request)