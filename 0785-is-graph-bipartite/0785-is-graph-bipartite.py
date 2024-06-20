class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloured = [-1] * len(graph)
        
        def dfs(node,color):
            coloured[node] = color
            for neighbour in graph[node]:
                if coloured[neighbour] == -1 and not dfs(neighbour,3-color):
                    return False
                elif coloured[neighbour] == color:
                    return False
            return True
        
        
        for node in range(len(graph)):
            if coloured[node] == -1 and not dfs(node,1):
                return False
        
        return True 