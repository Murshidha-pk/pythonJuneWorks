num1=int(input("enter num:"))   #3

num2=int(input("enter num:"))   #5

max=max(num1,num2)           #5

while (True):

    if max % num1==0  and max % num2==0:  #5%3!=0 & 5%5=0 ,6%3=0 & 6%5!=0.....#15%3=0 & 15%5=0

        lcm=max  #15

        break

    max=max+1   #5+1=6, 6+1=7,8......15

print(f"lcm = {lcm}")  #15









