from collections import defaultdict

def topologicalsort(graph):
    def depthfirstsearch(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                depthfirstsearch(neighbor)
        topologicalorder.append(node)

    visited = set()
    topologicalorder = []

    for node in graph:
        if node not in visited:
            depthfirstsearch(node)

    return topologicalorder[::-1]

graph = {
    'shirt': ['belt', 'tie'],
    'tie': ['jacket'],
    'undershorts': ['pants', 'shoes'],
    'socks': ['shoes'],
    'pants': ['belt', 'shoes'],
    'belt': ['jacket'],
    'jacket': [],
    'shoes': []
}

order = topologicalsort(graph)
print("Topological order:", order)


'''
output:
Topological order: ['socks', 'undershorts', 'pants', 'shoes', 'shirt', 'tie', 'belt', 'jacket']
'''
