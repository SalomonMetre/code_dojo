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