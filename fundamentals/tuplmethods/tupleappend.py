
numbers=[1,2,[3,(100,200,300),4],5,6]         #[1,2,[3,4,(100,150,200,300)],5,6]

num=numbers[2] #[3,(100,200,300),4]

num.pop()

num.insert(1,4)

print(num) #[3, 4, (100, 200, 300)]

new1=numbers[2][2]

print(new1)  #(100, 200, 300)

l=list(new1)  #[100,200,300]

l.insert(1,150)  
            
print(l) #[100, 150, 200, 300]

tuple=tuple(l)

print(tuple) #(100, 150, 200, 300)

numbers[2][2]=tuple



print(numbers)     #[1, 2, [3, 4, (100, 150, 200, 300)], 5, 6]
