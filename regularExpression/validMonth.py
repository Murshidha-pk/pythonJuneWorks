#validate month

#01
# 02
# 09
# 10
# 12

from re import fullmatch

month="12"

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

print("invalid" if matcher==None else "valid")

#date 01,1,10,31

date="3"

pattern="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,date)

print("invalid" if matcher==None else "valid")


