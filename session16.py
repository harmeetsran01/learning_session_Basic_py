import datetime

# create table customer( cid int primary key auto_increment,
#                       name varchar(20),
#                       phone int,
#                       email varchar(20),
#                       age int,
#                       gender varchar(20),
#                       created_on datetime
#                     );

# Customer Object: name , phone, email, age , gender, created_on

class Customer:
    def __init__(self,cid=int,name="",phone="",email="",age="",gender=""):
        self.cid=cid
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()

    def add_details(self):
        self.name=input("Enter name: ")
        self.phone=input("Enter Phone: ")
        self.email=input("Enter Email: ")
        self.age=input("Enter age: ")
        self.gender=input("Enter gender: ")

    def show(self):
        print("{} | {} | {} | {} | {} | {}".format(self.name,self.phone,self.email,self.age,self.gender,self.created_on))

print(vars(Customer))
