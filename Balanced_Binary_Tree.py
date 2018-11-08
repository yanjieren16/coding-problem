"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.traversal(root)

    def height(self, node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        height = max(left, right) + 1
        return height

    def traversal(self, node):
        queue = [node]
        while queue:
            curr = queue.pop()
            if not self.is_balance(curr):
                return False
            if curr.left:
                queue.insert(0, curr.left)
            if curr.right:
                queue.insert(0, curr.right)
        return True

    def is_balance(self, node):
        return not abs(self.height(node.left) - self.height(node.right)) > 1
