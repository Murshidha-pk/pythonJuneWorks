numbers=[10,10,26,32,54,55,23,41,62]

#print number of objects in numbers

print(len(numbers))

#even number

for i in range(0,len(numbers)):

    if numbers[i]%2==0:

        print(numbers[i])

#total numbers

total=0

for i in range(0,len(numbers)):

    total+=numbers[i]
print(total)

#odd total

odd_total=0
for i in range(0,len(numbers)):

    if numbers[i]%2!=0:
        odd_total+=numbers[i]
print(odd_total)
