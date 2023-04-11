class PushRelabel:
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
            if d < float("inf"):
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
            canUse = [bool(mask & (1 << (i // 2))) for i in range(2*n)]
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
