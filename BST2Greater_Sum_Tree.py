"""
Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    # Traverse BST in reverse in-order
    # 1) Ensure that the current node exists, recurse on the right subtree
    # 2) visit the current node by updating its value and the total sum
    # 3) recurse on the left subtree.
    # Time complexity: O(n)

    def __init__(self):
        self.sum = 0
    
    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            root.val += self.sum
            self.sum = root.val
            self.convertBST(root.left)
        return root

    def print_tree(self, root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.val)
        self.print_tree(root.right)

'''
Iterative method

Initialize an empty stack and set the current node to the root.
So long as there are unvisited nodes in the stack or node does not point to null
(= always processing the right subtree first in the recursive solution, and is crucial for the guarantee of visiting nodes in order of decreasing value.)
Visit the node on the top of our stack, and consider its left subtree. (= visiting the current node before recursing on the left subtree in the recursive solution.) 
Stack is empty and node points to the left null child of the tree's minimum value node, so the loop terminates.
'''

class Solution(object):

    # Time complexity: O(n)
    # Space complexity: O(n)
    
    def transformBST(self, root):

        stack = []
        curr = root
        sum = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            curr.val += sum
            sum = curr.val
            curr = curr.left
        return root

    def print_tree(self, root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.val)
        self.print_tree(root.right)

