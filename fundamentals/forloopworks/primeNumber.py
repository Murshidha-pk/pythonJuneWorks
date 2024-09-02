
#7(1,7)   prime
#11(1,11)  prime
#9(1,9,3) not prime
#27(1,3,9,27) not prime

num=int(input("enter num:"))

is_prime=True

for i in range(2,num):

    if num%i==0:

        is_prime=False

        break

print(f"{num} is prime" if is_prime==True else f"{num} not prime")