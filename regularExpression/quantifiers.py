
from re import finditer

text="af12gjhve434#@jkl&#$123"

#pattern="[a-z]{3}"
pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())



