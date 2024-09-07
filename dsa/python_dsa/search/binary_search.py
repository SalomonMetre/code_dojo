def binary_search(list:list[int], element:int):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return None

# my list
my_list = [1,3,5,7,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
print(binary_search(my_list,9))
