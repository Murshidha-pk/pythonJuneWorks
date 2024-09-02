num=int(input("enter number")) #2                      #3

pattern=0

total=0

for i in range(1,num+1):      #1,2                     #1,2,3

    pattern=pattern*10+num    #0*10+2=2,2*10+2=22      #0*10+3=3,3*10+3=33,33*10+3=333

    print(pattern)           #2,22                    #3,33,333       

    total=total+pattern
    
print(f"total={total}")

