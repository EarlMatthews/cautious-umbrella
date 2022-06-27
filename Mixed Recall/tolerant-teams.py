def tolerant_teams(rivalries):
    """
    Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 
    A rivalry is a pair of people who should not be placed on the same team. 
    The function should return a boolean indicating whether or not it is possible to 
    separate people into two teams, without rivals being on the same team. 
    The two teams formed do not have to be the same size.
    """
    graph = build_graph(rivalries)
    
    coloring = {}
    for node in graph:
        # only begin your traversal with a not not visited (it should not be in coloring dictionary)
        if node not in coloring and not is_bipartite(graph, node, coloring, False): #returns True if a bipartite graph
            return False
    return True

def is_bipartite(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color
    
    coloring[node] = current_color
    
    for neighbor in graph[node]:
        if not is_bipartite(graph, neighbor, coloring, not current_color): # boolean
            return False
    return True

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
print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
]) )# -> True

#test_01:
print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
])) # -> False

#test_02:
print(tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
])) # -> True

#test_03:
print(tolerant_teams([
  ('alex', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
])) # -> False

#test_04:
print(tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
])) # -> True

#test_05:
print(tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
])) # -> True

#test_06:
print(tolerant_teams([
  ('alan', 'jj'),
  ('jj', 'richard'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
])) # -> True

#test_07:
print(tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('betty', 'christine'),
  ('jj', 'simcha'),
  ('richard', 'christine')
])) # -> False