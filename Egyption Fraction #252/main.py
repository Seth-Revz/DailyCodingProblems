# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
# For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

import math
import random
  
def egyptianFraction(numerator, denomonator): 

    denomonatorList = [] 
  
    while numerator != 0: 
  
        temp = math.ceil(denomonator / numerator) 
        denomonatorList.append(temp) 

        numerator = temp * numerator - denomonator 
        denomonator = denomonator * temp 
  
    result = ''
    for i in range(len(arr)): 
        if i != len(arr) - 1: 
            result += "1/{} + ".format(arr[i])
        else: 
            result += "1/{}".format(arr[i])

    return result

if __name__ == "__main__":
    
    while True:
        arr = []
        arr.append(random.randrange(1, 20))
        arr.append(random.randrange(1, 20))
        if arr[0] != arr[1]:    
            break
        # print("num and den are same, getting new ones")
        # print(arr[0], end=" ")
        # print(arr[1])
    
    arr.sort()
    num, den = arr
    result = egyptianFraction(num, den)

    print("{}/{} = {}".format(num, den, result))