file=open("customer.csv","r")
print(file.read())
name =input("Enter Customer Name: ")
phone =input("Enter Customer phone: ")
email =input("Enter Customer email: ")

customer_details= "{} | {} | {} |\n".format(name,phone,email)

file=open("customer.csv","a")
file.write(customer_details)
print("Customer Details are saved..")
# file.close()

# lines=file.readlines() #results the output in list format

file=open("customer.csv","r")

print(file.read())
