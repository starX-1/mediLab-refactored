from flask import Blueprint, request
from controllers.bookingController import BookingController

booking_blueprint = Blueprint('booking', __name__, url_prefix='/booking')
booking_controller = BookingController()

@booking_blueprint.route('/create', methods=['POST'])
def makeBooking():
    return booking_controller.makeBooking(request)

@booking_blueprint.route('/myBookings', methods=['POST'])
def myBookings():
    return booking_controller.myBookings(request)