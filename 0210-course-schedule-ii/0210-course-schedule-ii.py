class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        stack = []
        visited = [False] * numCourses
        onPath = [False] * numCourses
        hasCycle = False
        
        def dfs(node):
            nonlocal hasCycle
            if onPath[node]:  # cycle detected
                hasCycle = True
                return
            if visited[node] or hasCycle:
                return
            
            visited[node] = True
            onPath[node] = True
            
            for neighbor in adj[node]:
                dfs(neighbor)
            
            onPath[node] = False
            stack.append(node)
        
        for i in range(numCourses):
            if not visited[i]:
                dfs(i)
        
        if hasCycle:
            return []
        
        return stack[::-1]