#validate pancard number

#first 3 alphabets
#4th place PCAFHT
#5th alphabets
#AFZPK7190K

from re import fullmatch

pancard_num=input("enter pancard num:")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_num)

print("invalid" if matcher==None else "valid") 