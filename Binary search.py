def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore the left half
        if arr[mid] < target:
            left = mid + 1
        else:  # If target is smaller, ignore the right half
            right = mid - 1

    # Target is not present in array
    return -1

def main():
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

main()
