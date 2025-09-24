from flask import Blueprint, request
from controllers.bookingController import BookingController

booking_blueprint = Blueprint('booking', __name__, url_prefix='/booking')
booking_controller = BookingController()

@booking_blueprint.route('/create', methods=['POST'])
def create_booking():
    return booking_controller.makeBooking(request)

@booking_blueprint.route('/view', methods=['POST'])
def view_booking():
    return booking_controller.getMyBookings(request)


@booking_blueprint.route('/view_lab', methods=['POST'])
def view_lab_booking():
    return booking_controller.viewLabBookings(request)


@booking_blueprint.route('/view_all', methods=['GET'])
def view_all_booking():
    return booking_controller.getallBoookings(request)