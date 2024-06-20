#to make a chess board using for loop

for i in range(0,8):

    for j in range(0,8):

        # print(j%2,end=" ")

        if i % 2 == 0:
            print ( j%2 ,end="")
            
        else:
            print((j+1)%2, end="")
    print()
   
   
    # 25a1
    # 25a0

blacksquare= "\u25a1"
blackPawn="\u2659"
blackKnight="\u2658"
blackBishop="\u2657"
blackRook="\u2656"
blackQueen="\u2655"
blackKing="\u2654"



whitesquare= "\u25a0"
whitePawn="\u265F"
whiteKnight="\u265e"
whiteBishop="\u265d"
whiteRook="\u265c"
whiteQueen="\u265b"
whiteKing="\u265a"



"""
rook knight bishop Queen King bishop knight rook
"""

# print(whitesquare)


for i in range (0,8):

    for j in range(0,8):

        if i%2==0:

            if j%2==0:
                print(blacksquare,end=" ")

            else:
                print(whitesquare,end=" ")

        else:  
            if j%2==0:
                print(whitesquare,end=" ")

            else:
                print(blacksquare,end=" ")
    print()


print()
print()
print()
       
"""
rook knight bishop Queen King bishop knight rook
"""

for i in range (0,8):

    for j in range(0,8):
        if i==0:
            if j==0 or j==7:
                print(blackRook, end = " ")

            elif j==1 or j==6:
                print(blackKnight, end = " ")

            elif j==2 or j==5:
                print(blackBishop, end = " ")
        
            elif j==3:
                print(blackQueen, end = " ")

            elif j==4:
                print(blackKing, end = " ")

        if i==1:
            print(blackPawn, end = " ")

        if i==2:
            
            if j%2==0:
                print(blacksquare, end = " ")

            elif (j+1)%2==0:
                print(whitesquare, end = " ")

        if i==3:
            if j%2==0:
                print(whitesquare, end = " ")

            elif (j+1)%2==0:
                print(blacksquare, end = " ")

        if i==4:
            
            if j%2==0:
                print(blacksquare, end = " ")

            elif (j+1)%2==0:
                print(whitesquare, end = " ")

        if i==5:
            if j%2==0:
                print(whitesquare, end = " ")

            elif (j+1)%2==0:
                print(blacksquare, end = " ")

        if i==6:
            print(whitePawn, end = " ")

        if i==7:
            if j==0 or j==7:
                print(whiteRook, end = " ")

            elif j==1 or j==6:
                print(whiteKnight, end = " ")

            elif j==2 or j==5:
                print(whiteBishop, end = " ")
        
            elif j==3:
                print(whiteQueen, end = " ")

            elif j==4:
                print(whiteKing, end = " ")

    
    print()



            