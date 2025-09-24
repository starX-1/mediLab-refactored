from flask import Blueprint, request
from controllers.membersController import MemberController

members_blueprint = Blueprint('members', __name__, url_prefix='/members')
members_controller = MemberController()

@members_blueprint.route('/register', methods=['POST'])
def memberRegistration():
    return members_controller.memberRegistration(request)

@members_blueprint.route('/login', methods=['POST'])
def memberLogin():
    return members_controller.loginMember(request)

@members_blueprint.route('/profile', methods=['POST'])
def memberProfile():
    return members_controller.memberProfile(request)


@members_blueprint.route('/update', methods=['PUT'])
def memberUpdate():
    return members_controller.updateProfile(request)


@members_blueprint.route('/getmembers', methods=['GET'])
def getMembers():
    return members_controller.getMembers(request)