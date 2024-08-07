def find_ways_iterative(n):
    # Initialize a list with an initial sequence (current_sum, current_sequence)
    sequences = [(0, [])]

    # Iterate through the list and build new sequences
    for current_sum, current_sequence in sequences:
        # If the current sum is equal to n, print the sequence
        if current_sum == n:
            print(current_sequence)
            continue
        
        # If the current sum is less than n, add new sequences to the list
        if current_sum + 1 <= n:
            sequences.append((current_sum + 1, current_sequence + [1]))
        if current_sum + 2 <= n:
            sequences.append((current_sum + 2, current_sequence + [2]))

N = 4
find_ways_iterative(N)
