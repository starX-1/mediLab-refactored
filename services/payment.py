from db import Database
import functions

class PaymentService:
    def __init__(self):
        self.db = Database()


    def checkout(self, invoice_no, test_id, phone ):
        compute_amount_query = "select * from lab_test where test_id=%s"
        query = "insert into payments (invoice_no, total_amount) values (%s, %s)"
        try:
            cursor = self.db.get_cursor()
            data = (test_id)
            cursor.execute(compute_amount_query, data)
            if cursor.rowcount == 0:
                return False
            fetched_test = cursor.fetchone()
            amount = fetched_test["test_cost"]
            payment_data = (invoice_no, amount)
            cursor.execute(query, payment_data)
            self.db.commit()
            functions.mpesa_payment(amount, phone, invoice_no)
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




                
                
        
       