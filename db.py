import pymysql

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'medilab'
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                cursorclass=pymysql.cursors.DictCursor
                 )
            
        return self.connection
    
    def get_cursor(self):
        return self.connect().cursor()
    
    def commit(self):
        return self.connect().commit()

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
    
    
            