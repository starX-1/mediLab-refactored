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
            # print(e)
            return False
        finally:
            self.db.close()

    def getLabs(self):
        query = "select * from laboratories  inner join lab_tests on laboratories.lab_id = lab_tests.lab_id"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                labs = cursor.fetchall()
                return labs
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()



    def AddLabTest(self, lab_id, test_name, test_description, test_cost, test_discount, availability, more_info):
        query = "insert into lab_tests(lab_id, test_name, test_description, test_cost, test_discount, availability, more_info) values(%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id, test_name, test_description, test_cost, test_discount, availability, more_info)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()

    def viewLabTests(self, lab_id):
        query = "select * from lab_tests where lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                tests = cursor.fetchall()
                return tests
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()