f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\file operations\\fileprograms\\students.txt","r")

students=[]

for stud in f:

    students.append(stud.rstrip("\n"))

print(students)