from db import Database
import functions
import uuid


class MemberService:
    def __init__(self):
        self.db = Database()


    def memberRegistration(self, surname, others, gender, email, password, dob, phone, status, location_id):
        check_location_query = "SELECT * FROM locations WHERE location_id = %s"
        register_memeber_query = "INSERT INTO members (member_id, surname, others, gender, email, password, dob, phone, status, location_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor () 
            data = (location_id)
            cursor.execute(check_location_query, data)
            if cursor.rowcount == 0:
                return False
            else:
                member_id = str(uuid.uuid4())
                member_data = (member_id, surname, others, gender, email, password, dob, phone, status, location_id)
                cursor.execute(register_memeber_query, member_data)
                self.db.commit()
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def loginMember (self,email, password):
        query = "SELECT * from members WHERE email = %s"
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
            print(e)
            return False
        finally:
            self.db.close()


    def memberProfile(self, member_id):
        query = "SELECT * FROM members WHERE member_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (member_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                member = cursor.fetchone()
                return member
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()


    def updateProfile(self, member_id, surname, others, gender, email, dob, phone, status, location_id):
        query = "UPDATE members SET surname = %s, others = %s, gender = %s, email = %s,  dob = %s, phone = %s, status = %s, location_id = %s WHERE member_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (surname, others, gender, email, dob, phone, status, location_id, member_id)
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


    def getMembers(self):
        query = "SELECT * FROM members"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                members = cursor.fetchall()
                return members
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()



    

