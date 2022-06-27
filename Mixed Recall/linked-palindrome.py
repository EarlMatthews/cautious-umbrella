class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def linked_palindrome(head):
	# traverse linked list adding current.val to value array
	current = head
	value =[]
	while current is not None:
		value.append(current.val)
		current = current.next
	return  value == value[::-1]
		


a = Node(3)
b = Node(2)
c = Node(7)
d = Node(7)
e = Node(2)
f = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f