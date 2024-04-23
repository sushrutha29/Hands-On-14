class Kruskalalgorithm:
    def __init__(self, node):
        self.node = node
        self.parent = [i for i in range(node)]
        self.Position = [0] * node
        self.edges = []

    def add(self, u, v, w):
        self.edges.append((u, v, w))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)

        if self.Position[p] < self.Position[q]:
            self.parent[p] = q
        elif self.Position[p] > self.Position[q]:
            self.parent[q] = p
        else:
            self.parent[q] = p
            self.Position[p] += 1

    def minimumsearchtree(self):
        self.edges.sort(key=lambda x: x[2])
        result = []
        e = 0
        i = 0
        while e < self.node - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(x, y)

        return result

vertex_labels = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
    5: 'f', 6: 'g', 7: 'h', 8: 'i'
}

m = Kruskalalgorithm(9)
m.add(0, 1, 4)  # a-b
m.add(0, 7, 8)  # a-h
m.add(1, 7, 11)  # b-h
m.add(1, 2, 8)  # b-c
m.add(7, 8, 7)  # h-i
m.add(6, 7, 1)  # g-h
m.add(6, 8, 6)  # g-i
m.add(2, 8, 2)  # c-i
m.add(2, 5, 4)  # c-f
m.add(2, 3, 7)  # c-d
m.add(5, 3, 14)  # f-d
m.add(5, 4, 10)  # f-e
m.add(3, 4, 9)  # d-e

mst = m.minimumsearchtree()

print("Minimum Spanning Tree:")
weight = 0
for u, v, w in mst:
    print(f"{vertex_labels[u]} - {vertex_labels[v]}: {w}")
    weight += w
print("Final weight for MST:", weight)


"""
output:

Minimum Spanning Tree:
g - h: 1
c - i: 2
a - b: 4
c - f: 4
g - i: 6
c - d: 7
a - h: 8
d - e: 9
Final weight for MST: 41
"""
