
text="The quick brown fox jumps over lazy dog"



text=(text.casefold())
is_panagram=True

alphabets="abcdefghijklmnopqstuvwxyz"

for ch in alphabets:
    if text.count(ch)==0:
        is_panagram=False
        break

print(is_panagram)
