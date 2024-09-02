
from re import finditer
text="hellohaihellohaihellohai"

match=finditer("hai",text)

count=0

for m in match:

    print(m.start(),"==",m.group())

    count+=1

print("no:of count",count)