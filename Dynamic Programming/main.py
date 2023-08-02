"""
This algorithm has a time complexity of O(n) and a space complexity of O(n),
as it stores solutions for all values up to n in the table. 
"""

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize table for dynamic programming
    fib_table = [0] * (n + 1)
    fib_table[0] = 0
    fib_table[1] = 1

    # Compute and store solutions for subproblems
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]