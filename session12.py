def square(num=5):
    return num * num

print(square())
print(square(9))
print(square(num=6))

# def add(num=7,num1):  #This will return a error, because default value is in left side not right side
#     return num + num1 #Hence this will not work here

# def add(num,num1=7):  #where we have to define one default value, which will be most right part
#     return num + num1

def addd(num,num2, num1=10):
    return num2

print(addd(2,3))



