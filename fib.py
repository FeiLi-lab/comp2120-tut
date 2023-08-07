def fib(n):
  '''
  When given a position, the function returns the fibonacci at that position in the sequence.
  The zeroth number in the fibonacci sequence is 0. The first number is 1
  Negative numbers should return None
  TODO: Make the algorithm work for larger numbers or implement faster algorithms
  '''

    # base case of 0
  if n == 0:
    return 0
  # base case of 1
  elif n == 1:
    return 1
  # recursive case
  else:
    return fib(n - 1) + fib(n - 2)

# Test cases
assert(fib(1) == 1)
assert(fib(21) == 10946)
assert(fib(0) == 0)
assert(fib(-1) == None)

print("Code ran successfully!")
