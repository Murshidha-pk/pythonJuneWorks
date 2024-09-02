from re import fullmatch

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\regularExpression\\domain.text")

pattern="[\w\W]+\\.com"

for line in f:

    domain=line.rstrip("\n")

    #print(domain)
    
    matcher=fullmatch(pattern,domain)

    if matcher!=None:

        print(domain)





