from flask import Flask
from routes.labRoutes import lab_blueprint

app = Flask(__name__)
app.register_blueprint(lab_blueprint)

if __name__ == '__main__':
    app.run(debug=True)