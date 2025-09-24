from flask import jsonify, request
from services.admin import AdminService
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt


class AdminController:
    def __init__(self):
        self.admin_service = AdminService()


    def registerAdmin(self, request):
        data = request.get_json()
        email = data["email"]
        username = data["username"]
        status = data["status"]
        phone = data["phone"]
        password = data["password"]
        result = self.admin_service.registerAdmin(email, username, status, phone, password)
        if result:
            return jsonify({"message": "Admin registered successfully"}), 200
        else:
            return jsonify({"message": "Failed to register admin"}), 500
        


    def loginAdmin(self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        result = self.admin_service.loginAdmin(email, password)
        if not result:
            return jsonify({"message": "Login failed"}), 401
        else:

            role = "admin"
            access_token = create_access_token(identity=email, fresh=True, additional_claims={"role": role})
            refresh_token = create_refresh_token(email)
            return jsonify({"message": "Login successful", "admin": result, "access_token":access_token, "refresh_token":refresh_token}), 200
        


        


       
       

