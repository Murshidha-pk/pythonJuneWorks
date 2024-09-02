

num1=10

num2=20

print("num1 is largest"if num1>num2 else "num2 is largest")
#return true expression if condition elsevfalse

#print("even"if num%2==0 else"odd")


year=int(input("enter year"))

result="leap year" if(year%100==0 and year%400==0 or year%100!=0 and year%4==0 ) else "not leapyear"

print(result)