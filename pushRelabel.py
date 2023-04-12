
from ProduceData import ProduceData


class PushRelabel(ProduceData):
    def maxFlow(self, H, src, snk, canUse, n):
        height = [0] * (2*n)
        height[src] = 2*n
        excess = [0] * (2*n)
        flow = [[0] * (2*n) for _ in range(2*n)]
        seen = [False] * (2*n)

        def push(u, v):
            d = min(excess[u], H[u][v] - flow[u][v])
            flow[u][v] += d
            flow[v][u] -= d
            excess[u] -= d
            excess[v] += d

        def relabel(u):
            d = float("inf")
            for v in range(2*n):
                if H[u][v] - flow[u][v] > 0 and canUse[v]:
                    d = min(d, height[v])
            height[u] = d + 1

        def discharge(u):
            while excess[u] > 0:
                if seen[u]:
                    relabel(u)
                else:
                    seen[u] = True
                    for v in range(2*n):
                        if H[u][v] - flow[u][v] > 0 and canUse[v] and height[u] == height[v] + 1:
                            push(u, v)
                            if excess[u] == 0:
                                break
                        else:
                            relabel(u)
                            seen[u] = False

        flow[src][src+1] = H[src][src+1]
        flow[src+1][src] = -H[src][src+1]
        excess[src+1] = H[src][src+1]

        active = [i for i in range(2*n) if excess[i]
                  > 0 and i != src and i != snk]
        i = 0
        while i < len(active):
            u = active[i]
            old_height = height[u]
            discharge(u)
            if height[u] > old_height:
                active.insert(0, active.pop(i))
                i = 0
            else:
                i += 1
        return flow[src][src+1]
