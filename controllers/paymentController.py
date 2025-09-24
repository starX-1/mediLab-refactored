from flask import jsonify, request
from services.payment import PaymentService
import functions
class PaymentController:
    def __init__(self):
        self.payment_service = PaymentService()

    def checkout(self, request):
        data = request.get_json()
        invoice_no = data["invoice_no"]
        test_id = data["test_id"]
        phone = data["phone"]
        result = self.payment_service.checkout(invoice_no, test_id, phone)
        if result:
            return jsonify({"message": "Payment successful"}), 200
        else:
            return jsonify({"message": "Payment failed"}), 500
        
        


           