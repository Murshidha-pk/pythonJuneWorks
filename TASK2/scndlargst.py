num1=int(input("enter number"))

num2=int(input("enter number"))

num3=int(input("enter number"))

if num1>num2 and num1>num3:

    if num2>num3:

        print(f"second largest---{num2}")

    else:

        print(f"num3={num3}")

elif num2>num1 and num2>num3:

    if num1>num3:

        print(f"num1--{num1}")

    else:

        print(f"num3--{num3}")

elif num3>num1 and num3>num2:

    if num2>num1:

        print(f"num2--{num2}")

    else:

        print(f"num1--{num1}")