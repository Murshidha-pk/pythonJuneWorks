

words=["hello","hai","hello","hai","hai","hi"]


#print word count
#hello:2,hai:3,hi:1

# word_set=set(words)   #{"hello","hai","hello","hai","hai","hi"}

# for w in word_set:

#     print(w,words.count(w))

word_count={}

for w in words:

    #w=hello

    if w in word_count:

        word_count[w]+=1
    else:
        word_count[w]=1

print(word_count)


