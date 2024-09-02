#find smallest number
number=[3,2,5,7,1,8,9,6]

smallest_number=number[0]

for i in number:

    if i<smallest_number:

        smallest_number=i

print(smallest_number)