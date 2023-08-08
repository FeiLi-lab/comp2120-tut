def fizzbuzz(n):
    '''
    Returns the stringified number itself except in 3 cases:
    1. For multiples of 3 return “Fizz”
    2. For the multiples of 5 print “Buzz”
    3. For numbers which are multiples of both 3 and 5 print “FizzBuzz"
    '''
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return str(n)

assert(fizzbuzz(3) == "Fizz")
assert(fizzbuzz(5) == "Buzz")

print("code ok")
print("Code ran successfully!")
