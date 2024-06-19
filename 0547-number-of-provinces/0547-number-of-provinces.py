class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(node):
            for i in range(n):
                if isConnected[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        
        
        provinces = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces = provinces + 1
        
        return provinces