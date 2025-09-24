from flask import Blueprint, request
from controllers.adminContoller import AdminController

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')
admin_controller = AdminController()

# Routes which simply forward the request to the controllers
@admin_blueprint.route('/register', methods=['POST'])
def register():
    return admin_controller.registerAdmin(request)

@admin_blueprint.route('/login', methods=['POST'])
def login():
    return admin_controller.loginAdmin(request)