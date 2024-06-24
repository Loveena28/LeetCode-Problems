import heapq
from typing import List
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, weight in times:
            adj[source - 1].append((target - 1, weight))

        dist = [float('inf')] * n
        dist[k - 1] = 0  

        minheap = [(0, k - 1)]  # (distance, node)

        while minheap:
            current_time, node = heapq.heappop(minheap)

            if current_time > dist[node]:
                continue

            for neighbour, weight in adj[node]:
                new_time = current_time + weight
                if new_time < dist[neighbour]:
                    dist[neighbour] = new_time
                    heapq.heappush(minheap, (new_time, neighbour))

        max_delay = max(dist)

        # If there is any node that wasn't reached, return -1
        return -1 if max_delay == float('inf') else max_delay