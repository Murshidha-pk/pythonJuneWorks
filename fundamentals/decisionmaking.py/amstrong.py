num=int(input("enter num:"))

original=num

total=0

digit_count=len(str(num))

while(num!=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print(total)

print("armstrong number" if original==total else "not armstrong")



    

