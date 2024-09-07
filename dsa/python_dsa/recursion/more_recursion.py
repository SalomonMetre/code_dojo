def sum(arr:list[int]):
    '''
    The function assumes the array has at least one element
    '''
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])

def arr_count(arr:list[int]):
    if arr == []:
        return 0
    return 1 + arr_count(arr[:-1])

def max_array(arr:list[int]):
    '''
    The function assumes the list contains at least one element
    '''
    return max_array_2(arr[-1], arr[:-1])

def max_array_2(current_max:int, arr:list[int]):
    if len(arr) == 0:
        return current_max
    new_element = arr[-1]
    current_max = new_element if new_element > current_max else current_max
    return max_array_2(current_max, arr[:-1])

def binary_search(element:int, arr:list[int]):
    low = 0
    high = len(arr) - 1
    return binary_search_2(low, element, arr, high)

def binary_search_2(low:int, element:int, arr:list[int], high:int):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        if arr[mid] < element:
            return binary_search_2(mid + 1, element, arr, high)
        else:
            return binary_search_2(low, element, arr, mid - 1)
    return None

# example
arr_test = [1,2,3,8,5]

# tests on functions
print(f"Sum of {arr_test} is : {sum(arr_test)}")
print(f"Number of elements : {arr_count(arr_test)}")
print(f"Max element in {arr_test} is : {max_array(arr_test)}")

# binary search
search_value = 8
print(f"Index of {search_value} in {arr_test} is : {binary_search(search_value, arr_test)}")
