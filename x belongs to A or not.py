def binary_search(A, x):
    i = 0
    j = len(A) - 1
    num = -1
    mid = (i + j) // 2
    while i <= j:
        if x == A[mid]:
            return x
        elif x > A[mid]:
            i = mid + 1
        else:
            j = mid - 1
        mid = (i + j) // 2
    return num

def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 11
    p = binary_search(A, x)
    if p == -1:
        print(f"Element {x} is not present in the list")
    else:
        print(f"Element {p} is present in the list")

main()
