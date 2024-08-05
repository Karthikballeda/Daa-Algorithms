n = int(input("Enter the number of terms: "))
a = 1
b = 1
next_num = b
print(next_num, end=" ")
count = 1 #stands for the number of elements printed till now

while count < n:
    print(next_num, end=" ")
    count += 1
    a,b= b, next_num
    next_num = a+b

print()
