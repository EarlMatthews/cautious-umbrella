def longest_path(graph):
    '''
    Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
    The function should return the length of the longest path within the graph. A path may start and end at any two nodes. 
    The length of a path is considered the number of edges in the path, not the number of nodes.
    '''
    distance = {} # dictionary that holds the distance of all nodes from terminal node

    # locate the terminal node(s)
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0
    # find the distance of all other nodes from terminal node
    for node in graph:
        traverse_distance(graph, node, distance)
    
    # return the max distance
    return max(distance.values())

def traverse_distance(graph, node, distance):
    # if we already have the distance for a node, return it
    if node in distance:
        return distance[node]
    
    # calculate MAX distance for a node not in dictionary
    max_length = 0 
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        if attempt > max_length:
            max_length = attempt
        
    distance[node] =  1 + max_length
    return distance[node]

#test_00:
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

print(longest_path(graph)) # -> 2
#test_01:
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print(longest_path(graph)) # -> 4
#test_02:
graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

print(longest_path(graph)) # -> 2
#test_03:
graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}

print(longest_path(graph)) # -> 3