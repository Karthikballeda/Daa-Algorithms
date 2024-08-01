def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example of using the generator
fib_gen = infinite_fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fib_gen))
