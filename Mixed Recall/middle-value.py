class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def middle_value(head):
	current = head
	count = 0
	while current:
		count += 1
		current = current.next
		
	current = head
	for i in range(0,count // 2):
		current = current.next
	return current.val
		
		
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e

print(middle_value(a))

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
print(middle_value(a)) # d