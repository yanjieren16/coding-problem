# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        length = len(nums)
        maxi = max(nums)
        index = nums.index(maxi)
        left = nums[0: index]
        right = nums[index + 1: length]
        node = TreeNode(maxi)
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)

        return node
