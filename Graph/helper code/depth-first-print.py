graph = { 'a' : ['c','b'],
          'b' : ['d'],
          'c' : ['e'],
          'd' : ['f'],
          'e' : [],
          'f' : [],
          }

def depthFirstPrintRecursive(graph,source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecursive(graph,neighbor)

def depthFirstPrintIterative(graph,source):
    stack = [source]
    while len(stack) > 0:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)

depthFirstPrintRecursive(graph,'a')
#print("_____")
depthFirstPrintIterative(graph,'a')
#a,c,e,b,d,f    