from queue import PriorityQueue


class ShortestAugmentingPath:
    def maxFlow(self, H, src, snk, canUse, n):
        res = 0
        while True:
            path = [0] * 2 * n
            From = [-1] * 2 * n
            seen = [False] * 2 * n
            dist = [float('inf')] * 2 * n
            dist[src] = 0
            pq = PriorityQueue()
            pq.put((0, src))
            while not pq.empty():
                d, i = pq.get()
                if seen[i]:
                    continue
                seen[i] = True
                for j in range(2*n):
                    if canUse[j] and H[i][j]:
                        w = H[i][j]
                        if dist[j] > dist[i] + w:
                            dist[j] = dist[i] + w
                            path[j] = min(path[i], H[i][j])
                            From[j] = i
                            pq.put((dist[j], j))
            if not path[snk]:
                break
            res += path[snk]
            i = snk
            while i != src:
                H[From[i]][i] -= path[snk]
                H[i][From[i]] += path[snk]
                i = From[i]
        return res

    def produceData(self, names, process, cost, amount, company1, company2):
        n = len(names)
        ids = dict(zip(names, range(n)))
        src, snk = ids[company1], ids[company2]

        G = [[0] * (2 * n) for _ in range(2*n)]
        for i in range(n):
            G[2*i][2*i+1] = amount[i]
            for c in process[i].split():
                G[2*i+1][2*ids[c]] = float("inf")

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
