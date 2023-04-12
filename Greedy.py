
from ProduceData import ProduceData


class Greedy(ProduceData):
    def maxFlow(self, H, src, snk, canUse, n):
        res = 0
        while True:
            dist = [0] * (2*n)
            dist[src] = float("inf")
            prev = [-1] * (2*n)
            seen = set()
            while True:
                i = -1
                for j in range(2*n):
                    if j not in seen and dist[j] and (i == -1 or dist[j] > dist[i]):
                        i = j
                if i == -1:
                    break
                seen.add(i)
                for j in range(2*n):
                    if canUse[j] and H[i][j]:
                        v = min(dist[i], H[i][j])
                        if v > dist[j]:
                            dist[j] = v
                            prev[j] = i
            if not dist[snk]:
                break
            res += dist[snk]
            i = snk
            while i != src:
                H[prev[i]][i] -= dist[snk]
                H[i][prev[i]] += dist[snk]
                i = prev[i]
        return res
