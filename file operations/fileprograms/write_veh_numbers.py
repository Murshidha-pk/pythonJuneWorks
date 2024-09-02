vehicle_numbers=["kl5614","kl5486","kl256","kl256"]

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\file operations\\fileprograms\\vehiclenumbers.txt","w")

for num in vehicle_numbers:
    
    f.write(num+"\n")