from db import Database
import functions

# Here we do the CRUD operations for the laboratories table

class LabService:
    def __init__(self):
        self.db = Database()

    def createLab(self, lab_name, permit_id, email, phone, password ):
        query = "INSERT INTO laboratories (lab_name, permit_id, email, phone , password) VALUES (%s, %s, %s, %s, %s)"

        try:
            # lab_id = str(uuid.uuid4())  # generate a unique lab_id
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()


    def labLogin(self, email, password):
        query = "SELECT * FROM laboratories WHERE email = %s"
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
            # print(e)
            return False
        finally:
            self.db.close()


    def labProfile(self, lab_id):
        query = "SELECT * FROM laboratories WHERE lab_id = %s"
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
        query = "UPDATE laboratories SET lab_name = %s, permit_id = %s, email = %s, phone = %s, password = %s WHERE lab_id = %s"
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
        query = "SELECT * FROM laboratories inner join lab_test on laboratories.lab_id = lab_test.lab_id"
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
        query= "INSERT INTO lab_test (lab_id, test_name, test_description, test_cost, test_discount, availability, more_info) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
        query = "SELECT * FROM lab_test WHERE lab_id = %s"
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


    #update the lab tests
    def updateLabTest(self, lab_id, test_name, test_description, test_cost, test_discount, availability, more_info):
        query = "UPDATE lab_test SET test_name = %s, test_description = %s, test_cost = %s, test_discount = %s, availability = %s, more_info = %s WHERE lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (test_name, test_description, test_cost, test_discount, availability, more_info, lab_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close() 


    def getAllTests(self):
        query = "SELECT * FROM lab_test"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
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

    
    
    # A function that  fetches all  tests and returns total tests count in each month
    def getTestsPerMonth(self):
        query = "SELECT MONTHNAME(appiontment_date) as month, COUNT(*) as total FROM bookings GROUP BY MONTHNAME(appiontment_date)"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
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



    
            
        

    