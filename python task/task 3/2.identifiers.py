from re import finditer

text="the rainy day @123*"

pattern="\S"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())