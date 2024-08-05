def divide_without_operator(a, b):
    if b == 0:
     raise ValueError("Cannot divide by zero")

    quotient = 0
    remainder = a

    while remainder >= b:
        remainder -= b
        quotient += 1

    return quotient, remainder


a = 23
b = 5
quotient, remainder = divide_without_operator(a, b)
print(f"Quotient of {a} divided by {b}: {quotient}")
print(f"Remainder of {a} divided by {b}: {remainder}")