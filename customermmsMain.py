from customermms import customer
print("~~~~~~~~~~~~~~~~~~~Welcome to Customer Management System~~~~~~~~~~~~~~~~~~~")

customer=customer()

while True:
    choice=int(input("1. To Add customer details.\n2. To view all data.\n0. To exit\n"))
    print()

    if choice==1:
        customer.addCustomer()
        customer.show()
        customer.store_data()

    if choice==2:
        customer.viewStoredData()
    
    if choice==0:
        break




