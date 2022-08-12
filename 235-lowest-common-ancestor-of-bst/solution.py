# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # starting at root
        cur = root
        
        # while current isnt null
        while cur:
            
            # if p and q vals are greater traverse the right sub tree 
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                
            # if p and q vals are less than traverse the left sub tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
                
            # split happens or we found lca
            else:
                return cur