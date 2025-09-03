from flask import jsonify, request
from services.dependants import DependantService
from flask_jwt_extended import jwt_required, get_jwt_identity

class DependantController:
    def __init__(self):
        self.dependant_service = DependantService()

    @jwt_required()
    def addDependant(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        surname = data["surname"]
        others = data["others"]
        dob = data["dob"]

        result = self.dependant_service.addDependant(member_id, surname, others, dob)

        if result:
            return jsonify({"message": "Dependant added successfully"}), 200
        else:
            return jsonify({"message": "Dependant addition failed"}), 500
    
    @jwt_required()
    def viewDependants(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        result = self.dependant_service.viewDependants(member_id)
        if not result:
            return jsonify({"message": "No dependants found"}), 404
        else:
            return jsonify({"message": result}), 200
        
    @jwt_required()
    def updateDependant(self, request):
        data = request.get_json()
        dependant_id = request.args.get("_id")
        surname = data["surname"]
        others = data["others"]
        dob = data["dob"]

        result = self.dependant_service.updateDependant(dependant_id, surname, others, dob)

        if result:
            return jsonify({"message": "Dependant updated successfully"}), 200
        else:
            return jsonify({"message": "Dependant update failed"}), 500