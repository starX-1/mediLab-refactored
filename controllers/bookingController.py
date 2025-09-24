from flask import jsonify, request
from services.booking import BookingService
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

class BookingController:
    def __init__(self):
        self.booking_service = BookingService()

    @jwt_required()
    def makeBooking(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        booked_for = data["booked_for"]
        dependant_id = None
        test_id = data["test_id"]
        appointment_date = data["appointment_date"]
        appointment_time = data["appointment_time"]
        where_taken = data["where_taken"]
        lattitude = None
        longitude = None
        lab_id = data["lab_id"]
        
        # cheCK if booked for is member or dependant
        if booked_for == "member":
            # set the dependant_id to null
            dependant_id = None

        if booked_for == "dependant":
            dependant_id = data["dependant_id"]

        # Check whether where taken is home
        if where_taken == "home":
            lattitude = data["lattitude"]
            longitude = data["longitude"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "member":
            return jsonify({"message": "Unauthorized access"}), 401

        result = self.booking_service.makeBooking(member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, lattitude, longitude, lab_id)
        if result:
            return jsonify({"message": "Booking successful"}), 201
        else:
            return jsonify({"message": "Invalid booking"}), 400
        
    @jwt_required() 
    def getMyBookings(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "member":
            return jsonify({"message": "Unauthorized access"}), 401
        result = self.booking_service.getMyBookings(member_id)
        if not result:
            return jsonify({"message": "No bookings found"}), 404

        else:
            return jsonify(result), 200
        

    @jwt_required() 
    def viewLabBookings(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized access"}), 401
        result = self.booking_service.viewLabBookings(lab_id)
        if not result:
            return jsonify({"message": "No bookings found"}), 404

        else:
            return jsonify(result), 200
        


    @jwt_required() 
    def getallBoookings(self, request):
        claims = get_jwt()
        role = claims.get("role")
        if role != "admin":
            return jsonify({"message": "Unauthorized access"}), 401
        result = self.booking_service.getallBookings()
        if not result:
            return jsonify({"message": "No bookings found"}), 404

        else:
            return jsonify(result), 200



