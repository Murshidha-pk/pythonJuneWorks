
list1=[10,20,30,40,50,20,60]

list2=[10,30,70,80,60,11,99]

common_elements=[]

for element in list1:

    if element in list2:

        common_elements.append(element)

if common_elements:

    print("common elements:",common_elements)

else:
    print("no common")


