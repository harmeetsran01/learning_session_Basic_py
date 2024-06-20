print("hello all")
a=10
b=20
c=a+b
print("Sum of ",a,"+ ",b,"is : ",c)

for i in range(0,3):
    print()

#dunder or magic varible: __ or __name__
#__name__=__main__
#print("__name__: "__main__) not working here

def square(num):
    print("num is: ",num)
    num*=num
    print("Square of num is: ",num)

number=int(input("Enter a number "))
square(number)
print("Sqaure of the number after function is: ", number)

#if gonna print has code of fucntion then i have to write: print(function_name)

