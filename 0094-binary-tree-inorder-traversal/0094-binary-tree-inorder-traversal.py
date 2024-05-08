# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive approach
    #     return self.inorder(root)
    # def inorder(self,root):
    #     if root is None:
    #         return []
    #     result = []
    #     if root.left:
    #         result.extend(self.inorder(root.left))  # Traverse left subtree
    #     result.append(root.val)  # Visit current node
    #     if root.right:
    #         result.extend(self.inorder(root.right))  # Traverse right subtree
    #     return result
    
    # iterative approach
        stack,result = [],[]
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result