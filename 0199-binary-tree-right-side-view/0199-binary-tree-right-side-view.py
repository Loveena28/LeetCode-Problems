# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        topNodes = {}
        queue = deque()
        result = []
        queue.append((root,0))
        
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                if node[0]:
                    topNodes[node[1]] = node[0].val
                    
                    queue.append((node[0].left,node[1]+1))
                    queue.append((node[0].right,node[1]+1))
        for i in sorted(topNodes.items()):
            result.append(i[1])
        return result
        