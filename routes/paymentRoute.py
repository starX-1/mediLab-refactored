from flask import Blueprint, request
from controllers.paymentController import PaymentController

payment_blueprint = Blueprint('payment', __name__, url_prefix='/payment')
payment_controller = PaymentController()

@payment_blueprint.route('/checkout', methods=['POST'])
def checkout():
    return payment_controller.checkout(request)