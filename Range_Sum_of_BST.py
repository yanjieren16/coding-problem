"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.    
"""

class Solution(object):
    def rangeSumBST(self, root, L, R):

        if root is None:
            return 0
        
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
