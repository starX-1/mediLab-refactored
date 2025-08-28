# 🏥 MediLab API Guide

Here is a step-by-step walkthrough for creating the MediLab API.

## Step 1. Create the db.py file (Database Connection)

Here we create a class which handles the connection to the database.
It has a constructor with the properties defining the DB connection details.

💡 Note: It is advisable to use .env variables so as not to expose the DB credentials.

 1. The class has 4 important methods which are responsible for:

 2. Triggering the connection to the DB

 3. Creating a cursor to execute SQL queries

 4. Committing any change made to the DB (e.g., insert or update)

 5. Closing the connection to the DB

```python
import pymysql

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'medilab'
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                cursorclass=pymysql.cursors.DictCursor
            )
        return self.connection
    
    def get_cursor(self):
        return self.connect().cursor()
    
    def commit(self):
        return self.connect().commit()
    
    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            
```

# Step 2. Create labs.py inside the services folder

This file contains the CRUD operations for the laboratories table.
In this step, we’ll start with creating a new lab.

The class has the following responsibilities:

 1. First initialize the database connection by creating the db object 

 2. Define the SQL query to insert a new lab record.

 3. Execute the query with the provided data.
 
 4. Commit the transaction if successful.

 5. Return True if the lab was created successfully, otherwise False.

 6. Close the database connection after the operation.

 ```python
from db import Database

class LabService:
    def __init__(self):
        self.db = Database()

    def createLab(self, lab_name, permit_id, email, phone, password):
        query = "insert into laboratories(lab_name, permit_id, email, phone, password) values(%s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
```

# Step 3. Create functions.py (Helper Functions)

This file contains helper functions that handle password security using bcrypt.
We define two main functions:

1. hash_password(password)

Converts the plain password into bytes.

Generates a random salt.

Hashes the password together with the salt.

Returns the hashed password as a string.

2. hash_verify(password, hashed_password)

Converts the input password into bytes.

Compares it with the stored hashed password.

Returns True if the password matches, otherwise False.

```python

import bcrypt

def hash_password(password):
    bytes = password.encode("utf-8")   # convert the password string into bytes
    salt = bcrypt.gensalt()            # generate a random salt (with cost factor, default 12)
    hash = bcrypt.hashpw(bytes, salt)  # hash the password + salt using bcrypt

    print("Bytes ", bytes)             
    print("Salt ", salt)               
    print("Hashed password ", hash.decode())  

    return hash.decode()               # return the hashed password as a string

def hash_verify(password, hashed_password):
    bytes = password.encode('utf-8')                  
    result = bcrypt.checkpw(bytes, hashed_password.encode())  
    print(result)                                    
    return result

```
# Step 4. Create labController.py inside the controllers folder

The controller is responsible for handling business logic.
It communicates with the service layer (labs.py) and ensures that data is properly processed before being sent to the database.

In this step, the controller:

 1. Extracts data from the incoming HTTP request.

 2. Hashes the user’s password before saving.

 3. Calls the LabService to create a new lab.

 4. Returns a JSON response with an appropriate status code.

```python

from flask import jsonify
from services.labs import LabService
import functions

class LabController:
    def __init__(self):
        self.lab_service = LabService()

    def createLab(self, request):
        # extract the data from the request
        data = request.get_json()
        lab_name = data["lab_name"]
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
```

# Step 5. Create labRoutes.py inside the routes folder

The routes act as entry points to the API.
They forward incoming HTTP requests to the appropriate controller methods.

In this step, we:

 1. Create a Blueprint for lab-related routes (with the prefix /lab).

 2. Initialize the LabController.

 3. Define a POST route /lab/create which calls the controller to create a lab.

 ```python
from flask import Blueprint, request
from controllers.labController import LabController

lab_blueprint = Blueprint('lab', __name__, url_prefix='/lab')
lab_controller = LabController()

# routes which simply forward requests to controllers 
@lab_blueprint.route('/create', methods=['POST'])
def createLab():
    return lab_controller.createLab(request)
```

# Step 6. Create app.py (Main Application Entry Point)

This file is the main switch of the application.
It brings everything together and starts the Flask server.

What happens here?

 1. Import Flask and the labRoutes blueprint.

 2. Create a Flask app instance.

 3. Register the lab blueprint so routes under /lab are active.

 4. Run the application in debug mode (useful for development).

 ```python
from flask import Flask
from routes.labRoutes import lab_blueprint

app = Flask(__name__)
app.register_blueprint(lab_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
```

✅ That’s it!
Now you can run the application with:

python app.py


The API will be available at:
👉 http://127.0.0.1:5000/lab/create

🥳 Now we have created the first API for creating a lab. 🥳