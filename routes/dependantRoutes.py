from flask import Blueprint, request
from controllers.dependantController import DependantController

dependant_blueprint = Blueprint('dependant', __name__, url_prefix='/dependant')
dependant_controller = DependantController()

@dependant_blueprint.route('/create', methods=['POST'])
def addDependant():
    return dependant_controller.addDependant(request)

@dependant_blueprint.route('/view', methods=['POST'])
def viewDependants():
    return dependant_controller.viewDependants(request)

@dependant_blueprint.route('/update', methods=['PUT'])
def updateDependant():
    return dependant_controller.updateDependant(request)