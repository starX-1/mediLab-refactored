from flask import jsonify, request
from services.dependants import DependantService
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


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
        claims = get_jwt
        role = claims.get("role")
        if role != "member":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.dependant_service.addDependant(member_id, surname, others, dob)
        if result:
            return jsonify({"message": "Dependant added successfully"}), 201
        else:
            return jsonify({"message": "Failed to add dependant"}), 500
        
    @jwt_required()
    def viewDependants(self, request):
        data= request.get_json()
        member_id = data["member_id"]
        claims = get_jwt()
        role = claims.get("role")
        print(role)
        if role == "member" or role == "admin":
            result = self.dependant_service.viewDependants(member_id)
            if result:
                return jsonify({"dependants": result}), 200
            else:
                return jsonify({"message": "No dependants found"}), 404
        else:
            return jsonify({"message": "Unauthorized"}), 401
        


    @jwt_required()
    def updateDependant(self, request):
        data = request.get_json()
        dependant_id = request.args.get("dependant_id")
        surname = data["surname"]
        others = data["others"]
        dob = data["dob"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "member":
            return jsonify({"message": "Unauthorized"}), 401
        
        result = self.dependant_service.updateDependant(dependant_id, surname, others, dob)
        if result:
            return jsonify({"message": "Dependant updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update dependant"}), 500
        


    @jwt_required()
    def getDependantById(self, request):
        data = request.get_json()
        dependant_id = data["dependant_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role not in ["member", "admin"]:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.dependant_service.getDependantById(dependant_id)
        if result:
            return jsonify( result), 200
        else:
            return jsonify({"message": "Dependant not found"})