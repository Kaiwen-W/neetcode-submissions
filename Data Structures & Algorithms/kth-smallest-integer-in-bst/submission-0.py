# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traversal(node):
            if not node:
                return 
            
            if node.left:
                traversal(node.left)

            res.append(node.val)

            if node.right:
                traversal(node.right)
        
        traversal(root)

        return res[k - 1]