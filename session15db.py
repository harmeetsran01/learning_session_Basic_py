class customer:
    def __init__(self,name,phone,email,age,gender):
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender

class address:
    def __init__(self, houseno, addressline, city, state,zipcode,landmark):
        self.houseno=houseno
        self.addressline=addressline
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.landmark=landmark

customer1=customer("John",999999,"example.com",77,"male")
print(vars(customer1))

