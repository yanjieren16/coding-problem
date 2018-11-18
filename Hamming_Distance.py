"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        z = x ^ y
        count = 0
        while z > 0:
            count += z & 1
            z >>= 1
        return count
