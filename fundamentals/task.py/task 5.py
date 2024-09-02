# fibanocci

def is_fibo(number):

    previous=0
    current=1
    if number==0 or number==1:
        return True
    
    while(current<=number):
        
        if current==number:
            return True
        
        next=previous+current
        previous=current
        current=next
        
    return False

print(is_fibo(21))   




