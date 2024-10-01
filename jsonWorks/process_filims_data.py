
from json import load
f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\jsonWorks\\filims.json")

movies=load(f)

for m in movies:

    print(m.get("title"))

print(len(movies))

#movie with genre drama

        
drama=[m.get("title")for m in movies if m.get("genres")=="drama"]

print(drama)