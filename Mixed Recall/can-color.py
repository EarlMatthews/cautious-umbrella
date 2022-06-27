def can_color(graph):
	'''
	Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. 
	The function should return a boolean indicating whether or not it is possible to color nodes of the graph
	using two colors in such a way that adjacent nodes are always different colors.
	'''
	coloring = {}
	for node in graph:
		# only colors are True and False
		if node not in coloring and validate(graph, node, coloring, False) == False:
			return False
	return True

def validate(graph, node, coloring, current_color):
	if node in coloring:
		return current_color == coloring[node]
	
	coloring[node] = current_color
	
	for neighbor in graph[node]:
		if validate(graph,neighbor, coloring, not current_color) == False:
			return False
	return True

#test_00:
print(can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
})) # -> True

#test_01:
print(can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})) # -> False

#test_02:
print(can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a"],
  "d": ["a"],
})) # -> True

#test_03:
can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a", "d"],
  "d": ["a", "c"],
}) # -> False

#test_04:
print(can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
})) # -> True

#test_05:
print(can_color({
  "z": []
})) # -> True

#test_06:
print(can_color({
  "h": ["i", "k"],
  "i": ["h", "j"],
  "j": ["i", "k"],
  "k": ["h", "j"],
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
})) # -> False