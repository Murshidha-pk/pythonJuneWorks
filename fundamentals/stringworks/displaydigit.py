
word="i have 2 bike and 1 car"

#print alaphabet

for ch in word:
    if ch.isalpha():
        print(ch,end=",")  


#print digit
print("\nprint digits")
for ch in word:
    if ch.isdigit():
        print(ch,end=",")
