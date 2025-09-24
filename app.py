from flask import Flask
from routes.labRoutes import lab_blueprint
from datetime import timedelta
from flask_jwt_extended import JWTManager
from routes.nurseRoutes import nurse_blueprint
from routes.locationRoutes import location_blueprint
from routes.memberRoutes import members_blueprint
from routes.dependantRoutes import dependant_blueprint
from routes.bookingRoutes import booking_blueprint
from routes.allocationsRoutes import allocations_blueprint
from routes.imageRoute import image_blueprint
from routes.adminRoutes import admin_blueprint
from routes.paymentRoute import payment_blueprint
from flask_cors import CORS



# Initialize the Flask app
app = Flask(__name__)
CORS(app)
# Setup the Flask-JWT-Extended extension

app.secret_key = "9514bcfe52538f01f1e4de931fbb272f5e60b65dc6ada80080ea4ccdd4929dd2"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours= 1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours= 1)
jwt = JWTManager(app)

app.register_blueprint(lab_blueprint)
app.register_blueprint(nurse_blueprint)
app.register_blueprint(location_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(dependant_blueprint)
app.register_blueprint(booking_blueprint)
app.register_blueprint(allocations_blueprint)
app.register_blueprint(image_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(payment_blueprint)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)