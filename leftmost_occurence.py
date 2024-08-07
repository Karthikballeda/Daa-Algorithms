def leftmost_occurrence(A, x):
    left, right = 0, len(A) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if A[mid] == x:
            result = mid
            right = mid - 1  # Move left to find the first occurrence
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

A = [1, 2, 2, 2, 3, 4, 5]
x = 5
print(leftmost_occurrence(A, x)) 
