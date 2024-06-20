from session12a import Customer
print("~~~~~~~~~~~~~~~~~~~~~~~WELCOME TO CUSTOMER MANAGEMENT SYSTEM~~~~~~~~~~~~~~~~~~~~~~~")

print("1. To Add customer: ")
print("2. To View customer: ")
print("0. To Quiet: ")

choice=int(input("Enter Your Choice: "))

print("Your Choice: ", choice)
while True:
    if choice==1:
        file=open("customers.csv","a")
        customer=Customer()
        customer.add_data_customer()
        customer.show()

        data=customer.to_csv()
        file.write(data)

        print("Data is written:...",data)

    elif choice==2:
        file=open("customers.csv","r")
        lines = file.readlines()

        for line in lines:



