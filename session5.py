#linear search
instagram_user_name=["john.j","fionna","leo.32","ben_a"]
names=["John Jackson","Fionna Flyn","leonlin","bennethan"]

user_name=input("Enter User Name to search ")
print(user_name==instagram_user_name)
index=0

while index < len(instagram_user_name):
    if user_name==instagram_user_name[index]:

        print(instagram_user_name[index]," name is ",names[index])
        break
    index = index + 1
    
print("bye")

# print(end=" ") it will print in one line not in next line.
for i in range(0,3):
    print(i,end=" ")
    #it will return:0 1 2


