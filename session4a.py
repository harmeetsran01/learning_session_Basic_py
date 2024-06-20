#bitwise
# & | ^(EXOR)

num1= 10
num2=8
print("IN binary", bin(num1))
print("IN binary", bin(num2))

result1 = num1 & num2 #1000->8
result2= num1 | num2 #1010->10
result3= num1 ^ num2 #0010->2

print(result1)
print(result2)
print(result3)

#Shift operator
#>> , <<

num1=8
num2=2

#in left shift
#the right side will divide by the num with base 2(as binary as base 2)
#suppose number is 3, means 2^3 then divide to left side

#and in right shift
#the right side is multiplied, means 2^3 then multiplied with left side



