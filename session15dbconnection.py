import mysql.connector as db
from session15db import Customer


customer=Customer()
customer.add_details()

username="root"
password="pcte"

host="127.0.0.1"
database="aurobises"
# 1.Creating Connection 
connection=db.connect(username=username,password=password,host=host,database=database)
# connection=db.connect(username="root",password="pcte",host="127.0.0.1",database="aurobises")
print("connection created")
print(connection)

# 2.Create SQL statement
sql="INSERT INTO customer1 values(null,'{}',{},'{}',{},'{}')".format(customer.name,customer.phone,customer.email,customer.age,customer.gender)


# 3.Obtaining Cursor -> Perform CRUD operatios with MYSQL
cursor=connection.cursor()

# 4.Execute SQL COmmand
cursor.execute(sql)

# 5.Commit to write operations
connection.commit()

print("done")