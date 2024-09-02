
source_word="CHICKEN"

target_word="HEN"

word_count={}#c

for w in source_word: #c                 #[OR]

    if w in word_count:#c                     #word_count[w]=source_word.count[w]

        word_count[w]+=1                      #print(word_count)

    else:
        word_count[w]=1

print(word_count)

is_kangaroo_word=True

for w in target_word:

    if w in word_count and word_count.get(w)>0:

        word_count[w]-=1
    else:
        is_kangaroo_word=False

        break
print(is_kangaroo_word)

