
arr=[10,11,12,13,11,10,14,15,16,13,12]

unique=[] #10,11,12,13

duplicates=[] #11,10

for element in arr:  #10,11,12,13,11,10

    if element not in unique: #10 ,11,12,13

        unique.append(element)

    

    elif element not in duplicates: #11,10

        duplicates.append(element)
     
print("duplicates:" ,duplicates)


