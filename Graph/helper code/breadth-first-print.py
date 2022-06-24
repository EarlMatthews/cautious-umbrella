# Breadth First search iterative
graph = { 'a' : ['c','b'],
          'b' : ['d'],
          'c' : ['e'],
          'd' : ['f'],
          'e' : [],
          'f' : [],
          }

def breadthFirstPrint(graph,source):
    queue = [ source ]
    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
            
breadthFirstPrint(graph,'a')