# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a = p.val
        b = q.val

        if a > b:
            a, b = b, a
        
        stack = [root]

        while stack:
            node = stack.pop()
            val = node.val

            if a > val and b > val:
                stack.append(node.right)
            elif a < val and b < val:
                stack.append(node.left)
            else:
                return node


            



                