from flask import jsonify
from services.members import MemberService
import functions
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

class MemberController:
    def __init__(self):
        self.member_service = MemberService()


    def memberRegistration(self, request):
        data = request.get_json()
        surname = data["surname"]
        others = data["others"]
        gender = data["gender"]
        phone = data["phone"]
        email = data["email"]
        password = data["password"]
        dob = data["dob"]
        status = data["status"]
        location_id = data["location_id"]

        hashed_password = functions.hash_password(password)

        result = self.member_service.memberRegistration(surname, others, gender, email, hashed_password, dob, phone, status, location_id)

        if result:
            return jsonify({"message": "Member registered successfully"}), 201
        else:
            return jsonify({"message": "Member registration failed"}), 500
        

    def loginMember (self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        result = self.member_service.loginMember(email, password)
        if not result:
            return jsonify({"message": "Login failed"}), 401
        else:
            if "password" in result:
                del result["password"]

            role = "member"
            access_token = create_access_token(identity=email, fresh=True, additional_claims={"role": role})  
            refresh_token = create_refresh_token(email)
            return jsonify({"message": "Login successful", "member": result, "access_token":access_token, "refresh_token":refresh_token}), 200
        

    @jwt_required()
    def memberProfile(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role == "member" or role == "admin": 
            result = self.member_service.memberProfile(member_id)
            if not result:
                return jsonify({"message": "No members found"})
            else:
                if "password" in result:
                    del result["password"]
                return jsonify({"members": result}), 200
        else:
            return jsonify({"message": "Unauthorized"}), 401
        


    @jwt_required()
    def updateProfile(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        surname = data["surname"]
        others = data["others"]
        gender = data["gender"]
        email = data["email"]
        dob = data["dob"]
        phone = data["phone"]
        status = data["status"]
        location_id = data["location_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "member":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.member_service.updateProfile(member_id, surname, others, gender, email, dob, phone, status, location_id)
        if result:
            return jsonify({"message": "Profile updated successfully"}), 200
        else:
            return jsonify({"message": "Profile update failed"}), 500


    @jwt_required()
    def getMembers(self, request):
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.member_service.getMembers()
        if not result:
            return jsonify({"message": "No members found"}), 404
        else:
            return jsonify({"members": result}), 200
        

        
