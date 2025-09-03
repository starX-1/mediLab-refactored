from flask import jsonify, request
from services.location import LocationService

class LocationController:
    def __init__(self):
        self.location_service = LocationService()

    def createLocation(self):
        data = request.get_json()
        location = data["location"]
        result = self.location_service.createLocation(location)
        if result:
            return jsonify({"message": "Location created successfully"}), 201
        else:
            return jsonify({"message": "Location creation failed"}), 500
        
    def viewLocations(self):
        result = self.location_service.viewLocations()
        if not result:
            return jsonify({"message": "No locations found"}), 404
        else:
            return jsonify({"message": result}), 200