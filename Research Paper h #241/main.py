# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
# It is calculated as follows:

# A researcher has index h if at least h of her N papers have h citations each. 
# If there are multiple h satisfying this formula, the maximum is chosen.

# For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. 
# Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

import random

def findH(citations, N):
    citations.sort(reverse=True)
    h = 0
    
    for i in range(N):
        if citations[i]>i:
            h += 1
    
    return h

if __name__ ==  "__main__":
    citations = []
    numCitations = random.randrange(1, 10)

    for i in range(0, numCitations):
        citations.append(random.randrange(0, 7, 1))

    result = findH(citations[:], numCitations) 
    # Pass the list by value [:] instead of reference to maintain the order of original citations list

    msg = ''
    msg += "No. of Papers: {}\n".format(numCitations)
    msg += "Citations: {}\n".format(citations)
    msg += "h index: {}\n".format(result)
    print(msg)