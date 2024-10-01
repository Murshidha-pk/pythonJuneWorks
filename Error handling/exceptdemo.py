num1=int(input("num1")) #int  10

num2=int(input("num2"))  #str  20  1020

try:

    result=num1+num2

    print(result)

except Exception as e:

    result=str(num1)+str(num2)

    print(result)



print("db commit")