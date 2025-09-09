from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager   
from routes.labRoutes import lab_blueprint
from routes.nurseRoutes import nurse_blueprint
from routes.locationRoutes import location_blueprint
from routes.memberRoutes import members_blueprint
from routes.dependantRoutes import dependant_blueprint
from routes.bookingRoutes import booking_blueprint
from routes.allocationRoutes import allocation_blueprint
from routes.imageRoute import image_blueprint
from routes.adminRoutes import admin_blueprint

app = Flask(__name__)
app.secret_key = "dbe71efcd20bfc2a5e641e9aeba3762c032f43b98c3e3236b4fc07fb6e929c84"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=3600)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=3600)
jwt = JWTManager(app)


app.register_blueprint(lab_blueprint)
app.register_blueprint(nurse_blueprint)
app.register_blueprint(location_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(dependant_blueprint)
app.register_blueprint(booking_blueprint)
app.register_blueprint(allocation_blueprint)
app.register_blueprint(image_blueprint)
app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
    app.run(debug=True)