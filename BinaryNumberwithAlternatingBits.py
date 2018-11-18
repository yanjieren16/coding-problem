"""
Given a positive integer, 
check whether it has alternating bits: 
namely, if two adjacent bits will always have different values.
eg: 101 True
    1010 True
    111 False
    1011 False
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        if n == 1 or n == 2:
            return True
        while n > 0:
            x = n & 1
            y = n & 2
            y = y >> 1
            if x == y:
                return False
            else:
                n = n >> 1
        return True
