from heapq import heappop, heappush
from ProduceData import ProduceData


class Dijkstra(ProduceData):
    def maxFlow(self, H, src, snk, canUse, n):
        res = 0
        while True:
            dist = [float("inf")] * 2 * n
            dist[src] = 0
            prev = [-1] * 2 * n
            heap = [(0, src)]
            while heap:
                d, u = heappop(heap)
                if d > dist[u]:
                    continue
                for v in range(2*n):
                    if canUse[v] and H[u][v] and d + H[u][v] < dist[v]:
                        dist[v] = d + H[u][v]
                        prev[v] = u
                        heappush(heap, (dist[v], v))
            if dist[snk] == float("inf"):
                break

            path = [snk]
            while path[-1] != src:
                path.append(prev[path[-1]])

            path = path[::-1]
            bottleneck = float("inf")

            for i in range(len(path) - 1):
                bottleneck = min(bottleneck, H[path[i]][path[i+1]])

            for i in range(len(path) - 1):
                H[path[i]][path[i+1]] -= bottleneck
                H[path[i+1]][path[i]] += bottleneck

            res += bottleneck

        return res
