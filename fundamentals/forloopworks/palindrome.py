num=int(input("enter number")) #123

result=0

original=num

while(num!=0):               #123!=0     12!=0       1!=0

    digit=num%10             #123%10=3    12%10=2     1%10=1

    result=result*10+digit   #0*10+3=3    3*10+2=32    32*10+1=321

    num=num//10              #123//10=12  12//10=1      1//10=0




print("palindrome" if result==original else "not palindrome")

















