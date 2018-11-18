"""
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Thoughts:
even number: num(1s) for i = num(1s) for (i/2)
            because i = i/2 << 1
odd number: num(1s) for i = num(1s) for (i - 1) + 1
"""

class Solution(object):

  def countBits_method_one(n):
      list = [0] * (n + 1)
      list[1] = 1
      i = 2
      for i in range(2, n + 1):
          if i & 1 == 1:
              list[i] = list[i - 1] + 1
          else:
              list[i] = list[i // 2]
      return list
      
    def countBits_method_two(self, num):
        if num == 0:
            return [0]
        list = [0] * (num + 1)
        list[1] = 1
        for i in range(2, num + 1):
            list[i] = list[i & (i - 1)] + 1
        return list
