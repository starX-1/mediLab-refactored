from flask import jsonify
from services.labs import LabService
import functions

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity



class LabController:
    def __init__(self):
        self.lab_service = LabService()


    def createLab(self, request):
        # extract the data from the request
        data = request.get_json()
        lab_name= data["lab_name"]
        permit_id = data["permit_id"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]

        # hash the password 
        hashed_password = functions.hash_password(password)

        # create the lab 
        result = self.lab_service.createLab(lab_name, permit_id, email, phone, hashed_password)

        if result:
            return jsonify({"message": "Lab created successfully"}), 201
        else:
            return jsonify({"message": "Lab creation failed"}), 500
    
    def labLogin(self, request):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        result = self.lab_service.labLogin(email, password)

        if not result:
            return jsonify({"message": "Login failed"}), 401
        else:
            if "password" in result:
                del result["password"]
            access_token = create_access_token(identity=email, fresh=True)
            refresh_token = create_refresh_token(email)

            return jsonify({"message": "Login successful", "access_token": access_token, "refresh_token": refresh_token, "Lab": result}), 200

    @jwt_required()
    def labProfile(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        result = self.lab_service.labProfile(lab_id)

        if not result:
            return jsonify({"message": "Lab  does not exist"}), 404
        else:
            if "password" in result:
                del result["password"]
            return jsonify({"message": result}), 200
        
    @jwt_required()
    def updateLab(self, request):
        data = request.get_json()
        lab_id = request.args.get("lab_id")
        lab_name = data["lab_name"]
        permit_id = data["permit_id"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]

        hashed_password = functions.hash_password(password)

        result = self.lab_service.updateLab(lab_id, lab_name, permit_id, email, phone, hashed_password)

        if result:
            return jsonify({"message": "Lab updated successfully"}), 200
        else:
            return jsonify({"message": "Lab update failed"}), 500
    
    def getLabs(self):
        result = self.lab_service.getLabs()
        if not result:
            return jsonify({"message": "No labs found"}), 404
        else:
            for lab in result:
                if "password" in lab:
                    del lab["password"]
            return jsonify({"message": result}), 200
        
        
    @jwt_required()
    def AddLabTest(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        test_name = data["test_name"]
        test_description = data["test_description"]
        test_cost = data["test_cost"]
        test_discount = data["test_discount"]
        availability = data["availability"]
        more_info = data["more_info"]

        result = self.lab_service.AddLabTest(lab_id, test_name, test_description, test_cost, test_discount, availability, more_info)

        if result:
            return jsonify({"message": "Test added successfully"}), 200
        else:
            return jsonify({"message": "Test addition failed"}), 500
        
    def getLabTests(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        result = self.lab_service.viewLabTests(lab_id)
        if not result:
            return jsonify({"message": "No tests found"}), 404
        else:
            return jsonify({"message": result}), 200



              
