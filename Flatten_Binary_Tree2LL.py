"""
Given a binary tree, flatten it to a linked list in-place.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use stack to pre-order traversal
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        stack = []
        if root.right:
                stack.append(root.right)
        if root.left:
                stack.append(root.left)
        pre = root
        while stack:
            curr = stack.pop()

            pre.left = None
            pre.right = curr

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

            pre = curr
        
