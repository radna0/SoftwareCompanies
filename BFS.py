from collections import deque
from ProduceData import ProduceData


class BFS(ProduceData):
    def maxFlow(self, H, src, snk, canUse, n):
        res = 0
        while True:
            dist = [0] * 2 * n
            dist[src] = float("inf")
            prev = [-1] * 2 * n
            seen = set()
            q = deque()
            q.append((dist[src], src))
            while q:
                d, u = q.popleft()
                seen.add(u)
                for v in range(2*n):
                    if v not in seen and canUse[v] and H[u][v]:
                        dist[v] = min(d, H[u][v])
                        prev[v] = u
                        q.append((dist[v], v))
            if not dist[snk]:
                break

            res += dist[snk]
            i = snk
            while i != src:
                H[prev[i]][i] -= dist[snk]
                H[i][prev[i]] += dist[snk]
                i = prev[i]

        return res
