numbers=[10,20,30,40,50]
print(numbers,type(numbers),id(numbers))
print(numbers[1],type(numbers[1]),id(numbers[1]))

#REFERENCE COPY OPERATION -> Copy the hashcode
my_numbers=numbers

print(my_numbers,type(my_numbers),id(my_numbers))

numbers[2]=1122

print(my_numbers[2],type(my_numbers[2]),id(my_numbers[2]))
print(numbers[2],type(numbers[2]),id(numbers[2]))

#Hashing is use by SET and dictionary, as it is unordered due to hashing 


#DICTIONARY -
#The final and mos tomportant and mostly used container in Computer
friends={"jj":"John","hh":"Harvey","mm":"michael"}
print(friends)







# Hashing is a way of converting data into a number or string that represents the original data in a compact and unambiguous way. In Python, there are several ways to hash data, including using built-in functions and external libraries.

# 1. Hashing using built-in functions:

# a. The hash() function in Python takes a Python object as input and returns a hash value for it. The hash value is an integer that represents the object's identity.

# Example:

# ```
# str1 = "Hello, world!"
# hash_value = hash(str1)
# print(hash_value)
# ```

# Output:

# ```
# 2377904610399053805
# ```

# b. The hashlib module in Python provides a set of secure hash functions that can be used to generate hash values for data. The hashlib module supports various hash functions such as MD5, SHA1, SHA256, SHA384, and SHA512.

# Example:

# ```
# import hashlib

# str1 = "Hello, world!"
# hash_object = hashlib.sha256(str1.encode())
# hex_dig = hash_object.hexdigest()
# print(hex_dig)
# ```

# Output:

# ```
# '133d22e3885f0fb880da9dc6c7bfa3fca28ab46349f443c715f6c4ff63f27ddf'
# ```

# 2. Hashing using external libraries:

# a. The bcrypt library is a popular Python library used for generating password hashes. It uses the Blowfish encryption algorithm to create the hashes, making them difficult to crack.

# Example:

# ```
# import bcrypt

# password = b"password" # 'b' before string start indicates it as byte string
# salt = bcrypt.gensalt()
# hashed_password = bcrypt.hashpw(password, salt)
# print(hashed_password)
# ```

# Output:

# ```
# b'$2b$12$4qmmhgB9Euxj3GtSpl3HuubIxhX./OZS5des8fr1N6JvLl2fiEE5.'
# ```

# b. The pyhash library is a Python wrapper for the non-cryptographic hash functions of the CityHash family. It provides fast and efficient hash functions for hash tables, dictionaries, and other data structures.

# Example:

# ```
# import pyhash

# hasher = pyhash.city_32()
# hash_value = hasher("Hello, world!")
# print(hash_value)
# ```

# Output:

# ```
# 172746518




