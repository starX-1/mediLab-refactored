import bcrypt
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


