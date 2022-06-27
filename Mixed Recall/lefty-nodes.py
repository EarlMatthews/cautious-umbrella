class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lefty_nodes(root):
	'''
	Write a function, lefty_nodes, that takes in the root of a binary tree. 
	The function should return a list containing the left-most value on every level of the tree. 
	The list must be ordered in a top-down fashion where the root is the first item.
	'''
	values = []

	traverse (root,0,values)
	
	return values

def traverse(root, level, values):
	if root is None:
		return
	# if there is no value stored at index 'level' add it
	if len(values) == level:
		values.append(root.val)
	
	#important to note that we visit left children before right children
	traverse(root.left,level + 1, values)
	traverse(root.right, level + 1, values)

#test_00
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(lefty_nodes(a)) # [ 'a', 'b', 'd', 'g' ]

#test_01
u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')

u.left = t
u.right = s
s.right = r
r.left = q
r.right = p

#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

print(lefty_nodes(u)) # [ 'u', 't', 'r', 'q' ]

#test_02
l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')

l.left = m
l.right = n
n.left = o
n.right = p
o.left = q
o.right = r
p.left = s
p.right = t

#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t

print(lefty_nodes(l)) # [ 'l', 'm', 'o', 'q' ]
#test_03
n = Node('n')
y = Node('y')
c = Node('c')

n.left = y
n.right = c

#       n
#     /   \
#    y     c

print(lefty_nodes(n)) # [ 'n', 'y' ]
#test_04
i = Node('i')
n = Node('n')
s = Node('s')
t = Node('t')

i.right = n
n.left = s
n.right = t

#       i
#        \
#         n
#        / \
#       s   t

print(lefty_nodes(i)) # [ 'i', 'n', 's' ]
#test_05
print(lefty_nodes(None)) # [ ]