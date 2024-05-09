# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)
        levelCount = 0
        
        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                levelCount = levelCount + 1
                result.append(level)
        for i in range(levelCount):
            if i % 2 != 0:
                result[i].reverse()
        return result