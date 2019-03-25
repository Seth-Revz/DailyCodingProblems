# Good morning! Here's your coding interview problem for today.

# This problem was asked by Yelp.

# You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. 
# Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

# For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

def findMinJumps(arr, a, b):
    
    if (a == b): 
        return 0
    if (arr[a] == 0): 
        return float('inf') 

    minimum = float('inf') 

    for i in range(a, b): 
        if (i < a + arr[a]): 
            numOfJumps = findMinJumps(arr, i + 1, b) 

            if (numOfJumps != float('inf') and numOfJumps + 1 < minimum): 
                minimum = numOfJumps + 1
  
    return minimum

if __name__ == "__main__":
    # arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9, 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9, 6, 6, 6, 6, 6, 6, 6, 6]
    # arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
    result = findMinJumps(arr, 0, len(arr) - 1)

    print(result)