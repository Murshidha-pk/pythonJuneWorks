# mobile={"name":"samsung","brand":"samsung","price":10000,"is_available":"true"}

# #offer:500

# mobile["offer"]=500
# print(mobile)

mobile={"name":"samsung","brand":"samsung","price":10000,"is_available":"true","offer":500}
print("name"in mobile)

#selling price

if "offer"in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:

    selling_price=mobile.get("price")

    print(selling_price)