from json import load

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\jsonWorks\\contry.json",encoding="UTF-8")

data=load(f)

print(len(data))




def fetch_country_by_name(name):

    return[c for c in data if c.get("name")==name][0]

country_data=fetch_country_by_name("Barbados")

if "regionalBlocs" in country_data:

    bloc_data=country_data.get("regionalBlocs")[0]

    if "otherNames" in bloc_data:

        print(bloc_data.get("otherNames"))

    else:
        print(country_data.get("name"))


#area

def get_area(dic):

    if "area" in dic:

        return dic.get("area")
    else:
        return 0
    
biggest_area=max(data,key=get_area)
print(biggest_area.get("name"))

    

#language with arabic

for c in data:

    for l in c.get("languages"):

        if l.get("name")=="Arabic":

            print(c.get("name"))


#country with capital



capital_summary={}

for c in data:

    name=c.get("name")

    #capital_name=c.get("capital")

    if name in capital_summary:

        capital_summary[name]+=c.get("capital")
    else:
        capital_summary[name]=c.get("capital")

print(capital_summary)

#capitals=[(k,v)for k,v in capital_summary.items()]
#print(capitals)


#all region

# all_region=[c.get("region")for c in data]
# print(all_region)

region_summary={}

for c in data:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)

    else:

        region_summary[region_name]=c.get("area",0)
print(region_summary)

value_key=[(v,k)for k,v in region_summary.items()]
print(max(value_key))

