from db import Database

class LocationService:
    def __init__(self):
        self.db = Database()

    def createLocation(self, location):
        query = "insert into locations(location) values(%s)"
        try:
            cursor = self.db.get_cursor()
            data = (location)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()

    def viewLocations(self):
        query = "select * from locations"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                locations = cursor.fetchall()
                return locations
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()