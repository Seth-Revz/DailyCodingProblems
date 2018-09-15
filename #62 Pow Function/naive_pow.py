# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

# Naive multiplication but faster than recursion

import timeit

start = timeit.default_timer()

def pow(x, y):
    ans = x
    for i in range(1, y):
        ans *= x
    return ans

ans = pow(5, 5)

print(ans)

stop = timeit.default_timer()
totaltime = stop - start
print('%f' % (totaltime))
