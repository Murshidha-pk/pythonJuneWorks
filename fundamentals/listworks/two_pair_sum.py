numbers=[2,3,4,5]

# sum=6

pairs=[(x,y) for x in numbers for y in numbers if x+y==6 and x!=y]
        
print(pairs)







