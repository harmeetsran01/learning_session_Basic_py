# Food delivery app
#     customer
#     dish 
#     order

# 1 customer can place many orders
# 1 order can have many dishes



class dish:
    def __init__(self,name="NA",price=0,rating=1.5):
        
        self.name=name
        self.price=price
        self.rating=rating

    def show(self):
        
        print("Dish: {} | {} | {}".format(self.name,self.price,self.rating))
        

class order:
    def __init__(self,oid="NA",dishes=None,customer=None,total=0):
        
        self.oid=oid
        self.dishes=dishes
        self.customer=customer
        self.total=total

    def show(self):
        print()
        print("Order:\n {} | {} ".format(self.oid,self.total))
        print()

        print("Ordered Placed by")
        self.customer.show()


        print("\nOrdered Dishes")
        for dish in self.dishes:
            dish.show()

    def link_dishes(self,dishes):
        self.dishes=dishes


        self.total=0
        for dish in self.dishes:
            self.total+=dish.price

    def link_customer(self,customer):
        self.customer = customer


class customer:
    def __init__(self,name="",phone=0,email=""):
        self.name=name
        self.phone=phone
        self.email=email

    def show(self):
        print("Customer::")
        print("{} | {} | {} ".format(self.name,self.phone,self.email))

# class sort:
#     def __init__(self,data):
#         for i in range(len(data)-1):

#             for j in range(len(data)-i-1):
                

#                 if data[j].price > data[j+1].price:
#                     # print("Swapping {} with {}".format(data[j], data[j+1]))
#                     # Swap Operation
#                     data[j], data[j+1] = data[j+1], data[j]
#             print()
#         return data


dishMenu=[dish(name="Dal Makhni",price = 250, rating = 4.5),dish(name="Paneer",price = 240, rating = 4.5),dish(name="Burji",price = 270, rating = 4.5),dish(name="Anda",price=300,rating=9)]

customer1= customer(name="Rajat", phone = 91, email="dalal@example.com")
customer2= customer(name="Samay", phone = 911, email="raina@example.com")


# Hard coding: as are developer linking objects
finalorder=order(oid=1, dishes=[dishMenu[0],dishMenu[1]],customer=customer1, total=dishMenu[0].price+dishMenu[1].price)
finalorder.show()


#  or

finalorder1=order(oid=1)
finalorder1.link_customer(customer1)
finalorder1.link_dishes([dishMenu[0],dishMenu[2]])
finalorder1.show()