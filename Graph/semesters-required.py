def semesters_required(num_courses, prereqs):
  '''
  Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments.
  Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A 
  must be taken before course B. Return the minimum number of semesters required to complete all n courses. 
  There is no limit on how many courses you can take in a single semester, as long the prerequisites
  of a course are satisfied before taking it.

  Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. 
  You must take A in some semester before B.

  You can assume that it is possible to eventually complete all courses.
  '''
  distance = {} # set up distance disctionary
  graph = build_graph(num_courses, prereqs)  # build graph from num_courses and prereq list
  # go through the nodes in the graph and find the terminal nodes (classes taken last)
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 1 # it takes at least one semester to take class
  # find distance of all other nodes in the graph
  for node in graph:
    traverse_distance(graph, node, distance)
  return max(distance.values())

def traverse_distance(graph, node, distance):
  # if we already have the distance for a node return it
  if node in distance:
    return distance[node]
  #calculate MAX distance for nodes not in dictionary
  max_length = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > max_length:
      max_length = attempt
  distance[node] = 1 + max_length
  return distance[node]

def build_graph(num_courses, prereqs):
  # build a graph from an edge list
  graph = {}
  for course in range(0, num_courses):
    graph[course] = []
  for prereq in prereqs:
    a,b = prereq
    graph[a].append(b)
  return graph