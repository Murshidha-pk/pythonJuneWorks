#read a number

number=int(input("enter number"))
previous=0
current=1
is_fibo=False
if number==0 or number==1:
    is_fibo=True
else:
    next=previous+current
    while(next<=number):
        next=previous+current 
        previous=current 
        current=next 
        if next==number:
            is_fibo=True
            break
print(is_fibo)    
     


