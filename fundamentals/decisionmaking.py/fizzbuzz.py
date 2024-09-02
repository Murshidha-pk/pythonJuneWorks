

num=int(input("enter the number"))

if num%15==0:

    print(f"{num}-fizzbuzz")

elif num%5==0:

    print(f"{num}-buzz")

elif num%3==0:

    print(f"{num}-fizz")
else:

    print("invalid")

