#Using constructor overloading with one constructor
"""
Code 3 objects
Dish: name, price , raitng
Menu: name, number_of_dishes, dishes
    1 menu can have many dishes ( 1 to many)
Restaurant: name, phone, email, address, operating_hours, ratings, menu
    1 Restaurant can have 1 Menu (1 to 1)

"""

class dish:
    def __init__(self,name="NA",price=0,rating=1.5):
        
        self.name=name
        self.price=price
        self.rating=rating

    def show(self):
        print()
        print("Dish: {} | {} | {}".format(self.name,self.price,self.rating))
        print()
        
dish1=dish() #default constructor
print()

dish2=dish("Dal Makhni",250,7.0)
print()

dish3=dish("ABC...")
print()

dish1.show()
dish2.show()
dish3.show()
print()
print()

#making a list of objects reference
dishes=[dish1,dish2,dish3]
"""
dishes=[dish1.show(),dish2.show(),dish3.show()] #will not work as function have no hashcode, list work on hashcode
print(dishes)
"""
for idx in range(len(dishes)):
    dishes[idx].show()



#making a list of objects
dishes=[dish(),dish("Dal Makhni",250,7.0),dish("Panner Butter Masala",450,7.0)] #will generate same ouput as above, hashcode of object(dish()) will store in index container
print(dishes[0], dishes[1], dishes[2])

#------------------------------------------------------Class Dishes ended-----------------------------------------------------


class Menu:
    def __init__(self,name="NA",number_of_dishes=0,menu_dishes=[]):
        self.name=name
        self.number_of_dishes=number_of_dishes
        self.menu_dishes=menu_dishes
        # print(self.menu_dishes)

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {}, {}, {}".format(self.name,self.number_of_dishes,self.menu_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("Dishes: ")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()

dishes=[dish(),dish("Dal Makhni",250,7.0),dish("ABC...")]

menu =Menu("Indian",len(dishes),dishes)
menu.show()


#------------------------------------------------------Class Menu ended-----------------------------------------------------

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

restaurant_1= restaurant("Basant","+919999955","basant.info@gmail.com","Subash Nagar", "9:00 to 7:00PM","6",menu=Menu("Indian",len(dishes),dishes))

restaurant_1.show()

# another way
restaurant("Basant","+919999955","basant.info@gmail.com","Subash Nagar", "9:00 to 7:00PM","6",menu=Menu("Indian",len(dishes),dishes)).show()
