def insertion_sort(arr):
    # Traverse from the second element to the last element
    for i in range(1, len(arr)):
        key = arr[i] # The element to be inserted in the sorted portion
        j = i - 1

        # Move elements of arr[0...i-1] that are greater than key to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key element at the correct position
        arr[j + 1] = key

# Example usage:
arr = [2,3,5,1,6]
insertion_sort(arr)
print("Sorted array is:", arr)
