num=int(input("enter num:")) #175

length=len(str(num))

original=num

total=0



while(num!=0):

    digit=num%10  # 5  7  1

    total=total+(digit**length)  #0+5**3=125 125+7**2=174   

    num=num//10      #175//10=17  17//10=1     

    length-=1         #3            2          

    

print("Disarium number" if original==total else "not disarium number")





    