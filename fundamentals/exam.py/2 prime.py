#prime or not
number=int(input("enter the number:"))
isprime=True
for i in range(2,number):
    if number%i==0:
        isprime=False
        break
if isprime==True:
    print("prime number")
else:
    print("not prime number")
