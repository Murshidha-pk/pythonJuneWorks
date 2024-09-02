
#S71 19973

from re import fullmatch

passport_num=input("enter passport num:")

pattern="[A-Z]{1}[1-9]{2}[0\\s]\\d{4}[1-9]"

matcher=fullmatch(pattern,passport_num)

print("invalid" if matcher==None else "valid")