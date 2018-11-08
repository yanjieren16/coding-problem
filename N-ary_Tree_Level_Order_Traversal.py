# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a Node.
class TreeNode(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

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
                if node.children:
                    next_level += node.children
                curr_level_result.append(node.val)
            total_result.append(curr_level_result)
            curr_level_result = []
            curr_level = next_level
            next_level = []

        return total_result
