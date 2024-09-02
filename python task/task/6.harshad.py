num=int(input("enter num:"))

length=len(str(num))

original=num

temp=num

total=0

for i in range(1,num+1):

    digit=num%10

    total=total+digit

    num=num//10

result=temp % total

print("harshad number"if result==0 else "not harshad")







