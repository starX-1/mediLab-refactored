from flask import Blueprint, request
from controllers.allocationsController import AllocationsController

allocations_blueprint = Blueprint('allocations', __name__, url_prefix='/allocations')
allocations_controller = AllocationsController()

@allocations_blueprint.route('/allocate', methods=['POST'])
def allocate ():
    return allocations_controller.allocate(request)

@allocations_blueprint.route('/get_nurse_allocations', methods=['POST'])
def get_nurse_allocations ():
    return allocations_controller.getNurseAllocations(request)

@allocations_blueprint.route('/get_all_allocations', methods=['GET'])
def get_all_allocations ():
    return allocations_controller.allAllocations()

@allocations_blueprint.route('/update_allocation', methods=['PUT'])
def update_allocation ():
    return allocations_controller.updateAllocation(request)

@allocations_blueprint.route('/delete_allocation', methods=['DELETE'])
def delete_allocation ():
    return allocations_controller.deleteAllocation(request)

@allocations_blueprint.route('/delete_nurse_allocations', methods=['DELETE'])
def delete_nurse_allocations ():
    return allocations_controller.deleteNurseAllocations(request)



