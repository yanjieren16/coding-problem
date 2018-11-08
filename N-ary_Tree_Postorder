"""
Postorder traversal can be done using two stacks.
1) get reversed post-order traversal and push them into stack A (This extra stack A is used to store reversed post-order traversal)
2) pop elements from stack A and print them

reversed postorder traversal = preorder with the right child visited before left child
"""


# Definition for a Node.
class TreeNode(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def postorder(self, root):

        list = []
        stack = []
        stack_2 = []

        if root is None:
            return None
        curr = root
        stack.append(curr)
        while stack:
            curr = stack.pop()
            stack_2.append(curr)

            if curr.children:
                for i in range(0, len(curr.children)):
                    stack.append(curr.children[i])

        while stack_2:
            list.append(stack_2.pop().val)
        return list
