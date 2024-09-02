
text="ABACDDBB"

word_count={}#A:1,B:1,A:2

for char in text:#A,B,A

    if char in word_count:#A,B,A

        print(char,"first recursive character")  #A:2

        break
    else:

        word_count[char]=1 #A,B