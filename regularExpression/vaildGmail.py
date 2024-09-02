#validate gmailid

#starting with alphanumeric
#_.0-9
#@gmail.com

#murshidha4969@gmail.com

from re import fullmatch

gmail=input("enter gmail:")

pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")

# + match one or more 
#? optional (0nly one)(ottathavana)
# * zero or more