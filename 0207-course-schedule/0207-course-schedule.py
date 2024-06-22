from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {node : 0 for node in range(numCourses)}
        adj = [[] for _ in range(numCourses)]
        queue = deque()
        
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        for node in adj:
            for neighbour in node:
                indegree[neighbour] = indegree[neighbour] + 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        # If the number of courses in ans is equal to numCourses, all courses can be finished
        return len(ans) == numCourses