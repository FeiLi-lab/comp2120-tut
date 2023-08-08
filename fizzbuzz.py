def fizzbuzz(n):
    '''
    Returns the stringified number itself except in 3 cases:
    1. For multiples of 3 return “Fizz”
    2. For the multiples of 5 print “Buzz”
    3. For numbers which are multiples of both 3 and 5 print “FizzBuzz"
    '''
    val = ""
    if n % 3 == 0:
        val += "Fizz"
    if n % 5 == 0:
        val += "Buzz"
    if len(val) == 0:
        return str(n)
    else:
        return val

assert(fizzbuzz(3) == "Fizz")
assert(fizzbuzz(5) == "Buzz")
assert(fizzbuzz(15) == "Fizz Buzz")

print("Code ran successfully!")
