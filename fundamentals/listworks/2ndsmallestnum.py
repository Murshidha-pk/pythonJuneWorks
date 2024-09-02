

number=[3,2,5,7,1,9,0,10,4]

#number.sort()  #ascending order

smallest_num=number[-1]      #1 (0)

scnd_smallest=number[0]    #1 2 (1,2)

for i in number:  #1 2 3 (0,1)

    if i<scnd_smallest and i<smallest_num: #1<1 1<1,2<1 2<1,3<2 3<1 (0<0 0<1,1<2 1<0)

        scnd_smallest=smallest_num

        smallest_num=i

    elif i<scnd_smallest and i>smallest_num:  #1<1 1>1,2<1 2>1,3<2 3>2(0<1 0>1,1<2 1>0)

        scnd_smallest=i #2

print(scnd_smallest)  #2


