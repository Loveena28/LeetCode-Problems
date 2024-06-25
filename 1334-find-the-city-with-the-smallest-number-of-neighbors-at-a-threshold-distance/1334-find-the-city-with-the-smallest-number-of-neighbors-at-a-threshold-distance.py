class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        adjMatrix = [[INF] * n for _ in range(n)]
        
        for u,v,weight in edges:
            adjMatrix[u][v] = weight
            adjMatrix[v][u] = weight
            
        adjMatrix = [[0 if i == j else adjMatrix[i][j] for j in range(n)] for i in range(n)]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adjMatrix[i][k] != INF and adjMatrix[k][j] != INF:
                        adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])
        cityIndex = -1
        maxCount = n
        for city in range(n):
            localCount = 0
            for adjCity in range(n):
                if adjMatrix[city][adjCity] <= distanceThreshold:
                    localCount = localCount + 1
            
            if localCount <= maxCount:
                maxCount = localCount
                cityIndex = city
            
        
        return cityIndex