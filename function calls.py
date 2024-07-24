def fib(n, count={'val': 0}):
    count['val'] += 1 #the value is incremented each time by 1 when function is called 
    if n <= 1:
        return count['val']
    else:
        fib(n-1, count)
        fib(n-2, count)
        return count['val']

def main():
    n = int(input("Enter n: "))
    x = fib(n)
    print(x)

main()