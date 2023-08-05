
# inp = open("input3_1.text", "r")
# out = open("output3_1.text", "w")

inp = open("input3_2.text", "r")
out = open("output3_2.text", "w")

# inp = open("input3_3.text", "r")
# out = open("output3_3.text", "w")

###########################################################

# create an adjacency list for unweighted graph

# Here n = number of vertices, m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(1, n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)

print(graph)
print("##############################################")
###########################################################

def dfs(graph, vertex, visited, stack):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)

    stack.append(vertex)


def transpose(graph):
    transposed_graph = {}
    for vertex in graph:
        transposed_graph[vertex] = []

    for vertex in graph:
        for neighbor in graph[vertex]:
            transposed_graph[neighbor].append(vertex)

    return transposed_graph


def kosaraju(graph):
    num_vertices = len(graph)

    # Step 1: Perform first DFS to fill the stack with the vertices in the order of finish times
    stack = []
    visited = {vertex: False for vertex in graph}
    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)

    # Step 2: Transpose the graph
    transposed_graph = transpose(graph)

    # Step 3: Perform second DFS to find strongly connected components
    visited = {vertex: False for vertex in graph}
    strongly_connected_components = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs(transposed_graph, vertex, visited, component)
            strongly_connected_components.append(component)

    # Step 4: Check if any vertices are not visited yet (disconnected components)
    for vertex in graph:
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            strongly_connected_components.append(component)

    return strongly_connected_components


strongly_connected_components = kosaraju(graph)
print(strongly_connected_components)
