def count_down(count:int):
    if count < 0:
        print("Count cannot be negative.")
        return
    print(count)
    if count == 0:
        return
    else:
        count_down(count-1)

# test 1
count_down(5)

# test 2
count_down(-2)