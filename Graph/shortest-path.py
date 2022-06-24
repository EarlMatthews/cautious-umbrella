from collections import deque

def shortest_path(edges, node_A, node_B):
    '''
    Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
    The function should return the length of the shortest path between A and B. 
    Consider the length as the number of edges in the path, not the number of nodes. 
    If there is no path between A and B, then return -1.
    '''
    graph = build_graph(edges)
    queue = deque([ ( node_A, 0 ) ])
    visited = set([node_A])
  
    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance
    
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1
  
def build_graph(edges):
    graph = {}
  
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

#test_00:
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v'],
]

print(shortest_path(edges, 'w', 'z')) # -> 2

#test_01:
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'y', 'x')) # -> 1

#test_03:
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'e', 'c')) # -> 2
#test_04:
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'b', 'g')) # -> -1
#test_05:
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

print(shortest_path(edges, 'w', 'e')) # -> 1
#test_06:
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

print(shortest_path(edges, 'n', 'e')) # -> 2

#test_07:
edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

print(shortest_path(edges, 'm', 's')) # -> 6