# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderMap = {}
        for index,i in enumerate(inorder):
            inOrderMap[i] = index
        return self.createTree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inOrderMap)
        
    def createTree(self,preorder,preStart,preEnd,inorder,inStart,inEnd,OrderMap):
        if preStart > preEnd or inStart > inEnd:
            return
        
        root = TreeNode()
        inRoot = OrderMap[preorder[preStart]]
        numsLeft = inRoot - inStart
        
        root.val = preorder[preStart]
        root.left = self.createTree(preorder,preStart+1,preStart+numsLeft,inorder,inStart,inRoot-1,OrderMap
            )
        root.right = self.createTree(preorder,preStart+numsLeft+1,preEnd,inorder,inRoot+1,inEnd,OrderMap)
        
        return root