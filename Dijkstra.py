from heapq import heappop, heappush


class Dijkstra:
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

    # None INF capacity

    def produceData(self, names, process, cost, amount, company1, company2):
        n = len(names)
        ids = dict(zip(names, range(n)))
        src, snk = ids[company1], ids[company2]

        G = [[0] * (2 * n) for _ in range(2*n)]
        for i in range(n):
            G[2*i][2*i+1] = amount[i]
            for c in process[i].split():
                G[2*i+1][2*ids[c]] = amount[ids[c]]

        bestFlow, bestCost, res = 0, 0, []
        for mask in range(1 << n):
            if not (1 << src & mask and 1 << snk & mask):
                continue
            H = [row[:] for row in G]
            canUse = [mask & (1 << (i // 2)) for i in range(2*n)]
            curFlow = self.maxFlow(H, 2*src, 2*snk+1, canUse, n)

            curCost, curPath = 0, []
            for i in range(n):
                if mask & (1 << i):
                    curPath.append(names[i])
                    curCost += cost[i]
            curPath.sort()
            if curFlow > bestFlow or (curFlow == bestFlow and (curCost < bestCost or (curCost == bestCost and curPath < res))):
                bestFlow, bestCost, res = curFlow, curCost, curPath
        return res
