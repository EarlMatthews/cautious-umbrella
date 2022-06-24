def largest_component(graph):
    '''
    Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
    The function should return the size of the largest connected component in the graph.
    '''
    visited = set()
    largest = 0
    for node in graph:
        size = explore_size(graph,node,visited) # return size of connected region
        if size > largest:
            largest = size
    return largest

def explore_size(graph, node, visited):
    if node in visited:
        return 0
  
    visited.add(node)
    size = 1 # node right now
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)
    return size


#test_00:
print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4

#test_01:
print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

#test_02:
print(largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # -> 5

#test_03:
print(largest_component({})) # -> 0

#test_04:
print(largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})) # -> 3