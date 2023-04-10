import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
from networkx.algorithms.flow import edmonds_karp


class SoftwareCompanies:
    def produceData(self, names, process, cost, amount, company1, company2):
        n = len(names)
        ids = dict(zip(names, range(n)))
        src, snk = ids[company1], ids[company2]

        G = nx.DiGraph()
        for i in range(n):
            G.add_edge(2*i, 2*i+1, capacity=amount[i])
            for c in process[i].split():
                G.add_edge(2*i+1, 2 * ids[c], capacity=float("inf"))

        bestFlow, bestCost, res = 0, 0, []
        for mask in range(1 << n):
            if not (1 << src & mask and 1 << snk & mask):
                continue
            H = G.copy()
            curCost, curPath = 0, []
            for i in range(n):
                if mask & (1 << i):
                    curPath.append(names[i])
                    curCost += cost[i]
                else:
                    H.remove_node(2*i)
                    H.remove_node(2*i+1)
            curPath.sort()

            curFlow, flowDict = nx.maximum_flow(H, 2*src, 2 * snk + 1)
            # curFlow, flowDict = nx.maximum_flow(
            #     H, 2*src, 2 * snk + 1, flow_func=edmonds_karp)
            # curFlow, flowDict = nx.maximum_flow(
            #     H, 2*src, 2 * snk + 1, flow_func=shortest_augmenting_path)

            if curFlow > bestFlow or (curFlow == bestFlow and (curCost < bestCost or (curCost == bestCost and curPath < res))):
                bestFlow, bestCost, res = curFlow, curCost, curPath
        return res


def maxFlow(H, src, snk, canUse, n):
    res = 0
    while True:
        path = [0] * 2 * n
        From = [-1] * 2 * n
        seen = [False] * 2 * n
        path[src] = float("inf")
        while True:
            i = -1
            for j in range(2*n):
                if not seen[j] and path[j] and (i == -1 or path[j] > path[i]):
                    i = j
            if i == -1:
                break
            seen[i] = True
            for j in range(2*n):
                if canUse[j] and H[i][j]:
                    v = min(path[i], H[i][j])
                    if v > path[j]:
                        path[j] = v
                        From[j] = i
        if not path[snk]:
            break
        res += path[snk]
        i = snk
        while i != src:
            H[From[i]][i] -= path[snk]
            H[i][From[i]] += path[snk]
            i = From[i]

    return res


class EdmondsKarp:

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
            curFlow = maxFlow(H, 2*src, 2*snk+1, canUse, n)

            curCost, curPath = 0, []
            for i in range(n):
                if mask & (1 << i):
                    curPath.append(names[i])
                    curCost += cost[i]
            curPath.sort()
            if curFlow > bestFlow or (curFlow == bestFlow and (curCost < bestCost or (curCost == bestCost and curPath < res))):
                bestFlow, bestCost, res = curFlow, curCost, curPath
        return res
