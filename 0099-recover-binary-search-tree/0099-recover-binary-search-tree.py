# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        
        first, middle, last, prev = None, None, None, TreeNode(float('-inf'))
        
        def dfs(root):
            nonlocal first, middle, last, prev
            if not root:
                return
            
            dfs(root.left)
            
            if prev and root.val < prev.val:
                if not first:
                    first = prev
                    middle = root
                else:
                    last = root
            
            prev = root
            dfs(root.right)
        
        dfs(root)
        
        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val