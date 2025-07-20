#Q 1

v = [12, 5, 18, 7, 19, 8, 19]
n = len(v)

T = [1] * n  

for i in range(1, n):
    for j in range(i):
        if v[j] < v[i] and T[j] + 1 > T[i]:
            T[i] = T[j] + 1

print(max(T))  


#Q2

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
    
def longest_path_dag(graph):
    topo_order = topological_sort(graph)
    d = {v: 0 for v in graph}
    pi = {v: None for v in graph}  

    for v in topo_order:
        for u in graph[v]:
            if d[u] < d[v] + 1:
                d[u] = d[v] + 1
                pi[u] = v

    
    max_node = max(d, key=d.get)
    max_dist = d[max_node]

    path = []
    current = max_node
    while current is not None:
        path.append(current)
        current = pi[current]
    path.reverse()

    return max_dist, path

graph = {
    'a': ['b'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': []
}

length, path = longest_path_dag(graph)
print("Longest path length:", length)
print("Longest path:", path)