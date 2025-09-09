import bcrypt
import uuid

import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth


def hash_password(password):
    bytes = password.encode("utf-8")   # convert the password string into bytes
    salt = bcrypt.gensalt()            # generate a random salt (with cost factor, default 12)
    hash = bcrypt.hashpw(bytes, salt)  # hash the password + salt using bcrypt

    print("Bytes ", bytes)             # e.g., b'kenya1234'
    print("Salt ", salt)               # e.g., b'$2b$12$LyTDdwhw5GHR6ILxTSrCfu'
    print("Hashed password ", hash.decode())  # full hash string

    return hash.decode()               # return the hashed password as a string


#hash_password("kenya1234")
# $2b$12$LyTDdwhw5GHR6ILxTSrCfu69/x4xpihitQ3QZXUHOXa7YRQtg2FcO
def hash_verify(password, hashed_password):
    bytes = password.encode('utf-8')                  # convert input password to bytes
    result = bcrypt.checkpw(bytes, hashed_password.encode())  # compare with stored hash
    print(result)                                     # True or False
    return result


def checkpasswordStrength (password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def genInvoiceNumber():
    return str(uuid.uuid4())

def mpesa_payment(amount, phone, invoice_no):
        # GENERATING THE ACCESS TOKEN
        consumer_key = "oAN7tFvWXa4qJ6XWAqcjG3RZoMGsSOXA"
        consumer_secret = "J2TFUVbsnM5CEvvr"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']
        print(access_token)

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
        print(password)

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "Lab Account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        