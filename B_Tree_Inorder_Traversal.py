# Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # recursive method, needs help function
    # Time complexity O(n)
    # Space complexity: worst O(n)/average O(log(n))
    def recursive_inorder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.helper(root, list)
        return list

    def helper(self, root, list):
        if root:
            if root.left:
                self.helper(root.left, list)
            list.append(root.val)
            if root.right:
                self.helper(root.right, list)

    # iterative method, using stack
    # Time complexity O(n)
    # Space complexity: O(n)
    def iterative_inorder(self, root):
        list = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            list.append(curr.val)
            curr = curr.right
        return list

    # Morris Traversal
    # Time complexity O(n)
    # Space complexity: O(1)
    def morris_inorder(self, root):
        list = []
        curr = root
        while curr:

            if curr.left is None:
                list.append(curr.val)
                curr = curr.right
            else:
                # find the inorder predecessor of curr
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right

                # make curr as right child of its inorder predecessor
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left

                # revert the changes made in if part to restore the original tree
                # i.e., fix the right child of predecessor
                else:
                    pre.right = None
                    list.append(curr.val)
                    curr = curr.right
        return list
