#validate mobile number with country code mandatory

#country code

#10 digit

#number starting with 6,7,8,9


from re import fullmatch
mobile_num=input("enter mob num:")

pattern="(91)\\s?[0-9]\\d{9}"

matcher=fullmatch(pattern,mobile_num)

print("invalid" if matcher==None else "valid")

