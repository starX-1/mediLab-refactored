from flask import Blueprint, request
from controllers.labController import LabController


lab_blueprint = Blueprint('lab', __name__, url_prefix='/lab')
lab_controller = LabController()

# Routes which simply forward the request to the controllers

@lab_blueprint.route('/create', methods=['POST'])
def create_lab():
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

@lab_blueprint.route('/getLabs', methods=['GET'])
def getLabs():
    return lab_controller.getLabs()

@lab_blueprint.route('/add_test', methods=['POST'])
def AdLabTest():
    return lab_controller.AddLabTest(request)

@lab_blueprint.route('/get_tests', methods=['POST'])
def viewLabTests():
    return lab_controller.viewLabTests(request)

@lab_blueprint.route('/updatetest', methods=['PUT'])
def updateLabTest():
    return lab_controller.updateLabTest(request)



@lab_blueprint.route('/get_all_tests', methods=['GET'])
def getAllTests():
    return lab_controller.getAllTests()


@lab_blueprint.route('/get_tests_per_month', methods=['GET'])
def getTestsPerMonth():
    return lab_controller.getTestsPerMonth()



