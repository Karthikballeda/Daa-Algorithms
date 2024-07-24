def fibonacci(n):
    fib_list = [0, 1]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib >= n:
            break
        fib_list.append(next_fib)
    return fib_list

def binary_search_fib(fib_list, n):
    left, right = 0, len(fib_list) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if fib_list[mid] < n:
            result = fib_list[mid]
            left = mid + 1
        else:
            right = mid - 1

    return result

def greatest_fibonacci(n):
    if n <= 0:
        return "There is no Fib number less than the n."
    
    fib_list = fibonacci(n)
    return binary_search_fib(fib_list, n)

n = 100
result = greatest_fibonacci(n)
print(f"The greatest Fibonacci number less than {n} is {result}")
