# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, min_allowed, max_allowed) -> bool:
            if not node:
                return True
            
            if min_allowed < node.val and node.val < max_allowed:
                return (traverse(node.left, min_allowed, min(max_allowed, node.val)) and traverse(node.right, max(min_allowed, node.val), max_allowed))
            else:
                return False
        
        return traverse(root, -inf, inf)