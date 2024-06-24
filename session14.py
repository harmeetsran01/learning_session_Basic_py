def bubblesort(data):
    i=0
    while True:
        temp=0
        i=i+1
        if i==len(data):
                break
        if data[i]>data[i+1]:
            
            temp=data[i+1]
            data[i+1]=data[i]
            data[i]=temp

            print(data)
        
def bubble_sort(data):
    for i in range(len(data)-1):
        print("i is:", i)
        for j in range(len(data)-i-1):
            print(j, end=" ")

            if data[j] > data[j+1]:
                print("Swapping {} with {}".format(data[j], data[j+1]))
                # Swap Operation
                data[j], data[j+1] = data[j+1], data[j]
        print()
    return data




numbers=[4,1,7,9,3,2]
print(bubble_sort(numbers))


    
        # elif data[i+1]>data[i+2]:
        #     temp=data[i+2]
        #     data[i+2]=data[i+1]
        #     data[i+1]=temp

        #     print(data)