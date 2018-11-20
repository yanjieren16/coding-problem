class Solution(object):

    def rangeBitwiseAnd_1(self, m, n):

        while m < n:
            n = n & (n - 1)
        return n

    '''
    Flip the LSB of b.
    And check if the new number is in range(a < number < b) or not
    if the number greater than 'a' again flip lsb
    if it is not then that's the answer
    '''
    def rangeBitwiseAnd_2(self, m, n):

        if m == n:
            return m
        while m < n:
            n -= (n & -n)
        return n
