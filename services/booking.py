from db import Database
import functions

class BookingService:
    def __init__(self):
        self.db = Database()


    def makeBooking(self, member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, lattitude, longitude, lab_id):
        query = "insert into bookings (member_id, booked_for, dependant_id, test_id, appiontment_date, appointment_time, where_taken, latitude, longitude, lab_id, invoice_no) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.get_cursor()
            data = (member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, lattitude, longitude, lab_id, functions.genInvoiceNumber())
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def getMyBookings(self, member_id):
        query = """
        select 
        book_id, member_id, booked_for, dependant_id, test_id, appiontment_date, 
        TIME_FORMAT(appointment_time, '%%H:%%i:%%s') as appointment_time,
        where_taken, reg_date, latitude, longitude, status, lab_id, invoice_no 
        from bookings 
        where member_id = %s
        """
        try:
            cursor = self.db.get_cursor()
            data = (member_id)
            cursor.execute(query, data)
            return cursor.fetchall()
        except Exception as e:
            #print(e)
            return False
        finally:
            self.db.close()



    def viewLabBookings(self,lab_id):
        query = """select book_id, member_id, booked_for, dependant_id, test_id, appiontment_date, 
        TIME_FORMAT(appointment_time, '%%H:%%i:%%s') as appointment_time,
        where_taken, reg_date, latitude, longitude, status, invoice_no from bookings where lab_id = %s"""
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def getallBookings(self):
        query = """select book_id, member_id, booked_for, dependant_id, test_id, appiontment_date, 
        TIME_FORMAT(appointment_time, '%H:%i:%s') as appointment_time,
        where_taken, reg_date, latitude, longitude, status, invoice_no, lab_id from bookings"""
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()