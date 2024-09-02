
from json import load

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\jsonWorks\\products.json",encoding="UTF-8")

items=load(f)

#items=[{},{},,,,,,,{}]

print(len(items))

# for i in items:

#     print(i.get("title"))

    #or or 

item_title=[i.get("title")for i in items]
print(item_title)

category=[i.get("title")for i in items if i.get("category")=="jewelery"]
print(category)

#product price <100

price=[i.get("title")for i in items if i.get("price")>100]
print(price)

#range(100-150)

product_range=[i.get("id")for i in items if i.get("price")>=100 and i.get("price")<=150]
print(product_range)

#most number of ratings

def get_rating_count(dict):
    return dict.get("rating").get("count")

top_selling_product=max(items,key=get_rating_count)
print(top_selling_product)

#lowest prdct

def get_rating_count(dict):

    return dict.get("rating").get("count")

lowest_product=min(items,key=get_rating_count)
print(lowest_product)

