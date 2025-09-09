from flask import jsonify, request
from services.admin import AdminService
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt

class AdminController():
    def __init__(self):
        self.admin_service = AdminService()
    
    def registerAdmin(self, request):
        data = request.get_json()
        email = data["email"]
        username = data["username"]
        status = data["status"]
        phone = data["phone"]
        password = data["password"]
        admin = self.admin_service.registerAdmin(email, username, status, phone, password)
        if admin:
            return jsonify({"message": "Admin registered successfully"}), 201
        else:   
            return jsonify({"message": "Admin registration failed"}), 500
    
    def loginAdmin(self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        admin = self.admin_service.loginAdmin(email, password)
        if not admin:
            return jsonify({"error": "Login failed"}), 401
        else:
            if "password" in admin:
                del admin["password"]
            
            role = "admin"
            access_token = create_access_token(identity=email, additional_claims={"role": role}, fresh=True)
            refresh_token = create_refresh_token(email)


            return jsonify({"message": "Login successful", "access_token": access_token, "refresh_token": refresh_token, "Admin": admin}), 200