from collections import defaultdict, deque

def classify_edges_and_dfs(graph):
    time = [0]
    color = {u: 'white' for u in graph}
    d = {}
    f = {}
    pi = {}
    edge_types = []

    def dfs_visit(u):
        color[u] = 'gray'
        time[0] += 1
        d[u] = time[0]

        for v in graph[u]:
            if color[v] == 'white':
                pi[v] = u
                edge_types.append((u, v, 'Tree'))
                dfs_visit(v)
            elif color[v] == 'gray':
                edge_types.append((u, v, 'Back'))
            elif color[v] == 'black':
                if d[u] < d[v]:
                    edge_types.append((u, v, 'Forward'))
                else:
                    edge_types.append((u, v, 'Cross'))

        color[u] = 'black'
        time[0] += 1
        f[u] = time[0]

    for u in graph:
        if color[u] == 'white':
            pi[u] = None
            dfs_visit(u)

    return pi, d, f, edge_types
    
    
def kosaraju_scc(graph):
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)

    def dfs2(u, label):
        component[u] = label
        for v in transpose[u]:
            if v not in component:
                dfs2(v, label)

    
    for node in graph:
        if node not in visited:
            dfs1(node)

    
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    
    component = {}
    label = 0
    for u in reversed(order):
        if u not in component:
            dfs2(u, label)
            label += 1

    return component, label  


def is_semi_connected(graph):
    scc_map, num_sccs = kosaraju_scc(graph)

    if num_sccs == 1:
        return True  

    
    scc_graph = defaultdict(set)
    for u in graph:
        for v in graph[u]:
            cu, cv = scc_map[u], scc_map[v]
            if cu != cv:
                scc_graph[cu].add(cv)

    
    indegree = [0] * num_sccs
    for u in scc_graph:
        for v in scc_graph[u]:
            indegree[v] += 1

    queue = deque([u for u in range(num_sccs) if indegree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in scc_graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    
    for i in range(len(topo_order) - 1):
        u = topo_order[i]
        v = topo_order[i + 1]
        if v not in scc_graph[u]:
            return False  

    return True
    
#1
    
graph = {
    's': ['z', 'w'],
    't': ['u', 'v'],
    'u': ['t', 'v'],
    'v': ['s', 'w'],
    'w': ['x'],
    'x': ['z'],
    'y': ['x'],
    'z': ['y','w']
}

pi, d, f, edge_types = classify_edges_and_dfs(graph)

print("Parent (pi):")
for u in pi:
    print(f"{u}: {pi[u]}")

print("\nDiscovery Time (d):")
for u in d:
    print(f"{u}: {d[u]}")

print("\nFinish Time (f):")
for u in f:
    print(f"{u}: {f[u]}")

print("\nEdge Types:")
for u, v, t in edge_types:
    print(f"{u} -> {v}: {t}")

#2
graph2 = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d'],
    'd': [],
    'e': ['a', 'd']
}

print("Semi-connected?" , is_semi_connected(graph2))