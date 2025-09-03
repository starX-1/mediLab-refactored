from db import Database
import functions

class NurseService:
    def __init__(self):
        self.db = Database()

    def NurseRegistration(self, surname, others, lab_id, gender, email, password, phone):
        check_lab_query = "select * from laboratories where lab_id = %s"
        check_Email_query = "select * from nurses where email = %s"
        #
        reg_nurse_query = "insert into nurses(surname, others, lab_id, gender, email, password, phone) values(%s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(check_lab_query,data)
            if cursor.rowcount == 0:
                return False
            else:
                data = (email)
                cursor.execute(check_Email_query,data)
                if cursor.rowcount != 0:
                    return False
                nurse_data = (surname, others, lab_id, gender, email, password, phone)
                cursor.execute(reg_nurse_query, nurse_data)
                self.db.commit()
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()

    def LoginNurse(self, email, password):
        query = "select * from nurses where email = %s"
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
            print(e)
            return False
        finally:
            self.db.close()

    def viewNurses(self, lab_id):
        query = "select * from nurses where lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                nurses = cursor.fetchall()
                return nurses
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close() 

