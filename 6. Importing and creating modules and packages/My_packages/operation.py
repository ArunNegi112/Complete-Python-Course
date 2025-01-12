# Checks if a string is palindrome (returns True/False)

def is_palindrome(word):
    word = word.lower().replace(" ","")
    if word[::-1]==word[::1]:
        return True
    else :
        return False