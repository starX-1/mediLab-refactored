from flask import jsonify, request
from services.booking import BookingService

from flask_jwt_extended import jwt_required, get_jwt_identity

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
        latitide = None
        longitude = None
        lab_id = data["lab_id"]

        # check whether booked for is member or dependant
        if booked_for == "member":
            # set the dependant_id to null
            dependant_id = None
        if booked_for == "dependant":
            dependant_id = data["dependant_id"]
        # check whether where_taken is home
        if where_taken == "home":
            latitide = data["latitude"]
            longitude = data["longitude"]

        result = self.booking_service.makeBooking(member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, latitide, longitude, lab_id)

        if result:
            return jsonify({"message": "Booking successful"}), 200
        else:
            return jsonify({"message": "Invalid booking"}), 400
        
    @jwt_required()
    def myBookings(self, request):
        data = request.get_json()
        member_id = data["member_id"]
        result = self.booking_service.myBookings(member_id)

        if not result:
            return jsonify({"message": "No bookings found"}), 404
        else:
            return jsonify({"message": result}), 200
        
    @jwt_required()
    def viewLabBookings(self, request):
        data = request.get_json()
        lab_id = data["lab_id"]
        result = self.booking_service.viewLabBookings(lab_id)

        if not result:
            return jsonify({"message": "No bookings found"}), 404
        else:
            return jsonify({"message": result}), 200


