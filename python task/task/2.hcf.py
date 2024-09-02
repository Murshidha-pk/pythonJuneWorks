num1=int(input("num1:"))  #6

num2=int(input("num2:"))  #8

min=min(num1,num2)       #6

for i in range(1,min+1):   #2

    if num1%i==0 and num2%i==0:  #6/2=0 and 8/2=0

        hcf=i  #2

print(hcf)