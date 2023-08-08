def fib(n):
  '''
  When given a position, the function returns the fibonacci at that position in the sequence.
  The zeroth number in the fibonacci sequence is 0. The first number is 1
  Negative numbers should return None
  TODO: Make the algorithm work for larger numbers or implement faster algorithms
  '''

  if (n < 0):
    return None
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    l = [0,1]
    index = 1
    while (index < n):
      l.append(l[-1] + l[-2])
      index += 1


    return l[-1]

# Test cases
assert(fib(1) == 1)
assert(fib(21) == 10946)
assert(fib(0) == 0)
assert(fib(-1) == None)
assert(fib(-2) == None)

print("Code ran successfully!")
