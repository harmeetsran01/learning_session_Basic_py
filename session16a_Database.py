# Database OOPS
from session16 import Customer
import mysql.connector as db

class Database:
    def __init__(self):
        self.connection = db.connect(user="root",password = "pcte", host = "127.0.0.1",database ="aurobises")


        print("Database connection created!")

        self.cursor = self.connection.cursor()
        print("Database cursor created!")

    # insert/upadte/delete in db 
    def write(self,sql):
        print("Database SQL statement: ",sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("Data sql statement executed...")

    def read(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result
    
    
        