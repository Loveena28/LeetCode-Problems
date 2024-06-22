from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adjRev = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []
        
        for node in range(n):
            for neighbor in graph[node]:
                adjRev[neighbor].append(node)
                indegree[node] += 1
        
        queue = deque()
        for index,i in enumerate(indegree):
            if i == 0:
                queue.append(index)
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in adjRev[node]:
                indegree[neighbour] = indegree[neighbour] - 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                
                    
        
        return sorted(ans)