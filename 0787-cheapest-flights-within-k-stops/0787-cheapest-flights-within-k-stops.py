class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        
        dist = [INF] * n
        dist[src] = 0
        
        # at most k stops and +1 for the source city
        for _ in range(k+1):
            distCopy = dist.copy()
            for source,dest,price in flights:
                if distCopy[source] == INF:
                    continue
                dist[dest] = min(dist[dest],distCopy[source]+price)
        
        return dist[dst] if dist[dst] != INF else -1