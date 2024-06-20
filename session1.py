# Our very first program
# Containers

# Single Value Container

# Createe Staement -> You are creating a SVC in RAM
user_name="auribises"
#user_name is a reference varible

#Read statement --> To read data inside a container
print(user_name)

print(user_name, id(user_name))

#update statement, even the address will be change --> Hash code

user_name="ishant"
print(user_name, 
id (user_name), 
type(user_name))

#address_code will state as Hash Code

#Delete Statement
del user_name
print(user_name)

#reference copy operation

promo_code1="zomato"
print(promo_code1, id(promo_code1))
promo_code2=promo_code1

print (promo_code2,id(promo_code2))

#delete of one reference

del promo_code1
#we had delete promocode 1 and gonna print promocode 2, will it work with? Hash code is deleted or not

print(promo_code2, id(promo_code2))

