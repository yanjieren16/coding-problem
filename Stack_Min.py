# Stack Min: How would you design a stack which, in addition to push and pop, has a function min 
#  which returns the minimum element? Push, pop and min should all operate in 0(1) time.


# store(element, current_min) pair in stack
class MinStack:

    def __init__(self):
        self.items = []

    def push(self, x):
        if self.items == []:
            current_min = x
        else:
            tmp = self.getMin()
            if tmp > x:
                current_min = x
            else:
                current_min = tmp
        self.items.append((x, current_min))

    def pop(self):
        self.items.pop()

    def top(self):
        if self.items:
            return self.items[-1][0]

    def getMin(self):
        if self.items:
            return self.items[-1][1]
