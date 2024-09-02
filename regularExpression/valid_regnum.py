from re import fullmatch

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\regularExpression\\reg_number.txt")

#KL-08-BN-4970

pattern="(KL)\\s?[0-8]{2}\\s?[A-Z]{1,2}\\s?[0-9]{4}"

for line in f:

    reg_num=line.rstrip("\n")

    matcher=fullmatch(pattern,reg_num)

    if matcher!=None:

        print(reg_num)



