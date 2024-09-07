def open_russian_dolls(n : int)->None:
    '''
    Simulates the opening of `n` russian dolls
    '''
    if n == 1:
        print("All dolls are open")
    else:
        print(f"Opening russian dolls {n}")
        open_russian_dolls(n-1)

def get_number_dolls()->int:
    """
    Takes user input and returns it
    """
    user_input = int(input("Enter number of dolls : "))
    return user_input

open_russian_dolls(get_number_dolls())