class Customer:
    def __init__(self,name="",phone=int,email="",age=int,gender=""):
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender

        

    def add_details(self):
        self.name=input("Enter Name: ")
        self.phone=int(input("Enter Phone: "))
        self.email=input("Enter email: ")
        self.age=int(input("Enter age: "))
        self.gender=input("Enter Gender: ")

class address:
    def __init__(self, houseno, addressline, city, state,zipcode,landmark):
        self.houseno=houseno
        self.addressline=addressline
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.landmark=landmark

customer1=Customer("John",999999,"example.com",77,"male")
# print(vars(customer1))

