from db import Database
import functions

class BookingService:
    def __init__(self):
        self.db = Database()

    def makeBooking(self, member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, latitude, longitude, lab_id):
        
        query = "insert into bookings(member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, latitude, longitude, lab_id, invoice_no) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            invoice_no = functions.genInvoiceNumber()
            cursor = self.db.get_cursor()
            data = (member_id, booked_for, dependant_id, test_id, appointment_date, appointment_time, where_taken, latitude, longitude, lab_id, invoice_no)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
        
    def myBookings(self, member_id):
        query = """
        SELECT 
            book_id, member_id, booked_for, dependant_id, test_id, 
            appointment_date, 
            TIME_FORMAT(appointment_time, '%%H:%%i:%%s') as appointment_time,
            where_taken, reg_date, latitude, longitude, status, lab_id, invoice_no
        FROM bookings 
        WHERE member_id = %s
        """

        try:
            cursor = self.db.get_cursor()
            data = (member_id,)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                bookings = cursor.fetchall()
                print(bookings)
                return bookings
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()

    
    # viewing lab bookings 
    def viewLabBookings(self, lab_id):
        query = """
        SELECT 
            book_id, member_id, booked_for, dependant_id, test_id, 
            appointment_date, 
            TIME_FORMAT(appointment_time, '%%H:%%i:%%s') as appointment_time,
            where_taken, reg_date, latitude, longitude, status, lab_id, invoice_no
        FROM bookings 
        WHERE lab_id = %s
        """

        try:
            cursor = self.db.get_cursor()
            data = (lab_id,)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                bookings = cursor.fetchall()
                print(bookings)
                return bookings
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()

