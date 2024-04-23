class Vertex:
    def __init__(self, node):
        self.node = node
        self.adjacent = []
        self.color = 'white'
        self.initialtime = 0
        self.finishtime = 0

def DFS(G):
    time = 0
    order = []

    def visited(u):
        nonlocal time
        time += 1
        u.initialtime = time
        u.color = 'gray'
        order.append(u)

        for v in u.adjacent:
            if v.color == 'white':
                visited(v)

        time += 1
        u.finishtime = time
        u.color = 'black'

    for vertex in G:
        if vertex.color == 'white':
            visited(vertex)

    return order

u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')

u.adjacent = [v, x]
v.adjacent = [y]
w.adjacent = [z]
x.adjacent = [v]
y.adjacent = [x]
z.adjacent = [z]

graph = [u, v, w, x, y, z]

result = DFS(graph)

dfs_order = ", ".join(f"{vertex.node} ({vertex.initialtime}/{vertex.finishtime})" for vertex in result)
print("DFS Ordering:")
print(dfs_order)

"""
output:
DFS Ordering:
u (1/8), v (2/7), y (3/6), x (4/5), w (9/12), z (10/11)
"""
