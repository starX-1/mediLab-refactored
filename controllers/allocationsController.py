from flask import jsonify, request
from services.allocations import AllocationsService
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


class AllocationsController:
    def __init__(self):
        self.allocations_service = AllocationsService()

    @jwt_required()
    def allocate(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        invoice_no = data["invoice_no"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.allocations_service.allocate(nurse_id, invoice_no)
        if result:
            return jsonify({"message": "Nurse allocated successfully"}), 200
        else:
            return jsonify({"message": "Failed to allocate nurse"}), 500
        

    @jwt_required()
    def getNurseAllocations(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role == "admin" or role == "nurse":
            result = self.allocations_service.viewNurseAllocations(nurse_id)
            if not result:
                return jsonify({"message": "Nurse allocations not found"})
            else:
                return jsonify({"message": result}), 200
        else:
            return jsonify({"message": "Unauthorized"}), 401
        

    @jwt_required()
    def allAllocations(self ):
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401


        result = self.allocations_service.allAllocations()
        if not result:
            return jsonify({"message": "Allocations not found"}), 500
        else:
            return jsonify({"message": result}), 200
        

    @jwt_required()
    def updateAllocation(self, request):
        data = request.get_json()
        # invoice_no = data["invoice_no"]
        # nurse_id = data["nurse_id"]
        flag = data["flag"]
        allocation_id = data["allocation_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.allocations_service.updateAllocation(flag, allocation_id)
        if result:
            return jsonify({"message": "Allocation updated successfully"}), 200
        else:
            return jsonify({"message": "Failed to update allocation"}), 500
        

    @jwt_required()
    def deleteAllocation(self, request):
        data = request.get_json()
        allocation_id = data["allocation_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.allocations_service.deleteAllocation(allocation_id)
        if result:
            return jsonify({"message": "Allocation deleted successfully"}), 200
        else:
            return jsonify({"message": "Failed to delete allocation"}), 500
        

    @jwt_required()
    def deleteNurseAllocations(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.allocations_service.deleteNurseAllocations(nurse_id)
        if result:
            return jsonify({"message": "Nurse allocations deleted successfully"}), 200
        else:
            return jsonify({"message": "Failed to delete nurse allocations"}), 500