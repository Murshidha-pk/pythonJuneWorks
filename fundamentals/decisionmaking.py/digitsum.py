#read a number print sum of digit

#input=543
#output=12

num=int(input("enter number"))

sum=0

while(num!=0):

    digit=num%10 #4    3  5

    sum=sum+digit
    
    num=num//10

print(sum)



