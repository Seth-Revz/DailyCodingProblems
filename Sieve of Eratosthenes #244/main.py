# Good morning! Here's your coding interview problem for today.

# This problem was asked by Square.

# The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
# The method is to take increasingly larger prime numbers, and mark their multiples as composite.

# For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. 
# Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

# Implement this algorithm.

# Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

def eratosthenes(N):
    
    arr = [] 
    # Fill array 2 to N
    for i in range(2, N + 1):
        arr.append(i)

    prime = arr[0]

    while prime * prime <= N:
        # remove the multiples of the prime because they are not prime
        for i in range(prime * 2, N + 1, prime):
            try:
                arr.remove(i)
                # catch trying to remove a value that is not in the arr
            except ValueError:
                pass
        
        prime += 1

    return arr


if __name__ == "__main__":
    n = 100
    result = eratosthenes(n)

    for i in result:
        print(i, end=" ")
