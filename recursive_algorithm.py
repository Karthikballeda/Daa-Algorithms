def using_recursive(n, curr_sum=0, current_seq=[]):
    if curr_sum == n:
        print(current_seq)
        return
    if curr_sum > n:
        return

    # Include a 1 in the sequence and recurse
    using_recursive(n, curr_sum + 1, current_seq + [1])

    # Include a 2 in the sequence and recurse
    using_recursive(n, curr_sum + 2, current_seq + [2])

N = 0
using_recursive(N)
