from collections import deque


class BFS:
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
