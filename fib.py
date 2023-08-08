def fib(n, memo={}):
    '''
    When given a position, the function returns the fibonacci at that position in the sequence.
    The zeroth number in the fibonacci sequence is 0. The first number is 1
    Negative numbers should return None
    TODO: Make the algorithm work for larger numbers or implement faster algorithms
    '''
    if n < 0:
        return None

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]

# Test cases
assert fib(1) == 1
assert fib(21) == 10946
assert fib(0) == 0
assert fib(-1) is None

print("Code ran successfully!")
