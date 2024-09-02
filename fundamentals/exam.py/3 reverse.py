#reverse digit

num=int(input("enter the digit"))
original=num

result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10

print(f"{result} is the reverse of{original}")
    

