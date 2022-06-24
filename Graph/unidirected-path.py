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

def has_path(graph,src,dst,visited):
    if src == dst:
        return True
  
    if src in visited:  # check if you've already seen this node
        return False
  
    visited.add(src)    # if its the first time add to visited set
  
    for neighbor in graph[src]:
        if has_path(graph,neighbor,dst,visited) == True:
            return True
    return False

def undirected_path(edges, node_A, node_B):
    '''
    Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
    The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
    '''
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())



# test 00:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n'),
]

print(undirected_path(edges, 'j', 'm')) # -> True

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n'),
]

print(undirected_path(edges, 'm', 'j')) # -> True