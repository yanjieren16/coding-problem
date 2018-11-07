"""
Maximum Depth of Binary Tree
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):

        if root is None:
            return 0

        self.depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return self.depth

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
