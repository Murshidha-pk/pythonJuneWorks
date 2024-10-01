
from re import fullmatch

text=" "

pattern="[a-zA-Z_][0-9_]*"

matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else"valid")


