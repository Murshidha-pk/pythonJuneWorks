mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsu0ng","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

#print all mobile name

mobile_name=[mob.get("title") for mob in mobiles]
print(mobile_name)

#print all brands

brands={mob.get("brand")for mob in mobiles} #set{} duplicates not allowed ,[] give duplicates
print(brands)

samsung=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
print(samsung)

mobile_range=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40001)]

print(mobile_range)

#costly mobile

max_price=0

for mob in mobiles:

    if mob.get("price")>max_price:

        max_price=mob.get("price")
print(max_price)

costly_mobile=[mob.get("title")for mob in mobiles if mob.get("price")==max_price]
print(costly_mobile)
#costly mob
def get_price(mob):

    return mob.get("price")

costly_mobile=max(mobiles,key=get_price)
print(costly_mobile)

#lowest mobile

def get_price(mob):
    
    return mob.get("price")
lowest_mobile=min(mobiles,key=get_price)
print(lowest_mobile)


#sorted mark 

def get_price(mob):

    return mob.get("price")

sorted_mobile=sorted(mobiles,key=get_price)

print(sorted_mobile)

#price sum

total=sum([mob.get("price")for mob in mobiles])
print(total)

#max(but not details in o/p)

max=max([mob.get("price")for mob in mobiles])
print(max)
