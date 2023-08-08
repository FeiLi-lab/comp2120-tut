def fizzbuzz(n):
    '''
    Returns the stringified number itself except in 3 cases:
    1. For multiples of 3 return “Fizz”
    2. For the multiples of 5 print “Buzz”
    3. For numbers which are multiples of both 3 and 5 print “FizzBuzz"
    '''
    val = ""
    
    if n > 3:
        val+= fizzbuzz(n-3)
    elif n == 0:
        return "Fizz"
    else:
        return ""
    
    if n > 5:
        val += fizzbuzz(n-5)
    elif n == 0:
        return "Buzz"
    else:
        return ""

    if len(val) != 0:
        return val
    else:
        return n

assert(fizzbuzz(3) == "Fizz")
assert(fizzbuzz(5) == "Buzz")
assert(fizzbuzz(15) == "Fizz Buzz")

print("Code ran successfully!")
