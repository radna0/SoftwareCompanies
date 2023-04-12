from collections import deque
from ProduceData import ProduceData


class Dinic(ProduceData):
    def maxFlow(self, H, src, snk, canUse, n):
        res = 0

        def dfs(u, flow):
            if u == snk:
                return flow
            for v in range(2*n):
                if H[u][v] and canUse[v] and level[v] == level[u] + 1:
                    f = dfs(v, min(flow, H[u][v]))
                    if f > 0:
                        H[u][v] -= f
                        H[v][u] += f
                        return f
            return 0

        while True:
            level = [-1] * (2*n)
            level[src] = 0
            q = deque()
            q.append(src)
            while q:
                u = q.popleft()
                for v in range(2*n):
                    if level[v] < 0 and canUse[v] and H[u][v]:
                        level[v] = level[u] + 1
                        q.append(v)

            if level[snk] < 0:
                break

            while True:
                f = dfs(src, float("inf"))
                if f == 0:
                    break
                res += f

        return res
