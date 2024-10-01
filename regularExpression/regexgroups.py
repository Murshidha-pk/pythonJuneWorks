
from re import finditer

text="abc123 @k,#7LMdef"

#pattern="[abf]"    #chk either a b or f

#pattern="[a-f]"   #check for alphabets from a-----f
#pattern="[a-z]"   #check for lowercase alphabets from a-----z
# pattern="[A-Z]"   #check for uppercase alphabets from A-----Z

#pattern="[a-zA-Z]"  #chc all alphabets

#pattern="[0-9]"  #chck digits

pattern="[a-zA-Z0-9]"

# pattern="[^a-zA-Z]" #include digit ,alphbts ,spsl chrctrs

# pattern="[^0-9]"  #not include digit and include all aplphabets,chrctrs

#pattern="[^a-zA-z0-9]" #spsl chrctr

#pattern="[\s]"  #chck space

pattern="[^a-zA-Z0-9\s]"


matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())