def counting_sort(arr):
    # Find the maximum element in the array
    maximum = max(arr)
    
    # Initialize count array with zeros
    count = [0] * (maximum + 1)
    
    # Count the occurrences of each element in the array
    for n in arr:
        count[n] += 1
    
    # Modify the count array such that each element at index i
    # stores the sum of previous counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Initialize output array
    result = [0] * len(arr)
    
    # Build the output array using the count array
    for n in arr:
        result[count[n] - 1] = n
        count[n] -= 1
    
    return result

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
