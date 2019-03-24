# Good morning! Here's your coding interview problem for today.
# This problem was asked by Microsoft.
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

def find_nth_perfect_number(n):
    cur = 19
    count = 0

    while True:
        sum = 0
        x = cur
        while (x > 0):
            sum = sum + (x % 10)
            x = (int)(x / 10)

        if (sum == 10):
            count += 1

        if (count == n):
            return cur

        cur += 9

print(find_nth_perfect_number(34))