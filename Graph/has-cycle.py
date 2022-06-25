def has_cycle(graph):
    '''
    Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. 
    The function should return a boolean indicating whether or not the graph contains a cycle.
    '''
    visiting = set()
    visited = set()
    
    for node in graph:
        if cycle_detect(graph, node, visiting, visited) == True:
            return True
      
    return False

def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        return False
    if node in visiting:
        return True
    
    visiting.add(node)
    
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) == True:
            return True
      
    visiting.remove(node)
    visited.add(node)
    
    return False

#test_00:
print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True

#test_01:
print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False

#test_02:
print(has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
})) # -> True

#test_03:
print(has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
})) # -> False

#test_04:
print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
})) # -> True

#test_05:
print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
})) # -> True