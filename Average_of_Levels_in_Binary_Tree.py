"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""

# following is Breath-First Solution:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):

        if root is None:
            return []
        # stores node in current level
        curr_level = [root]

        # stores node.val in current level
        curr_level_result = []

        # stores final val in all levels
        total_result = []

        # stores node in next level
        next_level = []
        while curr_level:
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                curr_level_result.append(node.val)
            total_result.append(self.average(curr_level_result))
            curr_level_result = []
            curr_level = next_level
            next_level = []

        return total_result

    def average(self, list):
        # use float() to force the result to be float
        return sum(list)/float(len(list))
