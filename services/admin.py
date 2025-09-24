from db import Database
import functions


class AdminService:
    def __init__(self):
        self.db = Database()


    def registerAdmin(self, email, username, status, phone,password):

        query = "insert into admin (email, username, status, phone, password) values (%s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            hashed_password = functions.hash_password(password)
            data = (email, username, status, phone, hashed_password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def loginAdmin(self, email, password):
        query = "SELECT * FROM admin WHERE email = %s"

        try:
            cursor = self.db.get_cursor()
            data = (email)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                result = cursor.fetchone()
                if functions.hash_verify(password, result["password"]):
                    if "password" in result:
                        del result["password"]
                    return result
                else:
                    return False
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()




   
       
 