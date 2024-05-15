# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftHeight = self.findLeftHeight(root)
        rightHeight = self.findRightHeight(root)
        if leftHeight == rightHeight:
            return (2**leftHeight ) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def findLeftHeight(self,root):
        h = 0
        while root:
            h = h + 1
            root = root.left
        return h
    def findRightHeight(self,root):
        h = 0
        while root:
            h = h + 1
            root = root.right
        return h