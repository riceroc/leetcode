# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # helper function for recursion
        def helper(node, left, right):
            
            # check if empty binary search tree
            if not node:
                return True
            
            # check if a node broke bst
            if not (node.val < right and node.val > left):
                return False
            
            # recursive call output as bool
            return (helper(node.left, left, node.val) and
            helper(node.right, node.val, right))
        
        # set left and right pointers to neg/pos inf
        return helper(root, float("-inf"), float("inf"))