def is_palindrome(word:str)->bool:
    return word == word[::-1]

word = "radar"
print(f"Is {word} a palindome ? ", "yes" if is_palindrome(word) else "no")
