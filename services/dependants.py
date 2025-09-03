from db import Database
import functions

class DependantService:
    def __init__(self):
        self.db = Database()

    def addDependant(self, member_id, surname, others, dob):
        check_member_query = "select * from members where member_id = %s"
        add_dependant_query = "insert into dependants(member_id, surname, others, dob) values(%s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (member_id)
            cursor.execute(check_member_query,data)
            if cursor.rowcount == 0:
                return False
            else:
                dependant_data = (member_id, surname, others, dob)
                cursor.execute(add_dependant_query, dependant_data)
                self.db.commit()
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
        
    def viewDependants(self, member_id):
        query = "select * from dependants where member_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (member_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                dependants = cursor.fetchall()
                return dependants
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
    
    def updateDependant(self, dependant_id, surname, others, dob):
        query = "update dependants set surname = %s, others = %s, dob = %s where dependant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (surname, others, dob, dependant_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
