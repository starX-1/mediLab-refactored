from flask import Blueprint, request
from controllers.nurseController import NurseController

nurse_blueprint = Blueprint('nurse', __name__, url_prefix='/nurse')
nurse_controller = NurseController()

@nurse_blueprint.route('/register', methods=['POST'])
def nurseRegistration():
    return nurse_controller.nurseRegistration(request)

@nurse_blueprint.route('/login', methods=['POST'])
def loginNurse():
    return nurse_controller.loginNurse(request)

@nurse_blueprint.route('/view', methods=['GET'])
def viewNurses():
    return nurse_controller.viewNurses(request)

@nurse_blueprint.route('/update', methods=['PUT'])
def updateNurse():
    return nurse_controller.updateNurse(request)


@nurse_blueprint.route('/viewall', methods=['GET'])
def viewAllNurses():
    return nurse_controller.viewAllNurses()


@nurse_blueprint.route('/viewsingle', methods=['POST'])
def viewSingleNurse():
    return nurse_controller.viewSingleNurse(request)

