from flask import jsonify
from services.nurses import NurseService
import functions
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token

class NurseController:
    def __init__(self):
        self.nurse_service = NurseService()

    def nurseRegistration(self, request):
        data = request.get_json()
        surname = data["surname"]
        others = data["others"]
        lab_id = data["lab_id"]
        gender = data["gender"]
        email = data["email"]
        password = data["password"]
        phone = data["phone"]

        hashed_password = functions.hash_password(password)

        result = self.nurse_service.NurseRegistration(surname, others, lab_id, gender, email, hashed_password, phone)

        if result:
            return jsonify({"message": "Nurse registered successfully"}), 201
        else:
            return jsonify({"message": "Nurse registration failed"}), 500
        
    def nurseLogin(self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]

        result = self.nurse_service.LoginNurse(email, password)

        if not result:
            return jsonify({"message": "Invalid email or password"}), 401
        else:
            access_token = create_access_token(identity=email, fresh=True)
            refresh_token = create_refresh_token(email)
            return jsonify({"message": "Login successful", "access_token": access_token, "refresh_token": refresh_token, "Nurse": result}), 200
        
    def getAllNurses(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        result = self.nurse_service.viewNurses(lab_id)
        if not result:
            return jsonify({"message": "No nurses found"}), 404
        else:
            for nurse in result:
                if "password" in nurse:
                    del nurse["password"]
            return jsonify({"message": result}), 200