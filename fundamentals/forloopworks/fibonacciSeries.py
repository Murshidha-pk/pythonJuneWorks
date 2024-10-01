#fibanocci series


def next__fibo_num(number:int):

    previous=0
    current=1
    next=previous+current

    while(next <= number):
        next=previous+current
        previous=current
        current=next

    return next

print(next__fibo_num(5))
print(next__fibo_num(13))


        

