# Driver had a vehivle
# Customer can book ride(s)

# class driver(self, driver_name=" ",vehicle_name=" ",vehicle_no=" ",ratings=" "):
#     pass
    
class vehicle:
    def __init__(self,reg_number=" ",brand=" ",model=" ",color="White"):
        self.reg_number=reg_number
        self.brand=brand
        self.model=model
        self.color=color

    def add_vehicle_details(self,reg_number=" ",brand=" ",model=" ",color="White"):
        print("~~~~~~~~~~~~~~~~~~~~~Enter vehicle details~~~~~~~~~~~~~~~~~~~~~")
        self.reg_number=input("Enter Registration number")
        self.brand=input("Enter Brand")
        self.model=input("Enter model")
        self.color=input("Enter color")

    def show(self):
        print("~~~~~~~~~~~~~~~~~VEHICLE~~~~~~~~~~~~~")
        print("Vehicle details: {} | {} | {} | {}".format(self.reg_number,self.brand,self.model,self.color))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


vehicle=vehicle()
vehicle.show()


# class customer(self, name, phone, email, address , gender, age):
#     pass

# class ride(self,customer,date,time,from_location,to_location,distance,fare):
#     pass

class driver:
    def __init__(self, driver_name=" ",phone=" ",email=" ",license_no=" ",ratings=" ",gender=" ",age= 18,vehicle=None):
        self.driver_name=driver_name
        self.phone=phone
        self.email=email
        self.license_no=license_no
        self.ratings=ratings
        self.gender=gender
        self.age=age
        self.vehicle=vehicle

    def add_driver_details(self):
        print("~~~~~~~~~~~~~~~~~~~~~Enter Driver details~~~~~~~~~~~~~~~~~~~~~")
        self.driver_name=input("Enter Driver's Name: ")
        self.phone=input("Enter Phone no: ")
        self.email=input("Enter Email: ")
        self.license_no=input("Enter license_no: ")
        self.ratings=input("Enter ratings: ")
        self.gender=input("Enter gender: ")
        self.age=input("Enter age: ")

        # 1 to 1 mapping:imp
        self.vehicle=vehicle
        self.vehicle.add_vehicle_details()
        
    def show(self):
        print("~~~~~~~~~~~~~~~~~DRIVER details~~~~~~~~~~~~~")
        print("{} | {} | {} | {} | {} | {} | {}".format(self.driver_name,self.phone,self.email,self.license_no,self.ratings,self.gender,self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.vehicle.show()



# ----------------------------------------class driver ended-------------------------



driver=driver()
driver.add_driver_details()
driver.show()

# ----------------------------------------class driver ended-------------------------
# ----------------------------------------class CUSTOMER STARTED-------------------------

class Customer:
    def __intit__(self,name, phone, email, address, gender, age):
        
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.gender=gender
        self.age=age

    def add_data_customer(self):
        print("Enter Custoemrs details.....\n\n")
        self.name=input("Enter Name of the customer: ")
        self.phone=input("Enter phone: ")
        self.email=input("Enter email: ")
        self.address=input("Enter Address: ")
        self.gender=input("Enter Gender: ")
        self.age=input("Enter age: ")

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Here are the Customer details:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{} | {} | {} | {} | {} | {} ".format(self.name,self.phone,self.email,self.address,self.gender,self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        

    def to_csv(self):

        





        

