from flask import jsonify, request
from services.allocations import AllocationService
from flask_jwt_extended import jwt_required

class AllocationController:
    def __init__(self):
        self.allocation_service = AllocationService()

    @jwt_required()
    def allocate(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        invoice_no = data["invoice_no"]

        result = self.allocation_service.allocate(nurse_id, invoice_no)

        if result:
            return jsonify({"message": "Allocation added successfully"}), 200
        else:
            return jsonify({"message": "Allocation addition failed"}), 500
    
    @jwt_required()
    def viewNurseAllocations(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        result = self.allocation_service.viewNurseAllocations(nurse_id)
        if not result:
            return jsonify({"message": "No allocations found"}), 404
        else:
            return jsonify({"message": result}), 200
        
    @jwt_required()
    def viewAllocations(self):
        result = self.allocation_service.viewAllocations()
        if not result:
            return jsonify({"message": "No allocations found"}), 404
        else:
            return jsonify({"message": result}), 200
    
    @jwt_required()
    def updateAllocation(self, request):
        data = request.get_json()
        # invoice_no = data["invoice_no"]
        # nurse_id = data["nurse_id"]
        flag = data["flag"]
        allocation_id = data["allocation_id"]
        result = self.allocation_service.updateAllocation(flag, allocation_id)

        if result:
            return jsonify({"message": "Allocation updated successfully"}), 200
        else:
            return jsonify({"message": "Allocation update failed"}), 500
        
    @jwt_required()
    def deleteAllocation(self, request):
        data = request.get_json()
        allocation_id = data["allocation_id"]
        result = self.allocation_service.deleteAllocation(allocation_id)
        if result:
            return jsonify({"message": "Allocation deleted successfully"}), 200
        else:
            return jsonify({"message": "Allocation deletion failed"}), 500
    
    @jwt_required()
    def deleteNurseAllocations(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        result = self.allocation_service.deleteNurseAllocations(nurse_id)
        if result:
            return jsonify({"message": "Nurse allocations deleted successfully"}), 200
        else:
            return jsonify({"message": "Nurse allocations deletion failed"}), 500
        