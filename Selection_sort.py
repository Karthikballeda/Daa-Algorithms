def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the min is the first element
        min_idx = i
        # Iterate over the array to find the smallest element
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
