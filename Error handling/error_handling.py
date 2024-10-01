# error handling


num1=int(input("enter num 1:"))


num2=int(input("enter num 2:"))

try:

    result=num1/num2  # /by zero

    print("division result",result)   

except Exception as e:           #(eliyasing =>e)===(display description)

    print(e)

print("database commit")

print("file operation")

