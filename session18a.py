import datetime
import hashlib
class User:
    def __init__(self,name="",phone="",email="",password="",age=0,gender="") -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.password=password
        self.age=age
        self.gender=gender
        self.creadted_on=datetime.datetime.now()

    def add_details(self):
        self.name=input("Enter Your name: ")
        self.phone=input("Enter Your Phone: ")
        self.email=input("Enter Your email: ")
        self.password=input("Enter Your password: ").encode('utf-8')
        self.password=hashlib.sha256(self.password).hexdigest()
        self.age=int(input("Enter Your age: "))
        self.gender=input("Enter Your gender: ")

# user=User()
# user.add_details()
# print(vars(user))


    