numbers=[10,20,30,40,50]
print()
print(id(numbers))
print("square of numbers")

def square_of_numbers(numbers):

    print("Number before ",numbers, type(numbers),id(numbers))

    for i in range(0, len(numbers)):
        numbers[i]*=numbers[i]

    print("Number after ",numbers, type(numbers),id(numbers))
    return numbers


print(square_of_numbers(numbers))


print(id(numbers))


#hence in MVC, the Hashcode will not change, but the SVC in MVC will change as the container are updating the values
# print(numbers)

