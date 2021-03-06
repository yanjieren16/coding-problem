# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L).
# You might need to change the root of the tree, 
# so the result should return the new root of the trimmed binary search tree.
# # Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return

    def trimBST(self, root, L, R):

        def trim(node):

            if node is None:
                return None

            elif node.val < L:
                return trim(node.right)

            elif node.val > R:
                return trim(node.left)

            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
