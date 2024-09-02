arr=[0,2,3,4]

n=len(arr)

sum_of_n=n*(n+1)/2 #=>10

curr_sum=sum(arr) #9

missing_number=sum_of_n-curr_sum #10-9=1

print(missing_number) #=>1