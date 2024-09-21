# array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 5]

# duplicates = []  # List to store duplicate elements
# seen = []  # List to store elements we have already seen

# for element in array:
#     if element in seen and element not in duplicates:
#         duplicates.append(element)
#     else:
#         seen.append(element)

# if duplicates:
#     print("Duplicate elements:", duplicates)
# else:
#     print("No duplicate elements found.")


arr=[10,11,12,13,11,10,14,15,16,13,12]

unique=[] #10,11,12,13

duplicates=[] #11,10

for element in arr:  #10,11,12,13,11,10

    if element not in unique: #10 ,11,12,13

        unique.append(element)

    

    elif element not in duplicates: #11,10

        duplicates.append(element)
     
print("duplicates:" ,duplicates)


