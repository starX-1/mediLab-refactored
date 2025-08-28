from flask import jsonify
from services.labs import LabService
import functions


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


