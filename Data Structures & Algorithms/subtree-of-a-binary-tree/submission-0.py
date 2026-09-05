# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # go to every node of root and check if the trees are the same 

        def traverse(root, subRoot):
            if same(root, subRoot):
                return True
            
            if not root:
                return False

            return (traverse(root.left, subRoot) or
            traverse(root.right, subRoot))

        def same(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return (same(root.left, subRoot.left) and 
            same(root.right, subRoot.right))
            
        return traverse(root, subRoot)