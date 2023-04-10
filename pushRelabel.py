
def maxFlow(H, src, snk, canUse, n):
    flow = [[0] * 2*n for _ in range(2*n)]
    excess = [0] * 2 * n
    height = [0] * 2 * n
    height[src],  excess[src] = 2*n, float("inf")

    def push(s, t):
        v = min(excess[s], H[s][t] - flow[s][t])
        flow[s][t] += v
        flow[t][s] -= v
        excess[s] -= v
        excess[t] += v
    
    def relabel():
        

    for i in range(2*n):
        push(src, i)

    print(flow)
    print(excess)

    return excess[snk]


class PushRelabel:

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
            if mask == 95:
                maxFlow(H, 2*src, 2*snk+1, canUse, n)
            curFlow = 0

            curCost, curPath = 0, []
            for i in range(n):
                if mask & (1 << i):
                    curPath.append(names[i])
                    curCost += cost[i]
            curPath.sort()
            if curFlow > bestFlow or (curFlow == bestFlow and (curCost < bestCost or (curCost == bestCost and curPath < res))):
                bestFlow, bestCost, res = curFlow, curCost, curPath
        return res
