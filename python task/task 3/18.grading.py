mark=int(input("enter your mark:"))

if(mark>=80):
    print("yuor grade is A")

elif(mark>=60 and mark<=80):
    print("your grade is B")

elif(mark>=50 and mark<=60):
    print("your grade is C")

elif(mark>=45 and mark<=50 ):
    print("your grade is D")

elif(mark>=25 and mark<45 ):
    print("your grade is E")

elif(mark<25  ):
    print("you are fail")
    