number=[3,2,5,1,7,8,11,10]

largest_number=number[0] #3,5,7

scnd_largest_number=number[0]#3,5,7

for i in number: #2,5,7

    if i>largest_number and i>scnd_largest_number:#2>3and2>3,5>3and5>3,7>3and7>3

        scnd_largest_number=largest_number#5,7

        largest_number=i#5,7

        print(largest_number)#5,7

    elif i>scnd_largest_number and i<largest_number:  #5>3and5<3

        scnd_largest_number=i #5

print(f"second largest is{scnd_largest_number}") #5