num=int(input("enter num:"))

original=num

total=0



for num in range(100,1000): #153
    
    length=len(str(num))  #3

    digit=num%10      #3    5
    
    exponent=digit**length #3**3   5

    total=total+exponent  #27

    num=num//10   #15  3 0

    if original==total:

        print("amstrong numbers between :",)



