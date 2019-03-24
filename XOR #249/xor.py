# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Salesforce.
# 
# Given an array of integers, find the maximum XOR of any two elements.

arr = [5,1,4,3,0,2]
barr = bytearray(arr)
max = 0
for i in barr:
    for j in barr:
        byte = i^j
        if max < byte:
            max = byte

print(max)
