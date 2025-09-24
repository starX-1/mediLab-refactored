from db import Database
import functions


class NurseService:
    def __init__(self):
        self.db = Database()

    
    def nurseRegistration(self, surname, others, lab_id, gender, email, phone, password):
        check_lab_query = "SELECT * FROM laboratories WHERE lab_id = %s"
        query = "INSERT INTO nurses (surname, others, lab_id, gender, email, phone, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.get_cursor () 
            data = (lab_id)
            cursor.execute(check_lab_query, data)
            if cursor.rowcount == 0:
                return False
            else:
                nurse_data = (surname, others, lab_id, gender, email, phone, password)
                cursor.execute(query, nurse_data)
                self.db.commit()
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def loginNurse(self, email, password):
        query = "SELECT * FROM nurses WHERE email = %s"
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


    def viewNurses(self, lab_id):
        query = "SELECT * FROM nurses WHERE lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                result = cursor.fetchall()
                for nurse in result:
                    if "password" in nurse:
                        del nurse["password"]
                return result
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()

    # update nurse
    def updateNurse(self, nurse_id, surname, others, lab_id, gender, email, phone, password):
        query = "UPDATE nurses SET surname = %s, others = %s, lab_id = %s, gender = %s, email = %s, phone = %s, password = %s WHERE nurse_id = %s"
        try:
            cursor = self.db.get_cursor()
            hashed_password = functions.hash_password(password)
            data = (surname, others, lab_id, gender, email, phone, hashed_password, nurse_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close() 


    def viewAllNurses(self):
        query = "SELECT * FROM nurses"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                result = cursor.fetchall()
                for nurse in result:
                    if "password" in nurse:
                        del nurse["password"]
                return result
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()



    def viewSingleNurse(self, nurse_id):
        query = "SELECT * FROM nurses WHERE nurse_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (nurse_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                result = cursor.fetchone()
                if "password" in result:
                    del result["password"]
                return result
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()