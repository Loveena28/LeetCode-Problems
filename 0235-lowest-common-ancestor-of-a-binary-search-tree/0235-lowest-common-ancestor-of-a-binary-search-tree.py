# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None :
            return None
        
        cur = root.val
        if (p.val > cur and q.val > cur):
            return self.lowestCommonAncestor(root.right,p,q)
        elif (p.val < cur and q.val < cur):
            return self.lowestCommonAncestor(root.left,p,q)
        return root