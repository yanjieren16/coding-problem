“”“
Reverse bits of a given 32 bits unsigned integer.
”“”
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(0, 32):
            x = n & 1
            n = n >> 1
            m = (m << 1) + x
        return m
