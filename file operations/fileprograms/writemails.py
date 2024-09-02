email_ids=[

    "ram@gmail.com",
    "sam@gmail.com",
    "bindu@gmail.com",
    "ramu@gmail.com",
    "raman@gmail.com",
]

f=open("C:\\Users\\ttnou\\OneDrive\\Desktop\\PythonJunWrk\\file operations\\fileprograms\\email_id.txt","w")

for email in email_ids:

    f.write(email+"\n")