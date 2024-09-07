def is_palindome(word:str) -> bool:
    while len(word) > 1:
        if word[0] != word[len(word) - 1]:
            return False
        word = word[1:len(word)-1]
    return True

word = "esoperesteetserepose"
print(f"Is {word} a palindome ? ", "yes" if is_palindome(word) else "no")