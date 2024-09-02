#gcd of (12,24)#1,2,3,4,16,12....(12)

num1=int(input("enter num:"))#4
num2=int(input("enter num:"))#8

gcd=1

for i in range(1,num1+1):        #1                     #2                   #3     #4

    if num1%i==0 and num2%i==0: #4%1==0 and 8%1==0      #4%2==0 and 8%2==0   #!=0   #4%4==0 and 8%4==0

        gcd=i                    #1                     #2                           #4

print(gcd)   #4(gcd)