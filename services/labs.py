from db import Database
import functions
import uuid

# here we do the CRUD ops for the labs table

class LabService:
    def __init__(self):
        self.db = Database()

    def createLab(self, lab_name, permit_id, email, phone, password):
        query = "insert into laboratories(lab_id, lab_name, permit_id, email, phone, password) values(%s, %s, %s, %s, %s)"

        try:
            lab_id = str(uuid.uuid4())
            cursor = self.db.get_cursor()
            data = (lab_id, lab_name, permit_id, email, phone, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()
    
    def labLogin(self, email, password):
         query = "select * from laboratories where email = %s"

         try:
             cursor = self.db.get_cursor()
             data = (email)
             cursor.execute(query, data)
             if cursor.rowcount == 0:
                 return False
             else:
                 result = cursor.fetchone()
                 if functions.hash_verify(password, result["password"]):
                     return result
                 else:
                     return False
         except Exception as e:
            #  print(e)
             return False
         finally:
             self.db.close()

    def labProfile(self, lab_id):
        query = "select * from laboratories where lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                lab = cursor.fetchone()
                return lab
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()

    def updateLab(self, lab_id, lab_name, permit_id, email, phone, password):
        query = "update laboratories set lab_name = %s, permit_id = %s, email = %s, phone = %s, password = %s where lab_id = %s"
        
        try: 
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password, lab_id)
            cursor.execute(query, data)
            self.db.commit()
            if cursor.rowcount == 0:
                return False
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()