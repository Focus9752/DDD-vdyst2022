from collections import namedtuple

def adj(graph):
    adj = {node: {} for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] = 1
        adj[node2][node1] = 1
    return adj

N = int(input())
efficiencyScores = list(map(int, input().split()))
edges = []

for i in range(N):
    edges.append(tuple(map(int, input().split())))

Graph = namedtuple("Graph",["nodes","edges"])

g = Graph([i + 1 for i in range(N)], edges)



