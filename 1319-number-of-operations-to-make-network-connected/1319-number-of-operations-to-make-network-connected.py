class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        extraEdges = 0
        mst = []
        edgeCount = 0
        parent = []
        rank = []
        
        for i in range(n):
            parent.append(i)
            rank.append(0)
        
        def find(node):
            if not (node == parent[node]):
                parent[node] = find(parent[node])
              
            return parent[node]
            
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        
        connectedComponents = n
        extraCables = 0

        for u, v in connections:
            if not union(u, v):
                extraCables += 1  # This cable is redundant

        # Count the number of connected components
        components = len(set(find(i) for i in range(n)))

        # We need (components - 1) cables to connect all components
        if extraCables >= components - 1:
            return components - 1
        else:
            return -1