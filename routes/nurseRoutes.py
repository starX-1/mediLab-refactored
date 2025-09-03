from flask import Blueprint, request
from controllers.nurseController import NurseController

nurse_blueprint = Blueprint('nurse', __name__, url_prefix='/nurse')
nurseController = NurseController()


@nurse_blueprint.route('/register', methods=['POST'])
def nurseRegistration():
    return nurseController.nurseRegistration(request)

@nurse_blueprint.route('/login', methods=['POST'])
def nurseLogin():
    return nurseController.nurseLogin(request)

@nurse_blueprint.route('/getAllNurses', methods=['POST'])
def getAllNurses():
    return nurseController.getAllNurses(request)