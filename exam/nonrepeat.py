numbers=[10,10,20,20,20,21,22,23]

#=>a)count

num_count={}

for num in numbers:

    if num in num_count:

        num_count[num]+=1

    else:

        num_count[num]=1
print(num_count)

#non repeating

for k,v in num_count.items():
    if v==1:

        print(k)

    





