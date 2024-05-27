# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        nextStack,prevStack = [],[]
        
        def pushRight(root):
            while root:
                prevStack.append(root)
                root = root.right
        
        def pushLeft(root):
            while root:
                nextStack.append(root)
                root = root.left
        
        pushRight(root)
        pushLeft(root)
        
        def prev():
            node = prevStack.pop()
            cur = node.left
            if cur:
                pushRight(cur)
            return node.val
        
        def next():
            node = nextStack.pop()
            cur = node.right
            if cur:
                pushLeft(cur)
            return node.val
        
        if not nextStack or not prevStack:
            return False
        
        i,j = prev(),next()
        
        while j < i:
            if i + j == k:
                return True
            elif i + j > k:
                i = prev()
            else:
                j = next()
                
        return False