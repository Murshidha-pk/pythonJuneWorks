
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even_count=0

odd_count=0



for i in num:

    if i %2==0 :

        num.count(i)

        even_count+=1

    elif i%2!=0:

        odd_count+=1

print(f"even count={even_count}")

print(f"odd count={odd_count}")





