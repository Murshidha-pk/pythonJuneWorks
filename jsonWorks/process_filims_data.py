
from json import load
f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\jsonWorks\\filims.json")

movies=load(f)

for m in movies:

    print(m.get("title"))