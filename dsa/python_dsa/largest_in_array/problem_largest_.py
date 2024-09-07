import random as rd

# finding the largest element
def largest(A:list):
    arr_len = len(A)
    if arr_len == 0:
        return None
    else:
        current_max = A[0]
        for i in range(1,arr_len):
            if A[i] > current_max:
                current_max = A[i]
    return current_max

# my attempt
# looking for the second largest element after finding the largest element
def two_largest(A:list):
    arr_len = len(A)
    if arr_len < 2:
        return None
    else:
        max1 = largest(A)
        max2 = A[0]
        for i in range(arr_len):
            if A[i] != max1 and A[i] > max2:
                max2 = A[i]
    return max1, max2

# elegant
# looping through elements of the array
# and comparing the current element with the two current largest
def two_largest_book(A:list):
    first, second = A[:2]
    if len(A) < 2:
        return None
    else:
        if first < second:
            first, second = second, first
        for i in range(2, len(A)):
            if A[i] > first:
                first, second = A[i], first
            elif A[i] > second:
                second = A[i]
    return first, second


arr_test = [-1,0,1,8,5,3,11]
# print(largest(arr_test))
# print(two_largest(arr_test))
print(two_largest_book(arr_test))