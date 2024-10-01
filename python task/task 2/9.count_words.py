text="tgjhojfdderplbfdweatuiowjdnbd"

word_count={}

for ch in text:

    if ch in word_count:

        word_count[ch]+=1

    else:

        word_count[ch]=1

print("word count:",word_count)

    

   

    