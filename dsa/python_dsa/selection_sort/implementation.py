def findSmallest(arr:list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selection_sort(arr:list):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

# array example
arr_example = [5, 3, 6, 2, 10]
print(f"The sorted version of {arr_example} is : {selection_sort(arr_example)}")