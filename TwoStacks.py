# A space efficient implementation of TwoStack
# This method efficiently utilizes the available space.
# It does not cause an overflow if there is space available in arr[].
# The idea is to start two stacks from two extreme corners of arr[].
# stack1 starts from the leftmost element, the first element in stack1 is pushed at index 0.
# The stack2 starts from the rightmost corner, the first element in stack2 is pushed at index (n-1).
# Both stacks grow (or shrink) in opposite direction.
# To check for overflow, all we need to check is for space between top elements of both stacks.
# This check is highlighted in the below code.


class TwoStacks:

    def __init__(self, length):
        self.items = [None] * length
        self.length = length
        self.left = -1
        self.right = length

    def push1(self, x):
        if self.right - self.left > 1:
            self.left += 1
            self.items[self.left] = x
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, y):
        if self.right - self.left > 1:
            self.right -= 1
            self.items[self.right] = y
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.left >= 0:
            tmp = self.items[self.left]
            self.items[self.left] = None
            self.left -= 1
            return tmp
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.left < self.length:
            tmp = self.items[self.right]
            self.items[self.right] = None
            self.right -= 1
            return tmp
        else:
            print("Stack Underflow")
            exit(1)

