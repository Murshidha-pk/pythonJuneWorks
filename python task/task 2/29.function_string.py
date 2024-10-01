def str_upper_lower(str):

    upper_count=0
    lower_count=0
    
    for char in str:

        if char.isupper():

            upper_count+=1

        elif char.islower():

            lower_count+=1

    return upper_count,lower_count

str=input("enter string:")

upper_count,lower_count=str_upper_lower(str)

print("uppercase:",upper_count)

print("lowercase:",lower_count)

