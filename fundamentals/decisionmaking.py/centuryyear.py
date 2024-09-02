# read year from user
#print century year if year ends with two zeros
#else print non century

year=int(input("enter the year"))

if year%100==0:

    print(f"{year}century year")

else:

    print(f"{year}non century year")


