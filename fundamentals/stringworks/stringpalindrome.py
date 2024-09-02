# create a function is_palindrome(word)return true if word is palindromic srting
#else return false

def is_palindrome(word):
    reversed_str=word[::-1]

    return word==reversed_str




print(is_palindrome("malayalam"))



