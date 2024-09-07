def tournament_max(arr:list[int]):
    if len(arr) == 1:
        return arr[0]
    
    winners = []
    for i in range(0, len(arr) - 1, 2):
        winners.append(max(arr[i], arr[i+1]))
    
    if len(arr) % 2 == 1:
        winners.append(arr[len(arr)-1])
    
    return tournament_max(winners)

def tournament_max_2(arr:list[int]):
    if len(arr) == 2:
        return arr[0], arr[1]
    
    winners = []
    for i in range(0, len(arr) - 1, 2):
        winners.append(max(arr[i], arr[i+1]))
    
    if len(arr) % 2 == 1:
        winners.append(arr[len(arr)-1])
    
    return tournament_max_2(winners)

# Example usage:
numbers = [3, 6, 2, 8, 15, 5, 9, 1, 4,13]
max_value = tournament_max(numbers)
print("The maximum value is:", max_value)

print("Top 2 largest elements : ", tournament_max_2(numbers))
