lst=[10,20,10,20,11,12,11,12,13,14]

number_dict={}
for num in lst:

    if num in number_dict:

        number_dict[num]+=1
    else:

        number_dict[num]=1

print(number_dict)

#or

number_count={num:lst.count(num)for num in lst}
print(number_count)

text=["hello"]