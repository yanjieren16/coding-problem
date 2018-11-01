# Implement the following operations of a queue using stacks.
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

class Queue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        
        # 1) While stack1 is not empty, push everything from stack1 to stack2.
        # 2) Push x to stack1 (assuming size of stacks is unlimited).
        # 3) Push everything back to stack1.
        # time complexity : O(n)

        if not self.stack1:
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack1:
            return self.stack1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack1:
            return self.stack1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1 == []
