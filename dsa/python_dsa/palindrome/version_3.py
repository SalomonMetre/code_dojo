import re
from version_2 import is_palindome

def is_palindome_final(word:str) -> bool:
    """
    this version removes spaces and punctuation before evaluating whether the word is a palindome or not
    """
    word = re.sub(r"[.,\w]", "", word)
    return is_palindome(word)

word = "esope reste et se repose"
print(f"Is '{word}' a palindrome ? ", "yes" if is_palindome_final(word) else "no")  