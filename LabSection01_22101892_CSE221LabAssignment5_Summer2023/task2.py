inp = open("input2_1.text", "r")
out = open("output2_1.text", "w")

# inp = open("input2_2.text", "r")
# out = open("output2_2.text", "w")

# inp = open("input2_3.text", "r")
# out = open("output2_3.text", "w")

###########################################################

# create an adjacency list for unweighted graph

# Here n = number of vertices, m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)

###########################################################

print("Adjacency List: ", graph)
