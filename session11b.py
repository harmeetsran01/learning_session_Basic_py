from session11 import dish
from session11a import menu

class restaurant:
    def __init__(self,name="NA", phone="NA", email="NA", address="NA", operating_hours="NA", ratings="NA", menu=None):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.operating_hours=operating_hours
        self.ratings=ratings
        self.menu=menu

    def show(self):
        print("RESTAURNT" )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("RESTAURNT: {} | {} | {}".format (self.name,self.phone,self.email ))
        print("ADDRESS: {} | {} | {}".format (self.address,self.operating_hours,self.ratings ))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        self.menu.show()



        
        
        
        
