#ames=set()

#print(names)

#not allowed duplicates

#elements are unorderd

#it doesnt have index position

#allow add and remove

#mutable

# names.add("kochi") #add element to a set object

# print(names)

# names.clear()#remove all elements,remain empty set
# print(names)

# names.pop() #which remove random elements
# print(names)

# names.discard("hello") #remove in set object present element
names={"hari","hello","chennai","hari","hp"}

new_names=["hp","dell","lenovo","hari"]

#names.update(new_names)

#print(names)

#union
#intrsection
#difference

# new_set=names.union(new_names)

# new_set=names.intersection(new_names)

# new_set=names.difference(new_names)

# print(new_set)

new_set=names.symmetric_difference(new_names)

print(new_set)
