"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, 
print the sequence of gray code. A gray code sequence must begin with 0.
"""
class Solution(object):
    def grayCode(self, n):
        list = [0]
        dict = {0: 1}
        total = 2 ** n
        i = 0
        while i < total - 1:
            tp = 1
            tmp = list[i] ^ tp

            while tmp in dict:
                    tp = tp << 1
                    tmp = list[i] ^ tp
            if tmp not in dict:
                list.append(tmp)
                dict[tmp] = 1
                i += 1
        return list
