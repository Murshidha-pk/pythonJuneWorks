# percentage = 90
#   grade A
#  percentage in between 80-90 
# grade B
# percentage in between 70-80 
# grade C 
# percentage less than 70 
# fail 
percentage=int(input("enter your mark in percentage:"))

if(percentage==90):
    print("yuor grade is A")

elif(percentage>=80 and percentage<=90):
    print("your grade is B")

elif(percentage>=70 and percentage<=80):
    print("your grade is C")

elif(percentage<=70):
    print("fail")
    