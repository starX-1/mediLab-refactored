from flask import jsonify
from services.nurses import NurseService
import functions
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt_identity,  create_refresh_token, get_jwt

class NurseController:
    def __init__(self):
        self.nurse_service = NurseService()

    @jwt_required()
    def nurseRegistration(self, request):
        data = request.get_json()
        surname = data["surname"]
        others = data["others"]
        lab_id = data["lab_id"]
        gender = data["gender"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]
        claims = get_jwt()
        role = claims.get("role")
        if role == "admin" or role == "nurse":
            hashed_password = functions.hash_password(password)
            result = self.nurse_service.nurseRegistration(surname, others, lab_id, gender, email, phone, hashed_password )

            if result:
                return jsonify({"message": "Nurse registered successfully"}), 201
            else:
                return jsonify({"message": "Nurse registration failed"}), 500
            
        else:
            return jsonify({"message": "Unauthorized access"}), 401
        


    
    def loginNurse(self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        result = self.nurse_service.loginNurse(email, password)
        if not result:
            return jsonify({"message": "Login failed"}), 401
        else:
            if "password" in result:
                del result["password"]
            role = "nurse"
            access_token = create_access_token(identity=email, fresh=True, additional_claims={"role": role})  
            refresh_token = create_refresh_token(email)
            return jsonify({"message": "Login successful", "nurse": result, "access_token":access_token, "refresh_token":refresh_token}), 200
        
    
    @jwt_required()
    def viewNurses(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized access"}), 401
        result = self.nurse_service.viewNurses(lab_id)
        if not result:
            return jsonify({"message": "No nurses found"}), 404
        else:
            for nurse in result:
                if "password" in nurse:
                    del nurse["password"]
            return jsonify({"nurses": result}), 200
        
    @jwt_required()
    def updateNurse(self, request):
        data = request.get_json()
        nurse_id = data["nurse_id"]
        surname = data["surname"]
        others = data["others"]
        lab_id = data["lab_id"]
        gender = data["gender"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]
        claims = get_jwt()
        role = claims.get("role")
        if role not in ["admin", "nurse"]:
            return jsonify({"message": "Unauthorized access"}), 401
        result = self.nurse_service.updateNurse(nurse_id, surname, others, lab_id, gender, email, phone, password)
        if result:
            return jsonify({"message": "Nurse updated successfully"}), 200
        else:
            return jsonify({"message": "Nurse update failed"}), 500
        

    def viewAllNurses(self):
        result = self.nurse_service.viewAllNurses()
        if not result:
            return jsonify({"message": "No nurses found"}), 404
        else:
            for nurse in result:
                if "password" in nurse:
                    del nurse["password"]
            return jsonify({"nurses": result}), 200
        
    @jwt_required()    
    def viewSingleNurse(self, request):
        claims = get_jwt()
        role = claims.get("role")
        if role == "admin" or role == "nurse":
            nurse_id = request.get_json()["nurse_id"] 
            result = self.nurse_service.viewSingleNurse(nurse_id)
            if not result:
                return jsonify({"message": "No nurses found"}), 404
            else:
                if "password" in result:
                    del result["password"]
                return jsonify({"nurse": result}), 200
            
        else:
            return jsonify({"message": "Unauthorized access"}), 401
        
