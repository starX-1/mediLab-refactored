from flask import Blueprint, request
from controllers.labController import LabController

lab_blueprint = Blueprint('lab', __name__, url_prefix='/lab')
lab_controller = LabController()

# routes which simply forward requests to controllers 
@lab_blueprint.route('/create', methods=['POST'])
def createLab():
    return lab_controller.createLab(request)

@lab_blueprint.route('/login', methods=['POST'])
def labLogin():
    return lab_controller.labLogin(request)

@lab_blueprint.route('/profile', methods=['POST'])
def labProfile():
    return lab_controller.labProfile(request)

@lab_blueprint.route('/update', methods=['PUT'])
def updateLab():
    return lab_controller.updateLab(request)