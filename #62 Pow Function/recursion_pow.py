# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

# Recursion cant handle big exponents. Bad implementation

import timeit

start = timeit.default_timer()

def pow(x, y):
    if y:
        return multiply(x, pow(x, y-1))
    else:
        return 1

def multiply(x, y):
    if y:
        return (x + multiply(x, y-1))
    else:
        return 0

ans = pow(5, 5)

print(ans)

stop = timeit.default_timer()
totaltime = stop - start
print('%f' % (totaltime))