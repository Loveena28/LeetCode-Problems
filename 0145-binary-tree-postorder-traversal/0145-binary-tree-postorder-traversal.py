# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
    #     return self.postorder(root)
    # def postorder(self,root):
    #     result = []
    #     if root is None:
    #         return []
    #     if root.left:
    #         result.extend(self.postorder(root.left))
    #     if root.right:
    #         result.extend(self.postorder(root.right))
    #     result.append(root.val)
    #     return result
    
    # iterative approach using 2 stack
        stack1,stack2 = [],[]
        result = []
        if not root:
            return []
        cur = root
        stack1.append(root)
        while stack1:
            cur = stack1[-1]
            stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
            
        while stack2:
            result.append(stack2.pop().val)
        return result
        