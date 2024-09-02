#kerala vehicle  registration number validation

#starting with kl
#2 digits
#alphabets(1 / 2)
#4digits

from re import fullmatch

#vehicle_num="KL08BN4970"

#pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
vehicle_num="KL-08-BN-4970"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")
 