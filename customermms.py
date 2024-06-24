
class customer:
    def addCustomer(self):
        print("Enter Custoemrs details....")
        self.name=input("Enter Name of the customer: ")
        self.phone=input("Enter phone: ")
        self.email=input("Enter email: ")
        self.address=input("Enter Address: ")
        self.gender=input("Enter Gender: ")
        self.age=input("Enter age: ")
        self.data=("Name: {},Phone: {},Email: {},Address: {},Gender: {},Age: {}\n".format(self.name,self.phone,self.email,self.address,self.gender,self.age))
        print("\n~~~~~~~~~~~~~~~~~~~Thankyou You~~~~~~~~~~~~~~~~~~~")

    def show(self):
        print("Here are the details you had entered: \n")
        print("Name: {}\nPhone: {}\nEmail: {}\nAddress: {}\nGender: {}\nAge: {}\n\n".format(self.name,self.phone,self.email,self.address,self.gender,self.age))

    def store_data(self):
        file=open("Custo.csv","a")
        file.write(self.data)

    def viewStoredData(self):
        file=open("Custo.csv","r")
        print(file.read())


        