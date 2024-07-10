import hashlib
# To encrypt passwords

password = input("Enter Your Password: ")
print("Password is:", password)

print("Afer Encryption:",hashlib.sha256(password.encode('utf-8')).hexdigest())


password = password.encode('utf-8')

password_encrypted = hashlib.sha256(password).hexdigest()
print("password_encrypted:", password_encrypted)

