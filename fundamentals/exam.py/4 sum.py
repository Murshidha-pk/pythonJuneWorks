#sum of digit,do not cnsdr one
num=int(input("enter the number:"))

sum=0
while(num!=0):
    digit=num%10
    if digit!=1:
        sum=sum+digit
    num=num//10
print(sum)    