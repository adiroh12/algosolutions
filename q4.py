def count_paths(graph):
    topo_order = topological_sort(graph)
    paths = {node: 1 for node in graph}

    
    for v in topo_order:
        for u in graph[v]:
            paths[u] += paths[v]

    return paths

def topological_sort(graph):
    visited = {node: False for node in graph}
    stack = []

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
        stack.append(v)

    for v in graph:
        if not visited[v]:
            dfs(v)

    stack.reverse()
    return stack
    
def reds(n):
    v = [1 for i in range(n+1)]
    for i in range(1, n+1):
        v[i] = 3**(n-1) + v[i-1]
    return v[n]


#1
graph = {
    'a': ['b'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': []
}

print(count_paths(graph)) #1
print(reds(3)) #2