from db import Database

class LocationService:
    def __init__(self):
        self.db = Database()

    
    def addLocation(self, location):
        query = "INSERT INTO locations (location) VALUES (%s)"
        try:
            cursor = self.db.get_cursor()
            data = (location)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()


    def viewLocations(self):
        query = "SELECT * FROM locations"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount == 0:
                return False
            else:
                locations = cursor.fetchall()
                return locations
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()

    # function to update location
    def updateLocation(self, location_id, location):
        query = "UPDATE locations SET location = %s WHERE location_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (location, location_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()
