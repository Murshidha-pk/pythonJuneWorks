
text="ABABCDE"

word_count={}

for char in text:

    if char in word_count:

        word_count[char]+=1

        
    else:

        word_count[char]=1

print(word_count)

for k,v in word_count.items():#{'A': 2, 'B': 2, 'C': 1, 'D': 1, 'E': 1}

    if v==1:   #c,d,e                                            (k :v)

        print(k)

    