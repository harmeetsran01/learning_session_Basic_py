#recursion



def get_max(data,length):
    if length == 1:
        return data[0]
    
    else:
        previous = get_max (data,length-1)

        current = data [length-1]

        if previous > current:
            return previous
        else:
            return current

numbers = [1,2]
max = get_max(numbers, len(numbers))

print("Max is: ",max)

# striver dsa sheet

    