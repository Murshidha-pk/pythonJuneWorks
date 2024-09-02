f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\file operations\\fileprograms\\land_slides.txt","r")

data=[]

for line in f: #kerala 2018 14

    lst=line.rstrip("\n").split(" ") #["kerala", 2018, 14]

    dict={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}

    data.append(dict)

print(data)

#death per state

death_per_state={}

for dict in data:

    state=dict.get("state")

    death_count=dict.get("death_count")

    if state in death_per_state:

        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count

print(death_per_state)

