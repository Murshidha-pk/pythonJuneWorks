# full pyramid

for row in range(0,6): #0,1,2...

    for col in range(6-row-1): #(6-0-1)=5,4,3..

        print(" ",end="") # print left space
   


    for col in range(row+1): # 0+1=1,1+1=2..
        print("*",end=" ")

    print()