from session11 import dish
class menu:
    def __init__(self,name="NA",number_of_dishes=0,menu_dishes=[]):
        self.name=name
        self.number_of_dishes=number_of_dishes
        self.menu_dishes=menu_dishes
        print(self.menu_dishes)

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {}, {}, {}".format(self.name,self.number_of_dishes,self.menu_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("Dishes: ")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()

dishes=[dish(),dish("Dal Makhni",250,7.0),dish("ABC...")]

menu =menu("Indian",len(dishes),dishes)
menu.show()

