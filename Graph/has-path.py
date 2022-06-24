# def has_path(graph, src, dst):
'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst).
The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ
Recursive Depth First search
'''
#   if src == dst: # You're already there so path exists
#     return True
#   for neighbor in graph[src]:
#     if has_path(graph,neighbor,dst) is True: #check if there is a path from a neighbor to dst
#       return True
#   return False  # no path was found return False
from collections import deque
'''
iterative Breadth first
'''
# def has_path(graph,src,dst):
#   queue = deque([src])  # set up a queue for breadth first search
#   while queue:
#     current = queue.popleft()
    
#     if current == dst:
#       return True
#     for neighbor in graph[current]:
#       queue.append(neighbor)
#   return False

def has_path(graph,src,dst):
    '''
    iterative Depth First search
    '''
    stack = [src]
    while stack:
        current = stack.pop()
    
    if current == dst:
        return True
    
    for neighbor in graph[current]:
        stack.append(neighbor)
    return False