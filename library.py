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
            curFlow, flowDict = nx.maximum_flow(
                H, 2*src, 2 * snk + 1, flow_func=edmonds_karp)
            curFlow, flowDict = nx.maximum_flow(
                H, 2*src, 2 * snk + 1, flow_func=shortest_augmenting_path)

            if curFlow > bestFlow or (curFlow == bestFlow and (curCost < bestCost or (curCost == bestCost and curPath < res))):
                bestFlow, bestCost, res = curFlow, curCost, curPath
        return res
