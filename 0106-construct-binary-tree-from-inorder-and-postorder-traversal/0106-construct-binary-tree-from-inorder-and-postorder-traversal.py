# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inOrderMap = {i:index for index,i in enumerate(inorder)}
            
        return self.createTree(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,inOrderMap)
        
    def createTree(self,postOrder,postStart,postEnd,inOrder,inStart,inEnd,OrderMap):
        if postStart > postEnd or inStart > inEnd:
            return None
        
        root = TreeNode(postOrder[postEnd])
        inRoot = OrderMap[root.val]
        numsLeft = inRoot - inStart

        root.left = self.createTree(postOrder,postStart,postStart+numsLeft-1,inOrder,inStart,inRoot-1,OrderMap
            )
        root.right = self.createTree(postOrder,postStart+numsLeft,postEnd- 1,inOrder,inRoot+1,inEnd,OrderMap)
        
        return root
        