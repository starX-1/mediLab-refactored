from flask import Blueprint, request
from controllers.allocationController import AllocationController

allocation_blueprint = Blueprint('allocation', __name__, url_prefix='/allocation')
allocation_controller = AllocationController()

@allocation_blueprint.route('/allocate', methods=['POST'])
def allocate():
    return allocation_controller.allocate(request)

@allocation_blueprint.route('/viewNurseAllocations', methods=['POST'])
def viewNurseAllocations():
    return allocation_controller.viewNurseAllocations(request)

@allocation_blueprint.route('/viewAllAllocations', methods=['GET'])
def viewAllocations():
    return allocation_controller.viewAllocations()

@allocation_blueprint.route('/update', methods=['PUT'])
def updateAllocation():
    return allocation_controller.updateAllocation(request)

@allocation_blueprint.route('/delete', methods=['DELETE'])
def deleteAllocation():
    return allocation_controller.deleteAllocation(request)

@allocation_blueprint.route('/deleteNurseAllocations', methods=['DELETE'])
def deleteNurseAllocations():
    return allocation_controller.deleteNurseAllocations(request)
