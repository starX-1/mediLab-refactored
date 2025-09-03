from flask import Blueprint, request
from controllers.membersController import MembersController

members_blueprint = Blueprint('members', __name__, url_prefix='/members')
members_controller = MembersController()

@members_blueprint.route('/register', methods=['POST'])
def registerMember():
    return members_controller.registerMember(request)

@members_blueprint.route('/login', methods=['POST'])
def loginMember():
    return members_controller.loginMember(request)

@members_blueprint.route('/profile', methods=['POST'])
def memberProfile():
    return members_controller.memberProfile(request)

@members_blueprint.route('/update', methods=['PUT'])
def updateMember():
    return members_controller.updateMember(request)