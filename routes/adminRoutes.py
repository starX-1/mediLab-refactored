from flask import Blueprint, request
from controllers.adminController import AdminController

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')
admin_controller = AdminController()

@admin_blueprint.route('/register', methods=['POST'])
def registerAdmin():    
    return admin_controller.registerAdmin(request)

@admin_blueprint.route('/login', methods=['POST'])
def loginAdmin():
    return admin_controller.loginAdmin(request)