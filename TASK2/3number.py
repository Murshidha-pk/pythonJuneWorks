
num1=int(input("enter number"))

num2=int(input("enter number"))

num3=int(input("enter number"))

if num1>num2 and num1>num3:

    print(f"largest num==={num1}")

elif num2>num1 and num2>num3:

    print(f"largest num==={num2}")

elif num3>num1 and num3>num2:

    print(f"largest num==={num3}")

elif num1==num2==num3:

    print("three are equal")
