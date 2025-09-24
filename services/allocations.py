from db import Database

class AllocationsService:
    def __init__(self):
        self.db = Database()

    def allocate(self, nurse_id, invoice_no ):
        query = "insert into nurse_booking_allocations (nurse_id, invoice_no) values (%s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (nurse_id, invoice_no)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def viewNurseAllocations(self, nurse_id):
        query = "select * from nurse_booking_allocations where nurse_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (nurse_id)
            cursor.execute(query, data)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def allAllocations(self):
        query = "select * from nurse_booking_allocations"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()



    def updateAllocation(self, flag, allocation_id):
        query = "update nurse_booking_allocations set flag = %s where allocation_id=%s"
        try:
            cursor = self.db.get_cursor()
            data = ( flag, allocation_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def deleteAllocation(self, allocation_id):
        query = "delete from nurse_booking_allocations where allocation_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (allocation_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def deleteNurseAllocations(self, nurse_id):
        query = "delete from nurse_booking_allocations where nurse_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (nurse_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()