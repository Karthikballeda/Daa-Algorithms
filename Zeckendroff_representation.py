def fibgen(n):
    fibl = [1, 2]
    while fibl[-1] <= n:
        fibl.append(fibl[-2] + fibl[-1])
    return fibl[:-1]

def zack(n):
    if n < 0:
        raise ValueError('Value has to be greater than zero!')
    
    fib = fibgen(n)
    rep = []
    for i in reversed(fib):
        if n >= i:
            rep.append(i)
            n -= i
    return rep

n = int(input("Enter a number: "))

if n < 0:
    print("Input number must be non-negative.")
else:
    representation = zack(n)
    print(f"The Zeckendorf representation of {n} is: {representation}")
