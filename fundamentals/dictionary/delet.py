student={"name":"hari","course":"datascience","place":"chennai"}

# student.pop("place")  ###remove

# print(student)

for i in student.items :

    if i=="place":

        student.pop(i)

print(student)


