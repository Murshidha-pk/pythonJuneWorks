num1=int(input("num1:"))

num2=int(input("num2:"))

try:

    result=num1/num2

    print(result)

except Exception as e:


    num2=int(input("num2:"))
    
    try:
        
        result=num1/num2
        
        print(result)

    except Exception as e:

        print(e)

finally:
    #clean up

    print("db commit")

    print("file transfer")
