from db import Database
import functions

class DependantService:
    def __init__(self):
        self.db = Database()
       
    def addDependant(self, member_id, surname, others, dob):
        check_member_query = "SELECT * FROM members WHERE member_id = %s"
        add_dependant_query = "INSERT INTO dependants (member_id, surname, others, dob) VALUES (%s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor () 
            data = (member_id)
            cursor.execute(check_member_query, data)
            if cursor.rowcount == 0:
                return False
            else:
                
                dependant_data = (member_id, surname, others, dob)
                cursor.execute(add_dependant_query, dependant_data)
                self.db.commit()
                return True
        except Exception as e:
           # print(e)
            return False
        finally:
            self.db.close()


    def viewDependants(self, member_id):
        view_dependants_query = "SELECT * FROM dependants WHERE member_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (member_id)
            cursor.execute(view_dependants_query, data)
            dependants = cursor.fetchall()
            return dependants
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def updateDependant(self, dependant_id, surname, others, dob):
        update_dependant_query = "UPDATE dependants SET surname = %s, others = %s, dob = %s WHERE dependant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (surname, others, dob, dependant_id)
            cursor.execute(update_dependant_query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def getDependantById (self, dependant_id):
        get_dependant_query = "SELECT * FROM dependants WHERE dependant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (dependant_id)
            cursor.execute(get_dependant_query, data)
            dependant = cursor.fetchone()
            return dependant
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close