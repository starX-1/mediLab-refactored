from db import Database

# here we do the CRUD ops for the labs table

class LabService:
    def __init__(self):
        self.db = Database()

    def createLab(self, lab_name, permit_id, email, phone, password):
        query = "insert into laboratories(lab_name, permit_id, email, phone, password) values(%s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()